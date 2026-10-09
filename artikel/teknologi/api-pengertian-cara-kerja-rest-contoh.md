---
title: "API: Pengertian, Cara Kerja REST, dan Contoh Penggunaannya"
meta_description: "API menghubungkan satu aplikasi dengan aplikasi lain lewat permintaan dan respons. Pahami konsep REST, metode HTTP, kode status, autentikasi, dan contoh pemakaiannya."
slug: "api-pengertian-cara-kerja-rest-contoh"
focus_keyword: "API"
keywords:
  - API
  - apa itu API
  - REST API
  - metode HTTP
  - JSON
  - autentikasi API
  - webhook
category: "Teknologi"
tags: ["API", "REST", "Pemrograman", "Teknologi"]
date: "2026-10-10"
lang: "id"
---

# API: Pengertian, Cara Kerja REST, dan Contoh Penggunaannya

Ketika aplikasi cuaca di ponsel Anda menampilkan suhu terkini, aplikasi itu tidak mengukur sendiri. Ia meminta data ke layanan lain. Ketika toko daring menawarkan pembayaran lewat dompet digital, toko itu berbicara dengan sistem pembayaran di tempat lain. Penghubung dalam kedua kasus tersebut disebut API.

## Apa Itu API

API adalah singkatan dari *Application Programming Interface*. Sederhananya, API adalah seperangkat aturan yang memungkinkan satu program meminta data atau layanan dari program lain tanpa perlu tahu bagaimana program itu bekerja di dalamnya. Analogi yang sering dipakai adalah pelayan restoran: Anda menyampaikan pesanan kepada pelayan, dapur mengolahnya, lalu pelayan mengantar hasilnya. Anda tidak perlu masuk ke dapur.

## Cara Kerja Dasar

Pola umumnya adalah permintaan dan respons. Aplikasi klien mengirim permintaan ke alamat tertentu, yang disebut *endpoint*. Server memproses permintaan itu dan mengirim balik respons, biasanya dalam format JSON yang mudah dibaca mesin maupun manusia.

Contohnya, permintaan ke sebuah endpoint bisa meminta daftar artikel, dan responsnya berisi judul, tanggal, serta penulis masing-masing artikel dalam bentuk data terstruktur.

## Apa Itu REST

REST adalah gaya perancangan API yang memakai protokol HTTP. Sumber daya, seperti artikel atau pengguna, diwakili oleh alamat, dan tindakan terhadapnya ditentukan oleh metode HTTP:

- **GET** untuk membaca data.
- **POST** untuk membuat data baru.
- **PUT** atau **PATCH** untuk memperbarui data.
- **DELETE** untuk menghapus data.

API REST umumnya bersifat *stateless*, artinya setiap permintaan membawa informasi yang cukup untuk diproses tanpa server mengingat permintaan sebelumnya.

## Kode Status HTTP

Respons selalu membawa kode status yang menjelaskan hasilnya:

- **200** berhasil.
- **201** data baru berhasil dibuat.
- **400** permintaan salah atau tidak lengkap.
- **401** belum terautentikasi.
- **403** terautentikasi tetapi tidak berhak.
- **404** sumber daya tidak ditemukan.
- **422** data tidak lolos validasi.
- **429** terlalu banyak permintaan.
- **500** kesalahan di sisi server.

Membaca kode status dengan benar membuat proses penelusuran masalah jauh lebih cepat.

## Autentikasi dan Keamanan

Tidak semua API terbuka untuk semua orang. Cara umum untuk membatasi akses meliputi:

- **Kunci API**, yaitu token sederhana yang dikirim bersama permintaan.
- **Token pembawa (Bearer token)**, sering dikeluarkan setelah login.
- **OAuth**, untuk memberi aplikasi pihak ketiga akses terbatas tanpa membagikan kata sandi.
- **Sesi dan cookie** disertai token CSRF, lazim pada aplikasi web yang memakai akun admin.

Beberapa praktik penting: selalu gunakan HTTPS, jangan menaruh kunci rahasia di kode yang dapat dilihat publik, beri hak akses seminimal mungkin, dan batasi jumlah permintaan agar API tidak disalahgunakan.

## Contoh Penggunaan Sehari-hari

- **Pembayaran daring** yang menghubungkan toko dengan penyedia pembayaran.
- **Peta dan lokasi** yang disematkan di aplikasi pesan antar.
- **Login dengan akun lain**, yang bergantung pada API penyedia identitas.
- **Pengelolaan konten otomatis**, misalnya menambahkan artikel ke situs lewat skrip.
- **Integrasi internal** antarlayanan di dalam satu perusahaan.

## API dan Webhook

Pada API biasa, klien yang bertanya. Pada webhook, arahnya dibalik: server mengirim pemberitahuan ke alamat Anda ketika ada kejadian, misalnya pembayaran berhasil. Webhook menghemat Anda dari keharusan terus-menerus menanyakan status.

## Tips Merancang dan Memakai API dengan Baik

1. Baca dokumentasi sampai paham format permintaan, respons, dan batas pemakaian.
2. Uji dengan alat seperti curl atau klien API sebelum menulis kode.
3. Tangani kesalahan secara eksplisit, termasuk waktu habis dan kode 4xx serta 5xx.
4. Jangan percaya data masuk. Validasi di sisi server.
5. Cantumkan versi pada alamat API, misalnya `/v1/`, agar perubahan tidak merusak klien lama.
6. Catat log permintaan yang gagal untuk memudahkan penelusuran.

## Penutup

API pada dasarnya adalah kesepakatan tentang cara dua program berbicara. Begitu Anda memahami alur permintaan, metode, dan kode status, hampir semua API yang Anda temui akan terasa familier. Cobalah memanggil satu API publik dengan curl, lihat responsnya, lalu ubah parameternya untuk memahami bagaimana perilakunya berubah.
