---
title: "Resource Hints: Cara Memakai Preload, Preconnect, dan Prefetch"
meta_description: "Resource hints memberi tahu browser apa yang dibutuhkan lebih awal. Pahami preload, preconnect, dns-prefetch, prefetch, dan fetchpriority beserta jebakannya."
slug: "resource-hints-preload-preconnect-prefetch-cara-memakai"
focus_keyword: "resource hints"
keywords:
  - resource hints
  - preload
  - preconnect
  - dns-prefetch
  - prefetch
  - fetchpriority
  - optimasi LCP
  - kecepatan website
  - Core Web Vitals
  - optimasi gambar
category: "Performa"
tags: ["Resource Hints", "Preload", "Preconnect", "Performa"]
image_alt: "Ilustrasi halaman web menyiapkan koneksi lebih awal ke beberapa domain eksternal sebelum sumber daya diminta"
date: "2026-10-13"
lang: "id"
---

# Resource Hints: Cara Memakai Preload, Preconnect, dan Prefetch

Browser menemukan sumber daya halaman secara bertahap. Ia membaca HTML, baru mengetahui ada stylesheet, lalu setelah stylesheet diunduh baru tahu ada font dan gambar latar di dalamnya. Setiap penemuan terlambat berarti unduhan yang dimulai terlambat. **Resource hints** adalah petunjuk yang Anda tulis di halaman agar browser tahu lebih awal apa yang akan dibutuhkan, sehingga koneksi dan unduhan bisa dimulai tanpa menunggu. Dipakai tepat, teknik ini memangkas jeda yang sebenarnya tidak perlu. Dipakai sembarangan, ia justru memboroskan bandwidth.

## Mengapa Penemuan Terlambat Menjadi Masalah

Sebelum mengunduh apa pun dari domain lain, browser harus menyelesaikan pencarian DNS, membuka koneksi TCP, dan menjalankan negosiasi TLS untuk HTTPS. Tahapan ini memakan waktu sebelum satu byte konten pun diterima. Jika font atau skrip Anda ada di domain pihak ketiga, tahapan itu baru dimulai ketika browser menemukan rujukannya. Resource hints memindahkan sebagian pekerjaan itu ke awal.

## Lima Petunjuk yang Perlu Dikenal

**dns-prefetch** hanya meminta browser menyelesaikan pencarian DNS suatu domain lebih dulu. Ringan dan didukung luas, cocok sebagai cadangan untuk domain yang mungkin dipakai.

**preconnect** melangkah lebih jauh: DNS, koneksi, dan TLS disiapkan sekaligus. Gunakan untuk domain pihak ketiga yang pasti dibutuhkan di awal pemuatan, seperti layanan font atau CDN gambar. Untuk font, tambahkan atribut crossorigin karena font diambil dengan mode CORS. Koneksi yang disiapkan tetapi tidak dipakai dalam beberapa saat akan ditutup, jadi jangan menyebarnya ke banyak domain.

**preload** meminta browser mengunduh satu sumber daya tertentu segera, dengan prioritas tinggi, karena Anda tahu halaman ini membutuhkannya. Atribut as wajib diisi agar browser tahu jenisnya, misalnya as="font", as="style", atau as="image". Font yang di-preload juga perlu atribut crossorigin, walau berasal dari domain yang sama.

**prefetch** berbeda sifatnya: ia mengunduh sumber daya yang mungkin dibutuhkan di halaman berikutnya, dengan prioritas rendah saat browser sedang menganggur. Contohnya mengambil skrip halaman checkout ketika pengunjung sudah berada di keranjang.

**fetchpriority** bukan petunjuk koneksi, melainkan penanda prioritas. Atribut fetchpriority="high" pada gambar utama membantu browser mengunduhnya lebih dulu, sedangkan fetchpriority="low" menurunkan prioritas gambar yang tidak mendesak.

## Contoh Kasus yang Masuk Akal

- **Gambar utama di beranda.** Gambar pahlawan sering menjadi elemen LCP. Jika gambar dipanggil lewat CSS, browser baru tahu setelah CSS diurai. Memberi preload atau memindahkannya ke tag img dengan fetchpriority="high" membuatnya diunduh lebih awal.
- **Font khusus.** Preload satu atau dua berkas font yang dipakai pada teks di atas lipatan, bersama font-display: swap agar teks tidak tertahan.
- **Layanan eksternal.** Jika situs memakai domain terpisah untuk gambar atau skrip penting, preconnect ke domain tersebut menghemat waktu awal.
- **Alur berurutan.** Pada toko daring, prefetch halaman pembayaran dari halaman keranjang mempercepat langkah berikutnya.

## Jebakan yang Harus Dihindari

Pertama, jangan mem-preload terlalu banyak. Setiap preload bersaing dengan sumber daya penting lain untuk bandwidth yang sama. Jika semuanya dibuat prioritas, tidak ada yang diprioritaskan.

Kedua, preload yang tidak terpakai adalah pemborosan. Browser biasanya menampilkan peringatan di konsol jika sumber daya yang di-preload tidak dipakai. Pastikan URL dan atributnya persis sama dengan yang dipakai halaman, termasuk crossorigin pada font, atau berkas akan diunduh dua kali.

Ketiga, jangan memberi loading="lazy" pada gambar LCP. Lazy loading cocok untuk gambar di bawah lipatan, tetapi pada gambar utama justru menunda tampilan.

Keempat, ingat bahwa dukungan dan perilaku tiap petunjuk dapat berbeda antarbrowser. Selalu uji, jangan mengandalkan asumsi.

## Cara Menerapkan dan Mengukur

Petunjuk ini ditulis sebagai tag link di dalam head, atau dikirim lewat header HTTP Link dari server. Pada WordPress dan CMS lain, tema atau plugin performa kadang menyediakan pengaturannya, tetapi tetap periksa hasil akhirnya di sumber halaman.

Untuk mengukur, buka tab Network di DevTools dan perhatikan waterfall: apakah sumber daya penting kini mulai lebih awal? Bandingkan nilai LCP sebelum dan sesudah di Lighthouse, dan lihat di data pengguna nyata seperti laporan Chrome UX jika situs Anda memilikinya. Ubah satu hal pada satu waktu supaya jelas mana yang berpengaruh.

## Penutup

Resource hints adalah alat presisi, bukan tombol percepatan otomatis. Prinsipnya sederhana: beri tahu browser hal yang pasti Anda butuhkan lebih cepat, dan biarkan sisanya mengalir seperti biasa. Mulailah dengan satu kandidat, misalnya gambar LCP atau domain font, uji dampaknya, lalu tambahkan hanya jika datanya mendukung.
