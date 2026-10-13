# konten-web

Repo konten artikel untuk https://maserta.my.id. Artikel ditulis di sini, lalu diunggah ke API Maserta.

## Struktur

- `artikel/<folder>/<slug>.md` (Indonesia) dan `<slug>.en.md` (Inggris), keduanya dengan slug yang sama.
- `og/<slug>.jpg`: gambar artikel, 1200x630, dipakai untuk kedua bahasa.
- `tools/upload-artikel.py`: skrip unggah ke API.
- `hero/`, `logo/`, `produk/`, `tentang/`, `screenshot/`: aset situs, jangan diubah untuk tugas artikel.

Folder artikel dan slug kategori API tidak selalu sama:

| Folder `artikel/` | Slug kategori API | Nama |
|---|---|---|
| `keuangan` | `keuangan` | Keuangan |
| `toko-online` | `toko` | Toko Online |
| `teknologi` | `teknologi` | Teknologi |
| `seo` | `seo` | SEO |
| `performa` | `performa` | Performa |
| `gaya-hidup` | `gaya-hidup-kesehatan-mental` | Gaya Hidup & Kesehatan Mental |
| `lainnya` | `lainnya` | Lainnya |

Daftar resmi selalu bisa diambil dari `GET /admin/api/kategori-artikel` (butuh login).

## Format artikel

Front matter `.md`: `title`, `meta_description`, `slug`, `focus_keyword`, `keywords` (hanya ID), `category`, `tags` (hanya ID), `date`, `lang`. File `.en.md` memakai `title`, `meta_description`, `slug`, `focus_keyword`, `category`, `date`, `lang: "en"`. Isi dimulai dengan `# Judul`, lalu `##` untuk subjudul. Markdown yang didukung skrip: `##`/`###`, paragraf, daftar `-` dan `1.`, `>`, dan `**tebal**`. Tabel Markdown tidak didukung (server membersihkan HTML), pakai daftar.

Aturan konten:
- Minimal 500 kata per bahasa. Versi Inggris ditulis natural, bukan terjemahan kata per kata.
- Topik harus unik: cek `artikel/**` dan `og/` dulu agar tidak dobel.
- Jangan mengarang statistik, kutipan, atau angka spesifik tanpa sumber.
- Untuk topik yang bergantung pada fakta terkini (jadwal, aturan, nominal, tokoh), verifikasi dengan pencarian web dulu. Jika tidak bisa dibuktikan, ganti topiknya atau tulis tanpa klaim spesifik dan arahkan pembaca ke sumber resmi.
- SEO: kata kunci fokus ada di judul (maks ~70 karakter), meta_description (maks 160 karakter), dan paragraf pertama; sertakan `image_alt` yang sesuai isi gambar di kedua file bahasa.
- `meta_description` 30-300 karakter (batas API untuk ringkasan); `title` maksimal 160 karakter.
- Opsional: `image_alt: "..."` di front matter untuk teks alternatif gambar. Tanpa itu, skrip memakai judul.

Gambar OG: gaya sama dengan `og/*.jpg` yang ada (latar `#F8FAF9`, logo maserta kiri atas, pil kategori, judul dua warna `#183541` dan `#166B70`, panel ilustrasi kanan, tombol "Panduan <kategori>", `maserta.my.id` di kiri bawah). Palet lengkap ada di `logo/README.md`. Cek hasil gambar secara visual sebelum diunggah.

## Mengunggah ke API Maserta

Dokumentasi: https://maserta.my.id/api/docs

Kredensial admin ada di environment sebagai `MASERTA_USER` dan `MASERTA_PASS` (cadangan: `username` dan `password`). Jangan menulis kredensial ke file, commit, atau chat, dan jangan meminta pengguna menempelkannya. Jika variabel kosong, minta pengguna menambahkannya di pengaturan environment, lalu mulai sesi baru.

```bash
# uji kering: validasi dan ukuran saja, tanpa login
python3 -I tools/upload-artikel.py --dir keuangan --category keuangan \
  --published-at 2026-10-12T09:00 --dry-run slug-satu slug-dua

# unggah sungguhan
python3 -I tools/upload-artikel.py --dir keuangan --category keuangan \
  --published-at 2026-10-12T09:00 slug-satu slug-dua
```

Catatan:
- `--published-at` memakai zona Asia/Jakarta. Pakai jam 09:00 supaya tanggalnya sama di WIB maupun UTC. Tanggal mendatang berarti artikel dijadwalkan; tanggal yang sudah lewat terbit langsung.
- Status selalu `published`. Gunakan tanggal sesuai permintaan pengguna; jika tidak disebut, tanyakan atau pakai hari berikutnya dan sebutkan asumsinya.
- API tidak punya kunci idempotensi dan skrip tidak mengulang kirim otomatis. Jika koneksi putus setelah pengiriman, periksa dulu apakah artikelnya sudah ada sebelum mengunggah ulang. Slug duplikat ditolak dengan 422.
- Batas: unggah 60 percobaan per 10 menit, request maksimal 8 MB, gambar maksimal 5 MB (JPEG/PNG/WebP). Login gagal 5 kali per nama pengguna dalam 15 menit akan diblokir, jadi jangan mencoba kredensial berulang.
- Artikel yang sudah terunggah tidak bisa diubah lewat API ini (hanya tambah, tidak ada hapus). Untuk mengganti tanggal terbit, pakai `python3 -I tools/ubah-tanggal-artikel.py 2026-10-14T09:00 <id> ...` (mengirim ulang form edit admin dan hanya mengubah `published_at`; teruji pada id 48-52). Perbaikan lain dilakukan lewat panel admin: `/admin/artikel/<id>/ubah`.

## Git

Setelah artikel dan gambar siap dan diunggah, commit dengan format konvensional (mis. `feat(artikel): add three bilingual ... articles with OG images`) dan push ke `main` bila pengguna memintanya.

## Riwayat unggahan

| ID | Slug | Terbit |
|---|---|---|
| 39 | `cara-memulai-toko-online-dari-nol-untuk-pemula` | 2026-10-11 |
| 40 | `foto-produk-toko-online-pakai-hp-tanpa-studio` | 2026-10-11 |
| 41 | `mengelola-stok-toko-online-cegah-oversell` | 2026-10-11 |
| 42 | `cara-melunasi-utang-metode-snowball-avalanche` | 2026-10-12 |
| 43 | `kartu-kredit-cara-pakai-bijak-hindari-jerat-bunga` | 2026-10-12 |
| 44 | `mencatat-pengeluaran-harian-cara-memulai` | 2026-10-12 |
| 45 | `penipuan-lowongan-kerja-ciri-ciri-cara-menghindari` | 2026-10-13 |
| 46 | `cara-membuat-cv-lolos-seleksi-awal` | 2026-10-13 |
| 47 | `cara-mengecek-hoaks-sebelum-membagikan-informasi` | 2026-10-13 |
| 48 | `wawancara-kerja-pertanyaan-umum-cara-menjawab` | 2026-10-14 |
| 49 | `negosiasi-gaji-cara-menyiapkan-dan-menyampaikan` | 2026-10-14 |
| 50 | `cara-mengamankan-whatsapp-dari-pembajakan` | 2026-10-14 |
| 51 | `cara-memilih-kursus-online-yang-layak` | 2026-10-14 |
| 52 | `liburan-hemat-cara-menyusun-anggaran-perjalanan` | 2026-10-14 |
| 53 | `hujan-meteor-orionid-2026-jadwal-cara-mengamati` | 2026-10-15 |
| 54 | `pekan-antariksa-dunia-2026-tema-rocket-revolution` | 2026-10-15 |
| 55 | `banjir-musim-hujan-persiapan-sebelum-saat-sesudah` | 2026-10-15 |
| 56 | `karhutla-kabut-asap-cara-melindungi-kesehatan` | 2026-10-15 |
| 57 | `simpanan-aman-di-bank-penjaminan-lps-cek-izin-ojk` | 2026-10-15 |
| 58 | `dana-pendidikan-anak-cara-menyiapkan-sejak-dini` | 2026-10-15 |
| 59 | `mcp-task-manager-kelola-tugas-agen-ai` | 2026-10-13 |
| 60 | `cache-control-browser-caching-cara-mengatur-header` | 2026-10-13 |
| 61 | `render-blocking-resources-cara-mengatasi-css-javascript` | 2026-10-13 |
| 62 | `resource-hints-preload-preconnect-prefetch-cara-memakai` | 2026-10-13 |
| 63 | `tautan-internal-internal-link-cara-menyusun-seo` | 2026-10-16 |
| 64 | `canonical-url-konten-duplikat-cara-mengatasi` | 2026-10-16 |
| 65 | `robots-txt-sitemap-xml-fungsi-cara-mengatur` | 2026-10-16 |

Artikel lain di `artikel/` mungkin sudah atau belum ada di situs; cek panel admin sebelum mengunggah ulang.
