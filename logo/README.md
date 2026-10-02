# Logo & Ikon Maserta

Warna: hitam `#0A0A0A`, putih `#FFFFFF`, biru `#2563EB`.

| File | Ukuran | Kegunaan |
|---|---|---|
| `maserta-icon.svg` / `.png` | vektor / 512 | Logo utama (latar terang) |
| `maserta-icon-dark.svg` / `.png` | vektor / 512 | Logo untuk latar gelap |
| `maserta-icon-square.svg` | vektor | Sumber ikon tanpa sudut bulat |
| `favicon.ico` | 16, 32, 48 | Favicon browser lama |
| `favicon.svg` | vektor | Favicon browser modern |
| `favicon-16x16.png`, `favicon-32x32.png` | 16, 32 | Favicon PNG |
| `apple-touch-icon.png` | 180 | Ikon home screen iOS |
| `android-chrome-192x192.png`, `android-chrome-512x512.png` | 192, 512 | Ikon Android / PWA |
| `maskable-icon-512x512.png` | 512 | Ikon adaptif Android (maskable) |
| `site.webmanifest` | — | Manifest PWA |

## Pemasangan

Salin semua file (kecuali `maserta-icon*` dan README ini) ke root web, lalu tambahkan di `<head>`:

```html
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#0A0A0A">
```
