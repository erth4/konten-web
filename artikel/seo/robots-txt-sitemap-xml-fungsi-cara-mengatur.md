---
title: "Robots.txt dan Sitemap XML: Fungsi, Perbedaan, dan Cara Mengatur"
meta_description: "Robots.txt mengatur apa yang boleh dirayapi, sitemap XML menunjukkan halaman penting. Pahami fungsi, perbedaan, contoh aturan, dan kesalahan yang merusak SEO."
slug: "robots-txt-sitemap-xml-fungsi-cara-mengatur"
focus_keyword: "robots.txt"
keywords:
  - robots.txt
  - sitemap XML
  - cara membuat sitemap
  - crawl
  - noindex
  - Google Search Console
  - pengindeksan
  - SEO teknis
  - perayapan website
  - sitemap index
category: "SEO"
tags: ["Robots.txt", "Sitemap XML", "SEO Teknis", "SEO"]
image_alt: "Ilustrasi robot perayap di gerbang situs dengan peta halaman dan daftar jalur yang diizinkan dan dilarang"
date: "2026-10-16"
lang: "id"
---

# Robots.txt dan Sitemap XML: Fungsi, Perbedaan, dan Cara Mengatur

Dua berkas kecil di root situs berperan besar dalam cara mesin pencari memperlakukan website Anda: **robots.txt** dan sitemap XML. Keduanya sering disebut berdampingan dan sering tertukar fungsinya. Robots.txt memberi tahu perayap bagian mana yang boleh atau tidak boleh dikunjungi, sedangkan sitemap XML menyodorkan daftar halaman yang ingin Anda tunjukkan. Salah kaprah di sini bisa berakibat serius, mulai dari halaman penting yang tak pernah dirayapi sampai halaman yang justru tampil padahal ingin disembunyikan.

## Fungsi Robots.txt

Robots.txt adalah berkas teks biasa yang harus berada di root domain, misalnya alamatanda.com/robots.txt. Perayap yang patuh, termasuk Googlebot, membacanya sebelum menjelajah situs. Isinya berupa aturan untuk agen pengguna tertentu.

Direktif yang paling umum:

- **User-agent**: menentukan perayap mana yang disasar. Tanda bintang berarti semua perayap.
- **Disallow**: melarang perayapan jalur tertentu.
- **Allow**: mengizinkan jalur tertentu, berguna sebagai pengecualian di dalam jalur yang dilarang.
- **Sitemap**: menunjuk alamat lengkap sitemap XML Anda.

Contoh sederhana yang melarang folder admin untuk semua perayap dan menunjuk sitemap berbunyi: User-agent: *, baris berikutnya Disallow: /admin/, lalu Sitemap: https://alamatanda.com/sitemap.xml. Perhatikan bahwa penulisan jalur membedakan huruf besar dan kecil.

## Hal yang Tidak Dilakukan Robots.txt

Ini bagian yang paling sering disalahpahami. Robots.txt mengatur **perayapan**, bukan **pengindeksan**. Halaman yang dilarang di robots.txt masih dapat muncul di hasil pencarian tanpa deskripsi jika ada situs lain yang menautkannya. Untuk menjaga halaman tidak masuk indeks, gunakan meta robots noindex atau header X-Robots-Tag, dan pastikan halaman itu tetap boleh dirayapi, sebab perayap harus bisa membaca instruksi noindex tersebut.

Robots.txt juga bukan alat keamanan. Berkasnya publik, sehingga mencantumkan jalur rahasia di sana justru menunjukkannya kepada siapa saja. Lindungi data sensitif dengan autentikasi, bukan dengan Disallow.

Terakhir, jangan memblokir berkas CSS dan JavaScript yang dibutuhkan untuk menampilkan halaman. Google perlu memuatnya untuk memahami tampilan dan isi halaman.

## Fungsi Sitemap XML

Sitemap XML adalah daftar URL yang ingin Anda tampilkan kepada mesin pencari, dalam format yang mudah dibaca mesin. Ia membantu penemuan halaman, terutama untuk situs besar, situs baru dengan sedikit tautan masuk, atau halaman yang jarang tertaut dari halaman lain. Sitemap tidak menjamin halaman dirayapi atau diindeks, tetapi memudahkan penemuannya.

Isi setiap entri minimal alamat lengkap pada elemen loc. Elemen lastmod berisi tanggal perubahan terakhir dan berguna jika akurat. Google menyatakan mengabaikan elemen priority dan changefreq, jadi tidak perlu repot mengisinya.

Satu berkas sitemap dibatasi maksimal 50.000 URL atau 50 MB tanpa kompresi. Situs yang lebih besar memakai sitemap index, yaitu berkas yang mendaftar beberapa sitemap.

## Perbedaan Singkat

- Robots.txt melarang atau mengizinkan perayapan. Sitemap menyarankan halaman untuk ditemukan.
- Robots.txt satu berkas per host. Sitemap bisa banyak berkas.
- Robots.txt tidak menjamin halaman tidak terindeks. Sitemap tidak menjamin halaman terindeks.

## Cara Menyusun Sitemap yang Sehat

1. **Masukkan hanya halaman yang ingin diindeks.** Hindari URL yang dialihkan, 404, diberi noindex, atau bukan versi canonical.
2. **Pakai alamat utama yang konsisten**, termasuk https dan versi www atau non-www yang Anda pilih.
3. **Isi lastmod hanya jika benar.** Mengubahnya setiap hari tanpa perubahan nyata membuat sinyalnya tidak berguna.
4. **Hasilkan otomatis.** Plugin SEO WordPress dan banyak kerangka kerja dapat membuatnya. Pada situs PHP buatan sendiri, buat skrip yang membaca daftar halaman dari basis data.
5. **Daftarkan.** Kirim sitemap di Google Search Console dan cantumkan juga lewat baris Sitemap di robots.txt.

## Kesalahan Fatal yang Sering Terjadi

- Disallow: / yang tertinggal dari masa pengembangan, sehingga seluruh situs terblokir.
- Memblokir folder yang berisi gambar, CSS, atau JavaScript penting.
- Mengandalkan robots.txt untuk menyembunyikan halaman dari hasil pencarian.
- Sitemap berisi ribuan URL yang error atau dialihkan.
- Lupa memperbarui sitemap setelah struktur situs berubah.

## Cara Memeriksa

Buka alamatanda.com/robots.txt di browser dan pastikan isinya sesuai. Laporan robots.txt di Google Search Console menunjukkan berkas yang dibaca Google dan masalah penguraiannya. Pada laporan Sitemap, periksa status pengiriman, jumlah URL yang ditemukan, dan kesalahan yang dilaporkan. Setelah mengubah aturan, uji beberapa URL penting dengan alat Pemeriksaan URL agar yakin tidak terblokir.

## Penutup

Robots.txt dan sitemap XML sederhana, tetapi salah satu kesalahan kecil bisa berdampak luas. Pegang prinsipnya: robots.txt untuk mengatur perayapan, noindex untuk menjaga halaman dari indeks, dan sitemap sebagai daftar halaman terbaik Anda. Periksa kedua berkas setiap kali ada perubahan besar pada situs.
