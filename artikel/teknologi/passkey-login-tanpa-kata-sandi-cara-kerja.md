---
title: "Passkey: Login Tanpa Kata Sandi, Cara Kerja, dan Cara Mengaktifkannya"
meta_description: "Passkey menggantikan kata sandi dengan kunci kriptografi yang tersimpan di perangkat Anda. Pahami cara kerjanya, kelebihan, batasannya, dan langkah mulai memakainya."
slug: "passkey-login-tanpa-kata-sandi-cara-kerja"
focus_keyword: "passkey"
keywords:
  - passkey
  - login tanpa kata sandi
  - passwordless
  - FIDO2 WebAuthn
  - autentikasi aman
  - phishing
category: "Teknologi"
tags: ["Passkey", "Keamanan", "Autentikasi", "Teknologi"]
date: "2026-10-10"
lang: "id"
---

# Passkey: Login Tanpa Kata Sandi, Cara Kerja, dan Cara Mengaktifkannya

Kata sandi sudah lama menjadi titik terlemah keamanan akun. Orang memakai sandi yang sama di banyak layanan, memilih kombinasi yang mudah ditebak, atau terkecoh halaman login palsu. Passkey hadir untuk menyelesaikan masalah itu dengan cara yang berbeda: tidak ada kata sandi yang perlu diingat, diketik, atau dicuri.

## Apa Itu Passkey

Passkey adalah kredensial login yang menggantikan kata sandi. Alih-alih rangkaian karakter, akun Anda dikaitkan dengan sepasang kunci kriptografi. Satu kunci bersifat publik dan disimpan di server layanan. Kunci lainnya bersifat privat dan tetap berada di perangkat Anda. Saat masuk, Anda cukup membuka kunci privat itu dengan sidik jari, pengenalan wajah, atau PIN perangkat.

Passkey dibangun di atas standar terbuka WebAuthn dan FIDO2, yang dikembangkan lewat kerja sama industri teknologi. Karena standar, passkey bisa dipakai lintas peramban dan sistem operasi yang mendukungnya.

## Cara Kerja Passkey

Proses ini terdiri dari dua tahap.

**Pendaftaran.** Ketika Anda membuat passkey untuk sebuah situs, perangkat membuat pasangan kunci baru. Kunci publik dikirim ke situs dan disimpan di akun Anda. Kunci privat tidak pernah meninggalkan perangkat atau penyimpanan aman milik Anda.

**Login.** Saat Anda masuk, situs mengirim tantangan berupa data acak. Perangkat menandatangani tantangan itu memakai kunci privat setelah Anda memverifikasi diri secara lokal. Situs memeriksa tanda tangan dengan kunci publik. Bila cocok, Anda masuk.

Verifikasi sidik jari atau wajah terjadi di perangkat Anda. Data biometrik tidak dikirim ke situs.

## Mengapa Lebih Aman

- **Tahan terhadap phishing.** Passkey terikat pada domain asli situs. Halaman palsu dengan alamat berbeda tidak akan bisa meminta tanda tangan yang valid.
- **Tidak ada rahasia bersama di server.** Server hanya menyimpan kunci publik. Jika basis datanya bocor, penyerang tidak mendapat sesuatu yang bisa dipakai untuk masuk.
- **Unik di setiap layanan.** Anda tidak bisa memakai ulang passkey yang sama, sehingga kebocoran di satu tempat tidak merembet ke tempat lain.
- **Tidak ada yang dihafal atau diketik**, sehingga serangan menebak sandi dan pengisian kredensial otomatis tidak relevan.

## Passkey Tersimpan di Mana

Ada dua pendekatan umum. Passkey yang tersinkron disimpan dalam layanan akun, misalnya pengelola kata sandi atau penyimpanan kredensial bawaan sistem operasi, dan tersalin ke perangkat lain di akun yang sama. Ini nyaman, karena ganti ponsel tidak membuat Anda kehilangan akses. Passkey yang terikat perangkat, misalnya pada kunci keamanan fisik, hanya ada di satu alat sehingga lebih terkendali tetapi lebih repot bila alat hilang.

## Batasan yang Perlu Diketahui

Passkey bukan solusi tanpa celah. Pertama, tidak semua situs dan aplikasi sudah mendukungnya, sehingga kata sandi masih dipakai berdampingan untuk beberapa waktu. Kedua, keamanan passkey yang tersinkron bergantung pada keamanan akun penyimpannya, jadi akun itu sendiri perlu dilindungi dengan verifikasi dua langkah dan pemulihan yang jelas. Ketiga, berpindah antar ekosistem, misalnya dari satu platform ke platform lain, bisa lebih rumit tergantung dukungan layanan. Terakhir, jika perangkat Anda dicuri dan PIN-nya diketahui, pelaku bisa mencoba membuka kredensial tersebut.

## Cara Mulai Memakai Passkey

1. **Pastikan perangkat siap.** Aktifkan kunci layar, biometrik, dan pembaruan sistem terbaru.
2. **Periksa dukungan layanan.** Buka pengaturan keamanan akun dan cari opsi "passkey" atau "masuk tanpa kata sandi".
3. **Buat passkey.** Ikuti petunjuk, lalu verifikasi dengan sidik jari, wajah, atau PIN.
4. **Pilih tempat penyimpanan.** Gunakan pengelola kredensial yang Anda percaya dan sudah dilindungi verifikasi dua langkah.
5. **Siapkan jalur pemulihan.** Simpan metode cadangan di tempat aman sebelum menghapus kata sandi lama.
6. **Mulai dari akun penting.** Surel, perbankan, dan akun yang tersambung ke banyak layanan lain paling layak diprioritaskan.

## Penutup

Passkey tidak menghapus semua risiko, tetapi menutup dua pintu yang paling sering dipakai penyerang: sandi yang lemah dan halaman login palsu. Cobalah mengaktifkannya untuk satu akun penting minggu ini, sambil mempertahankan jalur pemulihan. Setelah terbiasa, Anda bisa memperluasnya ke layanan lain seiring semakin banyak situs yang mendukungnya.
