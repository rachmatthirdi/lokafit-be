# LokaFit Backend - AI Engine

Backend AI service untuk fashion styling assistant **LokaFit**. Dibangun dengan **FastAPI** (Python) dan dilengkapi dengan 3 sistem AI terpisah untuk computer vision dan rekomendasi.

## Overview Arsitektur

LokaFit menggunakan **arsitektur Headless AI** (Backend-Frontend terpisah):

\`\`\`
┌─────────────────────────────────────────────────────────────┐
│                    Frontend (Next.js)                         │
│              (React, TypeScript, Tailwind CSS)               │
│        Berjalan di: https://lokafit.vercel.app              │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP/REST API
                     │ (JSON requests/responses)
                     │
┌────────────────────▼────────────────────────────────────────┐
│              Backend AI Engine (FastAPI)                     │
│    3 Sistem AI terpisah untuk CV & Rekomendasi             │
│       Berjalan di: https://api.lokafit.railway.app         │
└─────────────────────────────────────────────────────────────┘
\`\`\`

### Keuntungan Arsitektur Ini:
- **Skalabilitas**: Setiap AI bisa di-deploy terpisah jika perlu
- **Performance**: Backend AI heavy-lifting, Frontend responsif
- **Maintenance**: Update AI tidak perlu update Frontend
- **Reusability**: Backend bisa digunakan oleh multiple frontend (web, mobile, desktop)

---

## 3 Sistem AI Utama

### 1. Garment Processor (AI #1) - Pemrosesan Pakaian

**Tujuan**: Menganalisis gambar pakaian dan mengekstrak data terstruktur.

**Teknologi**:
- **OpenCV (cv2.kmeans)**: KMeans clustering untuk ekstraksi warna dominan
- **Contour Detection**: Pengukuran dimensi pakaian
- **PIL**: Manipulasi gambar

**Proses**:
1. Upload gambar pakaian
2. Ekstraksi warna dominan menggunakan KMeans → Hex color (#3A5B99)
3. Deteksi outline pakaian → Ukuran (width, height, area)
4. Klasifikasi tipe pakaian (wide, long, standard)

**Endpoint**: `POST /api/v1/scan/accurate`

**Request**:
\`\`\`bash
curl -X POST "http://localhost:8000/api/v1/scan/accurate" \
  -F "file=@clothing.jpg"
\`\`\`

**Response**:
\`\`\`json
{
  "garment_id": "garment_001",
  "color_hex": "#3A5B99",
  "color_name": "Blue",
  "garment_type": "standard",
  "measurements": {
    "width_px": 850,
    "height_px": 1200,
    "area_px": 1020000
  },
  "confidence": 0.85
}
\`\`\`

---

### 2. Profile Analyzer (AI #2) - Analisis Profil Pengguna

**Tujuan**: Menganalisis tipe kulit dan menentukan palet warna yang cocok.

**Teknologi**:
- **Face Detection**: OpenCV Cascade Classifier (optional)
- **Color Analysis**: RGB → HSV conversion
- **Undertone Classification**: Warm/Cool/Neutral

**Proses**:
1. Upload foto wajah pengguna
2. Ekstraksi area wajah (center region)
3. Analisis RGB rata-rata
4. Tentukan undertone (Warm jika R > B, Cool jika B > R)
5. Return recommended color palette

**Endpoint**: `POST /api/v1/profile/skin-tone`

**Request**:
\`\`\`bash
curl -X POST "http://localhost:8000/api/v1/profile/skin-tone" \
  -F "file=@face.jpg"
\`\`\`

**Response**:
\`\`\`json
{
  "user_id": "user_001",
  "skin_tone": "Medium",
  "undertone": "Warm",
  "recommended_colors": [
    { "name": "Coral", "hex": "#FF6B6B" },
    { "name": "Peach", "hex": "#FFAB91" },
    { "name": "Gold", "hex": "#FFD700" }
  ],
  "confidence": 0.80
}
\`\`\`

---

### 3. MixMatch Recommender (AI #3) - Mesin Rekomendasi

**Tujuan**: Memberikan rekomendasi warna cocok berdasarkan teori warna.

**Teknologi**:
- **Color Theory**: Complementary, Analogous, Triadic schemes
- **HSV Color Space**: Untuk perhitungan angle dan harmony
- **Undertone Filtering**: Filter rekomendasi sesuai undertone pengguna

**Proses**:
1. Input warna item current (hex) + undertone pengguna
2. Konversi hex → HSV
3. Hitung warna komplementer, analogous, triadic
4. Filter berdasarkan undertone pengguna
5. Sort by match score, return top 5

**Endpoint**: `GET /api/v1/recommend/instant`

**Request**:
\`\`\`bash
curl "http://localhost:8000/api/v1/recommend/instant?item_color=%23FF0000&undertone=Warm"
\`\`\`

**Response**:
\`\`\`json
{
  "status": "success",
  "item_color": "#FF0000",
  "recommendations": [
    {
      "color_hex": "#00FF00",
      "match_score": 0.95,
      "theory": "complementary"
    }
  ],
  "confidence": 0.88
}
\`\`\`

---

## Quick Start (Lokal)

### Prerequisites
- Python 3.9+
- pip / conda

### 1. Setup

\`\`\`bash
# Clone repository
git clone https://github.com/your-username/lokafit-backend.git
cd lokafit-backend

# Buat virtual environment
python -m venv venv

# Aktivasi (Windows)
venv\Scripts\activate

# Aktivasi (Mac/Linux)
source venv/bin/activate
\`\`\`

### 2. Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. Environment Setup

\`\`\`bash
# Copy .env.example ke .env
cp .env.example .env

# Edit .env (minimal untuk local dev)
ENVIRONMENT=development
\`\`\`

### 4. Jalankan Server

\`\`\`bash
uvicorn main:app --reload --port 8000
\`\`\`

Server berjalan di: `http://localhost:8000`

**Dokumentasi API**: `http://localhost:8000/docs` (Swagger UI)

---

## Deployment ke Railway

### 1. Push ke GitHub

\`\`\`bash
git add .
git commit -m "Initial commit"
git push origin main
\`\`\`

### 2. Connect Railway

- Buka [railway.app](https://railway.app)
- New Project → GitHub Repo
- Select repository `lokafit-backend`

### 3. Set Environment Variables

Di Railway dashboard → Variables:
- `ENVIRONMENT=production`
- `DATABASE_URL=postgresql://...` (optional, untuk future use)

### 4. Deploy

Railway otomatis deploy. URL akan seperti:
\`\`\`
https://lokafit-backend-production.up.railway.app
\`\`\`

Update frontend dengan URL ini di `.env.local`:
\`\`\`
NEXT_PUBLIC_API_URL=https://lokafit-backend-production.up.railway.app
\`\`\`

---

## API Endpoints Reference

### Health
\`\`\`bash
GET /api/v1/health
GET /api/v1/health/detailed
\`\`\`

### Scanning (AI #1)
\`\`\`bash
POST /api/v1/scan/accurate          # Full analysis
POST /api/v1/scan/quick              # Color only
\`\`\`

### Profile (AI #2)
\`\`\`bash
POST /api/v1/profile/skin-tone       # Analyze skin tone
POST /api/v1/profile/analyze         # Full profile
\`\`\`

### Recommendations (AI #3)
\`\`\`bash
GET /api/v1/recommend/instant        # Instant match
GET /api/v1/recommend/weekly         # Weekly curation
POST /api/v1/recommend/save-preference  # Save preference
\`\`\`

---

## Project Structure

\`\`\`
lokafit-backend/
├── app/
│   ├── ai_core/
│   │   ├── garment_processor.py    # AI #1
│   │   ├── profile_analyzer.py     # AI #2
│   │   ├── mixmatch_logic.py       # AI #3
│   │   └── __init__.py
│   ├── api/
│   │   └── v1/
│   │       ├── scan.py
│   │       ├── profile.py
│   │       ├── recommend.py
│   │       ├── health.py
│   │       └── __init__.py
│   ├── config.py
│   └── __init__.py
├── main.py
├── requirements.txt
├── nixpacks.toml
├── .env.example
├── .gitignore
└── README.md
\`\`\`

---

## Troubleshooting

### Error: "libGL.so.1 not found" (Railway)

Pastikan `nixpacks.toml` ada:
\`\`\`toml
[phases.setup]
nixPkgs = ["pkgs.libglvnd"]
\`\`\`

### Slow Processing

- Resize input gambar ke 150x150 sebelum KMeans
- Increase CPU allocation di Railway
- Implement caching untuk warna yang sering muncul

### CORS Error

Update `ALLOWED_ORIGINS` di `main.py`:
\`\`\`python
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://lokafit.vercel.app",
]
\`\`\`

---

## Environment Variables

\`\`\`bash
# Required
ENVIRONMENT=production

# Optional
DATABASE_URL=postgresql://...
AI_CONFIDENCE_THRESHOLD=0.7
\`\`\`

---

## License

MIT License

## Support

Buka issue di GitHub atau hubungi tim development.
