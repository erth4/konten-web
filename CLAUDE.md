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
| 66 | `deskripsi-produk-toko-online-yang-membuat-pembeli-yakin` | 2026-10-17 |
| 67 | `kebijakan-retur-refund-toko-online-cara-menyusun` | 2026-10-17 |
| 68 | `ulasan-pelanggan-toko-online-cara-mendapat-menanggapi` | 2026-10-17 |
| 69 | `chatgpt-gemini-claude-cara-memilih-asisten-ai` | 2026-10-17 |
| 70 | `cara-menulis-prompt-ai-yang-jelas-hasil-akurat` | 2026-10-17 |
| 71 | `proxy-vs-vpn-perbedaan-fungsi-kapan-dipakai` | 2026-10-17 |
| 72 | `search-intent-jenis-cara-menyesuaikan-konten` | 2026-10-18 |
| 73 | `google-trends-cara-riset-topik-artikel` | 2026-10-18 |
| 74 | `seo-mesin-pencari-alternatif-dan-jawaban-ai` | 2026-10-18 |
| 75 | `judul-produk-shopee-cara-menulis-agar-mudah-dicari` | 2026-10-19 |
| 76 | `canva-desain-gambar-produk-promosi-toko-online` | 2026-10-19 |
| 77 | `template-balasan-chat-pembeli-toko-online-cepat-ramah` | 2026-10-19 |
| 78 | `kurs-dolar-rupiah-cara-membaca-dan-dampaknya` | 2026-10-20 |
| 79 | `ihsg-adalah-cara-membaca-untuk-pemula` | 2026-10-20 |
| 80 | `langganan-digital-cara-mengelola-agar-tidak-boros` | 2026-10-20 |
| 81 | `cek-bansos-cara-cek-penerima-lewat-situs-resmi-kemensos` | 2026-10-21 |
| 82 | `cara-membaca-prakiraan-cuaca-bmkg-info-bmkg` | 2026-10-21 |
| 83 | `terjemahan-online-tips-hasil-akurat-google-translate` | 2026-10-21 |
| 84 | `google-drive-berbagi-file-aman-izin-akses` | 2026-10-22 |
| 85 | `word-ke-pdf-pdf-ke-word-cara-konversi-aman` | 2026-10-22 |
| 86 | `enkripsi-end-to-end-whatsapp-telegram-cara-kerja` | 2026-10-22 |
| 87 | `youtube-seo-judul-deskripsi-bab-thumbnail` | 2026-10-23 |
| 88 | `hreflang-situs-dua-bahasa-cara-memasang` | 2026-10-23 |
| 89 | `konten-tipis-thin-content-cara-memperbaiki` | 2026-10-23 |
| 90 | `konten-tiktok-untuk-jualan-online-ide-cara-membuat` | 2026-10-24 |
| 91 | `instagram-untuk-toko-online-bio-highlight-konten` | 2026-10-24 |
| 92 | `menentukan-harga-jual-produk-hitung-margin-untung` | 2026-10-24 |
| 93 | `paylater-cara-pakai-aman-hindari-gagal-bayar` | 2026-10-25 |
| 94 | `belanja-impulsif-online-cara-mengendalikan` | 2026-10-25 |
| 95 | `anggaran-freelancer-penghasilan-tidak-tetap` | 2026-10-25 |
| 96 | `google-scholar-cara-mencari-jurnal-dan-mengutip` | 2026-10-26 |
| 97 | `google-maps-tips-peta-offline-bagikan-lokasi` | 2026-10-26 |
| 98 | `gmail-merapikan-kotak-masuk-label-filter` | 2026-10-26 |
| 99 | `msci-standalone-market-indonesia-arti-bagi-investor` | 2026-10-16 |
| 100 | `stop-the-wedding-tanda-hubungan-tidak-sehat-cara-menyikapi` | 2026-10-19 |
| 101 | `optogenetika-nobel-kedokteran-2026-cara-kerja` | 2026-10-21 |
| 102 | `titik-kritis-iklim-pemanasan-global-dipercepat-artinya` | 2026-10-21 |
| 103 | `misi-mmx-jepang-phobos-sampel-bulan-mars` | 2026-10-21 |
| 104 | `kecemasan-terhadap-ai-survei-chapman-2026-cara-menyikapi` | 2026-10-21 |
| 105 | `olahraga-sebagai-resep-pernyataan-acc-kesehatan-jantung` | 2026-10-21 |
| 106 | `teleskop-antariksa-roman-nasa-misi-yang-dicari` | 2026-10-21 |

Artikel lain di `artikel/` mungkin sudah atau belum ada di situs; cek panel admin sebelum mengunggah ulang.
