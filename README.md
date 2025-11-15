# LokaFit - Fashion Styling Assistant PWA

LokaFit adalah aplikasi Progressive Web App (PWA) yang membantu pengguna mengelola lemari pakaian digital mereka dengan fitur-fitur canggih seperti AI-powered outfit recommendations, virtual try-on, dan skin tone analysis.

## 📋 Daftar Isi

- [Fitur Utama](#fitur-utama)
- [Tech Stack](#tech-stack)
- [Instalasi Lokal](#instalasi-lokal)
- [Struktur Proyek](#struktur-proyek)
- [Panduan Penggunaan](#panduan-penggunaan)
- [PWA Setup](#pwa-setup)
- [Deployment](#deployment)
- [Kontribusi](#kontribusi)

## ✨ Fitur Utama

### 1. Home Dashboard
- Daily outfit recommendations
- Filter berdasarkan hari dalam seminggu
- Quick access ke produk favorit
- Search functionality

### 2. Shop
- Browse koleksi lengkap fashion items
- Filter dan sorting options
- Add to favorites/wishlist
- Real-time product details

### 3. Product Detail
- Detailed product information
- User reviews dan recommendations
- Heart dan bookmark functionality
- Tags untuk kategori produk
- Virtual try-on integration

### 4. Virtual Try-On (VTO)
- Augmented reality try-on experience
- Interactive 2D manekin
- Category-based outfit customization
- "Fit Perfectly" preview

### 5. Digital Wardrobe
- Organize pakaian berdasarkan kategori
- View item counts per kategori
- Scan pakaian baru
- Easy management interface

### 6. Profile
- User profile management
- Skin tone preferences
- Account settings
- Logout functionality

### 7. PWA Features
- Installable on home screen
- Works offline
- Fast loading with caching
- Push notifications ready

## 🛠 Tech Stack

### Frontend
- **Framework**: Next.js 16+ (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS v4
- **Icons**: lucide-react
- **PWA**: next-pwa
- **State Management**: Client-side useState (dapat diperluas dengan Zustand)

### Build & Deploy
- **Package Manager**: pnpm (recommended) atau npm
- **Build Tool**: Turbopack (Next.js 16)
- **Deploy**: Vercel (optimal untuk Next.js)

### Browser Support
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari 14+, Chrome Android)

## 🚀 Instalasi Lokal

### Prerequisites
Pastikan Anda memiliki:
- Node.js 18+ atau lebih baru
- pnpm 8+, npm 9+, atau yarn 4+
- Git

### Step-by-step Installation

#### 1. Clone Repository
\`\`\`bash
git clone https://github.com/yourusername/lokafit-frontend.git
cd lokafit-frontend
\`\`\`

#### 2. Install Dependencies
\`\`\`bash
# Menggunakan pnpm (recommended)
pnpm install

# Atau menggunakan npm
npm install

# Atau menggunakan yarn
yarn install
\`\`\`

#### 3. Setup Environment Variables
Buat file `.env.local` di root directory:
\`\`\`bash
cp .env.example .env.local
\`\`\`

Edit `.env.local`:
\`\`\`env
# Next.js
NEXT_PUBLIC_APP_URL=http://localhost:3000

# Supabase (untuk integrasi database & auth)
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key

# Backend API (untuk AI features)
NEXT_PUBLIC_API_URL=http://localhost:8000
\`\`\`

#### 4. Jalankan Development Server
\`\`\`bash
pnpm dev
\`\`\`

Aplikasi akan berjalan di `http://localhost:3000`

#### 5. Build Production
\`\`\`bash
pnpm build
pnpm start
\`\`\`

## 📂 Struktur Proyek

\`\`\`
lokafit-frontend/
├── app/
│   ├── (main)/                    # Main app layout dengan bottom navigation
│   │   ├── page.tsx              # Home page
│   │   ├── layout.tsx            # Main layout
│   │   ├── shop/
│   │   │   └── page.tsx          # Shop page
│   │   ├── product/
│   │   │   └── [id]/
│   │   │       └── page.tsx      # Product detail page
│   │   ├── try-on/
│   │   │   └── page.tsx          # Virtual try-on page
│   │   ├── wardrobe/
│   │   │   └── page.tsx          # Digital wardrobe page
│   │   └── profile/
│   │       └── page.tsx          # Profile page
│   ├── layout.tsx                # Root layout
│   └── globals.css               # Global styles
│
├── components/
│   ├── navigation/
│   │   └── bottom-navigation.tsx # Bottom navigation bar
│   ├── ui/                       # Reusable UI components
│   └── ...
│
├── lib/
│   ├── pwa.ts                    # PWA utilities
│   └── ...
│
├── public/
│   ├── manifest.json             # PWA manifest
│   ├── sw.js                     # Service worker
│   ├── offline.html              # Offline fallback page
│   └── icons/                    # App icons
│
├── .env.local                    # Environment variables (local)
├── .env.example                  # Environment template
├── next.config.ts                # Next.js configuration
├── tsconfig.json                 # TypeScript configuration
├── tailwind.config.ts            # Tailwind CSS configuration
├── package.json                  # Dependencies
└── README.md                     # This file
\`\`\`

## 💻 Panduan Penggunaan

### Development Workflow

#### 1. Membuat Component Baru
\`\`\`bash
# Buat folder di components/
mkdir components/my-component

# Buat component file
echo "export default function MyComponent() { return <div>Hello</div> }" > components/my-component.tsx
\`\`\`

#### 2. Menambah Page Baru
\`\`\`bash
# Buat folder di app/(main)/
mkdir app/(main)/new-page

# Buat page.tsx
touch app/(main)/new-page/page.tsx
\`\`\`

#### 3. Update Styling
Edit `app/globals.css` untuk mengubah design tokens dan theme colors.

#### 4. Menambah Route
Routes otomatis dibuat dari struktur folder di `app/(main)/`. Tidak perlu konfigurasi tambahan.

### Testing Locally

1. **Desktop Browser**: Buka Chrome DevTools (F12) → Device Toolbar
2. **Mobile Emulation**: Gunakan Chrome Mobile Emulation atau perangkat fisik
3. **Service Worker**: DevTools → Application → Service Workers

### PWA Testing

1. **Install sebagai App**:
   - Desktop: Chrome menu → "Install LokaFit"
   - Mobile: Tap share button → "Add to Home Screen"

2. **Offline Mode**:
   - DevTools → Network → Offline
   - App tetap bisa diakses

3. **Push Notifications** (when implemented):
   - DevTools → Application → Manifest
   - Check push notification permissions

## 🔧 PWA Setup

### Manifest File (`public/manifest.json`)
File ini mendefinisikan:
- App name dan icon
- Color scheme
- Start URL
- Display mode (standalone/fullscreen)

### Service Worker (`public/sw.js`)
Handles:
- Offline caching
- Network requests
- Background sync (optional)

### Installation prompts
- Browser otomatis menampilkan install prompt
- Custom prompt dapat diimplementasikan di `lib/pwa.ts`

## 🚀 Deployment

### Deploy ke Vercel (Recommended)

#### 1. Push ke GitHub
\`\`\`bash
git add .
git commit -m "Initial commit"
git push origin main
\`\`\`

#### 2. Connect ke Vercel
\`\`\`bash
npm install -g vercel
vercel
\`\`\`

#### 3. Environment Variables
Di Vercel dashboard:
- Settings → Environment Variables
- Tambahkan:
  - `NEXT_PUBLIC_SUPABASE_URL`
  - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
  - `NEXT_PUBLIC_API_URL`

#### 4. Deploy
\`\`\`bash
vercel --prod
\`\`\`

### Alternative Deployment

#### Netlify
\`\`\`bash
npm run build
npm install -g netlify-cli
netlify deploy --prod --dir=.next
\`\`\`

#### Self-hosted (VPS/Docker)
\`\`\`bash
# Build
npm run build

# Start
npm start
\`\`\`

Gunakan Node.js 18+ runtime.

## 📱 Mobile Installation Guide

### iOS
1. Buka Safari
2. Tap share button
3. Tap "Add to Home Screen"
4. Confirm

### Android
1. Buka Chrome
2. Tap menu (3 dots)
3. Tap "Install app"
4. Confirm

## 🔐 Security Best Practices

1. **Never commit `.env.local`** - gunakan `.env.example`
2. **Validate user input** di client dan server
3. **Use HTTPS only** untuk production
4. **Implement CSRF protection** jika ada forms
5. **Keep dependencies updated**: `pnpm update`

## 🐛 Troubleshooting

### Service Worker tidak teregister
- Clear browser cache: Settings → Privacy → Clear browsing data
- Check console di DevTools untuk errors

### PWA install prompt tidak muncul
- Ensures HTTPS (production) atau localhost (development)
- Check manifest.json valid
- Minimum 2 images di manifest

### Build error
\`\`\`bash
# Clear cache dan rebuild
pnpm clean
rm -rf .next
pnpm build
\`\`\`

### Port 3000 sudah digunakan
\`\`\`bash
# Gunakan port berbeda
pnpm dev -- -p 3001
\`\`\`

## 📚 Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [Tailwind CSS v4](https://tailwindcss.com)
- [Web App Manifest Spec](https://www.w3.org/TR/appmanifest/)
- [Service Workers API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)
- [PWA Checklist](https://developers.google.com/web/progressive-web-apps/checklist)

## 🤝 Kontribusi

Kami terbuka untuk kontribusi! Silahkan:

1. Fork repository
2. Buat branch feature: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push ke branch: `git push origin feature/amazing-feature`
5. Open Pull Request

## 📄 License

MIT License - lihat file [LICENSE](LICENSE) untuk detail

## 👥 Team

- **Creator**: Wyena Style Team
- **Contact**: support@lokafit.app

## 🗓️ Roadmap

- [ ] Backend AI integration (FastAPI)
- [ ] Authentication system (Supabase Auth)
- [ ] Database integration (Supabase PostgreSQL)
- [ ] Real virtual try-on (AR/WebGL)
- [ ] Push notifications
- [ ] Skin tone analysis
- [ ] AI outfit recommendations
- [ ] User reviews dan ratings
- [ ] Payment integration
- [ ] Multi-language support

## 📞 Support

Jika mengalami masalah:
1. Check [Troubleshooting](#troubleshooting) section
2. Search existing GitHub issues
3. Buat issue baru dengan detail lengkap

---

**Happy styling! 👗👔👠**
