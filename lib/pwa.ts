// PWA Service Worker registration utility
export async function registerServiceWorker() {
  if ('serviceWorker' in navigator) {
    try {
      const registration = await navigator.serviceWorker.register('/sw.js', {
        scope: '/',
      })
      console.log('Service Worker registered:', registration)
      return registration
    } catch (error) {
      console.error('Service Worker registration failed:', error)
    }
  }
}

// Check if app is installed as PWA
export function isPWAInstalled() {
  return window.matchMedia('(display-mode: standalone)').matches ||
    (window.navigator as any).standalone === true
}

// Request PWA installation
export async function requestPWAInstall() {
  if ((window as any).deferredPrompt) {
    (window as any).deferredPrompt.prompt()
    const { outcome } = await (window as any).deferredPrompt.userChoice
    (window as any).deferredPrompt = null
    return outcome === 'accepted'
  }
  return false
}
