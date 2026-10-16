---
title: "Hreflang: Cara Mengatur SEO untuk Situs Dua Bahasa"
meta_description: "Hreflang memberi tahu Google versi bahasa mana yang cocok untuk tiap pengunjung. Pelajari aturan, contoh kode, kesalahan umum, dan cara mengujinya."
slug: "hreflang-situs-dua-bahasa-cara-memasang"
focus_keyword: "hreflang"
keywords:
  - hreflang
  - situs dua bahasa
  - SEO multibahasa
  - x-default
  - versi bahasa halaman
  - kode bahasa
  - konten terjemahan
  - SEO internasional
category: "SEO"
tags: ["SEO", "Hreflang", "SEO Teknis", "Multibahasa"]
image_alt: "Ilustrasi dua halaman berbahasa berbeda yang saling terhubung panah, dengan label kode bahasa di atasnya"
date: "2026-10-23"
lang: "id"
---

# Hreflang: Cara Mengatur SEO untuk Situs Dua Bahasa

Anda sudah menerjemahkan artikel ke bahasa Inggris. Rapi, enak dibaca, siap dipajang. Lalu seseorang di luar negeri mencari topik itu di Google, dan yang muncul adalah versi Indonesianya. Ia mengernyit, menekan tombol kembali, dan terjemahan Anda tidak pernah dibaca. Masalah itulah yang diatasi oleh **hreflang**.

Menyediakan dua bahasa saja tidak cukup. Mesin pencari perlu tahu bahwa kedua halaman itu pasangan, supaya tiap pengunjung diantar ke versi yang cocok. Itulah tugas **hreflang**.

## Apa yang Dilakukan Hreflang

Hreflang adalah anotasi yang memberi tahu mesin pencari bahwa sebuah halaman punya versi lain dalam bahasa atau wilayah berbeda. Dengan itu, Google bisa menampilkan versi yang paling pas dengan bahasa dan lokasi pengguna: pembaca dari Indonesia melihat versi Indonesia, pembaca berbahasa Inggris melihat versi Inggris.

Sifatnya sinyal, bukan perintah. Google tetap yang memutuskan, jadi jangan berharap hreflang menjamin versi tertentu selalu tampil.

Tanpa anotasi ini, hal-hal menjengkelkan bisa terjadi: versi yang salah tampil ke pembaca yang salah, Google bingung memilih di antara dua halaman yang mirip, dan sinyal seperti tautan masuk tersebar di dua alamat tanpa hubungan yang jelas. Terjemahan umumnya memang tidak dianggap duplikat, tetapi anotasi tetap menjernihkan hubungannya.

## Cara Menulisnya

Anotasi bisa ditaruh di tiga tempat: elemen link di bagian head halaman, header HTTP, atau sitemap XML. Untuk situs kecil, elemen link di head paling gampang. Menurut panduan Google, setiap halaman memuat sekumpulan elemen link, satu untuk setiap versi termasuk dirinya sendiri, dan kumpulan itu identik di semua versi.

Contoh untuk satu artikel dengan versi Indonesia dan Inggris:

```
<link rel="alternate" hreflang="id" href="https://contoh.id/artikel/cara-membuat-cv" />
<link rel="alternate" hreflang="en" href="https://contoh.id/en/artikel/how-to-write-a-cv" />
<link rel="alternate" hreflang="x-default" href="https://contoh.id/artikel/cara-membuat-cv" />
```

Artinya:

- `hreflang="id"` menandai versi Indonesia, memakai kode bahasa dua huruf.
- `hreflang="en"` menandai versi Inggris. Untuk wilayah tertentu, pakai format bahasa-wilayah seperti en-gb.
- `x-default` adalah halaman cadangan untuk pengunjung yang bahasanya tidak ada dalam daftar, atau halaman pemilih bahasa.
- `href` harus alamat lengkap, termasuk https.

## Aturan yang Sering Dilanggar

**Harus berbalas.** Kalau halaman A menunjuk B sebagai versi lain, B harus menunjuk balik ke A. Sumber di luar Google menyebut tautan satu arah akan diabaikan, dan itu kesalahan paling umum.

**Sertakan diri sendiri.** Setiap halaman mencantumkan dirinya dalam daftar.

**Hanya padanan sungguhan.** Hubungkan halaman yang memang isinya sama. Dua halaman yang topiknya sekadar mirip bukan pasangan.

**Kode bahasa yang valid.** "in" atau "eng" tidak dikenali. Anotasi dengan kode salah sama saja dengan tidak ada.

**Alamat harus bisa diakses.** Jangan menunjuk halaman yang dialihkan, diblokir, atau error.

**Satu metode saja.** Pilih elemen link, header, atau sitemap, dan jangan mencampur untuk kumpulan alamat yang sama supaya tidak saling bertentangan.

## Hreflang dan Canonical Harus Akur

Setiap versi bahasa sebaiknya punya canonical yang menunjuk ke dirinya sendiri. Kesalahan klasik: menetapkan canonical versi Inggris ke versi Indonesia. Itu sama dengan berkata kepada Google, "halaman Inggris ini cuma salinan", dan seluruh gunanya hreflang hilang.

## Struktur Alamat

Ada tiga pola umum. Subfolder (contoh.id/ dan contoh.id/en/) mudah dikelola dan lazim untuk situs kecil sampai menengah. Subdomain (en.contoh.id) lebih terpisah tetapi butuh pengaturan lebih banyak. Domain berbeda per negara cocok untuk bisnis besar, meski jauh lebih berat dirawat. Perlu diingat bahwa Google tidak menebak target audiens dari nama subdomain, jadi pemetaannya harus dinyatakan lewat hreflang.

## Anotasi Tidak Menyelamatkan Terjemahan Buruk

Hreflang hanya mengurus penunjukan, bukan mutu. Kalau versi Inggris Anda berupa hasil terjemahan otomatis mentah yang kaku, pembaca akan merasakannya dalam dua paragraf dan pergi. Tulis dengan natural. Sesuaikan juga judul, deskripsi meta, teks alternatif gambar, dan tautan internal agar menuju versi bahasa yang sama.

Satu detail yang sering terlewat: tombol pilih bahasa sebaiknya mengarah ke pasangan halaman yang sedang dibuka, bukan selalu ke beranda. Orang yang berganti bahasa biasanya ingin artikel yang sama.

## Cara Mengecek

1. Buka sumber halaman dan pastikan elemen link ada, lengkap, dan identik di semua versi.
2. Uji timbal balik: dari Indonesia ke Inggris, lalu dari Inggris kembali ke Indonesia.
3. Pakai alat pengujian di Google Search Console atau pemeriksa hreflang pihak ketiga bila ada.
4. Lihat laporan Pengindeksan di Search Console untuk tanda masalah pada halaman alternatif.
5. Coba cari dari lokasi dan bahasa peramban berbeda.

Setelah mengubah sesuatu, bersabarlah. Google butuh waktu merayapi ulang.

Kalau Anda hanya punya waktu untuk satu hal hari ini, periksa satu artikel: apakah pasangannya menunjuk balik? Jika tidak, mulai dari situ.
