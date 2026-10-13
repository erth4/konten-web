---
title: "Render-Blocking Resources: Cara Mengatasi CSS dan JavaScript"
meta_description: "Render-blocking resources menahan halaman tampil. Pelajari defer vs async, critical CSS, dan cara mengurangi CSS serta JavaScript yang memblokir render."
slug: "render-blocking-resources-cara-mengatasi-css-javascript"
focus_keyword: "render-blocking resources"
keywords:
  - render-blocking resources
  - eliminate render-blocking resources
  - defer dan async
  - critical CSS
  - JavaScript memblokir render
  - LCP
  - First Contentful Paint
  - Lighthouse
  - cara mempercepat website
  - Core Web Vitals
category: "Performa"
tags: ["Render-Blocking", "JavaScript", "CSS", "Performa"]
image_alt: "Ilustrasi garis waktu pemuatan halaman: skrip yang memblokir menahan tampilan, sedangkan skrip defer berjalan setelah halaman muncul"
date: "2026-10-13"
lang: "id"
---

# Render-Blocking Resources: Cara Mengatasi CSS dan JavaScript

Pernahkah Anda membuka sebuah situs dan menatap layar putih beberapa saat sebelum apa pun muncul, padahal koneksi internet baik-baik saja? Sering kali penyebabnya adalah **render-blocking resources**: berkas CSS atau JavaScript yang membuat browser menunda penggambaran halaman sampai berkas itu selesai diunduh dan diproses. Audit "Eliminate render-blocking resources" di Lighthouse dan PageSpeed Insights menyoroti persis hal ini. Artikel ini menjelaskan apa yang sebenarnya diblokir dan cara menanganinya tanpa merusak tampilan.

## Apa yang Diblokir dan Mengapa

Browser membaca HTML dari atas ke bawah untuk membangun struktur halaman. Ada dua jenis sumber daya yang bisa menghentikan proses ini atau penggambarannya.

**CSS memblokir render.** Browser tidak mau menampilkan halaman tanpa tahu gayanya, agar pengunjung tidak melihat teks polos yang tiba-tiba berubah. Maka setiap stylesheet di dalam head harus selesai dimuat sebelum halaman digambar.

**JavaScript sinkron memblokir parser.** Tag script biasa tanpa atribut membuat browser berhenti membaca HTML, mengunduh skrip, menjalankannya, baru melanjutkan. Skrip juga bisa menunggu CSS yang ada di atasnya, sehingga efeknya bertumpuk.

Dampaknya terasa pada metrik seperti First Contentful Paint dan Largest Contentful Paint, karena konten pertama baru muncul setelah semua penghalang tuntas.

## defer, async, dan Modul

Cara paling langsung untuk mengatasi skrip yang menghalangi adalah atribut pada tag script.

- **defer**: skrip diunduh sambil HTML terus dibaca, lalu dijalankan setelah dokumen selesai diurai, dengan urutan sesuai penulisan. Ini pilihan aman untuk sebagian besar skrip aplikasi.
- **async**: skrip diunduh sambil HTML dibaca, lalu dijalankan segera setelah selesai diunduh, tanpa jaminan urutan. Cocok untuk skrip yang berdiri sendiri, seperti penghitung statistik.
- **type="module"**: skrip modul berperilaku seperti defer secara bawaan.

Perhatikan satu jebakan: skrip yang saling bergantung jangan diberi async, karena urutannya tidak terjamin. Skrip inline yang memakai pustaka seperti jQuery juga bisa error jika pustakanya baru dimuat belakangan dengan defer. Ubah satu per satu dan uji setiap perubahan.

## Menangani CSS yang Memblokir

CSS tidak bisa begitu saja ditunda, tetapi ada beberapa cara mengurangi bebannya.

1. **Hapus CSS yang tidak dipakai.** Panel Coverage di Chrome DevTools menunjukkan bagian stylesheet yang tidak digunakan di halaman. Kerangka kerja yang dimuat penuh sering menyumbang banyak aturan yang tidak terpakai.
2. **Pisahkan berdasarkan kondisi.** Stylesheet untuk cetak dapat diberi atribut media="print" sehingga tidak memblokir penggambaran di layar.
3. **Critical CSS.** Aturan yang dibutuhkan untuk tampilan awal, yaitu bagian di atas lipatan layar, ditaruh langsung di dalam tag style pada head. Sisanya dimuat terpisah tanpa menghalangi. Teknik ini efektif, tetapi menambah kerumitan perawatan, jadi cocok untuk halaman yang benar-benar penting seperti beranda atau halaman landing.
4. **Minifikasi dan kompresi.** Berkas yang lebih kecil selesai diunduh lebih cepat. Gabungkan dengan kompresi Brotli atau Gzip dan cache browser.

## Font dan Skrip Pihak Ketiga

Font juga dapat menahan teks tampil. Atur font-display: swap pada deklarasi font agar teks langsung terbaca dengan font cadangan sampai font utama siap. Pastikan juga hanya memuat bobot dan gaya huruf yang benar-benar dipakai.

Skrip pihak ketiga seperti widget obrolan, pelacak iklan, dan tag manager sering menjadi penghalang terbesar karena berada di luar kendali Anda. Muat dengan async atau defer, tunda sampai ada interaksi pengguna bila memungkinkan, dan tinjau berkala apakah semuanya masih dibutuhkan. Setiap skrip yang tidak lagi dipakai adalah beban gratis yang bisa dibuang.

## Alur Kerja yang Disarankan

1. Jalankan Lighthouse atau PageSpeed Insights dan catat daftar berkas yang ditandai memblokir.
2. Buka tab Performance di DevTools untuk melihat kapan penggambaran pertama terjadi dan apa yang menunda.
3. Mulai dari skrip: tambahkan defer pada skrip aplikasi dan async pada skrip mandiri.
4. Bersihkan CSS tidak terpakai, lalu pertimbangkan critical CSS untuk halaman prioritas.
5. Uji semua fitur interaktif: menu, formulir, slider, dan keranjang belanja.
6. Ukur ulang dan bandingkan. Jika hasil tidak membaik, kembalikan perubahan terakhir dan coba pendekatan lain.

## Pengguna WordPress dan CMS

Pada WordPress, penyebab utamanya biasanya tema dan plugin yang memuat banyak berkas di setiap halaman. Plugin optimasi dapat menambahkan defer dan membuat critical CSS otomatis, tetapi hasilnya berbeda-beda per situs dan kadang merusak tampilan. Aktifkan satu fitur dalam satu waktu, uji di perangkat seluler, dan siapkan cara mudah untuk membatalkannya. Menonaktifkan plugin yang jarang dipakai sering memberi hasil lebih besar daripada trik teknis apa pun.

## Penutup

Render-blocking resources bukan musuh yang harus dihilangkan seluruhnya. Sebagian CSS memang wajib ada sebelum halaman digambar. Tujuannya adalah memastikan hanya yang benar-benar dibutuhkan untuk tampilan awal yang menghalangi, sementara sisanya menunggu giliran. Mulailah dari defer pada skrip, bersihkan CSS berlebih, dan ukur hasilnya di setiap langkah.
