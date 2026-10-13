---
title: "Browser Caching: Cara Mengatur Cache-Control agar Situs Cepat"
meta_description: "Browser caching mempercepat kunjungan ulang. Pahami Cache-Control, ETag, dan versi nama berkas, lalu atur header cache dengan benar tanpa tampilan basi."
slug: "cache-control-browser-caching-cara-mengatur-header"
focus_keyword: "browser caching"
keywords:
  - browser caching
  - Cache-Control
  - header cache
  - ETag
  - leverage browser caching
  - cache aset statis
  - kecepatan website
  - Core Web Vitals
  - CDN
  - PageSpeed Insights
category: "Performa"
tags: ["Browser Caching", "Cache-Control", "Kecepatan Website", "Performa"]
image_alt: "Ilustrasi browser menyimpan berkas situs di cache lokal sehingga tidak perlu mengunduh ulang dari server"
date: "2026-10-13"
lang: "id"
---

# Browser Caching: Cara Mengatur Cache-Control agar Situs Cepat

Kunjungan pertama ke sebuah situs selalu paling berat, karena browser harus mengunduh HTML, CSS, JavaScript, font, dan gambar. Kunjungan kedua seharusnya jauh lebih ringan, sebab sebagian besar berkas itu tidak berubah. Itulah gunanya **browser caching**: browser menyimpan salinan berkas di perangkat pengunjung dan memakainya lagi tanpa meminta ke server. Masalahnya, browser hanya tahu berapa lama boleh menyimpan jika server memberi tahu lewat header HTTP. Tanpa aturan yang jelas, hasilnya bisa berupa unduhan berulang yang sia-sia atau, sebaliknya, tampilan lama yang tidak ikut diperbarui.

## Cara Kerja Cache di Browser

Saat browser meminta sebuah berkas, server membalas dengan isi berkas beserta header. Dari header itu browser memutuskan apa yang dilakukan pada permintaan berikutnya. Ada dua kemungkinan.

Pertama, salinan masih dianggap segar. Browser memakainya langsung dari penyimpanan lokal tanpa menghubungi server sama sekali. Ini yang tercepat.

Kedua, salinan sudah kedaluwarsa atau harus divalidasi. Browser bertanya kepada server apakah berkas berubah, dengan membawa penanda versi yang pernah diterimanya. Jika tidak berubah, server cukup membalas status 304 Not Modified tanpa mengirim isi berkas. Jika berubah, server mengirim versi baru.

## Header yang Perlu Dikenal

- **Cache-Control**: header utama untuk mengatur perilaku cache. Nilai yang sering dipakai antara lain max-age (lama salinan dianggap segar, dalam detik), public dan private (boleh tidaknya disimpan oleh cache bersama seperti CDN), no-cache (boleh disimpan, tetapi wajib divalidasi dulu), no-store (jangan simpan sama sekali), dan immutable (berkas tidak akan berubah selama masa segarnya).
- **ETag**: penanda versi berkas. Browser mengirimkannya kembali lewat header If-None-Match untuk validasi.
- **Last-Modified**: waktu perubahan terakhir berkas. Pasangannya adalah If-Modified-Since.
- **Expires**: cara lama menentukan tanggal kedaluwarsa. Jika Cache-Control: max-age ada, browser modern mengutamakannya.

Salah kaprah yang sering muncul: no-cache bukan berarti "jangan disimpan". Artinya "simpan, tetapi tanyakan dulu ke server sebelum dipakai". Untuk melarang penyimpanan, gunakan no-store.

## Bedakan Aset Statis dan HTML

Satu aturan untuk semua jenis berkas hampir pasti keliru, karena sifatnya berbeda.

Aset statis seperti CSS, JavaScript, font, dan gambar jarang berubah. Berkas jenis ini cocok diberi masa simpan panjang, misalnya Cache-Control: public, max-age=31536000, immutable, yang setara dengan satu tahun.

Halaman HTML justru sering berubah dan memuat konten terbaru. Pilih masa simpan pendek, atau no-cache agar selalu divalidasi dengan ETag. Halaman yang berisi data pribadi pengguna, seperti keranjang belanja atau dasbor akun, sebaiknya memakai private atau no-store supaya tidak tersimpan di cache bersama.

## Versi pada Nama Berkas

Masa simpan satu tahun terdengar berisiko: bagaimana jika Anda memperbarui CSS besok? Jawabannya adalah menaruh versi pada nama berkas, misalnya app.3f9a1c.css, dengan kode yang dihasilkan dari isi berkas. Saat isi berubah, nama berubah, dan HTML merujuk ke nama baru. Browser menganggapnya berkas yang belum pernah diunduh, sementara berkas lama tetap aman di cache untuk halaman yang masih memakainya.

Cara ini umum dihasilkan oleh alat build seperti Vite atau webpack. Pada situs PHP sederhana, parameter versi seperti style.css?v=20261013 juga bisa dipakai, walau sebagian cache perantara kurang konsisten memperlakukan parameter query. Nama berkas yang berubah lebih andal.

## Menerapkan di Server

Pada Nginx, direktif expires dapat menetapkan masa simpan per jenis berkas di dalam blok location, dan add_header dipakai untuk menambahkan Cache-Control tertentu. Pada Apache, modul mod_expires dan mod_headers melakukan hal yang sama lewat konfigurasi atau berkas .htaccess. Aplikasi PHP yang mengirim berkas sendiri, misalnya hasil unduhan, dapat mengatur header lewat fungsi header() sebelum ada keluaran apa pun. Platform hosting dan CDN biasanya juga menyediakan pengaturan masa simpan di panelnya.

## Kesalahan yang Sering Terjadi

- Memberi masa simpan panjang pada berkas tanpa versi di nama, sehingga pengunjung terus melihat CSS lama setelah pembaruan.
- Men-cache halaman HTML dinamis terlalu lama, termasuk halaman yang memuat data pengguna.
- Mengira no-cache sama dengan no-store untuk data sensitif.
- Mengirim header yang saling bertentangan dari beberapa lapisan, misalnya aplikasi, server web, dan CDN yang masing-masing menambahkan aturan sendiri.
- Lupa bahwa cookie dan header Vary dapat memengaruhi apakah respons boleh dipakai ulang.

## Cara Memeriksa Hasilnya

Buka DevTools di browser, pilih tab Network, lalu muat ulang halaman dua kali. Pada pemuatan kedua, berkas yang berhasil di-cache biasanya tercantum dengan keterangan dari memory cache atau disk cache. Klik sebuah berkas dan lihat bagian Response Headers untuk memastikan Cache-Control sesuai rencana. Jangan lupa mematikan opsi Disable cache jika sedang dicentang, karena opsi itu membuat pengujian tidak mencerminkan pengunjung sungguhan. Anda juga dapat memeriksa header dari terminal dengan perintah curl -I diikuti alamat berkas. Laporan PageSpeed Insights turut menandai berkas statis yang belum memakai masa simpan efisien.

## Penutup

Browser caching termasuk perbaikan performa dengan biaya terendah: cukup beberapa baris konfigurasi, dan manfaatnya terasa setiap pengunjung kembali. Mulailah dengan memisahkan aset statis dari HTML, tambahkan versi pada nama berkas, lalu beri masa simpan panjang untuk aset statis. Uji di DevTools sebelum dan sesudah perubahan, dan pastikan halaman yang berisi data pribadi tidak ikut tersimpan di cache bersama.
