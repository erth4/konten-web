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

Front matter `.md`: `title`, `meta_description`, `slug`, `focus_keyword`, `keywords` (hanya ID), `category`, `tags` (hanya ID), `date`, `lang`. File `.en.md` memakai `title`, `meta_description`, `slug`, `focus_keyword`, `category`, `date`, `lang: "en"`. Isi dimulai dengan `# Judul`, lalu `##` untuk subjudul. Markdown yang didukung skrip: `##`/`###`, paragraf, daftar `-` dan `1.`, `>`, dan `**tebal**`.

Aturan konten:
- Minimal 500 kata per bahasa. Versi Inggris ditulis natural, bukan terjemahan kata per kata.
- Topik harus unik: cek `artikel/**` dan `og/` dulu agar tidak dobel.
- Jangan mengarang statistik, kutipan, atau angka spesifik tanpa sumber.
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
- Artikel yang sudah terunggah tidak bisa diubah lewat API ini (hanya tambah). Perbaikan dilakukan lewat panel admin: `/admin/artikel/<id>/ubah`.

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
| 48 | `wawancara-kerja-pertanyaan-umum-cara-menjawab` | 2026-10-13 |
| 49 | `negosiasi-gaji-cara-menyiapkan-dan-menyampaikan` | 2026-10-13 |
| 50 | `cara-mengamankan-whatsapp-dari-pembajakan` | 2026-10-13 |
| 51 | `cara-memilih-kursus-online-yang-layak` | 2026-10-13 |
| 52 | `liburan-hemat-cara-menyusun-anggaran-perjalanan` | 2026-10-13 |

Artikel lain di `artikel/` mungkin sudah atau belum ada di situs; cek panel admin sebelum mengunggah ulang.
