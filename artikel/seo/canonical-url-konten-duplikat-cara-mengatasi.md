---
title: "Canonical URL: Cara Mengatasi Konten Duplikat di Website"
meta_description: "Canonical URL menandai versi utama halaman yang mirip. Pahami penyebab konten duplikat, cara memasang rel canonical, kapan memakai redirect, dan cara cek."
slug: "canonical-url-konten-duplikat-cara-mengatasi"
focus_keyword: "canonical URL"
keywords:
  - canonical URL
  - rel canonical
  - konten duplikat
  - duplicate content
  - redirect 301
  - parameter URL
  - Google Search Console
  - pengindeksan
  - SEO teknis
  - sitemap
category: "SEO"
tags: ["Canonical URL", "Konten Duplikat", "SEO Teknis", "SEO"]
image_alt: "Ilustrasi beberapa alamat halaman yang mirip dengan satu alamat ditandai sebagai versi utama"
date: "2026-10-16"
lang: "id"
---

# Canonical URL: Cara Mengatasi Konten Duplikat di Website

Sebuah halaman bisa punya lebih dari satu alamat tanpa Anda sadari. Alamat dengan dan tanpa www, versi http dan https, URL dengan parameter pelacakan, atau halaman yang sama dengan urutan filter berbeda, semuanya bisa menampilkan isi yang identik. Bagi mesin pencari ini membingungkan: mana yang harus dikumpulkan sinyalnya dan ditampilkan di hasil pencarian? Di sinilah **canonical URL** berperan, yaitu penanda versi utama dari sekumpulan halaman yang mirip.

## Apa Itu Canonical URL

Canonical URL adalah alamat yang Anda nyatakan sebagai versi pilihan sebuah halaman. Biasanya dipasang lewat tag link di bagian head dengan atribut rel="canonical" dan href berisi alamat lengkap versi utama. Untuk berkas seperti PDF, penandanya dapat dikirim lewat header HTTP.

Perlu dipahami bahwa canonical adalah petunjuk, bukan perintah. Google mempertimbangkannya bersama sinyal lain seperti pengalihan, tautan internal, dan isi sitemap, lalu memilih versi yang dianggap paling tepat. Karena itu sinyal-sinyal Anda sebaiknya konsisten.

Soal kekhawatiran umum: konten duplikat biasa tidak otomatis menyebabkan situs dihukum. Masalah utamanya adalah pemborosan dan ketidakjelasan: sinyal tersebar di beberapa alamat, dan Google bisa memilih versi yang bukan Anda inginkan.

## Penyebab Konten Duplikat

- Variasi protokol dan domain: http dan https, www dan non-www.
- Garis miring di akhir alamat, atau perbedaan huruf besar dan kecil pada path.
- Parameter URL untuk pelacakan seperti utm, sesi, atau pengurutan dan filter produk.
- Halaman cetak, versi AMP lama, atau versi seluler terpisah.
- Arsip kategori, tag, dan penomoran halaman pada CMS yang menampilkan potongan konten sama.
- Varian produk dengan deskripsi hampir identik pada toko daring.
- Konten yang disalin atau disindikasikan ke situs lain.

## Cara Memasang Canonical dengan Benar

1. **Pilih satu versi utama** untuk setiap halaman, lalu pakai konsisten di seluruh situs.
2. **Gunakan alamat absolut lengkap**, termasuk https dan nama domain, bukan alamat relatif.
3. **Pasang canonical pada setiap halaman, termasuk yang menunjuk ke dirinya sendiri.** Canonical mandiri melindungi dari variasi parameter yang tidak terduga.
4. **Pasang di head dokumen.** Tag canonical yang muncul di body biasanya diabaikan.
5. **Tunjuk ke halaman yang setara.** Jangan mengarahkan canonical dari halaman yang isinya berbeda hanya demi mengumpulkan sinyal, karena petunjuk itu bisa diabaikan.

Pada WordPress, plugin SEO umumnya memasang canonical otomatis. Tetap periksa hasilnya, terutama untuk halaman arsip dan halaman berparameter. Pada situs buatan sendiri, buat fungsi yang menghasilkan alamat bersih dari path halaman dan membuang parameter yang tidak mengubah isi.

## Canonical atau Redirect 301

Keduanya sering tertukar. Pakai **redirect 301** ketika alamat lama memang tidak perlu diakses lagi, misalnya memaksa http ke https atau www ke non-www. Pengunjung dan crawler langsung dipindahkan. Pakai **canonical** ketika kedua alamat harus tetap bisa dibuka oleh pengguna, tetapi hanya satu yang ingin Anda jadikan versi utama, seperti halaman dengan parameter filter.

## Kesalahan yang Perlu Dihindari

- Canonical yang menunjuk ke halaman 404 atau yang dialihkan.
- Banyak tag canonical berbeda pada satu halaman, misalnya satu dari tema dan satu dari plugin.
- Menggabungkan canonical dengan noindex pada halaman yang sama dengan pesan bertentangan.
- Memasukkan alamat non-canonical ke sitemap. Sitemap sebaiknya hanya berisi versi utama.
- Menunjuk seluruh halaman penomoran ke halaman pertama, padahal isinya berbeda.

## Cara Memeriksa Canonical

Buka sumber halaman dan cari tag rel="canonical" di head, lalu pastikan alamatnya sesuai rencana. Di Google Search Console, alat Pemeriksaan URL menampilkan dua informasi penting: canonical yang dinyatakan pengguna dan canonical yang dipilih Google. Jika keduanya berbeda, cari tahu penyebabnya, misalnya tautan internal yang menunjuk ke versi lain atau konten yang ternyata tidak cukup mirip. Laporan Pengindeksan juga mencantumkan status seperti halaman duplikat tanpa canonical pilihan pengguna, yang menjadi petunjuk awal audit.

## Penutup

Canonical URL tidak mengubah isi situs, tetapi merapikan cara mesin pencari memahaminya. Mulailah dengan menyeragamkan versi domain lewat redirect, pasang canonical mandiri di semua halaman, lalu tangani parameter dan arsip yang menghasilkan duplikat. Pastikan semua sinyal, mulai dari tautan internal sampai sitemap, menunjuk ke alamat utama yang sama.
