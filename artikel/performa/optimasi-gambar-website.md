---
title: "Optimasi Gambar Website: Format, Kompresi, dan SEO Gambar"
meta_description: "Panduan optimasi gambar website: pilih format WebP, AVIF, atau SVG, kompres, buat gambar responsif dengan srcset, lazy load, dan SEO gambar."
slug: "optimasi-gambar-website"
focus_keyword: "optimasi gambar website"
keywords:
  - optimasi gambar website
  - kompres gambar untuk website
  - format gambar webp
  - format gambar avif
  - gambar responsif srcset
  - lazy load gambar
  - alt text gambar
  - SEO gambar
category: "Performa"
tags: ["Performa Website", "Optimasi Gambar", "SEO Gambar", "Web Development"]
date: "2026-10-02"
lang: "id"
---

# Optimasi Gambar Website: Panduan Format, Kompresi, Gambar Responsif, dan SEO Gambar

Gambar membuat website lebih hidup, informatif, dan menarik. Foto produk membantu calon pembeli membayangkan barang yang akan mereka beli. Ilustrasi memperjelas penjelasan yang rumit. Grafik membuat data lebih mudah dipahami. Namun, di balik semua manfaat itu, gambar juga sering menjadi penyebab utama website terasa berat.

Di banyak website, gambar menyumbang porsi terbesar dari total ukuran halaman. Satu foto yang diunggah langsung dari kamera bisa berukuran beberapa megabita. Jika sebuah halaman memuat belasan foto seperti itu, pengunjung di jaringan seluler harus menunggu lama. **Optimasi gambar website** adalah cara untuk menjaga kualitas visual sambil mengurangi beban tersebut secara drastis. Panduan ini membahas cara memilih format, mengompres, membuat gambar responsif, mengatur pemuatan, dan mengoptimasi gambar untuk mesin pencari.

## Daftar Isi

1. [Mengapa Optimasi Gambar Penting?](#mengapa-optimasi-gambar-penting)
2. [Konsep Dasar yang Perlu Dipahami](#konsep-dasar-yang-perlu-dipahami)
3. [Mengenal Format Gambar untuk Web](#mengenal-format-gambar-untuk-web)
4. [Langkah-Langkah Optimasi Gambar](#langkah-langkah-optimasi-gambar)
5. [Otomatisasi Optimasi Gambar](#otomatisasi-optimasi-gambar)
6. [Ikon, SVG, dan Gambar Latar CSS](#ikon-svg-dan-gambar-latar-css)
7. [Optimasi Gambar untuk SEO](#optimasi-gambar-untuk-seo)
8. [Gambar dan Aksesibilitas](#gambar-dan-aksesibilitas)
9. [Optimasi Gambar di WordPress](#optimasi-gambar-di-wordpress)
10. [Alat Optimasi Gambar yang Direkomendasikan](#alat-optimasi-gambar-yang-direkomendasikan)
11. [Optimasi Gambar untuk Toko Daring](#optimasi-gambar-untuk-toko-daring)
12. [Mengganti GIF dengan Video](#mengganti-gif-dengan-video)
13. [Kesalahan Umum dalam Optimasi Gambar](#kesalahan-umum-dalam-optimasi-gambar)
14. [Checklist Optimasi Gambar](#checklist-optimasi-gambar)
15. [FAQ Optimasi Gambar](#faq-optimasi-gambar)
16. [Kesimpulan](#kesimpulan)

## Mengapa Optimasi Gambar Penting?

Alasan pertama adalah kecepatan. Gambar berukuran besar membutuhkan waktu unduh yang lama, terutama di jaringan seluler. Semakin lama gambar diunduh, semakin lama pula halaman terasa siap. Pengunjung yang tidak sabar akan menutup halaman sebelum gambar selesai dimuat. Mengecilkan ukuran gambar adalah salah satu cara tercepat untuk membuat halaman terasa lebih ringan.

Alasan kedua berkaitan dengan Core Web Vitals. Pada banyak halaman, elemen konten terbesar yang tampil di layar pertama adalah sebuah gambar. Gambar ini menentukan nilai Largest Contentful Paint atau LCP. Jika gambar tersebut lambat dimuat, nilai LCP akan buruk. Penjelasan lengkap tentang metrik ini dapat dibaca di artikel Core Web Vitals.

Alasan ketiga adalah penghematan kuota data pengunjung. Banyak pengguna internet di Indonesia mengandalkan paket data dengan kuota terbatas. Halaman yang memuat gambar berukuran besar menghabiskan kuota mereka dengan cepat. Pengunjung mungkin enggan kembali ke website yang terasa boros. Gambar yang dioptimasi menunjukkan bahwa Anda menghargai pengunjung.

Alasan keempat adalah biaya dan kapasitas server. Gambar yang besar memakan ruang penyimpanan dan bandwidth hosting. Pada website dengan banyak pengunjung, biaya bandwidth bisa membengkak. Gambar yang lebih kecil mengurangi beban server dan biaya operasional. Proses pencadangan website juga menjadi lebih cepat.

Alasan kelima adalah visibilitas di mesin pencari. Gambar yang dioptimasi dengan baik dapat tampil di Google Gambar dan fitur pencarian visual lainnya. Banyak orang mencari inspirasi, produk, atau tutorial melalui pencarian gambar. Gambar yang relevan dan diberi keterangan yang tepat bisa menjadi sumber trafik tambahan. Bagian khusus tentang SEO gambar akan dibahas di bawah.

## Konsep Dasar yang Perlu Dipahami

Sebelum masuk ke teknik optimasi, ada beberapa konsep dasar yang perlu dipahami. Konsep ini akan membantu Anda mengambil keputusan yang tepat. Banyak kesalahan dalam optimasi gambar terjadi karena konsep-konsep ini tertukar. Penjelasannya sengaja dibuat sederhana. Anda tidak perlu menjadi ahli grafis untuk memahaminya.

### Dimensi dan Ukuran File

Dimensi gambar adalah lebar dan tinggi gambar dalam satuan piksel, misalnya 1200 × 800 piksel. Ukuran file adalah besarnya data yang disimpan, misalnya 150 kilobita. Keduanya berhubungan, tetapi tidak sama. Gambar berdimensi sama bisa memiliki ukuran file yang sangat berbeda, tergantung format dan tingkat kompresinya. Optimasi gambar berarti mengatur keduanya agar seimbang.

Kesalahan yang sering terjadi adalah menampilkan gambar berdimensi besar di area yang kecil. Misalnya, foto berdimensi 4000 piksel ditampilkan di kotak selebar 400 piksel. Browser akan mengecilkan tampilannya, tetapi pengunjung tetap harus mengunduh file aslinya. Akibatnya, sebagian besar data yang diunduh terbuang sia-sia. Menyesuaikan dimensi dengan ukuran tampilan adalah langkah optimasi yang paling dasar.

### Kepadatan Piksel Layar

Layar ponsel dan laptop modern memiliki kepadatan piksel yang tinggi. Pada layar seperti ini, satu piksel CSS bisa diwakili oleh dua atau tiga piksel fisik. Agar gambar tetap tajam, gambar perlu memiliki dimensi lebih besar daripada ukuran tampilannya dalam piksel CSS. Misalnya, gambar yang tampil selebar 400 piksel CSS idealnya tersedia dalam versi 800 piksel untuk layar berkepadatan dua kali lipat. Teknik gambar responsif memungkinkan browser memilih versi yang sesuai dengan layar pengguna.

Namun, menyediakan gambar dengan kepadatan tiga kali lipat untuk semua pengguna sering kali berlebihan. Perbedaan ketajaman antara kepadatan dua kali dan tiga kali lipat sulit dilihat oleh kebanyakan orang. Sementara itu, ukuran filenya bertambah cukup besar. Banyak praktisi memilih untuk membatasi hingga kepadatan dua kali lipat. Keputusan ini adalah keseimbangan antara ketajaman dan kecepatan.

### Kompresi Lossy dan Lossless

Kompresi adalah proses mengecilkan ukuran file gambar. Ada dua jenis kompresi utama. Kompresi *lossless* mengecilkan ukuran tanpa menghilangkan data gambar sama sekali. Gambar hasil kompresi lossless identik dengan aslinya ketika ditampilkan. Penghematannya biasanya tidak terlalu besar.

Kompresi *lossy* mengecilkan ukuran dengan membuang sebagian data yang dianggap kurang terlihat oleh mata manusia. Penghematannya jauh lebih besar dibanding kompresi lossless. Pada tingkat kompresi yang wajar, perbedaan kualitas hampir tidak terlihat. Namun, kompresi yang terlalu agresif akan menimbulkan artefak seperti blok kotak-kotak atau warna yang pecah. Kunci kompresi lossy adalah menemukan titik di mana ukuran file kecil tetapi kualitas masih nyaman dilihat.

### Metadata Gambar

Selain data visual, file gambar sering menyimpan metadata. Metadata bisa berisi informasi kamera, tanggal pengambilan, pengaturan lensa, hingga koordinat lokasi GPS. Untuk tampilan di website, sebagian besar metadata ini tidak diperlukan. Metadata menambah ukuran file tanpa memberi manfaat bagi pengunjung. Lebih dari itu, koordinat lokasi bisa membocorkan informasi pribadi, misalnya lokasi rumah pemotret.

## Mengenal Format Gambar untuk Web

Memilih format yang tepat adalah keputusan penting dalam optimasi gambar. Setiap format memiliki kelebihan dan kekurangan untuk jenis gambar tertentu. Format yang cocok untuk foto belum tentu cocok untuk logo atau ilustrasi. Memahami karakter setiap format akan membantu Anda mendapatkan ukuran file terkecil dengan kualitas terbaik. Berikut format-format gambar yang umum digunakan di web.

### JPEG

JPEG adalah format yang paling lama dan paling luas digunakan untuk foto. Format ini menggunakan kompresi lossy yang sangat efektif untuk gambar dengan gradasi warna halus, seperti foto pemandangan atau wajah. JPEG didukung oleh semua browser dan hampir semua perangkat lunak. Kelemahannya, JPEG tidak mendukung transparansi. Format ini juga kurang cocok untuk gambar dengan garis tegas dan teks, karena kompresinya menimbulkan artefak di sekitar tepi.

JPEG memiliki varian bernama *progressive JPEG*. Varian ini menampilkan gambar secara bertahap, dari versi buram menjadi tajam, saat sedang diunduh. Pengunjung bisa melihat gambaran kasar lebih awal sambil menunggu gambar lengkap. Untuk gambar berukuran besar, versi progresif sering kali sedikit lebih kecil daripada versi biasa. Banyak alat kompresi menyediakan opsi untuk menyimpan JPEG secara progresif.

### PNG

PNG menggunakan kompresi lossless dan mendukung transparansi penuh. Format ini sangat cocok untuk gambar dengan warna solid, garis tegas, dan teks, seperti tangkapan layar, diagram, dan logo. Kualitasnya tetap tajam tanpa artefak kompresi. Namun, PNG menghasilkan ukuran file yang sangat besar jika digunakan untuk foto. Menyimpan foto dalam format PNG adalah salah satu kesalahan yang paling sering ditemui.

Ukuran PNG masih bisa dikecilkan dengan beberapa cara. Salah satunya adalah mengurangi jumlah warna menjadi palet terbatas, yang dikenal sebagai PNG-8. Teknik ini sangat efektif untuk ilustrasi sederhana dengan sedikit warna. Alat seperti TinyPNG dan pngquant melakukan pengurangan warna secara otomatis. Untuk sebagian besar kebutuhan, format WebP kini bisa menggantikan PNG dengan ukuran yang lebih kecil.

### GIF

GIF dikenal sebagai format untuk animasi sederhana. Format ini hanya mendukung hingga 256 warna, sehingga kualitas foto dalam GIF terlihat kasar. Untuk animasi, GIF sangat tidak efisien dibandingkan format video modern. Animasi GIF berdurasi beberapa detik bisa berukuran beberapa megabita. Sebaiknya ganti animasi GIF dengan video MP4 atau WebM, atau dengan animasi WebP.

### SVG

SVG adalah format gambar berbasis vektor. Berbeda dengan format lain yang menyimpan gambar sebagai kumpulan piksel, SVG menyimpan gambar sebagai instruksi bentuk, garis, dan warna. Karena itu, SVG tetap tajam pada ukuran berapa pun. Format ini sangat cocok untuk logo, ikon, ilustrasi sederhana, dan grafik. Ukuran filenya biasanya sangat kecil untuk gambar yang tidak terlalu rumit.

SVG tidak cocok untuk foto atau gambar dengan detail yang sangat kompleks. Instruksi vektor untuk gambar seperti itu akan menjadi sangat panjang dan berat. Karena SVG berupa kode, file ini bisa dikompres dengan Gzip atau Brotli seperti file teks lainnya. Perlu diingat juga bahwa SVG dapat berisi skrip. Jangan menampilkan file SVG yang diunggah oleh pengguna tanpa pemeriksaan keamanan yang memadai.

### WebP

WebP adalah format modern yang dikembangkan oleh Google. Format ini mendukung kompresi lossy dan lossless, transparansi, serta animasi. Untuk kualitas visual yang setara, WebP umumnya menghasilkan file yang lebih kecil daripada JPEG dan PNG. WebP didukung oleh semua browser modern utama. Karena itu, WebP kini menjadi pilihan aman untuk menggantikan JPEG dan PNG di sebagian besar website.

### AVIF

AVIF adalah format yang lebih baru, berbasis teknologi kompresi video AV1. Format ini sering menghasilkan ukuran file lebih kecil daripada WebP pada kualitas yang setara, terutama untuk foto. AVIF juga mendukung transparansi, rentang warna yang lebih luas, dan HDR. Dukungannya di browser modern sudah luas, meski tidak selengkap WebP pada perangkat lama. Kelemahan AVIF adalah proses pengodeannya lebih lambat dan lebih berat bagi server.

### Perbandingan Format Gambar

| Format | Jenis Kompresi | Transparansi | Animasi | Cocok untuk |
|---|---|---|---|---|
| JPEG | Lossy | Tidak | Tidak | Foto, gambar dengan gradasi halus |
| PNG | Lossless | Ya | Tidak | Tangkapan layar, diagram, gambar dengan teks |
| GIF | Lossless (256 warna) | Ya (terbatas) | Ya | Animasi sangat sederhana (sebaiknya diganti video) |
| SVG | Vektor | Ya | Ya | Logo, ikon, ilustrasi sederhana |
| WebP | Lossy dan lossless | Ya | Ya | Pengganti umum JPEG dan PNG |
| AVIF | Lossy dan lossless | Ya | Ya | Foto dengan kebutuhan ukuran sangat kecil |

Sebagai panduan praktis, gunakan SVG untuk logo dan ikon. Gunakan AVIF atau WebP untuk foto, dengan JPEG sebagai cadangan jika diperlukan. Gunakan WebP lossless atau PNG untuk tangkapan layar dan gambar dengan teks. Hindari GIF untuk animasi dan gantilah dengan video. Dengan aturan sederhana ini, sebagian besar kebutuhan gambar di website sudah terpenuhi.

## Langkah-Langkah Optimasi Gambar

Setelah memahami konsep dasar dan format gambar, saatnya masuk ke langkah praktis. Langkah-langkah berikut bisa diterapkan pada website apa pun, baik yang dibangun dengan CMS maupun kode sendiri. Urutannya disusun agar setiap langkah melengkapi langkah sebelumnya. Anda bisa menerapkannya secara manual untuk website kecil. Untuk website besar, sebaiknya proses ini diotomatiskan.

### Langkah 1: Tentukan Format yang Tepat

Mulailah dengan menentukan format berdasarkan jenis gambar. Foto produk, foto artikel, dan foto latar sebaiknya disajikan dalam format AVIF atau WebP. Logo dan ikon sebaiknya menggunakan SVG. Tangkapan layar aplikasi bisa menggunakan WebP lossless atau PNG yang sudah dikurangi warnanya. Jangan menyimpan foto dalam format PNG kecuali benar-benar membutuhkan kualitas tanpa kompresi.

Jika ingin menyajikan format modern sambil tetap mendukung browser lama, gunakan elemen `<picture>`. Elemen ini memungkinkan browser memilih format pertama yang didukungnya. Browser yang mendukung AVIF akan mengambil versi AVIF. Browser yang hanya mendukung WebP akan mengambil versi WebP. Browser lama akan menggunakan versi JPEG sebagai cadangan.

```html
<picture>
  <source srcset="/gambar/kebun-teh.avif" type="image/avif">
  <source srcset="/gambar/kebun-teh.webp" type="image/webp">
  <img src="/gambar/kebun-teh.jpg" width="1200" height="800"
       alt="Hamparan kebun teh di lereng gunung saat pagi berkabut">
</picture>
```

### Langkah 2: Sesuaikan Dimensi dengan Ukuran Tampilan

Ketahui berapa lebar maksimum gambar saat ditampilkan di website. Misalnya, kolom artikel Anda memiliki lebar maksimum 760 piksel. Gambar di dalam artikel tidak perlu lebih lebar dari sekitar dua kali lipat ukuran tersebut untuk layar berkepadatan tinggi. Ubah ukuran gambar sebelum diunggah atau biarkan sistem membuat beberapa versi secara otomatis. Jangan mengunggah gambar mentah dari kamera atau ponsel yang dimensinya ribuan piksel.

Buatlah standar ukuran untuk berbagai jenis gambar di website. Contohnya adalah ukuran untuk gambar sampul artikel, gambar di dalam artikel, gambar produk, dan gambar mini. Standar ini memudahkan tim konten dan memastikan konsistensi tampilan. Standar juga membantu Anda menghitung ukuran versi responsif yang perlu dibuat. Dokumentasikan standar tersebut agar semua anggota tim mengikutinya.

### Langkah 3: Kompres dengan Tingkat Kualitas yang Wajar

Setelah dimensi disesuaikan, kompres gambar untuk mengurangi ukuran file. Untuk format lossy seperti JPEG, WebP, dan AVIF, tentukan tingkat kualitas yang menyeimbangkan ukuran dan tampilan. Tidak ada angka kualitas yang ideal untuk semua gambar. Sebagai titik awal, banyak praktisi menggunakan pengaturan kualitas menengah hingga tinggi, lalu menyesuaikannya setelah membandingkan hasil secara visual. Perhatikan bahwa skala kualitas di setiap format dan alat bisa berbeda, sehingga angka yang sama belum tentu menghasilkan kualitas yang sama.

Bandingkan hasil kompresi dengan gambar asli pada ukuran tampilan sebenarnya. Alat seperti Squoosh menyediakan tampilan berdampingan sehingga perbedaan mudah dilihat. Jika perbedaan tidak terlihat pada ukuran normal, kompresi tersebut sudah cukup baik. Perhatikan area dengan gradasi halus, seperti langit atau kulit, karena area ini paling cepat menunjukkan artefak. Untuk foto produk yang membutuhkan detail tinggi, gunakan kualitas sedikit lebih tinggi.

### Langkah 4: Sediakan Gambar Responsif

Pengunjung mengakses website dari perangkat dengan ukuran layar yang sangat beragam. Gambar yang cocok untuk layar desktop terlalu besar untuk layar ponsel. Teknik gambar responsif memungkinkan browser memilih versi gambar yang paling sesuai. Caranya adalah menyediakan beberapa versi gambar dengan lebar berbeda melalui atribut `srcset`. Atribut `sizes` memberi tahu browser berapa lebar gambar akan ditampilkan pada berbagai ukuran layar.

```html
<img
  src="/gambar/resep-rendang-800.webp"
  srcset="/gambar/resep-rendang-400.webp 400w,
          /gambar/resep-rendang-800.webp 800w,
          /gambar/resep-rendang-1200.webp 1200w,
          /gambar/resep-rendang-1600.webp 1600w"
  sizes="(max-width: 600px) 100vw, (max-width: 1024px) 80vw, 760px"
  width="1600" height="1067"
  alt="Rendang daging sapi dalam wajan tanah liat dengan taburan bawang goreng"
  loading="lazy" decoding="async">
```

Pada contoh di atas, browser di ponsel dengan layar sempit mungkin memilih versi 400 atau 800 piksel. Browser di laptop dengan layar lebar mungkin memilih versi 1200 atau 1600 piksel. Pilihan juga mempertimbangkan kepadatan piksel layar. Anda tidak perlu menghitung manual versi mana yang dipilih, karena browser yang memutuskan. Tugas Anda adalah menyediakan versi yang cukup beragam dan menulis atribut `sizes` dengan akurat.

Atribut `sizes` sering ditulis dengan keliru. Jika tidak dicantumkan, browser mengasumsikan gambar ditampilkan selebar layar penuh. Akibatnya, browser bisa memilih versi yang jauh lebih besar dari yang dibutuhkan. Periksa tata letak website Anda dan tuliskan lebar tampilan gambar yang sebenarnya. Untuk gambar dengan ukuran tetap, seperti avatar, Anda bisa menggunakan deskriptor kepadatan seperti `1x` dan `2x`.

Elemen `<picture>` juga bisa digunakan untuk *art direction*. Art direction berarti menampilkan potongan gambar yang berbeda untuk ukuran layar yang berbeda. Misalnya, gambar banner lebar di desktop dipotong menjadi lebih fokus pada objek utama di ponsel. Teknik ini menggunakan atribut `media` pada elemen `<source>`. Gunakan art direction jika gambar yang diperkecil kehilangan makna atau detail penting.

### Langkah 5: Atur Waktu dan Prioritas Pemuatan

Tidak semua gambar perlu dimuat saat halaman pertama kali dibuka. Gambar di bagian bawah halaman baru terlihat setelah pengunjung menggulir. Atribut `loading="lazy"` memerintahkan browser untuk menunda pemuatan gambar tersebut sampai mendekati area pandang. Teknik ini mengurangi jumlah data yang diunduh di awal. Hasilnya, sumber daya penting di bagian atas halaman bisa dimuat lebih cepat.

Aturan penting dalam lazy load adalah tidak menerapkannya pada gambar yang langsung terlihat. Gambar sampul artikel, banner utama, atau foto produk di bagian atas halaman harus dimuat secepat mungkin. Menunda gambar-gambar ini justru membuat konten utama tampil lebih lambat. Untuk gambar terpenting di layar pertama, tambahkan atribut `fetchpriority="high"` agar browser mengunduhnya lebih awal. Cukup terapkan pada satu atau dua gambar saja.

Atribut `decoding="async"` juga bisa ditambahkan pada gambar. Atribut ini memberi petunjuk kepada browser bahwa proses mengurai gambar boleh dilakukan tanpa menahan tampilan konten lain. Dampaknya biasanya kecil, tetapi tidak ada salahnya digunakan untuk gambar yang tidak kritis. Untuk elemen `<iframe>`, atribut `loading="lazy"` juga tersedia dan sangat berguna. Gunakan untuk sematan peta atau video di bagian bawah halaman.

### Langkah 6: Cantumkan Atribut Lebar dan Tinggi

Setiap elemen gambar sebaiknya memiliki atribut `width` dan `height`. Dengan atribut ini, browser bisa menghitung rasio aspek gambar sebelum file selesai diunduh. Browser kemudian menyediakan ruang yang tepat di tata letak. Tanpa atribut ini, teks dan elemen lain akan bergeser saat gambar muncul. Pergeseran tersebut mengganggu pembaca dan memperburuk metrik stabilitas visual.

Atribut lebar dan tinggi tidak membuat gambar menjadi kaku. Gambar tetap bisa menyesuaikan lebar layar dengan CSS `max-width: 100%` dan `height: auto`. Nilai atribut cukup mencerminkan rasio aspek gambar asli. Untuk gambar responsif dengan beberapa versi, gunakan dimensi versi terbesar atau versi mana pun dengan rasio yang sama. Yang penting, rasio lebar terhadap tinggi sesuai dengan gambar yang sebenarnya.

### Langkah 7: Hapus Metadata yang Tidak Perlu

Seperti dijelaskan sebelumnya, metadata menambah ukuran file dan berpotensi membocorkan informasi pribadi. Sebagian besar alat kompresi menyediakan opsi untuk menghapus metadata. Banyak alat bahkan menghapusnya secara otomatis saat mengonversi format. Periksa kembali gambar hasil olahan untuk memastikan data lokasi GPS sudah hilang. Hal ini sangat penting untuk foto yang diambil di rumah atau tempat pribadi.

Ada pengecualian untuk metadata tertentu. Profil warna kadang perlu dipertahankan agar warna gambar tampil sesuai. Informasi hak cipta dan kredit juga bisa dipertahankan jika diperlukan. Pilih opsi alat yang menghapus data kamera dan lokasi, tetapi tetap mempertahankan profil warna. Jika ragu, uji tampilan warna gambar sebelum dan sesudah penghapusan metadata.

### Langkah 8: Atur Cache untuk File Gambar

Gambar jarang berubah setelah diunggah. Karena itu, gambar sangat cocok untuk disimpan lama di cache browser. Dengan cache yang tepat, pengunjung yang kembali tidak perlu mengunduh ulang gambar yang sama. Atur header `Cache-Control` dengan masa simpan yang panjang untuk file gambar. Jika gambar diganti, gunakan nama file baru agar browser mengunduh versi terbaru.

Menyimpan gambar di CDN juga sangat dianjurkan. CDN menyajikan gambar dari server yang dekat dengan pengunjung. Hal ini mempercepat pengunduhan, terutama untuk pengunjung yang jauh dari server utama. Pengaturan cache dan CDN dibahas lebih lengkap di artikel cara mempercepat loading website. Kombinasi gambar yang kecil dan pengiriman yang cepat memberikan hasil terbaik.

## Otomatisasi Optimasi Gambar

Mengoptimasi gambar secara manual cukup untuk website kecil dengan sedikit gambar. Namun, untuk website dengan ratusan atau ribuan gambar, cara manual tidak praktis. Gambar baru juga terus ditambahkan oleh tim konten setiap hari. Otomatisasi memastikan setiap gambar dioptimasi tanpa bergantung pada ingatan seseorang. Ada beberapa pendekatan untuk mengotomatiskan proses ini.

### Optimasi Saat Gambar Diunggah

Pendekatan pertama adalah mengoptimasi gambar saat diunggah ke server. Sistem secara otomatis mengubah ukuran, mengompres, membuat beberapa versi responsif, dan mengonversi format. Gambar asli bisa disimpan sebagai cadangan atau dibuang sesuai kebutuhan. Pendekatan ini cocok untuk website yang dikelola dengan CMS atau aplikasi sendiri. Beban pemrosesan hanya terjadi sekali, saat gambar pertama kali diunggah.

Berikut contoh fungsi PHP sederhana menggunakan ekstensi GD untuk mengubah ukuran dan mengonversi gambar ke WebP. Proses pengodean ulang dengan GD juga otomatis membuang metadata EXIF.

```php
<?php

function konversiKeWebp(string $sumber, string $tujuan, int $lebarMaks = 1600, int $kualitas = 80): void
{
    $info = @getimagesize($sumber);
    if ($info === false) {
        throw new InvalidArgumentException("Bukan file gambar yang valid: {$sumber}");
    }

    [$lebar, $tinggi, $tipe] = $info;

    $gambar = match ($tipe) {
        IMAGETYPE_JPEG => imagecreatefromjpeg($sumber),
        IMAGETYPE_PNG  => imagecreatefrompng($sumber),
        default        => throw new InvalidArgumentException('Hanya JPEG dan PNG yang didukung.'),
    };

    if ($gambar === false) {
        throw new RuntimeException("Gagal membaca gambar: {$sumber}");
    }

    if ($lebar > $lebarMaks) {
        $tinggiBaru = (int) round($tinggi * $lebarMaks / $lebar);
        $diperkecil = imagescale($gambar, $lebarMaks, $tinggiBaru);
        if ($diperkecil === false) {
            throw new RuntimeException("Gagal mengubah ukuran gambar: {$sumber}");
        }
        $gambar = $diperkecil;
    }

    // PNG berpalet harus diubah ke truecolor agar transparansi tetap terjaga di WebP
    imagepalettetotruecolor($gambar);
    imagealphablending($gambar, true);
    imagesavealpha($gambar, true);

    if (!imagewebp($gambar, $tujuan, $kualitas)) {
        throw new RuntimeException("Gagal menyimpan WebP ke: {$tujuan}");
    }
}
```

Fungsi di atas bisa dipanggil setelah file berhasil diunggah dan divalidasi. Untuk membuat beberapa versi responsif, panggil fungsi tersebut beberapa kali dengan nilai lebar maksimum yang berbeda. Jika server menggunakan PHP 8.1 atau lebih baru dengan dukungan AVIF, fungsi `imageavif()` dapat digunakan dengan pola serupa. Untuk volume gambar yang besar, pertimbangkan pustaka yang lebih cepat seperti Imagick atau libvips. Jalankan proses konversi di antrean latar belakang agar pengunggahan tidak terasa lambat bagi pengguna.

### Optimasi Saat Proses Build

Untuk website statis atau aplikasi berbasis framework JavaScript, gambar bisa dioptimasi saat proses build. Alat build akan memproses semua gambar di folder sumber dan menghasilkan versi yang sudah dioptimasi. Banyak framework menyediakan komponen gambar yang menangani proses ini secara otomatis. Contohnya adalah komponen gambar di Next.js, Nuxt, dan Astro. Komponen tersebut juga otomatis menulis atribut `srcset`, `sizes`, dan dimensi.

Untuk proyek berbasis Node.js, pustaka `sharp` sangat populer untuk memproses gambar. Pustaka ini cepat karena dibangun di atas libvips. Anda bisa menulis skrip sederhana untuk mengonversi seluruh folder gambar ke WebP atau AVIF dalam berbagai ukuran. Skrip ini kemudian dijalankan sebagai bagian dari proses build. Dengan begitu, tim konten cukup menambahkan gambar asli, dan sistem menangani sisanya.

### Menggunakan Image CDN

Pendekatan ketiga adalah menggunakan layanan *image CDN*. Layanan ini mengoptimasi gambar secara langsung saat diminta oleh browser. Anda cukup menyimpan gambar asli, lalu menentukan ukuran dan format melalui parameter di URL. Layanan akan mengubah ukuran, mengompres, dan memilih format terbaik sesuai dukungan browser. Hasilnya kemudian disimpan di cache CDN untuk permintaan berikutnya.

Image CDN sangat praktis untuk website dengan banyak gambar dari berbagai sumber. Anda tidak perlu membangun sistem pemrosesan gambar sendiri. Beberapa penyedia CDN umum juga menawarkan fitur optimasi gambar sebagai layanan tambahan. Kelemahannya adalah biaya berlangganan yang bisa meningkat seiring jumlah gambar dan trafik. Bandingkan biaya tersebut dengan waktu dan sumber daya yang dibutuhkan untuk membangun solusi sendiri.

## Ikon, SVG, dan Gambar Latar CSS

### Ikon

Ikon adalah elemen kecil yang muncul di banyak tempat, seperti menu, tombol, dan daftar fitur. Dulu, ikon sering disajikan sebagai banyak file gambar kecil atau sebagai *icon font*. Kedua cara ini kini kurang dianjurkan. Banyak file kecil menambah jumlah permintaan, sedangkan icon font memuat ratusan ikon meskipun hanya beberapa yang digunakan. Icon font juga bisa menimbulkan masalah aksesibilitas jika tidak ditangani dengan benar.

Cara yang lebih baik adalah menggunakan ikon SVG. Ikon SVG bisa ditanam langsung di HTML atau digabungkan dalam satu file *sprite*. Dengan cara ini, Anda hanya memuat ikon yang benar-benar digunakan. Ikon SVG juga mudah diwarnai dengan CSS dan tetap tajam di semua ukuran layar. Banyak pustaka ikon modern menyediakan ikon dalam format SVG yang bisa diimpor satu per satu.

### Mengoptimasi File SVG

File SVG yang diekspor dari aplikasi desain sering berisi data yang tidak diperlukan. Data tersebut meliputi komentar, metadata editor, atribut kosong, dan angka dengan presisi desimal berlebihan. Alat seperti SVGO dapat membersihkan data tersebut secara otomatis. Penghematan ukurannya bisa cukup besar, terutama untuk ilustrasi yang rumit. Periksa tampilan SVG setelah dioptimasi untuk memastikan tidak ada bagian yang rusak.

### Gambar Latar CSS

Gambar yang dipasang melalui properti CSS `background-image` diperlakukan berbeda oleh browser. Browser baru menemukan gambar tersebut setelah mengunduh dan memproses file CSS. Akibatnya, gambar latar biasanya mulai diunduh lebih lambat dibanding gambar di HTML. Jika gambar latar adalah elemen penting di layar pertama, keterlambatan ini terasa. Pertimbangkan menggunakan elemen `<img>` biasa dengan CSS `object-fit` sebagai gantinya.

Jika gambar latar tetap diperlukan, gunakan petunjuk *preload* untuk gambar yang penting. Untuk gambar latar responsif, gunakan fungsi CSS `image-set()` agar browser bisa memilih versi sesuai kepadatan layar. Gunakan juga *media query* untuk menyajikan gambar latar yang lebih kecil di layar sempit. Ingat bahwa gambar latar tidak memiliki teks alternatif. Jangan gunakan gambar latar untuk gambar yang mengandung informasi penting bagi pembaca.

## Optimasi Gambar untuk SEO

Optimasi gambar tidak hanya soal kecepatan, tetapi juga soal visibilitas di mesin pencari. Google Gambar adalah salah satu sumber trafik yang sering diabaikan. Banyak orang mencari ide desain, resep, produk, atau cara melakukan sesuatu melalui pencarian gambar. Gambar juga bisa muncul di hasil pencarian utama dan di fitur seperti Google Discover. Berikut cara membuat gambar lebih mudah ditemukan dan dipahami oleh mesin pencari.

### Gunakan Nama File yang Deskriptif

Nama file memberikan petunjuk awal tentang isi gambar. Nama seperti `IMG_20240815_093211.jpg` tidak menjelaskan apa pun. Ganti dengan nama yang menggambarkan isi gambar, seperti `nasi-goreng-kampung-telur-ceplok.webp`. Gunakan huruf kecil dan pisahkan kata dengan tanda hubung. Jangan menjejalkan kata kunci secara berlebihan ke dalam nama file.

### Tulis Teks Alternatif yang Tepat

Teks alternatif atau *alt text* adalah deskripsi gambar yang ditulis di atribut `alt`. Teks ini dibacakan oleh pembaca layar untuk pengguna tunanetra. Teks ini juga ditampilkan jika gambar gagal dimuat. Bagi mesin pencari, teks alternatif adalah sumber informasi penting untuk memahami isi gambar. Google menyebutkan bahwa teks alternatif yang deskriptif membantu sistemnya memahami gambar dan konteks halaman.

Tulis teks alternatif yang singkat, spesifik, dan menggambarkan isi gambar sesuai konteks halaman. Contoh yang kurang baik adalah `alt="sepatu"`. Contoh yang lebih baik adalah `alt="Sepatu lari pria warna hitam dengan sol putih tampak samping"`. Hindari memulai dengan frasa "gambar dari" atau "foto dari", karena pembaca layar sudah memberi tahu bahwa elemen tersebut adalah gambar. Jangan menuliskan deretan kata kunci yang tidak menggambarkan gambar.

### Tempatkan Gambar di Dekat Teks yang Relevan

Mesin pencari memahami gambar tidak hanya dari teks alternatif, tetapi juga dari teks di sekitarnya. Gambar yang diletakkan di dekat paragraf yang membahas isinya akan lebih mudah dipahami. Keterangan gambar atau *caption* juga memberikan konteks tambahan. Pembaca pun sering membaca keterangan gambar karena letaknya menonjol. Gunakan elemen `<figure>` dan `<figcaption>` untuk menuliskan keterangan secara semantis.

```html
<figure>
  <img src="/gambar/grafik-penjualan-2026.webp" width="1200" height="675"
       alt="Grafik batang penjualan bulanan toko yang naik dari Januari hingga Juni"
       loading="lazy">
  <figcaption>Penjualan bulanan selama semester pertama.</figcaption>
</figure>
```

### Gunakan Gambar yang Orisinal dan Berkualitas

Gambar stok yang sama sering digunakan oleh ribuan website. Gambar seperti itu tidak memberi nilai tambah dan sulit menonjol di pencarian gambar. Gambar orisinal, seperti foto produk asli, foto proses kerja, atau grafik buatan sendiri, lebih berharga. Gambar orisinal juga memperkuat kesan pengalaman nyata yang dihargai pembaca. Jika harus menggunakan gambar stok, pilih yang relevan dan tambahkan konteks yang jelas.

Untuk tampil dengan baik di Google Discover, Google menyarankan penggunaan gambar besar yang berkualitas tinggi. Panduan Google menyebutkan gambar dengan lebar minimal 1200 piksel. Halaman juga perlu mengizinkan pratinjau gambar besar melalui pengaturan `max-image-preview:large` atau dengan menggunakan AMP. Gambar besar ini tidak harus menjadi gambar yang dimuat di setiap perangkat. Dengan teknik gambar responsif, perangkat kecil tetap mengunduh versi yang lebih ringan.

### Sitemap Gambar dan Data Terstruktur

Sitemap gambar membantu Google menemukan gambar yang mungkin tidak ditemukan melalui perayapan biasa. Misalnya, gambar yang dimuat melalui JavaScript. Anda bisa menambahkan informasi gambar ke sitemap halaman yang sudah ada menggunakan tag `image:image` dan `image:loc`. Google telah menyederhanakan dukungan tag sitemap gambar, sehingga tag lain seperti judul dan keterangan tidak lagi digunakan. Pastikan URL gambar di sitemap dapat diakses dan tidak diblokir oleh robots.txt.

Data terstruktur juga dapat membantu gambar tampil lebih menonjol. Untuk halaman produk, resep, dan artikel, sertakan properti gambar di data terstruktur yang sesuai. Gambar tersebut bisa ditampilkan sebagai bagian dari hasil kaya di pencarian. Pastikan gambar yang dicantumkan di data terstruktur memang terlihat di halaman. Uji data terstruktur dengan alat Rich Results Test dari Google.

### Pastikan Gambar Dapat Dirayapi

Gambar yang ingin tampil di pencarian harus bisa diakses oleh Googlebot. Jangan memblokir folder gambar di robots.txt jika gambar tersebut penting. Gunakan elemen `<img>` dengan atribut `src` yang jelas, karena Google tidak mengindeks gambar latar CSS. Jika menggunakan lazy load berbasis JavaScript, pastikan URL gambar tetap tersedia di HTML yang dirender. Lazy load bawaan browser dengan atribut `loading="lazy"` aman untuk keperluan ini.

## Gambar dan Aksesibilitas

Aksesibilitas berarti memastikan website dapat digunakan oleh semua orang, termasuk penyandang disabilitas. Gambar memiliki peran besar dalam aksesibilitas. Pengguna tunanetra mengandalkan teks alternatif untuk memahami isi gambar. Pengguna dengan penglihatan terbatas membutuhkan kontras dan ukuran yang memadai. Memperhatikan aksesibilitas juga sering sejalan dengan praktik SEO yang baik.

**Bedakan gambar informatif dan dekoratif.** Gambar informatif menyampaikan isi yang penting, seperti grafik, foto produk, atau diagram. Gambar seperti ini wajib memiliki teks alternatif yang deskriptif. Gambar dekoratif hanya berfungsi sebagai hiasan, seperti garis pemisah atau pola latar. Untuk gambar dekoratif, gunakan atribut `alt=""` yang kosong agar pembaca layar melewatinya. Jangan menghapus atribut `alt` sama sekali, karena pembaca layar mungkin membacakan nama file.

**Hindari teks di dalam gambar.** Teks yang ditulis di dalam gambar tidak bisa dibaca oleh pembaca layar, tidak bisa diperbesar dengan baik, dan tidak bisa diterjemahkan otomatis. Teks seperti itu juga sulit dipahami oleh mesin pencari. Jika memungkinkan, tulis teks sebagai HTML biasa dan letakkan di atas gambar dengan CSS. Jika teks di dalam gambar tidak bisa dihindari, misalnya pada infografik, cantumkan isi teks tersebut di teks alternatif atau di paragraf terdekat. Untuk infografik yang panjang, sediakan versi teks lengkap di halaman.

**Jelaskan grafik dan diagram dengan memadai.** Grafik dan diagram sering mengandung informasi yang kompleks. Teks alternatif yang singkat mungkin tidak cukup untuk menjelaskan semuanya. Tuliskan ringkasan temuan utama di teks alternatif, lalu jelaskan detailnya di paragraf sekitar. Untuk data yang penting, sediakan juga tabel HTML. Dengan begitu, semua pengguna bisa mengakses informasi yang sama.

## Optimasi Gambar di WordPress

WordPress memiliki beberapa fitur bawaan yang membantu optimasi gambar. Saat gambar diunggah, WordPress otomatis membuat beberapa versi dengan ukuran berbeda. WordPress juga otomatis menambahkan atribut `srcset` dan `sizes` pada gambar di dalam konten. Atribut lebar, tinggi, dan `loading="lazy"` juga ditambahkan secara otomatis pada banyak kasus. Fitur-fitur ini sudah menangani sebagian pekerjaan optimasi.

Versi WordPress yang lebih baru juga mendukung pengunggahan gambar WebP dan AVIF, selama server memiliki pustaka pengolah gambar yang mendukung format tersebut. Untuk mengonversi gambar yang sudah ada atau mengonversi gambar secara otomatis saat diunggah, Anda bisa menggunakan plugin optimasi gambar. Banyak plugin juga menyediakan fitur kompresi massal untuk gambar lama. Pilih plugin yang memproses gambar di server Anda sendiri atau melalui layanan yang terpercaya. Perhatikan juga batas kuota pada paket gratis plugin tersebut.

Beberapa tips tambahan untuk pengguna WordPress dapat membantu. Pertama, atur ukuran gambar bawaan di menu Pengaturan Media agar sesuai dengan tata letak tema. Kedua, hapus ukuran gambar tambahan yang dibuat tema atau plugin jika tidak digunakan, karena setiap ukuran memakan ruang penyimpanan. Ketiga, latih penulis untuk mengisi teks alternatif setiap kali mengunggah gambar. Keempat, periksa apakah tema menerapkan lazy load pada gambar utama dan kecualikan jika perlu.

## Alat Optimasi Gambar yang Direkomendasikan

Ada banyak alat yang dapat membantu mengoptimasi gambar. Sebagian berupa aplikasi web yang mudah digunakan, sebagian lagi berupa perangkat lunak baris perintah untuk otomatisasi. Pilih alat sesuai kebutuhan dan tingkat keahlian Anda. Untuk penggunaan sesekali, alat berbasis web sudah cukup. Untuk proses rutin dalam jumlah besar, gunakan alat yang bisa diotomatiskan.

**Squoosh.** Squoosh adalah aplikasi web dari tim Chrome Labs untuk mengompres dan mengonversi gambar. Aplikasi ini menampilkan perbandingan berdampingan antara gambar asli dan hasil kompresi. Anda bisa mengatur format, kualitas, dan dimensi secara langsung. Pemrosesan dilakukan di browser, sehingga gambar tidak perlu dikirim ke server. Alat ini sangat cocok untuk belajar memahami efek pengaturan kompresi.

**TinyPNG dan TinyJPG.** Layanan web ini populer karena kemudahannya. Cukup unggah gambar, lalu layanan akan mengompresnya secara otomatis. Layanan ini mendukung format PNG, JPEG, WebP, dan AVIF. Tersedia juga API dan plugin untuk integrasi dengan CMS. Versi gratis memiliki batas jumlah dan ukuran gambar.

**ImageOptim dan alat desktop lainnya.** ImageOptim adalah aplikasi untuk macOS yang mengompres gambar dengan cara menarik dan melepas file. Aplikasi ini juga menghapus metadata secara otomatis. Pengguna Windows dan Linux memiliki pilihan alat serupa. Alat desktop cocok untuk desainer dan penulis yang mengolah gambar sebelum diunggah. Keuntungannya, gambar sudah optimal sebelum masuk ke website.

**Alat baris perintah.** Untuk otomatisasi, alat seperti `cwebp`, `avifenc`, ImageMagick, dan libvips sangat berguna. Alat-alat ini bisa dipanggil dari skrip untuk memproses banyak gambar sekaligus. Pustaka `sharp` untuk Node.js dan ekstensi GD atau Imagick untuk PHP bisa digunakan langsung di dalam aplikasi. Untuk SVG, gunakan SVGO. Kombinasi alat-alat ini memungkinkan pembuatan alur optimasi yang sepenuhnya otomatis.

## Optimasi Gambar untuk Toko Daring

Toko daring adalah jenis website yang paling bergantung pada gambar. Calon pembeli tidak bisa menyentuh atau mencoba barang secara langsung. Mereka mengandalkan foto untuk menilai warna, bahan, ukuran, dan detail produk. Karena itu, kualitas gambar tidak boleh dikorbankan demi kecepatan. Tantangannya adalah menyajikan gambar yang detail tanpa membuat halaman berat.

**Bedakan gambar daftar dan gambar detail.** Di halaman kategori, gambar produk ditampilkan kecil dalam bentuk kisi. Gunakan versi gambar mini yang ringan untuk tampilan ini. Di halaman produk, tampilkan gambar yang lebih besar dan tajam. Versi resolusi tinggi untuk fitur perbesaran sebaiknya baru dimuat saat pengguna mengaktifkan fitur tersebut. Dengan cara ini, pengunjung yang hanya melihat sekilas tidak perlu mengunduh gambar besar.

**Kelola galeri produk dengan cermat.** Halaman produk sering memiliki banyak foto dalam galeri atau *carousel*. Hanya foto pertama yang langsung terlihat saat halaman dibuka. Muat foto pertama dengan prioritas tinggi dan tunda pemuatan foto-foto berikutnya. Pastikan *carousel* tidak memuat semua gambar resolusi penuh sekaligus. Gunakan gambar mini untuk navigasi galeri.

**Jaga konsistensi latar dan rasio.** Foto produk dengan latar dan rasio yang seragam terlihat lebih rapi di halaman kategori. Konsistensi rasio juga memudahkan pengaturan dimensi untuk mencegah pergeseran tata letak. Latar polos cenderung menghasilkan ukuran file lebih kecil setelah dikompres. Buat panduan pemotretan sederhana untuk tim atau mitra penjual. Panduan ini menghemat waktu penyuntingan di kemudian hari.

**Manfaatkan data terstruktur produk.** Cantumkan gambar produk di data terstruktur Product. Gambar ini dapat ditampilkan di hasil pencarian bersama harga dan ketersediaan. Gunakan beberapa gambar dengan rasio berbeda jika memungkinkan. Pastikan gambar tersebut sama dengan yang tampil di halaman. Informasi yang konsisten meningkatkan kepercayaan calon pembeli.

## Mengganti GIF dengan Video

Animasi GIF masih sering digunakan untuk tutorial singkat, demo produk, atau konten hiburan. Padahal, GIF adalah format yang sangat boros untuk animasi. Setiap bingkai disimpan hampir seperti gambar terpisah dengan palet warna terbatas. Video modern menggunakan kompresi yang jauh lebih efisien antarbingkai. Hasilnya, video dengan isi yang sama bisa berukuran jauh lebih kecil dan terlihat lebih jernih.

Untuk menggantikan GIF, konversi animasi menjadi video MP4 dan WebM. Tampilkan video menggunakan elemen `<video>` dengan atribut `autoplay`, `muted`, `loop`, dan `playsinline`. Kombinasi atribut ini membuat video berputar otomatis tanpa suara, seperti perilaku GIF. Tambahkan atribut `width`, `height`, dan gambar pratinjau melalui atribut `poster`. Jika video berada di bagian bawah halaman, tunda pemuatannya agar tidak membebani awal pemuatan.

```html
<video autoplay muted loop playsinline width="640" height="360" poster="/media/demo-poster.webp">
  <source src="/media/demo-fitur.webm" type="video/webm">
  <source src="/media/demo-fitur.mp4" type="video/mp4">
</video>
```

Pertimbangkan juga pengguna yang sensitif terhadap gerakan. Beberapa orang merasa tidak nyaman atau pusing melihat animasi yang terus bergerak. Gunakan *media query* `prefers-reduced-motion` untuk menghentikan putar otomatis bagi pengguna yang mengaktifkan pengaturan tersebut. Sediakan juga tombol untuk menjeda animasi. Langkah kecil ini membuat website lebih ramah bagi semua pengguna.

## Kesalahan Umum dalam Optimasi Gambar

Banyak website sudah berusaha mengoptimasi gambar, tetapi masih melakukan kesalahan yang mengurangi hasilnya. Sebagian kesalahan membuat gambar tetap berat. Sebagian lain membuat gambar terlihat buruk atau sulit ditemukan mesin pencari. Kenali kesalahan-kesalahan berikut agar Anda bisa menghindarinya. Periksa juga apakah website Anda saat ini mengalami salah satunya.

**Mengunggah gambar langsung dari kamera.** Foto dari kamera atau ponsel modern berdimensi sangat besar dan berukuran beberapa megabita. Mengunggahnya langsung tanpa diolah adalah penyebab paling umum halaman yang berat. Meskipun CMS membuat versi yang lebih kecil, file asli sering masih digunakan di beberapa tempat. Biasakan mengubah ukuran dan mengompres gambar sebelum diunggah. Lebih baik lagi, otomatiskan proses ini di server.

**Mengompres terlalu agresif.** Mengejar ukuran file sekecil mungkin bisa membuat kualitas gambar rusak. Foto produk yang buram atau penuh artefak membuat calon pembeli ragu. Gambar berkualitas rendah juga mencerminkan citra merek yang kurang profesional. Selalu periksa hasil kompresi secara visual pada ukuran tampilan sebenarnya. Cari titik keseimbangan, bukan angka terkecil.

**Menerapkan lazy load pada gambar utama.** Kesalahan ini sudah disinggung sebelumnya, tetapi sangat sering terjadi sehingga perlu diulang. Banyak plugin dan tema menerapkan lazy load ke semua gambar secara otomatis. Akibatnya, gambar sampul artikel atau banner utama dimuat terlambat. Konten utama pun tampil lebih lambat dari seharusnya. Periksa kode HTML halaman dan pastikan gambar di layar pertama tidak memiliki atribut `loading="lazy"`.

**Lupa menulis atribut dimensi.** Gambar tanpa atribut `width` dan `height` menyebabkan tata letak bergeser saat dimuat. Masalah ini sering muncul pada gambar yang disisipkan secara manual atau melalui pembangun halaman. Pergeseran tata letak mengganggu pembaca dan merusak metrik stabilitas. Biasakan selalu mencantumkan kedua atribut tersebut. Sebagian besar CMS dan framework modern sudah menambahkannya secara otomatis.

**Mengabaikan teks alternatif.** Banyak gambar diunggah tanpa teks alternatif atau dengan teks alternatif yang hanya berisi nama file. Kebiasaan ini merugikan pengguna pembaca layar sekaligus SEO. Menulis teks alternatif hanya membutuhkan beberapa detik untuk setiap gambar. Jadikan pengisian teks alternatif sebagai bagian wajib dari proses penerbitan. Untuk gambar lama, lakukan audit dan lengkapi secara bertahap.

**Menggunakan format yang salah.** Foto disimpan dalam PNG, logo disimpan dalam JPEG, dan animasi menggunakan GIF berukuran besar. Kesalahan format ini membuat ukuran file jauh lebih besar dari yang diperlukan. Logo dalam JPEG juga terlihat kabur di sekitar tepinya. Tinjau kembali panduan pemilihan format di atas. Mengganti format yang salah sering memberikan penghematan yang sangat besar.

**Tidak menyediakan gambar responsif.** Menyajikan satu ukuran gambar untuk semua perangkat berarti pengguna ponsel mengunduh gambar seukuran layar desktop. Masalah ini sangat merugikan di jaringan seluler yang lambat. Gunakan atribut `srcset` dan `sizes` untuk menyediakan beberapa ukuran. Pastikan nilai `sizes` sesuai dengan tata letak yang sebenarnya. Uji di beberapa ukuran layar untuk memastikan browser memilih versi yang tepat.

## Checklist Optimasi Gambar

Gunakan daftar periksa berikut setiap kali menambahkan gambar ke website. Daftar ini merangkum langkah-langkah penting yang telah dibahas. Anda bisa membagikannya kepada tim konten sebagai panduan kerja. Jika semua poin terpenuhi, gambar Anda sudah teroptimasi dengan baik. Simpan daftar ini di tempat yang mudah diakses.

1. Format sudah sesuai dengan jenis gambar.
2. Dimensi gambar tidak jauh melebihi ukuran tampilan terbesarnya.
3. Gambar sudah dikompres dan kualitasnya sudah diperiksa secara visual.
4. Beberapa ukuran gambar tersedia melalui atribut `srcset` dengan nilai `sizes` yang akurat.
5. Gambar di bawah layar pertama menggunakan `loading="lazy"`.
6. Gambar utama di layar pertama tidak di-lazy load dan diberi prioritas tinggi.
7. Atribut `width` dan `height` sudah dicantumkan.
8. Metadata lokasi dan data kamera sudah dihapus.
9. Nama file sudah deskriptif.
10. Teks alternatif sudah ditulis sesuai isi dan konteks gambar.
11. File gambar disajikan dengan pengaturan cache yang panjang.

## FAQ Optimasi Gambar

### Format gambar apa yang terbaik untuk website?

Untuk foto, WebP dan AVIF adalah pilihan terbaik karena ukurannya kecil dengan kualitas yang baik. Untuk logo dan ikon, gunakan SVG. Untuk tangkapan layar dan gambar dengan teks, gunakan WebP lossless atau PNG.

### Berapa ukuran file gambar yang ideal untuk website?

Tidak ada angka yang berlaku untuk semua gambar karena ukuran bergantung pada dimensi dan isi gambar. Prinsipnya, gunakan dimensi sesuai kebutuhan tampilan dan kompres hingga kualitas masih nyaman dilihat. Gambar sampul artikel yang dioptimasi dengan baik umumnya berukuran puluhan hingga sekitar seratusan kilobita.

### Apakah WebP didukung semua browser?

WebP didukung oleh semua browser modern utama, termasuk Chrome, Firefox, Safari, dan Edge. Browser yang sangat lama mungkin belum mendukungnya. Jika ingin aman, gunakan elemen `<picture>` dengan cadangan JPEG atau PNG.

### Apakah lazy load buruk untuk SEO?

Tidak, selama diterapkan dengan benar. Lazy load bawaan browser dengan atribut `loading="lazy"` aman untuk mesin pencari. Pastikan saja gambar utama di layar pertama tidak di-lazy load dan URL gambar tetap ada di HTML.

### Apakah teks alternatif harus mengandung kata kunci?

Teks alternatif sebaiknya menggambarkan isi gambar secara akurat. Jika kata kunci relevan dengan isi gambar, kata kunci tersebut akan muncul secara alami. Jangan memaksakan kata kunci yang tidak menggambarkan gambar.

### Apakah perlu menyimpan gambar asli setelah dioptimasi?

Menyimpan gambar asli di tempat cadangan sangat dianjurkan. Gambar asli dibutuhkan jika suatu saat Anda ingin membuat ukuran baru atau mengonversi ke format yang lebih baru. Simpan di penyimpanan terpisah agar tidak memenuhi ruang hosting website.

## Kesimpulan

Optimasi gambar website adalah salah satu langkah paling efektif untuk membuat halaman lebih cepat dan ringan. Mulailah dengan memilih format yang tepat, seperti AVIF atau WebP untuk foto dan SVG untuk logo. Sesuaikan dimensi gambar dengan ukuran tampilan, kompres dengan tingkat kualitas yang wajar, dan sediakan versi responsif dengan `srcset`. Atur pemuatan dengan lazy load untuk gambar di bawah layar pertama, dan berikan prioritas pada gambar utama. Jangan lupa mencantumkan dimensi, menghapus metadata, dan mengatur cache.

Selain kecepatan, perhatikan juga sisi SEO dan aksesibilitas. Gunakan nama file yang deskriptif, teks alternatif yang tepat, dan gambar orisinal yang relevan dengan konten. Untuk website besar, otomatiskan proses optimasi agar setiap gambar baru langsung optimal. Setelah gambar beres, lanjutkan dengan teknik lain di artikel cara mempercepat loading website. Pantau hasilnya melalui metrik di artikel Core Web Vitals untuk memastikan pengalaman pengunjung terus membaik.
