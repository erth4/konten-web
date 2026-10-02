---
title: "Cara Mempercepat Loading Website: 20 Teknik yang Terbukti Efektif"
meta_description: "Website lambat? Ikuti 20 cara mempercepat loading website: hosting, caching, CDN, kompresi, HTTP/2, optimasi CSS-JavaScript, font, database, hingga tips WordPress."
slug: "cara-mempercepat-loading-website"
focus_keyword: "cara mempercepat loading website"
keywords:
  - cara mempercepat loading website
  - website lambat
  - optimasi kecepatan website
  - cache website
  - CDN adalah
  - kompresi gzip brotli
  - mempercepat wordpress
  - page speed
category: "Performa"
tags: ["Performa Website", "Kecepatan Website", "Web Development", "WordPress"]
date: "2026-10-02"
lang: "id"
---

# Cara Mempercepat Loading Website: 20 Teknik yang Terbukti Efektif

Website yang lambat adalah salah satu penyebab utama pengunjung pergi sebelum sempat melihat isinya. Pengguna internet saat ini terbiasa dengan aplikasi yang responsif. Mereka jarang mau menunggu lama hanya untuk membuka sebuah halaman. Bagi pemilik bisnis, setiap detik keterlambatan bisa berarti calon pelanggan yang hilang. Bagi blogger, halaman yang lambat berarti pembaca yang tidak sempat membaca artikel.

Kabar baiknya, sebagian besar masalah kecepatan bisa diperbaiki dengan langkah yang jelas. Artikel ini menyajikan **cara mempercepat loading website** yang disusun dari sisi server hingga sisi browser. Anda akan mempelajari cara mengukur kecepatan, memilih hosting, mengatur *caching*, menggunakan CDN, dan mengoptimasi CSS, JavaScript, serta font. Kami juga menyertakan tips khusus untuk WordPress dan aplikasi berbasis PHP. Setiap teknik dilengkapi penjelasan tentang mengapa teknik itu bekerja, sehingga Anda bisa menyesuaikannya dengan kondisi website Anda.

## Daftar Isi

1. [Mengapa Kecepatan Website Penting?](#mengapa-kecepatan-website-penting)
2. [Apa yang Terjadi Saat Halaman Dimuat?](#apa-yang-terjadi-saat-halaman-dimuat)
3. [Cara Mengukur Kecepatan Website](#cara-mengukur-kecepatan-website)
4. [Optimasi di Sisi Server](#optimasi-di-sisi-server)
5. [Optimasi Pengiriman Konten](#optimasi-pengiriman-konten)
6. [Optimasi CSS dan JavaScript](#optimasi-css-dan-javascript)
7. [Optimasi Font, Gambar, dan Media](#optimasi-font-gambar-dan-media)
8. [Optimasi Navigasi Antarhalaman](#optimasi-navigasi-antarhalaman)
9. [Tips Khusus WordPress dan PHP](#tips-khusus-wordpress-dan-php)
10. [Menyusun Prioritas Perbaikan](#menyusun-prioritas-perbaikan)
11. [Menjaga Kecepatan dalam Jangka Panjang](#menjaga-kecepatan-dalam-jangka-panjang)
12. [Kesalahan Umum Saat Mempercepat Website](#kesalahan-umum-saat-mempercepat-website)
13. [Checklist Cepat Mempercepat Website](#checklist-cepat-mempercepat-website)
14. [FAQ Mempercepat Website](#faq-mempercepat-website)
15. [Kesimpulan](#kesimpulan)

## Mengapa Kecepatan Website Penting?

Kecepatan website memengaruhi hampir semua aspek keberhasilan sebuah website. Aspek yang paling jelas adalah kenyamanan pengunjung. Halaman yang cepat terasa profesional dan dapat diandalkan. Sebaliknya, halaman yang lambat menimbulkan kesan bahwa website tidak terurus. Kesan pertama ini sangat memengaruhi keputusan pengunjung untuk tetap tinggal atau pergi.

Kecepatan juga berpengaruh pada pencapaian bisnis. Di toko daring, halaman produk yang lambat dapat membuat calon pembeli membatalkan niatnya. Di website layanan, formulir yang lambat merespons bisa membuat calon klien menyerah. Banyak perusahaan teknologi telah membagikan studi kasus tentang perbaikan kecepatan yang diikuti peningkatan konversi. Meski hasil setiap website berbeda, polanya cukup konsisten.

Dari sisi mesin pencari, kecepatan merupakan bagian dari pengalaman halaman yang diperhatikan Google. Metrik seperti Largest Contentful Paint sangat dipengaruhi oleh kecepatan server dan ukuran sumber daya. Penjelasan lengkap metrik tersebut ada di artikel [Core Web Vitals](/core-web-vitals-lcp-inp-cls/). Website yang cepat juga lebih mudah dirayapi oleh mesin pencari. Server yang responsif memungkinkan lebih banyak halaman dirayapi dalam waktu yang sama.

Terakhir, kecepatan berkaitan dengan biaya dan inklusivitas. Halaman yang ringan menghemat kuota data pengunjung. Hal ini penting di Indonesia, di mana banyak pengguna masih mengandalkan paket data dengan kuota terbatas. Halaman yang efisien juga mengurangi beban server dan biaya bandwidth. Dengan kata lain, website yang cepat menguntungkan pengunjung sekaligus pemilik website.

## Apa yang Terjadi Saat Halaman Dimuat?

Untuk mempercepat website, Anda perlu memahami apa yang terjadi saat halaman dimuat. Proses ini terdiri dari beberapa tahap yang berurutan. Setiap tahap bisa menjadi sumber keterlambatan. Dengan memahami alurnya, Anda bisa menebak di mana masalah kemungkinan berada. Berikut gambaran sederhananya.

**Tahap pertama adalah pencarian DNS.** Browser perlu mengetahui alamat IP server dari nama domain yang diketik. Proses ini dilakukan dengan bertanya kepada server DNS. Jika penyedia DNS lambat, tahap ini bisa memakan waktu cukup lama. Hasil pencarian biasanya disimpan sementara, sehingga kunjungan berikutnya lebih cepat. Menggunakan penyedia DNS yang andal membantu mempercepat tahap ini.

**Tahap kedua adalah membuka koneksi.** Browser membuka koneksi ke server dan melakukan negosiasi keamanan untuk HTTPS. Setiap pertukaran pesan dalam proses ini membutuhkan waktu perjalanan bolak-balik antara browser dan server. Semakin jauh jarak fisik ke server, semakin lama waktu perjalanan tersebut. Protokol modern seperti HTTP/3 dan TLS 1.3 mengurangi jumlah pertukaran yang diperlukan. CDN juga membantu dengan memperpendek jarak ke pengguna.

**Tahap ketiga adalah server memproses permintaan.** Server menerima permintaan dan menyiapkan respons. Untuk halaman dinamis, server mungkin perlu menjalankan kode aplikasi dan mengambil data dari basis data. Jika proses ini lambat, browser hanya bisa menunggu. Waktu sampai byte pertama diterima dikenal sebagai *Time to First Byte* atau TTFB. Caching di server adalah cara paling efektif untuk memperpendek tahap ini.

**Tahap keempat adalah mengunduh dan memproses sumber daya.** Setelah menerima HTML, browser membacanya dan menemukan sumber daya lain seperti CSS, JavaScript, font, dan gambar. Browser kemudian mengunduh sumber daya tersebut. Sebagian sumber daya, terutama CSS dan skrip sinkron, menghalangi browser menampilkan halaman sampai selesai diproses. Ukuran dan jumlah sumber daya sangat memengaruhi tahap ini. Sebagian besar teknik optimasi di sisi browser berfokus pada tahap ini.

**Tahap kelima adalah rendering dan interaksi.** Browser menyusun tata letak dan menggambar halaman di layar. Setelah itu, JavaScript dijalankan untuk membuat halaman interaktif. Jika JavaScript terlalu berat, halaman mungkin sudah terlihat tetapi belum bisa diklik dengan lancar. Tahap ini sangat bergantung pada kemampuan perangkat pengguna. Ponsel kelas menengah memproses JavaScript jauh lebih lambat daripada laptop.

## Cara Mengukur Kecepatan Website

Langkah pertama sebelum melakukan optimasi adalah mengukur. Tanpa pengukuran, Anda tidak tahu apa yang perlu diperbaiki dan apakah perbaikan berhasil. Ukur kondisi awal, catat hasilnya, lalu bandingkan setelah setiap perubahan. Gunakan beberapa alat untuk mendapatkan gambaran yang lengkap. Berikut alat yang paling umum digunakan.

**PageSpeed Insights.** Alat gratis dari Google ini menampilkan data pengguna nyata dan hasil pengujian laboratorium. Laporan ini juga memberikan daftar peluang perbaikan beserta perkiraan penghematannya. Gunakan alat ini untuk mendapatkan gambaran awal tentang kondisi halaman. Uji beberapa jenis halaman, seperti beranda, artikel, dan halaman produk. Setiap jenis halaman sering memiliki masalah yang berbeda.

**WebPageTest.** Alat ini memungkinkan pengujian dari berbagai lokasi dan kondisi jaringan. Hasilnya dilengkapi diagram *waterfall* yang menunjukkan urutan dan durasi pemuatan setiap sumber daya. Diagram ini sangat berguna untuk melihat sumber daya mana yang paling lambat atau memblokir. WebPageTest juga menampilkan rekaman visual proses pemuatan halaman. Anda bisa melihat dengan jelas kapan konten mulai muncul.

**Panel Network di Chrome DevTools.** Panel ini menampilkan semua permintaan jaringan saat halaman dimuat. Anda bisa melihat ukuran setiap file, waktu unduh, dan apakah file diambil dari *cache*. Fitur simulasi jaringan memungkinkan pengujian dengan kecepatan koneksi yang lebih lambat. Panel ini sangat berguna saat mengembangkan dan menguji perubahan. Biasakan memeriksa total ukuran halaman dan jumlah permintaan di bagian bawah panel.

Saat mengukur, perhatikan beberapa angka penting. Perhatikan TTFB untuk menilai kecepatan server. Perhatikan waktu hingga konten utama tampil untuk menilai pengalaman awal pengguna. Perhatikan juga total ukuran halaman dan jumlah permintaan. Angka-angka ini membantu menentukan apakah masalah utama ada di server, di jaringan, atau di browser.

## Optimasi di Sisi Server

Optimasi di sisi server adalah fondasi dari semua upaya mempercepat website. Jika server lambat, optimasi di sisi browser tidak akan banyak membantu. Browser tidak bisa mulai bekerja sebelum menerima respons pertama dari server. Karena itu, mulailah dari sini jika TTFB website Anda tinggi. Berikut teknik-teknik optimasi di sisi server.

### 1. Gunakan Hosting yang Memadai dan Dekat dengan Pengguna

Kualitas hosting sangat menentukan kecepatan website. Hosting murah dengan sumber daya yang dibagi ke sangat banyak website sering kali lambat saat trafik meningkat. Server yang kelebihan beban akan membutuhkan waktu lama untuk merespons setiap permintaan. Pilih paket hosting yang sesuai dengan ukuran dan trafik website Anda. Jangan memilih hanya berdasarkan harga termurah.

Perhatikan juga lokasi pusat data hosting. Jika sebagian besar pengunjung berasal dari Indonesia, pilih server yang berada di Indonesia atau di negara terdekat seperti Singapura. Jarak fisik yang lebih dekat berarti waktu perjalanan data yang lebih singkat. Perbedaan ini sangat terasa pada tahap pembukaan koneksi. Untuk pengunjung dari banyak negara, kombinasikan hosting dengan CDN.

Seiring bertambahnya trafik, pertimbangkan untuk naik ke jenis hosting yang lebih kuat. Pilihan yang umum adalah VPS, *cloud hosting*, atau server khusus. Jenis hosting ini memberikan sumber daya yang lebih terjamin. Anda juga mendapat kendali lebih besar atas konfigurasi server. Namun, pengelolaannya membutuhkan pengetahuan teknis yang lebih dalam.

### 2. Gunakan Versi Runtime yang Terbaru

Bahasa pemrograman di sisi server terus diperbarui, dan versi baru sering membawa peningkatan kinerja. Untuk website berbasis PHP, setiap versi utama biasanya memproses kode dengan lebih efisien daripada versi sebelumnya. Hal yang sama berlaku untuk Node.js, Python, dan bahasa lainnya. Versi lama juga berhenti menerima pembaruan keamanan setelah masa dukungannya berakhir. Jadi, memperbarui runtime bermanfaat untuk kecepatan sekaligus keamanan.

Sebelum memperbarui, uji kompatibilitas aplikasi di lingkungan pengujian. Beberapa plugin atau pustaka lama mungkin belum mendukung versi terbaru. Perbarui pustaka-pustaka tersebut terlebih dahulu, atau cari penggantinya. Untuk PHP, pastikan juga ekstensi OPcache aktif. OPcache menyimpan kode PHP yang sudah dikompilasi di memori, sehingga tidak perlu dikompilasi ulang di setiap permintaan.

### 3. Aktifkan Caching Halaman di Server

Caching halaman adalah teknik menyimpan hasil akhir halaman dalam bentuk HTML siap kirim. Tanpa caching, server harus menjalankan kode dan mengambil data dari basis data setiap kali halaman diminta. Dengan caching, server cukup mengirimkan HTML yang sudah tersimpan. Perbedaannya bisa sangat besar, terutama untuk halaman yang kontennya jarang berubah. Teknik ini adalah salah satu cara paling efektif untuk menurunkan TTFB.

Caching halaman bisa dilakukan di beberapa tingkat. Di tingkat aplikasi, plugin atau modul caching menyimpan HTML dalam bentuk file atau di memori. Di tingkat server web, modul seperti FastCGI cache di Nginx dapat menyimpan respons secara langsung. Di tingkat jaringan, CDN atau *reverse proxy* seperti Varnish juga bisa menyimpan halaman. Pilih tingkat yang sesuai dengan arsitektur website Anda.

Hal yang perlu diperhatikan adalah halaman yang bersifat personal. Halaman keranjang belanja, akun pengguna, dan halaman setelah login tidak boleh disimpan dalam cache bersama. Jika tidak, pengguna bisa melihat data milik orang lain. Atur pengecualian untuk halaman-halaman tersebut dengan cermat. Atur juga mekanisme pembersihan cache agar konten yang diperbarui segera tampil.

### 4. Optimalkan Basis Data dan Gunakan Object Cache

Untuk halaman yang tidak bisa disimpan sepenuhnya dalam cache, kecepatan basis data menjadi sangat penting. Kueri yang tidak efisien bisa memperlambat setiap permintaan. Gunakan indeks pada kolom yang sering digunakan untuk pencarian dan pengurutan. Hindari mengambil data yang tidak diperlukan, misalnya memilih semua kolom padahal hanya butuh beberapa. Aktifkan pencatatan kueri lambat untuk menemukan kueri yang bermasalah.

*Object cache* menyimpan hasil kueri atau perhitungan yang sering digunakan di memori. Sistem seperti Redis dan Memcached sangat populer untuk keperluan ini. Ketika data yang sama dibutuhkan kembali, aplikasi mengambilnya dari memori yang jauh lebih cepat daripada basis data. Teknik ini sangat bermanfaat untuk website dinamis seperti toko daring dan forum. Pastikan data di cache diperbarui ketika data aslinya berubah.

Bersihkan juga basis data secara berkala. Seiring waktu, basis data bisa dipenuhi data yang tidak lagi dibutuhkan. Contohnya revisi artikel yang menumpuk, komentar spam, dan data sementara yang kedaluwarsa. Data yang menumpuk memperbesar ukuran tabel dan memperlambat kueri. Lakukan pembersihan dengan hati-hati dan selalu buat cadangan terlebih dahulu.

### 5. Kurangi Pengalihan (Redirect)

Setiap pengalihan menambah satu perjalanan bolak-balik antara browser dan server. Jika ada beberapa pengalihan berantai, waktu tunggu bertambah berkali-kali lipat. Contoh rantai yang umum adalah dari HTTP ke HTTPS, lalu dari tanpa www ke www, lalu dari URL lama ke URL baru. Rantai seperti ini sebaiknya disederhanakan menjadi satu pengalihan langsung ke tujuan akhir. Pastikan juga tautan internal langsung mengarah ke URL final.

Periksa pengalihan menggunakan panel Network di DevTools atau alat pemeriksa pengalihan. Perhatikan permintaan dengan kode status 301 atau 302. Perbarui tautan di menu, artikel, dan sitemap agar tidak melewati pengalihan. Untuk pengalihan dari HTTP ke HTTPS, aktifkan HSTS agar browser langsung menggunakan HTTPS pada kunjungan berikutnya. Langkah-langkah kecil ini menghemat waktu di setiap kunjungan.

## Optimasi Pengiriman Konten

Setelah server merespons dengan cepat, langkah berikutnya adalah memastikan data sampai ke browser secepat mungkin. Optimasi pengiriman berfokus pada jarak, ukuran, dan cara data dikirim. Sebagian besar teknik di bagian ini hanya perlu diatur sekali. Namun, dampaknya terasa di setiap kunjungan. Berikut teknik-teknik yang bisa diterapkan.

### 6. Gunakan Content Delivery Network (CDN)

CDN adalah jaringan server yang tersebar di banyak lokasi di seluruh dunia. CDN menyimpan salinan file statis website, seperti gambar, CSS, dan JavaScript. Ketika pengunjung membuka website, file dikirim dari server CDN yang paling dekat dengan lokasi mereka. Hasilnya, jarak tempuh data menjadi jauh lebih pendek. CDN juga mengurangi beban server utama karena sebagian besar permintaan ditangani oleh jaringan CDN.

Banyak CDN modern juga mampu menyimpan halaman HTML dalam cache. Dengan pengaturan yang tepat, seluruh halaman bisa dikirim dari lokasi terdekat tanpa menyentuh server utama. CDN juga sering menyediakan fitur tambahan seperti kompresi otomatis, optimasi gambar, dan perlindungan dari serangan. Banyak penyedia CDN menawarkan paket gratis yang cukup untuk website kecil. Pilih CDN yang memiliki titik kehadiran di Indonesia atau Asia Tenggara.

### 7. Aktifkan Kompresi Brotli atau Gzip

Kompresi mengecilkan ukuran file teks seperti HTML, CSS, JavaScript, dan SVG sebelum dikirim. Browser kemudian membuka kompresi tersebut setelah menerima file. Penghematan ukuran untuk file teks biasanya sangat besar. Gzip sudah lama menjadi standar dan didukung oleh semua browser. Brotli adalah algoritma yang lebih baru dan umumnya menghasilkan file yang lebih kecil daripada Gzip.

Sebagian besar server web dan CDN modern mendukung kedua algoritma tersebut. Aktifkan Brotli sebagai pilihan utama dan Gzip sebagai cadangan untuk klien lama. Periksa apakah kompresi sudah aktif dengan melihat *header* `Content-Encoding` di panel Network. Jangan mengompresi ulang file yang sudah terkompresi, seperti gambar JPEG atau WebP. Upaya tersebut hanya membuang waktu prosesor tanpa memberi penghematan.

Berikut contoh konfigurasi kompresi sederhana di Nginx:

```nginx
gzip on;
gzip_comp_level 5;
gzip_min_length 256;
gzip_types text/css application/javascript application/json image/svg+xml text/plain;

# Brotli memerlukan modul ngx_brotli
brotli on;
brotli_comp_level 5;
brotli_types text/css application/javascript application/json image/svg+xml text/plain;
```

### 8. Gunakan HTTP/2 dan HTTP/3

HTTP/2 memungkinkan banyak file dikirim secara bersamaan melalui satu koneksi. Pada HTTP/1.1, browser harus membuka banyak koneksi atau mengantre untuk mengunduh file. HTTP/2 mengatasi hambatan ini sehingga pengunduhan banyak file kecil menjadi jauh lebih efisien. HTTP/3 melangkah lebih jauh dengan menggunakan protokol QUIC. Protokol ini mempercepat pembukaan koneksi dan lebih tahan terhadap jaringan yang tidak stabil, seperti jaringan seluler.

Sebagian besar hosting modern dan CDN sudah mendukung HTTP/2 secara bawaan. Dukungan HTTP/3 juga semakin luas, terutama di penyedia CDN. Periksa protokol yang digunakan di kolom Protocol pada panel Network. Jika masih menggunakan HTTP/1.1, hubungi penyedia hosting atau aktifkan melalui CDN. Dengan HTTP/2, beberapa trik lama seperti menggabungkan semua file menjadi satu tidak lagi terlalu diperlukan.

### 9. Atur Browser Caching dengan Benar

Browser caching memungkinkan browser menyimpan file di perangkat pengguna. Pada kunjungan berikutnya, browser tidak perlu mengunduh ulang file yang sama. Pengaturannya dilakukan melalui *header* HTTP `Cache-Control`. File statis seperti gambar, font, CSS, dan JavaScript bisa disimpan dalam waktu lama. Halaman HTML biasanya disimpan dalam waktu singkat atau selalu divalidasi ulang.

Agar file statis bisa disimpan lama tanpa masalah, gunakan teknik penamaan berversi. Caranya adalah menambahkan kode unik di nama file, misalnya `app.3f9a2c.js`. Ketika isi file berubah, kodenya ikut berubah, sehingga browser akan mengunduh versi baru. Dengan teknik ini, Anda bisa mengatur masa simpan sangat lama tanpa khawatir pengguna melihat versi lama. Sebagian besar alat build modern menerapkan teknik ini secara otomatis.

Berikut contoh pengaturan `Cache-Control` yang umum digunakan:

```nginx
# File statis dengan nama berversi: simpan selama satu tahun
location ~* \.(css|js|woff2|webp|avif|png|jpg|svg)$ {
  add_header Cache-Control "public, max-age=31536000, immutable";
}

# Dokumen HTML: selalu periksa versi terbaru ke server
location / {
  add_header Cache-Control "no-cache";
}
```

### 10. Gunakan Preconnect untuk Domain Penting

Banyak website memuat sumber daya dari domain lain, seperti CDN font, layanan gambar, atau API. Setiap domain baru membutuhkan pencarian DNS dan pembukaan koneksi tersendiri. Petunjuk `preconnect` memberi tahu browser untuk membuka koneksi ke domain tersebut lebih awal. Dengan begitu, saat sumber daya dibutuhkan, koneksi sudah siap. Teknik ini bisa menghemat waktu yang cukup berarti.

Gunakan `preconnect` hanya untuk satu atau dua domain yang paling penting dan pasti digunakan di awal pemuatan. Terlalu banyak `preconnect` justru membuang sumber daya untuk koneksi yang belum tentu dipakai. Untuk domain yang kurang penting, gunakan `dns-prefetch` yang lebih ringan. Petunjuk ini hanya melakukan pencarian DNS tanpa membuka koneksi penuh. Cara terbaik tetap mengurangi jumlah domain pihak ketiga yang digunakan.

```html
<link rel="preconnect" href="https://cdn.contoh.com" crossorigin>
<link rel="dns-prefetch" href="https://analitik.contoh.com">
```

## Optimasi CSS dan JavaScript

CSS dan JavaScript sering menjadi penyumbang terbesar lambatnya halaman, terutama di perangkat seluler. Keduanya bukan hanya perlu diunduh, tetapi juga harus diproses oleh browser. CSS diperlukan sebelum halaman bisa ditampilkan dengan benar. JavaScript bisa menghentikan proses pembacaan HTML dan membebani prosesor. Mengelola keduanya dengan baik akan berdampak besar pada kecepatan.

### 11. Minifikasi File CSS, JavaScript, dan HTML

Minifikasi adalah proses menghapus karakter yang tidak diperlukan dari kode tanpa mengubah fungsinya. Karakter tersebut meliputi spasi, baris baru, dan komentar. Untuk JavaScript, minifikasi juga bisa memperpendek nama variabel. Hasilnya adalah file yang lebih kecil dan lebih cepat diunduh. Minifikasi paling efektif jika dikombinasikan dengan kompresi Brotli atau Gzip.

Alat build modern seperti Vite, esbuild, dan webpack melakukan minifikasi secara otomatis saat membuat versi produksi. Untuk website berbasis CMS, plugin optimasi biasanya menyediakan fitur ini. Pastikan minifikasi hanya diterapkan pada versi produksi. Versi pengembangan sebaiknya tetap dapat dibaca agar mudah di-*debug*. Setelah mengaktifkan minifikasi, uji website untuk memastikan tidak ada fungsi yang rusak.

### 12. Hapus CSS dan JavaScript yang Tidak Digunakan

Banyak website memuat kode yang sebenarnya tidak digunakan di halaman tersebut. Tema dan plugin sering memuat CSS dan JavaScript di semua halaman, meskipun fiturnya hanya dipakai di satu halaman. Kerangka CSS yang besar juga sering dimuat utuh walaupun hanya sebagian kecil kelas yang digunakan. Kode yang tidak terpakai tetap harus diunduh dan diproses oleh browser. Menghapusnya adalah cara cepat untuk mengurangi beban.

Gunakan fitur Coverage di Chrome DevTools untuk melihat berapa persen kode CSS dan JavaScript yang benar-benar digunakan. Fitur ini menandai baris kode yang dijalankan dan yang tidak. Untuk CSS, alat seperti PurgeCSS dapat menghapus kelas yang tidak digunakan secara otomatis. Untuk JavaScript, fitur *tree shaking* pada alat build menghapus fungsi yang tidak diimpor. Lakukan penghapusan dengan hati-hati dan uji semua halaman setelahnya.

### 13. Tunda JavaScript dengan defer dan async

Secara bawaan, ketika browser menemukan tag `<script>`, browser berhenti membaca HTML untuk mengunduh dan menjalankan skrip tersebut. Perilaku ini menunda tampilan halaman. Atribut `defer` membuat skrip diunduh secara paralel dan baru dijalankan setelah HTML selesai dibaca. Atribut `async` membuat skrip diunduh secara paralel dan dijalankan segera setelah selesai diunduh. Keduanya mencegah skrip memblokir pembacaan HTML.

Gunakan `defer` untuk skrip yang bergantung pada struktur halaman atau pada skrip lain. Skrip dengan `defer` dijalankan sesuai urutan kemunculannya. Gunakan `async` untuk skrip yang berdiri sendiri, seperti skrip analitik. Urutan eksekusi skrip `async` tidak dijamin. Skrip berjenis modul (`type="module"`) secara bawaan sudah berperilaku seperti `defer`.

```html
<!-- Skrip utama aplikasi: dijalankan setelah HTML selesai dibaca -->
<script src="/js/app.js" defer></script>

<!-- Skrip independen: dijalankan begitu selesai diunduh -->
<script src="https://analitik.contoh.com/tag.js" async></script>
```

### 14. Prioritaskan CSS Kritis

CSS kritis adalah gaya yang dibutuhkan untuk menampilkan bagian halaman yang pertama kali terlihat. Dengan menanam CSS kritis langsung di dalam HTML, browser bisa menampilkan bagian atas halaman tanpa menunggu file CSS eksternal. Sisa CSS kemudian dimuat dengan cara yang tidak memblokir tampilan. Teknik ini bisa mempercepat waktu tampil konten pertama secara signifikan. Teknik ini sangat berguna untuk website dengan file CSS yang besar.

Menentukan CSS kritis secara manual cukup rumit. Ada alat yang dapat mengekstraknya secara otomatis dengan menganalisis halaman. Beberapa plugin optimasi WordPress juga menyediakan fitur ini. Pastikan CSS kritis tetap kecil, karena CSS yang ditanam tidak bisa disimpan di cache browser secara terpisah. Jika ukuran total CSS sudah kecil, memuatnya sebagai satu file biasa sering kali sudah cukup.

### 15. Terapkan Code Splitting dan Kurangi Dependensi

*Code splitting* adalah teknik membagi JavaScript menjadi beberapa bagian kecil. Setiap halaman hanya memuat bagian yang dibutuhkan, bukan seluruh kode aplikasi. Bagian lain dimuat saat pengguna berpindah halaman atau membuka fitur tertentu. Framework modern seperti Next.js, Nuxt, dan SvelteKit menerapkan pemisahan per rute secara otomatis. Anda juga bisa memuat komponen secara dinamis dengan sintaks `import()`.

Perhatikan juga pustaka pihak ketiga yang ditambahkan ke proyek. Satu pustaka besar bisa menambah ukuran JavaScript secara drastis. Sebelum menambahkan dependensi, periksa ukurannya dan pertimbangkan alternatif yang lebih ringan. Banyak fungsi sederhana kini tersedia secara bawaan di browser tanpa perlu pustaka tambahan. Gunakan alat analisis *bundle* untuk melihat bagian mana yang paling besar dalam aplikasi Anda.

### 16. Kendalikan Skrip Pihak Ketiga

Skrip pihak ketiga meliputi analitik, iklan, piksel pelacakan, widget obrolan, dan tombol berbagi. Setiap skrip menambah permintaan jaringan, ukuran unduhan, dan beban pemrosesan. Banyak skrip pihak ketiga juga memuat skrip lain secara berantai. Akibatnya, dampak satu skrip bisa jauh lebih besar daripada yang terlihat. Skrip seperti ini sering menjadi penyebab utama halaman terasa berat.

Mulailah dengan mendata semua skrip pihak ketiga yang ada di website. Tanyakan apakah setiap skrip masih digunakan dan apakah manfaatnya sepadan. Hapus skrip yang tidak lagi diperlukan, misalnya piksel dari kampanye yang sudah selesai. Muat skrip yang tersisa dengan `async` atau `defer`. Untuk widget yang tidak dibutuhkan segera, tunda pemuatannya hingga pengguna berinteraksi atau hingga halaman selesai dimuat.

Jika menggunakan pengelola tag seperti Google Tag Manager, lakukan peninjauan secara berkala. Pengelola tag memudahkan tim pemasaran menambah skrip tanpa bantuan pengembang. Kemudahan ini sering membuat jumlah skrip bertambah tanpa terkendali. Tetapkan aturan bahwa setiap tag baru harus memiliki pemilik dan tujuan yang jelas. Hapus tag yang sudah tidak digunakan setiap beberapa bulan.

## Optimasi Font, Gambar, dan Media

Font, gambar, dan video adalah sumber daya yang ukurannya sering paling besar di sebuah halaman. Gambar yang tidak dioptimasi saja bisa membuat halaman berukuran beberapa megabita. Font kustom bisa menunda tampilnya teks. Video dan sematan dari pihak ketiga bisa memuat banyak skrip tambahan. Mengoptimasi ketiganya memberikan penghematan yang sangat terasa.

### 17. Optimalkan Pemuatan Font Web

Font kustom membuat tampilan website lebih menarik, tetapi menambah beban unduhan. Setiap ketebalan dan gaya font adalah file terpisah. Website yang menggunakan banyak varian font bisa memuat banyak file sekaligus. Batasi jumlah varian font hanya pada yang benar-benar digunakan. Pertimbangkan juga *variable font* yang menggabungkan banyak varian dalam satu file.

Gunakan format WOFF2 yang memiliki kompresi terbaik dan didukung oleh browser modern. Lakukan *subsetting*, yaitu menghapus karakter yang tidak digunakan dari file font. Untuk website berbahasa Indonesia, karakter Latin dasar biasanya sudah cukup. Tambahkan properti `font-display: swap` agar teks tetap tampil dengan font cadangan selama font kustom dimuat. Untuk font paling penting, gunakan *preload* agar browser mengunduhnya lebih awal.

Jika memungkinkan, simpan file font di server sendiri daripada memuatnya dari layanan pihak ketiga. Dengan menyimpan sendiri, browser tidak perlu membuka koneksi ke domain lain. Anda juga memiliki kendali penuh atas pengaturan cache dan subsetting. Pertimbangkan pula menggunakan font sistem untuk teks isi. Font sistem tidak perlu diunduh sama sekali dan tetap terlihat rapi di semua perangkat.

```html
<link rel="preload" href="/fonts/inter-latin-400.woff2" as="font" type="font/woff2" crossorigin>
<style>
  @font-face {
    font-family: "Inter";
    src: url("/fonts/inter-latin-400.woff2") format("woff2");
    font-weight: 400;
    font-display: swap;
  }
</style>
```

### 18. Kompres dan Sesuaikan Ukuran Gambar

Gambar biasanya menyumbang porsi terbesar dari ukuran halaman. Mengoptimasi gambar sering menjadi cara tercepat untuk mengurangi berat halaman secara drastis. Langkah utamanya adalah mengubah ukuran gambar sesuai tampilan, menggunakan format modern seperti WebP atau AVIF, dan mengompresnya. Sediakan beberapa ukuran gambar agar perangkat kecil tidak mengunduh gambar berukuran besar. Gunakan lazy load untuk gambar di bawah area layar pertama.

Topik ini cukup luas sehingga kami membahasnya dalam artikel tersendiri. Di sana Anda akan menemukan perbandingan format gambar, cara menulis `srcset` dan `sizes`, serta alat kompresi yang direkomendasikan. Pembahasan juga mencakup optimasi gambar untuk SEO dan aksesibilitas. Silakan baca panduan lengkap [optimasi gambar website](/optimasi-gambar-website/). Menerapkan panduan tersebut sering memberikan hasil paling nyata dalam waktu singkat.

### 19. Tunda Pemuatan Video, Iframe, dan Sematan

Sematan video YouTube, peta, dan media sosial memuat banyak sumber daya dari pihak ketiga. Satu sematan video saja bisa memuat beberapa skrip dan file berukuran besar. Jika sematan berada di bagian bawah halaman, sumber daya tersebut tidak dibutuhkan saat halaman pertama kali dibuka. Tambahkan atribut `loading="lazy"` pada elemen `<iframe>` agar pemuatannya ditunda hingga mendekati area pandang. Atribut ini didukung oleh browser modern.

Untuk mengurangi beban lebih jauh, gunakan teknik *facade*. Teknik ini menampilkan gambar pratinjau statis yang ringan sebagai pengganti sematan asli. Ketika pengguna mengklik pratinjau tersebut, barulah sematan asli dimuat. Dengan cara ini, pengguna yang tidak menonton video tidak perlu mengunduh semua sumber daya pemutar. Banyak pustaka ringan dan plugin menyediakan fitur ini untuk video YouTube.

Ganti juga animasi GIF yang besar dengan video. Format GIF sangat tidak efisien untuk animasi panjang. Video MP4 atau WebM dengan konten yang sama biasanya jauh lebih kecil. Gunakan elemen `<video>` dengan atribut `autoplay`, `muted`, `loop`, dan `playsinline` agar perilakunya mirip GIF. Penghematan ukuran dari perubahan ini sering sangat besar.

## Optimasi Navigasi Antarhalaman

Kecepatan tidak hanya penting saat pengunjung membuka halaman pertama. Navigasi dari satu halaman ke halaman lain juga menentukan kenyamanan. Pengunjung yang membaca beberapa artikel atau melihat beberapa produk akan merasakan setiap jeda. Ada teknik yang dapat membuat perpindahan halaman terasa hampir instan. Teknik-teknik ini memanfaatkan waktu ketika pengguna sedang membaca untuk menyiapkan halaman berikutnya.

### 20. Manfaatkan Prefetch, Prerender, dan Back/Forward Cache

*Prefetch* adalah teknik mengunduh sumber daya halaman berikutnya sebelum pengguna membukanya. Jika pengguna kemudian mengklik tautan, halaman sudah tersedia di cache dan tampil lebih cepat. Browser berbasis Chromium mendukung Speculation Rules API yang memungkinkan *prefetch* bahkan *prerender* halaman. *Prerender* menyiapkan halaman secara utuh di latar belakang, sehingga perpindahan halaman terasa instan. Gunakan aturan yang moderat, misalnya hanya menyiapkan halaman saat pengguna mengarahkan kursor ke tautan.

```html
<script type="speculationrules">
{
  "prerender": [{
    "where": { "href_matches": "/artikel/*" },
    "eagerness": "moderate"
  }]
}
</script>
```

Teknik ini perlu digunakan dengan bijak. Menyiapkan terlalu banyak halaman akan membuang kuota data dan sumber daya perangkat pengguna. Kecualikan halaman yang memiliki efek samping, seperti tautan untuk keluar dari akun atau menambah barang ke keranjang. Pastikan juga analitik Anda menangani halaman yang di-*prerender* dengan benar agar tidak menghitung kunjungan ganda. Framework modern sering memiliki fitur *prefetch* bawaan untuk tautan internal.

Fitur *back/forward cache* pada browser menyimpan halaman secara utuh saat pengguna pindah ke halaman lain. Ketika pengguna menekan tombol kembali, halaman ditampilkan langsung dari memori. Hasilnya, navigasi mundur dan maju terasa instan. Beberapa praktik dapat membuat halaman tidak bisa disimpan di cache ini, seperti penggunaan *event* `unload`. Periksa kelayakan halaman Anda melalui panel Application di Chrome DevTools.

## Tips Khusus WordPress dan PHP

WordPress dan aplikasi berbasis PHP mendominasi banyak website di Indonesia. Platform ini fleksibel, tetapi juga rentan menjadi lambat jika tidak dikelola dengan baik. Masalah yang paling sering muncul berasal dari tema, plugin, dan konfigurasi server. Teknik-teknik umum di atas tetap berlaku. Berikut beberapa tips tambahan yang spesifik untuk platform ini.

**Pilih tema yang ringan.** Banyak tema premium menawarkan ratusan fitur dan opsi tampilan. Sayangnya, semua fitur itu sering dimuat di setiap halaman, meskipun tidak digunakan. Pilih tema yang dikenal ringan dan dibangun dengan kode yang bersih. Sebelum membeli tema, uji halaman demonya dengan PageSpeed Insights. Tema yang lambat sejak awal akan sulit dipercepat di kemudian hari.

**Audit plugin secara berkala.** Setiap plugin menambah kode yang dijalankan di server, dan sering juga menambah CSS serta JavaScript di browser. Plugin yang buruk bisa menjalankan kueri basis data yang berat di setiap halaman. Nonaktifkan dan hapus plugin yang tidak lagi digunakan. Untuk plugin yang masih dibutuhkan, cari alternatif yang lebih ringan jika ada. Gunakan plugin pemantau kueri di lingkungan pengujian untuk menemukan plugin yang paling membebani.

**Gunakan plugin caching yang sesuai dengan server.** Ada banyak plugin caching untuk WordPress dengan fitur yang beragam. Beberapa hosting menyediakan sistem caching sendiri di tingkat server yang lebih efisien. Pilih satu solusi caching saja agar tidak terjadi konflik. Aktifkan caching halaman, kompresi, dan pengaturan cache browser. Uji kembali website setelah mengaktifkan fitur optimasi yang lebih agresif, seperti penundaan JavaScript.

**Atur WP-Cron dengan benar.** Secara bawaan, WordPress menjalankan tugas terjadwal saat ada pengunjung yang membuka halaman. Pada website dengan trafik tinggi, mekanisme ini bisa membebani server. Pada website dengan trafik rendah, tugas terjadwal bisa terlambat. Solusinya adalah menonaktifkan WP-Cron bawaan dan menggantinya dengan cron di tingkat server. Dengan cara ini, tugas berjalan sesuai jadwal tanpa membebani permintaan pengunjung.

**Batasi revisi dan bersihkan basis data.** WordPress menyimpan setiap revisi artikel secara bawaan. Pada website dengan banyak artikel yang sering disunting, jumlah revisi bisa sangat besar. Batasi jumlah revisi yang disimpan melalui pengaturan di file konfigurasi. Bersihkan juga data sementara yang kedaluwarsa dan komentar spam. Selalu buat cadangan basis data sebelum melakukan pembersihan.

**Aktifkan OPcache dan gunakan object cache persisten.** Pastikan ekstensi OPcache aktif di server agar kode PHP tidak dikompilasi ulang di setiap permintaan. Untuk website dinamis seperti toko WooCommerce, gunakan object cache persisten dengan Redis atau Memcached. Object cache mengurangi jumlah kueri ke basis data secara signifikan. Banyak hosting terkelola sudah menyediakan fitur ini. Jika belum, tanyakan kepada penyedia hosting Anda.

## Menyusun Prioritas Perbaikan

Dua puluh teknik di atas tidak harus diterapkan semuanya sekaligus. Setiap website memiliki masalah utama yang berbeda. Menerapkan teknik yang tidak relevan hanya membuang waktu. Karena itu, susunlah prioritas berdasarkan hasil pengukuran. Berikut panduan sederhana untuk menentukan langkah pertama.

**Jika TTFB tinggi**, fokuskan perbaikan di sisi server. Periksa kualitas hosting, aktifkan caching halaman, dan gunakan CDN. Optimalkan kueri basis data yang lambat. Perbaikan di sisi browser tidak akan banyak membantu sebelum masalah server teratasi. Biasanya, perbaikan di sisi server memberikan peningkatan paling besar untuk website dinamis.

**Jika ukuran halaman besar**, periksa jenis file yang paling banyak menyumbang ukuran. Jika gambar mendominasi, mulailah dengan optimasi gambar. Jika JavaScript mendominasi, hapus kode yang tidak digunakan dan kendalikan skrip pihak ketiga. Pastikan kompresi dan cache browser sudah aktif. Langkah-langkah ini mengurangi waktu unduh, terutama di jaringan seluler.

**Jika halaman lama tampil meskipun ukurannya kecil**, kemungkinan besar ada sumber daya yang memblokir rendering. Periksa CSS dan JavaScript yang dimuat di bagian `<head>`. Tambahkan `defer` pada skrip yang tidak dibutuhkan untuk tampilan awal. Pertimbangkan teknik CSS kritis. Periksa juga apakah font kustom menunda tampilnya teks.

**Jika halaman terasa berat saat digunakan**, masalahnya biasanya ada pada JavaScript yang membebani prosesor. Gunakan panel Performance di DevTools untuk menemukan tugas panjang. Kurangi skrip pihak ketiga dan pecah pekerjaan berat menjadi bagian yang lebih kecil. Pembahasan teknik ini secara mendalam ada di bagian INP pada artikel [Core Web Vitals](/core-web-vitals-lcp-inp-cls/). Uji perbaikan di perangkat yang mewakili pengguna Anda.

Setelah menentukan fokus, buat daftar perbaikan dan perkirakan dampak serta usahanya. Kerjakan terlebih dahulu perbaikan yang dampaknya besar dan usahanya kecil. Contohnya adalah mengaktifkan kompresi, menghapus plugin yang tidak terpakai, atau mengecilkan gambar utama. Perbaikan yang lebih rumit, seperti mengubah arsitektur rendering, bisa dijadwalkan kemudian. Ukur kembali setelah setiap perbaikan agar Anda tahu dampaknya.

## Menjaga Kecepatan dalam Jangka Panjang

Website yang sudah cepat bisa kembali lambat seiring waktu. Penyebabnya adalah penambahan fitur, plugin, skrip, dan konten yang tidak dioptimasi. Tanpa pengawasan, kemunduran ini terjadi sedikit demi sedikit hingga tidak disadari. Karena itu, kecepatan perlu dijaga sebagai bagian dari proses kerja. Berikut beberapa kebiasaan yang membantu menjaga kecepatan.

**Tetapkan anggaran kinerja.** Anggaran kinerja adalah batas yang disepakati untuk ukuran atau metrik tertentu. Contohnya adalah batas total JavaScript per halaman atau batas waktu tampil konten utama. Setiap perubahan baru harus tetap berada dalam batas tersebut. Jika melampaui, tim perlu mencari cara mengurangi beban lain atau meninjau ulang perubahan tersebut. Anggaran ini membuat kinerja menjadi pertimbangan sejak awal, bukan setelah masalah muncul.

**Otomatiskan pengujian.** Jalankan pengujian kinerja secara otomatis setiap kali ada perubahan kode. Alat seperti Lighthouse CI dapat diintegrasikan ke dalam alur kerja pengembangan. Jika hasil pengujian memburuk melewati batas tertentu, perubahan bisa ditandai untuk ditinjau. Cara ini mencegah kemunduran masuk ke website utama. Pengujian otomatis sangat bermanfaat untuk tim yang sering melakukan pembaruan.

**Pantau data pengguna nyata.** Hasil pengujian laboratorium tidak selalu mencerminkan pengalaman pengguna. Pantau laporan Core Web Vitals di Search Console secara rutin. Jika memungkinkan, kumpulkan data kinerja dari pengguna nyata menggunakan analitik sendiri. Data ini membantu mendeteksi masalah yang hanya terjadi di perangkat atau jaringan tertentu. Tinjau data tersebut setidaknya sebulan sekali.

**Libatkan seluruh tim.** Kecepatan website bukan hanya tanggung jawab pengembang. Penulis konten perlu mengunggah gambar yang sudah dioptimasi. Tim pemasaran perlu mempertimbangkan dampak setiap skrip pelacakan baru. Desainer perlu memperhatikan jumlah font dan efek visual yang berat. Ketika semua pihak memahami pentingnya kecepatan, menjaga website tetap cepat menjadi jauh lebih mudah.

## Kesalahan Umum Saat Mempercepat Website

Upaya mempercepat website kadang justru menimbulkan masalah baru. Kesalahan ini biasanya terjadi karena menerapkan teknik tanpa memahami dampaknya. Ada juga kesalahan yang muncul karena terlalu fokus pada angka. Mengenali kesalahan-kesalahan berikut akan membantu Anda bekerja lebih efektif. Hindari kesalahan ini agar upaya optimasi tidak sia-sia.

**Memasang terlalu banyak plugin optimasi.** Beberapa pemilik WordPress memasang beberapa plugin caching dan optimasi sekaligus. Plugin-plugin tersebut bisa saling bertentangan dan menyebabkan halaman rusak. Fitur yang sama juga bisa dijalankan dua kali sehingga justru memperlambat server. Pilih satu solusi yang lengkap dan sesuai dengan hosting Anda. Matikan fitur yang sudah ditangani oleh server atau CDN.

**Menunda semua JavaScript tanpa pengecualian.** Fitur penundaan JavaScript bisa sangat efektif. Namun, jika diterapkan pada semua skrip, beberapa fungsi penting bisa terlambat berjalan. Menu navigasi, formulir, atau tombol pembelian mungkin tidak berfungsi saat pengguna pertama kali mencobanya. Uji semua fungsi penting setelah mengaktifkan fitur ini. Kecualikan skrip yang dibutuhkan untuk interaksi awal.

**Hanya menguji dari komputer kantor.** Pengembang sering menguji website dari komputer yang cepat dengan koneksi internet kantor yang stabil. Dari kondisi seperti itu, hampir semua website terasa cepat. Pengguna nyata banyak yang mengakses dari ponsel dengan jaringan seluler yang berubah-ubah. Selalu uji dengan simulasi jaringan dan CPU yang lebih lambat. Jika memungkinkan, uji langsung di ponsel kelas menengah.

**Mengoptimasi tanpa mengukur.** Menerapkan teknik berdasarkan daftar periksa tanpa mengukur dampaknya bisa menyesatkan. Teknik yang sangat efektif di satu website bisa tidak berpengaruh di website lain. Catat hasil pengukuran sebelum dan sesudah setiap perubahan. Dengan begitu, Anda tahu teknik mana yang benar-benar membantu. Data juga memudahkan Anda menjelaskan hasil kepada atasan atau klien.

**Melupakan halaman selain beranda.** Banyak pemilik website hanya menguji beranda. Padahal, sebagian besar pengunjung dari mesin pencari masuk melalui halaman artikel atau produk. Halaman-halaman tersebut sering memiliki elemen berbeda, seperti sematan video, galeri, atau widget ulasan. Uji setiap jenis templat halaman yang penting. Prioritaskan halaman yang paling banyak menerima kunjungan.

**Mengabaikan dampak konten baru.** Setelah website dioptimasi, konten baru terus ditambahkan setiap hari. Jika penulis mengunggah gambar berukuran besar atau menyematkan banyak widget, kecepatan perlahan menurun. Buat panduan sederhana untuk tim konten tentang ukuran gambar dan penggunaan sematan. Otomatiskan kompresi gambar saat diunggah jika memungkinkan. Kebiasaan kecil ini mencegah kemunduran yang tidak disadari.

## Checklist Cepat Mempercepat Website

Gunakan daftar periksa berikut untuk meninjau kondisi website Anda secara cepat. Setiap poin mewakili teknik yang sudah dijelaskan di atas. Tandai poin yang sudah diterapkan dan catat poin yang belum. Poin yang belum diterapkan bisa menjadi daftar pekerjaan berikutnya. Ulangi peninjauan ini setiap beberapa bulan.

1. Hosting memadai dan server berada dekat dengan mayoritas pengunjung.
2. Versi PHP atau runtime lain masih didukung, dan OPcache sudah aktif.
3. Caching halaman sudah aktif, dengan pengecualian untuk halaman personal.
4. Kueri basis data yang lambat sudah diperbaiki, dan object cache digunakan jika perlu.
5. Tidak ada rantai pengalihan yang panjang.
6. CDN sudah digunakan untuk file statis.
7. Kompresi Brotli atau Gzip sudah aktif untuk file teks.
8. Server sudah mendukung HTTP/2 atau HTTP/3.
9. Header cache browser sudah diatur dengan benar untuk file statis.
10. CSS, JavaScript, dan HTML sudah diminifikasi.
11. Kode yang tidak digunakan sudah dihapus.
12. Skrip yang tidak dibutuhkan di awal sudah diberi atribut `defer` atau `async`.
13. Skrip pihak ketiga sudah ditinjau dan dikurangi.
14. Font menggunakan format WOFF2 dengan `font-display` yang tepat.
15. Gambar sudah dikompres, berukuran sesuai, dan menggunakan format modern.
16. Video dan iframe di bagian bawah halaman sudah ditunda pemuatannya.

## FAQ Mempercepat Website

### Apa penyebab paling umum website lambat?

Penyebab paling umum adalah hosting yang kurang memadai, tidak adanya caching, gambar yang terlalu besar, dan JavaScript yang berlebihan. Skrip pihak ketiga seperti iklan dan widget juga sering menjadi penyebab utama. Ukur terlebih dahulu untuk mengetahui penyebab di website Anda.

### Apakah CDN wajib digunakan?

CDN tidak wajib, tetapi sangat dianjurkan, terutama jika pengunjung berasal dari banyak lokasi. CDN mempercepat pengiriman file dan mengurangi beban server utama. Banyak penyedia CDN menawarkan paket gratis yang cukup untuk website kecil.

### Berapa kecepatan loading website yang ideal?

Tidak ada satu angka yang berlaku untuk semua website. Sebagai acuan, Google menganggap konten utama yang tampil dalam 2,5 detik sebagai kategori baik. Semakin cepat halaman tampil dan merespons, semakin baik pengalaman pengguna.

### Apakah plugin caching saja cukup untuk mempercepat WordPress?

Plugin caching sangat membantu, tetapi biasanya tidak cukup jika masalah utamanya ada di tempat lain. Tema yang berat, gambar yang besar, dan skrip pihak ketiga tetap perlu ditangani. Kombinasikan caching dengan optimasi lain untuk hasil terbaik.

### Apakah skor PageSpeed 100 diperlukan?

Tidak. Skor PageSpeed adalah hasil pengujian laboratorium yang berguna untuk diagnosis. Yang lebih penting adalah pengalaman pengguna nyata yang tercermin dalam data Core Web Vitals. Website dengan skor di bawah 100 tetap bisa memberikan pengalaman yang sangat baik.

### Seberapa sering kecepatan website perlu diperiksa?

Periksa kecepatan setiap kali ada perubahan besar, seperti mengganti tema, menambah plugin, atau meluncurkan fitur baru. Selain itu, tinjau data Core Web Vitals setidaknya sebulan sekali. Pemeriksaan rutin membantu mendeteksi kemunduran sejak dini.

### Apakah hosting di luar negeri membuat website lambat untuk pengunjung Indonesia?

Jarak server memang menambah waktu perjalanan data, terutama saat membuka koneksi. Pengaruhnya bisa dikurangi secara signifikan dengan menggunakan CDN yang memiliki titik kehadiran di dekat Indonesia. Jika sebagian besar pengunjung berasal dari Indonesia dan halaman bersifat dinamis, server di Indonesia atau Singapura biasanya memberikan hasil lebih baik.

### Apakah lazy load memperlambat website?

Lazy load justru mempercepat halaman jika diterapkan pada gambar dan iframe di bawah area layar pertama. Masalah muncul jika lazy load diterapkan pada gambar utama yang langsung terlihat. Pastikan gambar di bagian atas halaman dimuat secara normal agar konten utama tampil secepat mungkin.

### Apakah mengganti tema bisa membuat website lebih cepat?

Bisa, terutama jika tema lama memuat banyak kode yang tidak digunakan. Namun, mengganti tema adalah perubahan besar yang dapat memengaruhi tampilan dan fungsi website. Ukur kinerja tema baru di lingkungan pengujian, lalu pindahkan secara terencana agar tidak mengganggu pengunjung.

## Kesimpulan

Mempercepat loading website membutuhkan pendekatan menyeluruh dari sisi server hingga sisi browser. Mulailah dengan mengukur menggunakan PageSpeed Insights, WebPageTest, dan Chrome DevTools. Jika server lambat, perbaiki hosting, aktifkan caching, dan gunakan CDN. Kurangi ukuran halaman dengan kompresi, minifikasi, dan penghapusan kode yang tidak digunakan. Tunda skrip yang tidak penting, kendalikan skrip pihak ketiga, dan optimalkan font serta media.

Tidak semua teknik harus diterapkan sekaligus. Susun prioritas berdasarkan hasil pengukuran, lalu kerjakan perbaikan yang paling berdampak terlebih dahulu. Setelah website cepat, jaga kecepatannya dengan anggaran kinerja, pengujian otomatis, dan pemantauan rutin. Untuk memahami metrik yang digunakan Google dalam menilai pengalaman halaman, baca artikel [Core Web Vitals](/core-web-vitals-lcp-inp-cls/). Karena gambar sering menjadi beban terbesar, lanjutkan dengan panduan [optimasi gambar website](/optimasi-gambar-website/).
