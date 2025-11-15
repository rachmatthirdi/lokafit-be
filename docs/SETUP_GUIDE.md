# Complete Setup Guide - LokaFit

Panduan lengkap setup LokaFit (Frontend + Backend) dari awal hingga production.

---

## Prerequisites

Pastikan Anda memiliki:

- **Node.js** 18+ dan pnpm 8+ (untuk frontend)
- **Python** 3.9+ (untuk backend)
- **Git** untuk version control
- **GitHub Account** untuk push code
- **Vercel Account** untuk deploy frontend
- **Railway Account** untuk deploy backend
- **Supabase Account** (optional, untuk database)

---

## Part 1: Frontend Setup

### Step 1.1 - Clone Frontend Repository

\`\`\`bash
# Clone
git clone https://github.com/yourusername/lokafit-frontend.git
cd lokafit-frontend

# Install dependencies
pnpm install

# Atau npm
npm install
\`\`\`

### Step 1.2 - Environment Setup

Buat file `.env.local`:

\`\`\`bash
cp .env.example .env.local
\`\`\`

Edit `.env.local`:

\`\`\`env
# App
NEXT_PUBLIC_APP_URL=http://localhost:3000

# Backend (lokal dulu)
NEXT_PUBLIC_API_URL=http://localhost:8000

# Supabase (opsional untuk sekarang)
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key
\`\`\`

### Step 1.3 - Run Frontend Locally

\`\`\`bash
pnpm dev
\`\`\`

Buka `http://localhost:3000` di browser.

---

## Part 2: Backend Setup

### Step 2.1 - Clone Backend Repository

\`\`\`bash
# Clone
git clone https://github.com/yourusername/lokafit-backend.git
cd lokafit-backend

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
\`\`\`

### Step 2.2 - Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### Step 2.3 - Environment Setup

Buat file `.env`:

\`\`\`bash
cp .env.example .env
\`\`\`

Edit `.env`:

\`\`\`env
ENVIRONMENT=development
\`\`\`

### Step 2.4 - Run Backend Locally

\`\`\`bash
uvicorn main:app --reload --port 8000
\`\`\`

Buka `http://localhost:8000/docs` untuk API documentation.

---

## Part 3: Local Development Test

### Test Both Services Together

**Terminal 1 - Frontend**:
\`\`\`bash
cd lokafit-frontend
pnpm dev
\`\`\`

**Terminal 2 - Backend**:
\`\`\`bash
cd lokafit-backend
source venv/bin/activate
uvicorn main:app --reload --port 8000
\`\`\`

### Test API Integration

Di frontend, coba upload foto ke Shop:
1. Navigate ke Shop page
2. Klik camera/upload button
3. Pilih gambar
4. Tunggu processing - backend akan extract warna

Backend logs akan tampil di terminal:
\`\`\`
INFO:     Started server process [12345]
INFO:     Uvicorn running on http://0.0.0.0:8000
\`\`\`

---

## Part 4: Deploy Frontend ke Vercel

### Step 4.1 - Push ke GitHub

\`\`\`bash
cd lokafit-frontend

git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/lokafit-frontend.git
git push -u origin main
\`\`\`

### Step 4.2 - Connect Vercel

1. Buka [vercel.com](https://vercel.com)
2. Sign in dengan GitHub account
3. New Project → Import Git Repository
4. Select `lokafit-frontend` repository

### Step 4.3 - Configure Build Settings

- **Framework**: Next.js
- **Build Command**: `pnpm build`
- **Output Directory**: `.next`
- **Install Command**: `pnpm install`

### Step 4.4 - Set Environment Variables

Di Vercel dashboard → Project Settings → Environment Variables:

\`\`\`
NEXT_PUBLIC_APP_URL=https://lokafit.vercel.app
NEXT_PUBLIC_API_URL=https://api.lokafit.railway.app  (akan diset setelah backend deploy)
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key
\`\`\`

### Step 4.5 - Deploy

Vercel otomatis deploy ketika push ke main branch.

Production URL: `https://lokafit.vercel.app`

---

## Part 5: Deploy Backend ke Railway

### Step 5.1 - Push ke GitHub

\`\`\`bash
cd lokafit-backend

git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/lokafit-backend.git
git push -u origin main
\`\`\`

### Step 5.2 - Connect Railway

1. Buka [railway.app](https://railway.app)
2. Dashboard → New Project
3. Deploy from GitHub repo
4. Select `lokafit-backend` repository

### Step 5.3 - Configure Environment

Railway → Project → Variables:

\`\`\`
ENVIRONMENT=production
\`\`\`

### Step 5.4 - Set Domain (Custom)

Railway → Project → Settings → Domain:

- Enable custom domain
- Format: `https://api.lokafit.railway.app`

Production Backend URL: `https://api.lokafit.railway.app`

---

## Part 6: Connect Frontend & Backend

### Step 6.1 - Update Frontend Env Variables

Di Vercel dashboard:
- Project → Settings → Environment Variables
- Update `NEXT_PUBLIC_API_URL=https://api.lokafit.railway.app`

### Step 6.2 - Redeploy Frontend

\`\`\`bash
cd lokafit-frontend
git add .
git commit -m "Update API URL"
git push origin main
\`\`\`

Vercel otomatis redeploy.

### Step 6.3 - Test Integration

1. Buka `https://lokafit.vercel.app`
2. Navigate ke Shop
3. Coba upload foto
4. Tunggu backend process
5. Lihat hasil di UI

---

## Part 7: Optional - Setup Database (Supabase)

### Step 7.1 - Create Supabase Project

1. Buka [supabase.com](https://supabase.com)
2. New Project
3. Set database password
4. Wait untuk setup (~2 menit)

### Step 7.2 - Get Connection String

Supabase → Project Settings → Database:
- Copy "PostgreSQL Connection String"

### Step 7.3 - Add to Backend

Backend `.env`:
\`\`\`
DATABASE_URL=postgresql://postgres:[PASSWORD]@[HOST]/postgres
\`\`\`

Railway Variables:
\`\`\`
DATABASE_URL=postgresql://postgres:[PASSWORD]@[HOST]/postgres
\`\`\`

### Step 7.4 - Create Tables (Future)

Sebelum implement database queries, Anda perlu create tables:

\`\`\`sql
-- Akan ditambahkan saat ada data persistence feature
\`\`\`

---

## Troubleshooting

### Frontend Issues

**Port 3000 sudah digunakan**:
\`\`\`bash
pnpm dev -- -p 3001
\`\`\`

**Build error di Vercel**:
- Check build logs di Vercel dashboard
- Ensure `.env.example` ada
- Verify TypeScript errors: `pnpm build` lokal

**Image tidak tampil**:
- Check image paths di `public/` folder
- Ensure CORS enabled di backend

### Backend Issues

**libGL.so.1 error di Railway**:
- Verify `nixpacks.toml` ada dan benar

**CORS error**:
- Check `ALLOWED_ORIGINS` di `main.py`
- Add `https://lokafit.vercel.app`

**API timeout**:
- Check Python dependencies installed: `pip list`
- Verify Railway has enough CPU allocated

### Network Issues

**Backend tidak respond**:
\`\`\`bash
# Test dari frontend console
curl https://api.lokafit.railway.app/api/v1/health
\`\`\`

**Slow API calls**:
- Check Railway CPU usage
- Reduce image size sebelum upload

---

## Post-Deployment Checklist

- [ ] Frontend running di Vercel
- [ ] Backend running di Railway
- [ ] Health check passing: `/api/v1/health`
- [ ] Environment variables set di both services
- [ ] CORS configured untuk production domain
- [ ] Image upload working end-to-end
- [ ] Color extraction working
- [ ] Recommendations API working
- [ ] PWA installable
- [ ] Offline mode tested

---

## Next Steps

1. **Implement Authentication**
   - Supabase Auth di frontend
   - JWT validation di backend

2. **Add Database**
   - User profiles
   - Wardrobe items
   - Recommendation history

3. **Enhance AI**
   - Train custom models
   - Add AR try-on
   - Implement more recommendation algorithms

4. **Scale Infrastructure**
   - Split AI services ke separate servers
   - Add caching (Redis)
   - Implement queue system (Celery)

---

## Support & Resources

- **Frontend Docs**: [nextjs.org](https://nextjs.org)
- **Backend Docs**: [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- **Deployment**: [vercel.com/docs](https://vercel.com/docs), [railway.app/docs](https://railway.app/docs)
- **Python AI**: [opencv.org](https://opencv.org), [numpy.org](https://numpy.org)

---

**Happy Coding! Deploy with confidence!**
