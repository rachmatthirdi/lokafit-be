# Frontend-Backend Integration Guide

Panduan lengkap untuk mengintegrasikan frontend Next.js dengan backend FastAPI.

## Architecture Overview

\`\`\`
┌──────────────────────────────────────┐
│      Frontend (Next.js)              │
│  - React Components                  │
│  - PWA Features                      │
│  - UI/UX Layer                       │
└──────────────┬───────────────────────┘
               │
        HTTP/REST API
    (JSON payload requests)
               │
┌──────────────▼───────────────────────┐
│     Backend (FastAPI)                │
│  - AI Processing                     │
│  - Computer Vision                   │
│  - Data Analysis                     │
└──────────────────────────────────────┘
\`\`\`

---

## 1. Environment Setup

### Frontend (.env.local)

\`\`\`env
# App URL
NEXT_PUBLIC_APP_URL=http://localhost:3000

# Backend API (Development)
NEXT_PUBLIC_API_URL=http://localhost:8000

# Backend API (Production Railway)
# NEXT_PUBLIC_API_URL=https://lokafit-backend-production.up.railway.app

# Supabase (untuk database & auth)
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key
\`\`\`

### Backend (.env)

\`\`\`env
ENVIRONMENT=development

# Optional: Database connection
# DATABASE_URL=postgresql://...

# AI Configuration
AI_CONFIDENCE_THRESHOLD=0.7
\`\`\`

---

## 2. API Integration Examples

### 2.1 Garment Scanning (AI #1)

**Frontend (TypeScript)**:
\`\`\`typescript
// app/(main)/shop/page.tsx

async function scanGarment(imageFile: File) {
  try {
    const formData = new FormData();
    formData.append('file', imageFile);
    
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/api/v1/scan/accurate`,
      {
        method: 'POST',
        body: formData,
      }
    );
    
    if (!response.ok) throw new Error('Scan failed');
    
    const data = await response.json();
    
    return {
      colorHex: data.color_hex,
      colorName: data.color_name,
      garmentType: data.garment_type,
      measurements: data.measurements,
      confidence: data.confidence,
    };
  } catch (error) {
    console.error('Scan error:', error);
    throw error;
  }
}

export default function ShopPage() {
  const handleImageUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    
    const garmentData = await scanGarment(file);
    console.log('Garment data:', garmentData);
  };
  
  return (
    <div>
      <input type="file" onChange={handleImageUpload} accept="image/*" />
    </div>
  );
}
\`\`\`

---

### 2.2 Skin Tone Analysis (AI #2)

**Frontend (TypeScript)**:
\`\`\`typescript
// app/(main)/profile/page.tsx

async function analyzeSkinTone(photoFile: File) {
  try {
    const formData = new FormData();
    formData.append('file', photoFile);
    
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/api/v1/profile/skin-tone`,
      {
        method: 'POST',
        body: formData,
      }
    );
    
    if (!response.ok) throw new Error('Analysis failed');
    
    const data = await response.json();
    
    return {
      skinTone: data.skin_tone,
      undertone: data.undertone,
      recommendedColors: data.recommended_colors,
      confidence: data.confidence,
    };
  } catch (error) {
    console.error('Analysis error:', error);
    throw error;
  }
}

export default function ProfilePage() {
  const handlePhotoUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    
    const profileData = await analyzeSkinTone(file);
    console.log('Profile data:', profileData);
    
    // Simpan ke state atau database
    // setUserProfile(profileData);
  };
  
  return (
    <div>
      <input type="file" onChange={handlePhotoUpload} accept="image/*" />
    </div>
  );
}
\`\`\`

---

### 2.3 Get Recommendations (AI #3)

**Frontend (TypeScript)**:
\`\`\`typescript
// app/(main)/product/[id]/page.tsx

async function getRecommendations(itemColor: string, undertone: string) {
  try {
    const params = new URLSearchParams({
      item_color: itemColor,
      undertone: undertone,
    });
    
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/api/v1/recommend/instant?${params}`,
      {
        method: 'GET',
      }
    );
    
    if (!response.ok) throw new Error('Recommendation failed');
    
    const data = await response.json();
    
    return data.recommendations.map((rec: any) => ({
      colorHex: rec.color_hex,
      matchScore: rec.match_score,
      theory: rec.theory,
    }));
  } catch (error) {
    console.error('Recommendation error:', error);
    throw error;
  }
}

export default function ProductDetail({ params }: { params: { id: string } }) {
  const [recommendations, setRecommendations] = React.useState([]);
  
  React.useEffect(() => {
    // Contoh: dapatkan rekomendasi untuk item biru dengan undertone Warm
    getRecommendations('#3A5B99', 'Warm')
      .then(setRecommendations)
      .catch(console.error);
  }, []);
  
  return (
    <div>
      <h2>Recommended Colors</h2>
      {recommendations.map((rec, idx) => (
        <div key={idx}>
          <div style={{ backgroundColor: rec.colorHex, width: 50, height: 50 }} />
          <p>Match Score: {(rec.matchScore * 100).toFixed(0)}%</p>
          <p>Theory: {rec.theory}</p>
        </div>
      ))}
    </div>
  );
}
\`\`\`

---

## 3. Error Handling & Retry Logic

**Best Practice - Fetch Wrapper**:

\`\`\`typescript
// lib/api-client.ts

interface ApiResponse<T> {
  data?: T;
  error?: string;
  status: number;
}

export async function apiCall<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<ApiResponse<T>> {
  const maxRetries = 3;
  let lastError: Error | null = null;
  
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      const url = `${process.env.NEXT_PUBLIC_API_URL}${endpoint}`;
      const response = await fetch(url, {
        ...options,
        headers: {
          'Content-Type': options.headers && 'Content-Type' in options.headers 
            ? (options.headers as any)['Content-Type'] 
            : 'application/json',
          ...options.headers,
        },
      });
      
      if (response.ok) {
        const data = await response.json();
        return { data, status: response.status };
      }
      
      if (response.status === 429 || response.status >= 500) {
        // Retry untuk rate limit atau server error
        await new Promise(resolve => 
          setTimeout(resolve, Math.pow(2, attempt) * 1000)
        );
        continue;
      }
      
      const errorData = await response.json();
      return {
        error: errorData.detail || response.statusText,
        status: response.status,
      };
    } catch (error) {
      lastError = error as Error;
      if (attempt < maxRetries - 1) {
        await new Promise(resolve => 
          setTimeout(resolve, Math.pow(2, attempt) * 1000)
        );
      }
    }
  }
  
  return {
    error: lastError?.message || 'Request failed after retries',
    status: 0,
  };
}

// Usage
const { data, error } = await apiCall('/api/v1/scan/accurate', {
  method: 'POST',
  body: formData,
});
\`\`\`

---

## 4. CORS Configuration

Backend sudah dikonfigurasi untuk CORS. Jika error, update `main.py`:

\`\`\`python
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "https://localhost:3000",
    "https://lokafit.vercel.app",  # Production domain
    "https://*.vercel.app",
]
\`\`\`

---

## 5. Development Workflow

### Running Both Services Locally

**Terminal 1 - Frontend**:
\`\`\`bash
cd lokafit-frontend
pnpm dev
# http://localhost:3000
\`\`\`

**Terminal 2 - Backend**:
\`\`\`bash
cd lokafit-backend
source venv/bin/activate  # Mac/Linux
uvicorn main:app --reload --port 8000
# http://localhost:8000/docs
\`\`\`

### Testing API Calls

**Using curl**:
\`\`\`bash
# Test garment scanning
curl -X POST "http://localhost:8000/api/v1/scan/accurate" \
  -F "file=@test-image.jpg"

# Test skin tone
curl -X POST "http://localhost:8000/api/v1/profile/skin-tone" \
  -F "file=@face.jpg"

# Test recommendations
curl "http://localhost:8000/api/v1/recommend/instant?item_color=%23FF0000&undertone=Warm"
\`\`\`

**Using Swagger UI**:
1. Buka `http://localhost:8000/docs`
2. Try out setiap endpoint
3. Upload file dan lihat response

---

## 6. Production Deployment

### Frontend → Vercel

\`\`\`bash
git push origin main
# Vercel otomatis deploy
\`\`\`

**Set Production Env Variables**:
- `NEXT_PUBLIC_API_URL=https://lokafit-backend-production.up.railway.app`

### Backend → Railway

\`\`\`bash
git push origin main
# Railway otomatis deploy
\`\`\`

### Health Check

\`\`\`bash
# Test backend is running
curl https://api.lokafit.railway.app/api/v1/health
\`\`\`

---

## 7. Monitoring & Logging

### Frontend Errors

\`\`\`typescript
// utils/error-logger.ts

export function logApiError(
  endpoint: string, 
  error: Error | string,
  context?: Record<string, any>
) {
  console.error(`API Error [${endpoint}]:`, error, context);
  
  // Kirim ke monitoring service (Sentry, LogRocket, dll)
  // sendToMonitoring({ endpoint, error, context });
}
\`\`\`

### Backend Logs

\`\`\`python
# main.py

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/api/v1/scan/accurate")
async def scan_garment(file: UploadFile):
    logger.info(f"Processing file: {file.filename}")
    # ...
\`\`\`

---

## 8. Caching Strategy

### Frontend Cache

\`\`\`typescript
// lib/cache.ts

export function cacheRecommendations(
  itemColor: string,
  undertone: string,
  recommendations: any[]
) {
  const key = `rec_${itemColor}_${undertone}`;
  localStorage.setItem(key, JSON.stringify(recommendations));
}

export function getCachedRecommendations(
  itemColor: string,
  undertone: string
) {
  const key = `rec_${itemColor}_${undertone}`;
  return localStorage.getItem(key);
}
\`\`\`

---

## 9. Future Enhancements

- [ ] Implement WebSocket untuk real-time updates
- [ ] Add caching layer (Redis)
- [ ] Implement GraphQL instead of REST
- [ ] Add authentication (JWT)
- [ ] Database persistence for user data
- [ ] Rate limiting dan throttling
- [ ] Analytics dan telemetry

---

## Support

Jika ada masalah integrasi:
1. Check API documentation: `http://localhost:8000/docs`
2. Verify environment variables
3. Check browser DevTools Network tab
4. Review error logs di backend console
