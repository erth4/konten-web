---
title: "CDN Adalah: Pengertian, Cara Kerja, dan Manfaatnya"
meta_description: "Apa itu CDN? Pelajari cara kerja content delivery network, edge server, cache hit dan miss, manfaat untuk kecepatan dan keamanan, serta cara memasang CDN dengan benar."
slug: "cdn-pengertian-cara-kerja-manfaat"
focus_keyword: "CDN"
keywords:
  - cdn adalah
  - content delivery network
  - cara kerja cdn
  - manfaat cdn
  - edge server
  - cache cdn
  - cara memasang cdn
  - cdn untuk website
category: "Performa"
tags: ["Performa Website", "CDN", "Caching", "Infrastruktur Web"]
date: "2026-10-02"
lang: "id"
---

# CDN Adalah: Pengertian, Cara Kerja, Manfaat, dan Cara Memasangnya dengan Benar

Bayangkan website Anda di-*hosting* di sebuah server di Jakarta. Pengunjung dari Jakarta bisa membukanya dengan cepat. Namun, pengunjung dari Makassar, Medan, atau bahkan luar negeri harus menunggu lebih lama karena data menempuh jarak yang lebih jauh. Semakin jauh jaraknya, semakin terasa keterlambatannya, terutama pada jaringan seluler. Masalah inilah yang diselesaikan oleh **CDN** atau *content delivery network*.

Artikel ini menjelaskan apa itu CDN, bagaimana cara kerjanya, dan mengapa teknologi ini penting bagi hampir semua website modern. Anda akan mempelajari istilah-istilah penting seperti edge server, origin, cache hit, dan TTL. Kami juga membahas manfaat CDN untuk kecepatan, ketersediaan, dan keamanan. Di bagian praktis, Anda akan menemukan langkah memasang CDN, cara mengatur cache, dan kesalahan yang sering terjadi. Pembahasan ini memperdalam teknik CDN yang disinggung singkat di artikel [cara mempercepat loading website](/cara-mempercepat-loading-website/).

## Daftar Isi

1. [Apa Itu CDN?](#apa-itu-cdn)
2. [Istilah Penting dalam CDN](#istilah-penting-dalam-cdn)
3. [Bagaimana Cara Kerja CDN?](#bagaimana-cara-kerja-cdn)
4. [Jenis Konten yang Dilayani CDN](#jenis-konten-yang-dilayani-cdn)
5. [Manfaat CDN](#manfaat-cdn)
6. [Jenis-Jenis CDN](#jenis-jenis-cdn)
7. [Cara Memasang CDN untuk Website](#cara-memasang-cdn-untuk-website)
8. [Mengatur Header Cache dengan Benar](#mengatur-header-cache-dengan-benar)
9. [Menyimpan Halaman HTML di Cache CDN](#menyimpan-halaman-html-di-cache-cdn)
10. [Fitur Lanjutan CDN Modern](#fitur-lanjutan-cdn-modern)
11. [Cara Memilih Penyedia CDN](#cara-memilih-penyedia-cdn)
12. [Memahami Cache Key dan Parameter URL](#memahami-cache-key-dan-parameter-url)
13. [CDN untuk Website WordPress](#cdn-untuk-website-wordpress)
14. [CDN untuk Video dan File Berukuran Besar](#cdn-untuk-video-dan-file-berukuran-besar)
15. [CDN untuk Aplikasi Berbasis Framework JavaScript](#cdn-untuk-aplikasi-berbasis-framework-javascript)
16. [Memperhitungkan Biaya CDN](#memperhitungkan-biaya-cdn)
17. [Checklist Pemasangan CDN](#checklist-pemasangan-cdn)
18. [Perbedaan CDN, Hosting, dan Layanan Cloud](#perbedaan-cdn-hosting-dan-layanan-cloud)
19. [CDN dan Privasi Data](#cdn-dan-privasi-data)
20. [Kesalahan Umum Saat Menggunakan CDN](#kesalahan-umum-saat-menggunakan-cdn)
21. [Mengukur Dampak CDN](#mengukur-dampak-cdn)
22. [FAQ CDN](#faq-cdn)
23. [Kesimpulan](#kesimpulan)

## Apa Itu CDN?

CDN adalah jaringan server yang tersebar di banyak lokasi geografis dan bekerja sama untuk mengirimkan konten website kepada pengguna. Server-server ini menyimpan salinan konten dari server utama website. Ketika pengguna membuka website, konten dikirim dari server CDN yang paling dekat dengan lokasi pengguna. Dengan begitu, jarak tempuh data menjadi lebih pendek dan waktu pemuatan menjadi lebih cepat. Server utama juga tidak perlu melayani semua permintaan sendirian.

CDN bukan pengganti hosting. Website tetap membutuhkan server utama yang menyimpan file asli dan menjalankan aplikasi. Server utama ini disebut *origin* atau server asal. CDN berdiri di antara pengguna dan server asal sebagai lapisan pengiriman. Sebagian besar permintaan dapat dilayani langsung oleh CDN tanpa menyentuh server asal.

Konsep CDN sudah ada sejak akhir 1990-an, ketika internet mulai ramai dan server sering kewalahan melayani lonjakan pengunjung. Perusahaan-perusahaan pelopor mulai membangun jaringan server di banyak lokasi untuk mendistribusikan konten. Sejak itu, CDN berkembang menjadi bagian penting dari infrastruktur internet. Saat ini, banyak situs besar, layanan streaming, dan aplikasi menggunakan CDN. Bahkan website kecil pun bisa menggunakan CDN dengan paket gratis yang ditawarkan sejumlah penyedia.

## Istilah Penting dalam CDN

Sebelum membahas cara kerja CDN, ada beberapa istilah yang perlu dipahami. Istilah-istilah ini akan sering muncul di panel pengaturan CDN dan dokumentasi penyedia. Memahaminya membantu Anda mengatur CDN dengan benar. Banyak masalah CDN terjadi karena istilah-istilah ini disalahpahami. Berikut penjelasannya.

**Origin.** Origin adalah server utama tempat website Anda di-*hosting*. Server ini menyimpan versi asli dari semua file dan menjalankan aplikasi website. CDN mengambil konten dari origin ketika belum memiliki salinannya. Origin bisa berupa hosting biasa, VPS, layanan cloud, atau layanan penyimpanan objek. Kinerja origin tetap penting karena CDN tidak bisa menyimpan semua jenis konten.

**Edge server dan PoP.** Edge server adalah server CDN yang berada dekat dengan pengguna. Kumpulan edge server di satu lokasi disebut *point of presence* atau PoP. Penyedia CDN memiliki banyak PoP di berbagai kota dan negara. Semakin banyak PoP di dekat pengguna Anda, semakin cepat konten dapat dikirim. Untuk pengunjung Indonesia, keberadaan PoP di Indonesia atau negara tetangga sangat penting.

**Cache.** Cache adalah salinan sementara dari konten yang disimpan di edge server. Ketika konten tersimpan di cache, edge server dapat langsung mengirimkannya kepada pengguna. Proses ini jauh lebih cepat daripada mengambil konten dari origin. Konten di cache memiliki masa berlaku tertentu. Setelah masa berlaku habis, edge server akan memeriksa atau mengambil ulang konten dari origin.

**Cache hit dan cache miss.** Cache hit terjadi ketika edge server sudah memiliki salinan konten yang diminta dan masih berlaku. Cache miss terjadi ketika edge server belum memiliki salinan atau salinannya sudah kedaluwarsa. Pada kondisi cache miss, edge server harus mengambil konten dari origin terlebih dahulu. Rasio antara cache hit dan total permintaan disebut *cache hit ratio*. Semakin tinggi rasionya, semakin efektif CDN bekerja.

**TTL.** TTL adalah singkatan dari *time to live*, yaitu lamanya konten boleh disimpan di cache sebelum dianggap kedaluwarsa. TTL bisa ditentukan melalui header HTTP dari origin atau melalui pengaturan di panel CDN. TTL yang panjang meningkatkan cache hit ratio, tetapi membuat perubahan konten lebih lambat terlihat. TTL yang pendek membuat konten selalu segar, tetapi lebih sering mengambil dari origin. Pengaturan TTL yang tepat adalah keseimbangan antara kecepatan dan kesegaran.

**Purge.** Purge adalah proses menghapus konten dari cache CDN sebelum TTL-nya habis. Proses ini dilakukan ketika konten di origin berubah dan Anda ingin perubahan segera terlihat. Purge bisa dilakukan untuk satu file, sekelompok file, atau seluruh cache. Sebagian penyedia juga mendukung purge berdasarkan label atau tag. Purge yang terlalu sering dan menyeluruh mengurangi manfaat cache.

## Bagaimana Cara Kerja CDN?

Cara kerja CDN dapat dipahami melalui perjalanan sebuah permintaan dari pengguna hingga konten tampil di layar. Proses ini terjadi dalam hitungan milidetik dan tidak terlihat oleh pengguna. Meski begitu, setiap tahapnya menentukan seberapa cepat konten sampai. Memahami alur ini juga membantu Anda mendiagnosis masalah ketika CDN tidak bekerja sesuai harapan. Berikut tahapan cara kerja CDN secara umum.

### 1. Pengguna Meminta Konten

Pengguna mengetik alamat website atau mengklik tautan. Browser kemudian mencari alamat IP dari nama domain melalui sistem DNS. Jika website menggunakan CDN, DNS akan mengarahkan pengguna ke jaringan CDN, bukan langsung ke origin. Penyedia CDN menggunakan berbagai teknik untuk menentukan edge server yang paling tepat. Teknik tersebut mempertimbangkan lokasi pengguna, kondisi jaringan, dan beban server.

Salah satu teknik yang umum digunakan adalah *anycast*. Dengan anycast, banyak edge server di berbagai lokasi menggunakan alamat IP yang sama. Jaringan internet secara otomatis mengarahkan permintaan ke lokasi yang paling dekat secara jalur jaringan. Teknik lain adalah pengarahan berbasis DNS, di mana server DNS memberikan alamat IP berbeda tergantung lokasi pengguna. Kedua teknik ini bertujuan sama, yaitu menghubungkan pengguna dengan edge server terbaik.

### 2. Edge Server Memeriksa Cache

Setelah permintaan sampai di edge server, server memeriksa apakah konten yang diminta sudah tersimpan di cache. Pemeriksaan dilakukan berdasarkan *cache key*, yang biasanya terdiri dari URL lengkap dan beberapa informasi tambahan. Jika konten ditemukan dan masih berlaku, terjadilah cache hit. Edge server langsung mengirimkan konten kepada pengguna. Proses ini sangat cepat karena tidak perlu menghubungi origin.

### 3. Mengambil Konten dari Origin Saat Cache Miss

Jika konten belum ada di cache atau sudah kedaluwarsa, terjadilah cache miss. Edge server kemudian meminta konten dari origin. Setelah menerima konten, edge server mengirimkannya kepada pengguna sekaligus menyimpannya di cache. Permintaan berikutnya untuk konten yang sama dari wilayah tersebut akan dilayani langsung dari cache. Dengan begitu, hanya pengguna pertama yang mengalami waktu tunggu lebih lama.

Beberapa CDN menggunakan lapisan cache tambahan di antara edge server dan origin. Fitur ini sering disebut *tiered cache* atau *origin shield*. Ketika edge server mengalami cache miss, ia terlebih dahulu bertanya ke lapisan tengah tersebut, bukan langsung ke origin. Jika lapisan tengah sudah memiliki konten, origin tidak perlu dihubungi. Fitur ini sangat mengurangi beban origin, terutama untuk website dengan pengunjung dari banyak wilayah.

### 4. Validasi Ulang Konten

Ketika TTL habis, edge server tidak selalu harus mengunduh ulang seluruh konten. Edge server dapat bertanya kepada origin apakah konten sudah berubah. Pertanyaan ini menggunakan informasi seperti `ETag` atau `Last-Modified`. Jika konten belum berubah, origin cukup menjawab dengan kode status 304 tanpa mengirim ulang isinya. Edge server kemudian memperpanjang masa berlaku salinannya.

Ada juga pengaturan yang memungkinkan edge server tetap menyajikan konten lama sambil mengambil versi baru di latar belakang. Pengaturan ini dikenal dengan arahan `stale-while-revalidate`. Pengguna tetap mendapat respons cepat, sementara konten diperbarui tanpa menunggu. Pengaturan serupa, `stale-if-error`, memungkinkan konten lama tetap disajikan jika origin sedang bermasalah. Kedua pengaturan ini meningkatkan kecepatan sekaligus ketahanan website.

## Jenis Konten yang Dilayani CDN

Tidak semua konten bisa diperlakukan sama oleh CDN. Sebagian konten sangat cocok untuk disimpan di cache dalam waktu lama. Sebagian lain harus selalu diambil dari origin karena bersifat personal atau sering berubah. Memahami perbedaan ini sangat penting untuk mengatur CDN dengan aman. Berikut pembagian jenis konten secara umum.

**Konten statis.** Konten statis adalah file yang isinya sama untuk semua pengguna dan jarang berubah. Contohnya adalah gambar, file CSS, file JavaScript, font, video, dan dokumen yang dapat diunduh. Konten jenis ini sangat cocok disimpan di cache CDN dalam waktu lama. Sebagian besar manfaat CDN berasal dari penyajian konten statis. Dengan nama file berversi, konten statis bisa disimpan hingga berbulan-bulan tanpa masalah.

**Halaman HTML publik.** Halaman seperti artikel blog, halaman produk, dan halaman informasi umumnya sama untuk semua pengunjung yang belum masuk ke akun. Halaman seperti ini juga bisa disimpan di cache CDN. Manfaatnya sangat besar karena server tidak perlu membangun halaman untuk setiap pengunjung. Namun, TTL-nya biasanya lebih pendek daripada file statis. Mekanisme purge perlu disiapkan agar perubahan konten segera terlihat.

**Konten dinamis dan personal.** Halaman keranjang belanja, akun pengguna, dasbor, dan hasil pencarian internal bersifat personal atau sangat dinamis. Konten seperti ini tidak boleh disimpan di cache bersama. Jika tersimpan, pengguna lain bisa melihat data milik orang lain. CDN tetap bisa mempercepat konten dinamis melalui jalur jaringan yang lebih optimal dan koneksi yang sudah terbuka ke origin. Namun, konten tersebut harus dikirim langsung dari origin untuk setiap pengguna.

**API.** Respons API bisa bersifat publik atau personal. Respons API publik yang jarang berubah, seperti daftar kategori, bisa disimpan di cache dengan TTL pendek. Respons API yang berisi data pengguna tidak boleh disimpan di cache bersama. Atur header cache dengan hati-hati untuk setiap jenis respons. Uji dengan beberapa akun berbeda untuk memastikan tidak ada data yang tertukar.

## Manfaat CDN

CDN memberikan banyak manfaat yang dirasakan oleh pengunjung maupun pemilik website. Manfaat utamanya memang kecepatan, tetapi CDN juga meningkatkan ketersediaan dan keamanan. Banyak fitur modern di CDN membuatnya menjadi platform yang lebih dari sekadar penyimpan cache. Bagi website kecil, manfaat ini bisa diperoleh dengan biaya rendah atau bahkan gratis. Berikut manfaat-manfaat utama CDN.

**Mempercepat waktu muat halaman.** CDN mengirim konten dari lokasi yang dekat dengan pengguna. Jarak yang lebih pendek berarti waktu perjalanan data yang lebih singkat. Proses pembukaan koneksi, termasuk negosiasi keamanan HTTPS, juga lebih cepat. Hasilnya, konten tampil lebih cepat, terutama bagi pengguna yang jauh dari origin. Peningkatan ini berdampak langsung pada metrik seperti TTFB dan LCP.

**Mengurangi beban server asal.** Karena sebagian besar permintaan dilayani dari cache, origin menerima jauh lebih sedikit permintaan. Server asal dapat fokus melayani konten dinamis yang memang harus diproses. Beban yang lebih ringan membuat origin lebih stabil, terutama saat trafik meningkat. Anda juga mungkin tidak perlu meningkatkan spesifikasi hosting secepat sebelumnya. Penghematan ini bisa cukup signifikan untuk website dengan trafik besar.

**Menghemat bandwidth hosting.** Banyak paket hosting membatasi atau mengenakan biaya untuk bandwidth. Dengan CDN, sebagian besar data dikirim dari jaringan CDN, bukan dari hosting. Penggunaan bandwidth di hosting pun berkurang. Penghematan ini paling terasa pada website dengan banyak gambar, video, atau file unduhan. Pastikan Anda juga memahami model biaya bandwidth di penyedia CDN.

**Meningkatkan ketersediaan.** CDN dapat tetap menyajikan konten yang tersimpan di cache meskipun origin sedang bermasalah. Fitur seperti `stale-if-error` atau mode selalu daring membantu website tetap dapat diakses dalam kondisi tertentu. Jaringan CDN yang tersebar juga lebih tahan terhadap gangguan di satu lokasi. Jika satu PoP bermasalah, permintaan bisa dialihkan ke PoP lain. Ketahanan ini sangat penting untuk website bisnis.

**Menangani lonjakan trafik.** Lonjakan trafik bisa terjadi saat promo besar, artikel viral, atau liputan media. Tanpa CDN, server asal bisa kewalahan dan website tidak dapat diakses. CDN menyerap sebagian besar lonjakan tersebut melalui cache yang tersebar. Server asal hanya menerima sebagian kecil permintaan. Dengan begitu, website tetap dapat diakses meskipun pengunjung melonjak drastis.

**Meningkatkan keamanan.** Banyak penyedia CDN menyediakan fitur keamanan bawaan. Fitur tersebut antara lain perlindungan dari serangan DDoS, *web application firewall*, dan pengelolaan bot. CDN juga menyembunyikan alamat IP origin dari publik jika dikonfigurasi dengan benar. Sertifikat HTTPS biasanya disediakan dan diperbarui secara otomatis. Fitur-fitur ini memberikan lapisan perlindungan tambahan bagi website, seperti dibahas pula di artikel [keamanan siber](/keamanan-siber-cara-melindungi-data-pribadi/).

**Mendukung protokol modern.** Penyedia CDN umumnya cepat mengadopsi protokol terbaru seperti HTTP/2, HTTP/3, dan TLS 1.3. Website Anda bisa langsung memanfaatkan protokol tersebut tanpa perlu mengubah konfigurasi server asal. Kompresi Brotli juga sering tersedia secara otomatis. Protokol modern ini mempercepat pemuatan, terutama di jaringan seluler yang tidak stabil. Bagi pemilik website, ini adalah peningkatan yang diperoleh dengan usaha minimal.

## Jenis-Jenis CDN

CDN dapat dibedakan berdasarkan cara konten masuk ke jaringan CDN dan cakupan layanannya. Perbedaan ini memengaruhi cara pemasangan dan pengelolaannya. Sebagian besar website saat ini menggunakan CDN jenis tarik karena lebih mudah diterapkan. Namun, CDN jenis dorong masih relevan untuk kebutuhan tertentu. Berikut penjelasan jenis-jenis CDN.

**Pull CDN.** Pada pull CDN, edge server mengambil konten dari origin secara otomatis ketika ada permintaan dan cache masih kosong. Pemilik website tidak perlu mengunggah file ke CDN secara manual. Cukup arahkan domain atau URL file ke CDN, dan CDN akan menangani sisanya. Model ini sangat praktis untuk website yang kontennya sering berubah. Kekurangannya, pengguna pertama di setiap lokasi mengalami cache miss.

**Push CDN.** Pada push CDN, pemilik website mengunggah file langsung ke penyimpanan CDN. File tersebut kemudian didistribusikan ke edge server. Model ini cocok untuk file besar yang jarang berubah, seperti video, perangkat lunak yang dapat diunduh, atau arsip. Pemilik website memiliki kendali penuh atas kapan file tersedia dan kapan diperbarui. Namun, pengelolaannya membutuhkan proses unggah yang terpisah.

**CDN dengan reverse proxy penuh.** Beberapa penyedia CDN bekerja sebagai *reverse proxy* untuk seluruh domain. Semua lalu lintas ke website, termasuk halaman HTML, melewati jaringan CDN. Model ini memungkinkan penggunaan fitur keamanan, caching halaman, dan optimasi lainnya secara menyeluruh. Pemasangannya biasanya dilakukan dengan mengubah *nameserver* domain ke penyedia CDN. Model ini populer karena kemudahan dan kelengkapan fiturnya.

**CDN khusus.** Ada juga CDN yang dikhususkan untuk jenis konten tertentu. Contohnya adalah CDN gambar yang dapat mengubah ukuran dan format gambar secara otomatis. Ada pula CDN video yang dirancang untuk streaming dengan berbagai kualitas. CDN pustaka publik menyediakan file JavaScript dan CSS populer untuk digunakan banyak website. Pilih CDN khusus jika kebutuhan Anda sangat spesifik.

## Cara Memasang CDN untuk Website

Pemasangan CDN saat ini relatif mudah dan bisa dilakukan tanpa mengubah kode website secara besar-besaran. Langkah-langkah persisnya berbeda tergantung penyedia dan jenis CDN yang dipilih. Namun, alur umumnya cukup mirip. Sebelum memulai, pastikan Anda memiliki akses ke pengaturan domain dan hosting. Lakukan pemasangan pada waktu trafik sedang rendah untuk mengurangi risiko gangguan.

### Langkah 1: Pilih Penyedia CDN

Pilih penyedia CDN yang sesuai dengan kebutuhan dan anggaran Anda. Pertimbangan utamanya adalah lokasi PoP, fitur yang tersedia, model biaya, dan kemudahan penggunaan. Untuk website dengan pengunjung mayoritas dari Indonesia, pilih penyedia yang memiliki PoP di Indonesia atau Asia Tenggara. Banyak penyedia menawarkan paket gratis atau uji coba yang cukup untuk website kecil. Panduan memilih penyedia dibahas di bagian tersendiri di bawah.

### Langkah 2: Hubungkan Domain

Untuk CDN dengan reverse proxy penuh, Anda biasanya diminta mengubah *nameserver* domain ke penyedia CDN. Penyedia akan memindai catatan DNS yang ada dan menyalinnya. Periksa kembali semua catatan DNS, termasuk catatan email, agar tidak ada yang tertinggal. Untuk CDN yang hanya melayani file statis, Anda cukup membuat subdomain khusus, misalnya `cdn.namadomain.com`. Subdomain tersebut diarahkan ke CDN menggunakan catatan CNAME.

Perubahan DNS membutuhkan waktu untuk menyebar ke seluruh internet. Proses ini bisa berlangsung dari beberapa menit hingga beberapa jam. Selama masa transisi, sebagian pengunjung mungkin masih terhubung langsung ke origin. Hal ini normal dan tidak perlu dikhawatirkan. Pantau status di panel penyedia CDN hingga domain dinyatakan aktif.

### Langkah 3: Atur HTTPS

Pastikan HTTPS berfungsi dengan benar setelah CDN aktif. Sebagian besar penyedia CDN menyediakan sertifikat untuk domain Anda secara otomatis. Atur mode enkripsi agar koneksi antara CDN dan origin juga terenkripsi. Mode yang hanya mengenkripsi koneksi antara pengguna dan CDN membuat data antara CDN dan origin tidak terlindungi. Pasang sertifikat yang valid di origin dan pilih mode enkripsi penuh yang memverifikasi sertifikat.

### Langkah 4: Atur Aturan Cache

Tentukan konten apa saja yang boleh disimpan di cache dan berapa lama. Cara terbaik adalah mengatur header `Cache-Control` dari origin sesuai jenis konten. Banyak CDN juga menyediakan aturan cache di panel pengaturan yang dapat mengesampingkan header dari origin. Pastikan halaman personal, seperti keranjang dan akun, dikecualikan dari cache. Pembahasan rinci tentang header cache ada di bagian berikutnya.

### Langkah 5: Uji dan Pantau

Setelah CDN aktif, uji website secara menyeluruh. Periksa apakah semua halaman tampil dengan benar dan semua fungsi berjalan normal. Uji proses masuk akun, keranjang belanja, dan formulir. Periksa header respons untuk memastikan konten disajikan dari cache sesuai harapan. Pantau statistik di panel CDN, seperti cache hit ratio dan jumlah permintaan ke origin.

## Mengatur Header Cache dengan Benar

Header HTTP adalah cara utama untuk memberi tahu CDN dan browser bagaimana konten harus disimpan. Pengaturan yang tepat membuat CDN bekerja optimal tanpa menyajikan konten yang salah. Pengaturan yang keliru bisa membuat CDN tidak menyimpan apa pun, atau sebaliknya, menyimpan konten yang seharusnya personal. Karena itu, bagian ini sangat penting untuk dipahami. Berikut header-header utama yang perlu diketahui.

**Cache-Control.** Header ini adalah pengatur utama perilaku cache. Arahan `max-age` menentukan berapa lama konten boleh disimpan dalam detik. Arahan `s-maxage` berlaku khusus untuk cache bersama seperti CDN dan mengesampingkan `max-age` untuk cache tersebut. Arahan `public` mengizinkan konten disimpan di cache bersama. Arahan `private` berarti konten hanya boleh disimpan di browser pengguna, bukan di CDN.

**no-cache dan no-store.** Kedua arahan ini sering tertukar. Arahan `no-cache` tidak berarti konten tidak boleh disimpan. Arahan ini berarti konten boleh disimpan tetapi harus divalidasi ulang ke origin sebelum digunakan. Arahan `no-store` berarti konten sama sekali tidak boleh disimpan. Gunakan `no-store` untuk konten yang sangat sensitif, seperti halaman berisi data pribadi.

**Vary.** Header `Vary` memberi tahu cache bahwa respons bisa berbeda tergantung header permintaan tertentu. Contohnya, `Vary: Accept-Encoding` menunjukkan bahwa respons berbeda untuk browser yang mendukung kompresi berbeda. Penggunaan `Vary` yang berlebihan, seperti terhadap header yang sangat beragam, dapat membuat cache hit ratio turun drastis. Gunakan header ini hanya jika respons memang berbeda. Banyak CDN memiliki aturan khusus dalam menangani header ini.

Berikut contoh pengaturan header cache untuk berbagai jenis konten:

```nginx
# File statis dengan nama berversi: simpan lama di browser dan CDN
location ~* \.(css|js|woff2|webp|avif|svg)$ {
  add_header Cache-Control "public, max-age=31536000, immutable";
}

# Halaman artikel publik: browser selalu memeriksa ulang,
# CDN boleh menyimpan 10 menit dan menyajikan versi lama sambil memperbarui
location /artikel/ {
  add_header Cache-Control "public, max-age=0, s-maxage=600, stale-while-revalidate=60";
}

# Halaman akun dan keranjang: jangan disimpan di cache bersama
location ~ ^/(akun|keranjang|checkout)/ {
  add_header Cache-Control "private, no-store";
}
```

Perhatikan bahwa pengaturan di atas hanyalah contoh. Sesuaikan dengan struktur URL dan kebutuhan website Anda. Uji setiap pengaturan dengan memeriksa header respons di panel Network browser. Banyak CDN menambahkan header khusus yang menunjukkan status cache, seperti `x-cache` atau `cf-cache-status`. Nilai seperti `HIT` atau `MISS` membantu Anda memastikan aturan cache bekerja sesuai harapan.

## Menyimpan Halaman HTML di Cache CDN

Menyimpan file statis di CDN adalah langkah yang relatif aman dan mudah. Langkah berikutnya yang memberikan dampak lebih besar adalah menyimpan halaman HTML di cache CDN. Dengan cara ini, halaman bisa dikirim langsung dari edge server tanpa menunggu server asal membangunnya. Waktu respons pertama atau TTFB bisa turun drastis. Namun, langkah ini membutuhkan perencanaan yang lebih matang.

Hal pertama yang perlu dipastikan adalah halaman mana yang aman untuk disimpan. Halaman publik yang sama untuk semua pengunjung, seperti artikel dan halaman produk, umumnya aman. Halaman yang menampilkan informasi personal, seperti nama pengguna atau isi keranjang, tidak boleh disimpan. Banyak website menampilkan elemen personal kecil di halaman publik, misalnya jumlah barang di keranjang di bagian atas. Elemen seperti itu sebaiknya dimuat terpisah melalui JavaScript agar halaman utamanya tetap bisa disimpan.

Hal kedua adalah menangani pengguna yang sudah masuk ke akun. Pengguna yang masuk biasanya memiliki cookie sesi. Atur CDN agar melewati cache untuk permintaan yang membawa cookie sesi tersebut. Dengan begitu, pengguna yang masuk selalu mendapat halaman yang sesuai dengan akunnya. Sementara itu, pengunjung anonim tetap mendapat halaman dari cache.

Hal ketiga adalah mekanisme pembaruan. Ketika artikel diperbarui atau harga produk berubah, versi lama di cache harus segera diganti. Gunakan fitur purge otomatis yang disediakan plugin atau integrasi CMS dengan CDN. Alternatifnya, gunakan TTL yang pendek dikombinasikan dengan `stale-while-revalidate`. Pilih pendekatan yang sesuai dengan seberapa sering konten Anda berubah.

## Fitur Lanjutan CDN Modern

CDN modern menawarkan jauh lebih banyak fitur daripada sekadar menyimpan file di cache. Banyak penyedia menjadikan jaringan mereka sebagai platform untuk menjalankan berbagai layanan di dekat pengguna. Fitur-fitur ini dapat meningkatkan kinerja dan keamanan tanpa mengubah server asal. Tidak semua fitur dibutuhkan oleh setiap website. Berikut beberapa fitur yang sering ditemui.

**Optimasi gambar otomatis.** Beberapa CDN dapat mengubah ukuran, mengompres, dan mengonversi format gambar secara otomatis. Browser yang mendukung WebP atau AVIF akan menerima format tersebut, sedangkan browser lain menerima format standar. Fitur ini menghemat banyak pekerjaan manual. Anda cukup menyimpan gambar asli di origin. Panduan lengkap tentang optimasi gambar ada di artikel [optimasi gambar website](/optimasi-gambar-website/).

**Web application firewall.** WAF menyaring permintaan yang mencurigakan sebelum mencapai server asal. WAF dapat memblokir pola serangan umum, seperti injeksi SQL dan skrip lintas situs. Banyak penyedia menyediakan aturan bawaan yang diperbarui secara berkala. Anda juga bisa membuat aturan khusus, misalnya membatasi akses ke halaman administrator. WAF sangat membantu untuk website yang menggunakan CMS populer yang sering menjadi sasaran serangan.

**Perlindungan DDoS dan pembatasan laju.** Serangan DDoS membanjiri website dengan permintaan dalam jumlah sangat besar. Jaringan CDN yang luas mampu menyerap dan menyaring lalu lintas serangan. Fitur pembatasan laju membatasi jumlah permintaan dari satu sumber dalam periode tertentu. Fitur ini berguna untuk melindungi halaman masuk dari upaya menebak kata sandi. Perlindungan ini membantu website tetap dapat diakses oleh pengguna yang sah.

**Komputasi di edge.** Beberapa penyedia memungkinkan Anda menjalankan kode langsung di edge server. Kode ini bisa digunakan untuk mengubah respons, melakukan pengalihan, menguji variasi halaman, atau mengautentikasi permintaan. Karena dijalankan dekat dengan pengguna, prosesnya sangat cepat. Fitur ini membuka peluang arsitektur baru untuk aplikasi web. Namun, penggunaannya membutuhkan pemahaman teknis yang lebih dalam.

**Analitik dan log.** CDN menyediakan data tentang jumlah permintaan, bandwidth, cache hit ratio, dan ancaman yang diblokir. Data ini membantu memahami pola lalu lintas dan efektivitas pengaturan cache. Beberapa penyedia juga menyediakan log permintaan yang lengkap. Log ini berguna untuk mendiagnosis masalah dan menyelidiki insiden keamanan. Tinjau data ini secara rutin untuk mengoptimalkan konfigurasi.

## Cara Memilih Penyedia CDN

Ada banyak penyedia CDN dengan fitur dan harga yang beragam. Memilih penyedia yang tepat bergantung pada kebutuhan website, lokasi pengunjung, dan anggaran. Jangan hanya memilih berdasarkan popularitas atau harga termurah. Pertimbangkan beberapa faktor berikut sebelum memutuskan. Manfaatkan masa uji coba untuk membandingkan secara langsung.

**Lokasi PoP.** Periksa apakah penyedia memiliki PoP di dekat mayoritas pengunjung Anda. Untuk pengunjung Indonesia, PoP di Jakarta dan kota-kota besar lain sangat menguntungkan. PoP di Singapura juga cukup dekat bagi banyak wilayah Indonesia. Peta jaringan biasanya tersedia di situs penyedia. Lakukan pengujian kecepatan dari beberapa kota untuk memastikan.

**Model biaya.** Penyedia CDN mengenakan biaya dengan berbagai cara. Ada yang berdasarkan jumlah bandwidth, jumlah permintaan, fitur yang digunakan, atau paket bulanan tetap. Biaya bandwidth juga bisa berbeda antarwilayah. Hitung perkiraan biaya berdasarkan pola trafik website Anda. Perhatikan juga biaya fitur tambahan seperti optimasi gambar atau WAF.

**Fitur yang dibutuhkan.** Daftar fitur yang benar-benar Anda butuhkan, misalnya caching HTML, optimasi gambar, WAF, atau komputasi di edge. Pastikan fitur tersebut tersedia di paket yang sesuai anggaran. Jangan membayar fitur yang tidak akan digunakan. Sebaliknya, jangan memilih paket yang terlalu terbatas sehingga harus berpindah penyedia dalam waktu dekat. Pertimbangkan juga rencana pertumbuhan website.

**Kemudahan penggunaan dan integrasi.** Panel pengaturan yang mudah dipahami sangat membantu, terutama bagi tim kecil. Periksa ketersediaan integrasi dengan CMS yang Anda gunakan. Integrasi seperti plugin WordPress memudahkan purge cache otomatis saat konten diperbarui. Dokumentasi yang lengkap juga menjadi nilai tambah. API yang baik memudahkan otomatisasi bagi tim pengembang.

**Dukungan dan keandalan.** Periksa jenis dukungan teknis yang tersedia di setiap paket. Untuk website bisnis yang kritis, dukungan cepat sangat penting. Pelajari juga riwayat keandalan penyedia dan halaman status layanannya. Perjanjian tingkat layanan atau SLA biasanya tersedia di paket berbayar. Pertimbangkan semua faktor ini bersama dengan harga.

## Memahami Cache Key dan Parameter URL

Cache key adalah identitas yang digunakan CDN untuk menentukan apakah dua permintaan meminta konten yang sama. Secara bawaan, cache key biasanya terdiri dari protokol, nama host, jalur URL, dan parameter kueri. Jika ada satu bagian yang berbeda, CDN menganggapnya sebagai konten yang berbeda. Akibatnya, CDN harus mengambil dan menyimpan salinan terpisah. Memahami cache key membantu Anda meningkatkan efektivitas cache.

Masalah sering muncul dari parameter pelacakan kampanye pemasaran. Tautan yang dibagikan di media sosial atau email sering ditambahi parameter seperti `utm_source` atau `utm_campaign`. Bagi CDN, setiap kombinasi parameter dianggap URL berbeda, padahal isi halamannya sama. Hasilnya, cache hit ratio turun dan origin menerima lebih banyak permintaan. Banyak penyedia CDN memungkinkan Anda mengabaikan parameter tertentu dalam cache key.

Sebaliknya, ada parameter yang memang mengubah isi halaman. Contohnya adalah parameter halaman pada paginasi atau parameter filter di toko daring. Parameter seperti ini harus tetap menjadi bagian dari cache key. Jika diabaikan, pengguna bisa melihat isi halaman yang salah. Karena itu, kenali setiap parameter yang digunakan di website Anda. Atur cache key berdasarkan dampak parameter terhadap isi halaman.

## CDN untuk Website WordPress

WordPress adalah salah satu platform yang paling banyak menggunakan CDN. Banyak hosting WordPress terkelola bahkan sudah menyertakan CDN dalam paketnya. Jika belum, CDN bisa dipasang dengan bantuan plugin atau melalui pengaturan DNS. Integrasi yang baik memudahkan pembersihan cache saat artikel diperbarui. Namun, ada beberapa hal khusus yang perlu diperhatikan.

Pertama, halaman administrator WordPress tidak boleh disimpan di cache. Pastikan jalur seperti halaman masuk dan dasbor administrator dikecualikan dari aturan cache. Kedua, pengguna yang sudah masuk, termasuk pelanggan toko WooCommerce, harus melewati cache halaman. WordPress dan WooCommerce menggunakan cookie tertentu untuk menandai pengguna yang masuk atau memiliki isi keranjang. Atur CDN agar melewati cache ketika cookie tersebut ada.

Ketiga, koordinasikan plugin caching di WordPress dengan cache di CDN. Plugin caching menyimpan halaman di server, sedangkan CDN menyimpan di edge. Saat konten diperbarui, keduanya harus dibersihkan agar versi terbaru tampil. Banyak plugin caching menyediakan integrasi langsung dengan penyedia CDN populer. Gunakan integrasi tersebut agar purge berjalan otomatis.

## CDN untuk Video dan File Berukuran Besar

Video dan file berukuran besar memiliki kebutuhan pengiriman yang berbeda dari halaman web biasa. Satu file video bisa berukuran ratusan megabita atau lebih. Mengirimkan file seperti itu dari server hosting biasa bisa sangat membebani bandwidth. CDN sangat membantu dengan mendistribusikan file ke banyak lokasi. Pengguna dapat mengunduh atau memutar video dengan lebih lancar.

Untuk video yang diputar langsung di website, gunakan format streaming adaptif. Format ini memecah video menjadi potongan-potongan kecil dengan beberapa tingkat kualitas. Pemutar video memilih kualitas sesuai kecepatan internet pengguna secara otomatis. CDN video khusus biasanya menangani proses pengodean dan pemecahan ini. Bagi pengguna di jaringan seluler, pengalaman menonton menjadi jauh lebih stabil.

## CDN untuk Aplikasi Berbasis Framework JavaScript

Aplikasi yang dibangun dengan framework seperti Next.js, Nuxt, atau SvelteKit sangat cocok dipadukan dengan CDN. File hasil build, seperti JavaScript dan CSS, biasanya sudah diberi nama berversi. File tersebut bisa disimpan di CDN dalam waktu sangat lama. Halaman yang dibuat secara statis saat build juga bisa disajikan langsung dari edge. Hasilnya adalah waktu muat yang sangat cepat.

Untuk halaman yang dirender di server pada setiap permintaan, atur header cache dengan cermat sesuai sifat halaman. Beberapa framework mendukung pola pembaruan bertahap, di mana halaman statis dibangun ulang secara berkala di latar belakang. Pola ini bekerja sangat baik dengan cache CDN dan arahan `stale-while-revalidate`. Banyak platform penerapan aplikasi modern sudah menyertakan jaringan edge secara bawaan. Pastikan Anda memahami cara platform tersebut mengatur cache agar tidak terjadi konten personal yang tersimpan.

## Memperhitungkan Biaya CDN

Banyak penyedia CDN menawarkan paket gratis, tetapi kebutuhan yang lebih besar biasanya memerlukan paket berbayar. Biaya CDN bisa meningkat seiring pertumbuhan trafik. Memahami komponen biaya membantu Anda menghindari tagihan yang tidak terduga. Komponen utama biasanya adalah bandwidth yang dikirim ke pengguna. Sebagian penyedia juga mengenakan biaya per jumlah permintaan.

Fitur tambahan seperti optimasi gambar, WAF lanjutan, atau komputasi di edge sering dikenakan biaya terpisah. Biaya bandwidth juga bisa berbeda tergantung wilayah tempat konten dikirim. Untuk website dengan banyak video atau unduhan, biaya bandwidth bisa menjadi komponen terbesar. Gunakan kalkulator harga dari penyedia untuk memperkirakan biaya berdasarkan data trafik nyata. Atur peringatan anggaran jika tersedia.

## Checklist Pemasangan CDN

1. Penyedia CDN memiliki PoP yang dekat dengan mayoritas pengunjung.
2. Semua catatan DNS, termasuk catatan email, sudah diperiksa setelah domain dipindahkan.
3. Mode HTTPS menggunakan enkripsi penuh hingga ke server asal.
4. File statis menggunakan nama berversi dan masa cache yang panjang.
5. Halaman personal dan permintaan dengan cookie sesi dikecualikan dari cache.
6. Parameter pelacakan yang tidak memengaruhi isi halaman diabaikan dalam cache key.
7. Mekanisme purge otomatis sudah diatur untuk konten yang diperbarui.
8. Akses langsung ke server asal dibatasi jika memungkinkan.
9. Header status cache sudah diperiksa untuk memastikan aturan bekerja.
10. Cache hit ratio dan beban server asal dipantau secara berkala.

## Perbedaan CDN, Hosting, dan Layanan Cloud

Istilah CDN sering tertukar dengan hosting dan layanan cloud. Ketiganya memang berkaitan, tetapi memiliki peran yang berbeda dalam infrastruktur website. Hosting adalah tempat aplikasi website dijalankan dan file aslinya disimpan. Layanan cloud adalah penyediaan sumber daya komputasi sesuai permintaan, yang bisa digunakan sebagai hosting maupun keperluan lain. CDN adalah lapisan pengiriman yang mempercepat dan melindungi akses ke konten.

Ketiganya sering digunakan bersama. Contohnya, aplikasi dijalankan di server cloud, gambar disimpan di layanan penyimpanan objek, dan semuanya dikirim kepada pengguna melalui CDN. Banyak penyedia cloud besar juga memiliki layanan CDN sendiri yang terintegrasi. Memahami peran masing-masing membantu Anda merancang arsitektur yang tepat. Penjelasan tentang layanan cloud dapat dibaca di artikel [cloud computing](/cloud-computing-pengertian-jenis-manfaat/).

## CDN dan Privasi Data

Saat menggunakan CDN, lalu lintas pengunjung melewati jaringan penyedia CDN. Artinya, penyedia CDN dapat memproses data seperti alamat IP dan informasi permintaan. Bagi website yang menangani data pribadi, hal ini perlu diperhatikan. Di Indonesia, pemrosesan data pribadi diatur dalam Undang-Undang Pelindungan Data Pribadi. Pastikan penggunaan CDN tercantum dalam kebijakan privasi website Anda.

Pelajari kebijakan privasi dan perjanjian pemrosesan data dari penyedia CDN. Periksa lokasi penyimpanan log dan berapa lama log tersebut disimpan. Beberapa penyedia menawarkan pengaturan untuk membatasi wilayah pemrosesan data. Pilih pengaturan yang sesuai dengan kebutuhan kepatuhan organisasi Anda. Untuk data yang sangat sensitif, konsultasikan dengan tim hukum atau ahli pelindungan data.

## Kesalahan Umum Saat Menggunakan CDN

CDN memang mudah dipasang, tetapi konfigurasi yang keliru bisa menimbulkan masalah serius. Sebagian kesalahan membuat CDN tidak memberikan manfaat apa pun. Sebagian lain justru membahayakan keamanan data pengguna. Kenali kesalahan-kesalahan berikut agar Anda bisa menghindarinya. Periksa juga apakah konfigurasi CDN Anda saat ini mengalami salah satunya.

**Menyimpan konten personal di cache.** Ini adalah kesalahan paling berbahaya dalam penggunaan CDN. Jika halaman akun atau keranjang tersimpan di cache bersama, pengguna lain bisa melihat data milik orang lain. Kesalahan ini sering terjadi saat aturan cache dibuat terlalu luas, misalnya menyimpan semua halaman HTML. Selalu kecualikan halaman personal dan permintaan dengan cookie sesi. Uji dengan beberapa akun berbeda setelah mengubah aturan cache.

**Mode HTTPS yang tidak aman.** Beberapa penyedia menawarkan mode di mana koneksi antara pengguna dan CDN terenkripsi, tetapi koneksi antara CDN dan origin tidak. Pengguna melihat ikon gembok di browser, tetapi data tetap dikirim tanpa enkripsi di sebagian perjalanan. Mode ini memberi rasa aman yang semu. Pasang sertifikat yang valid di origin dan gunakan mode enkripsi penuh dengan verifikasi. Langkah ini penting terutama untuk website yang menangani data pengguna.

**Alamat IP origin tetap terbuka.** Salah satu manfaat CDN adalah menyembunyikan origin dari serangan langsung. Namun, jika alamat IP origin masih bisa diketahui, penyerang bisa melewati CDN. Alamat IP sering bocor melalui catatan DNS lama, subdomain yang tidak melalui CDN, atau header email. Batasi akses ke origin hanya dari jaringan CDN jika penyedia mendukungnya. Periksa juga apakah ada subdomain yang mengarah langsung ke origin.

**Konten lama tidak kunjung berubah.** Setelah memperbarui file CSS atau JavaScript, pengunjung masih melihat tampilan lama. Hal ini terjadi karena file lama masih tersimpan di cache CDN dan browser. Solusi terbaik adalah menggunakan nama file berversi yang berubah setiap kali isinya berubah. Untuk halaman HTML, siapkan mekanisme purge otomatis saat konten diperbarui. Hindari mengandalkan purge manual seluruh cache setiap kali ada perubahan kecil.

**Cache hit ratio yang rendah.** Kadang CDN sudah dipasang, tetapi hampir semua permintaan tetap diteruskan ke origin. Penyebabnya bisa header `Cache-Control` yang melarang penyimpanan, cookie yang dikirim pada semua respons, atau parameter URL yang berbeda-beda. Parameter pelacakan seperti kode kampanye bisa membuat setiap URL dianggap berbeda oleh cache. Atur CDN agar mengabaikan parameter yang tidak memengaruhi isi halaman. Pantau cache hit ratio di panel CDN untuk mendeteksi masalah ini.

**Masalah CORS pada font dan aset.** Jika file font dilayani dari domain CDN yang berbeda, browser mungkin memblokirnya karena aturan keamanan lintas domain. Akibatnya, font kustom tidak tampil dan teks menggunakan font cadangan. Masalah ini diatasi dengan menambahkan header `Access-Control-Allow-Origin` yang tepat. Alternatifnya, layani font dari domain yang sama dengan website. Periksa konsol browser untuk melihat pesan galat terkait.

## Mengukur Dampak CDN

Setelah CDN terpasang, ukur dampaknya untuk memastikan investasi Anda memberikan hasil. Bandingkan metrik sebelum dan sesudah pemasangan. Pengukuran juga membantu menemukan pengaturan yang masih bisa dioptimalkan. Gunakan beberapa sumber data agar gambarannya lengkap. Berikut metrik yang perlu diperhatikan.

**Time to First Byte.** TTFB menunjukkan seberapa cepat server merespons permintaan pertama. Jika halaman HTML disimpan di cache CDN, TTFB biasanya turun signifikan. Jika hanya file statis yang disimpan, TTFB halaman mungkin tidak banyak berubah. Ukur TTFB dari beberapa lokasi menggunakan alat seperti WebPageTest. Bandingkan hasil dari kota yang dekat dan jauh dari origin.

**Core Web Vitals.** Pantau laporan Core Web Vitals di Search Console dan data pengguna nyata di PageSpeed Insights. Perbaikan TTFB dan kecepatan pengiriman file biasanya berdampak positif pada LCP. Ingat bahwa data pengguna nyata membutuhkan waktu beberapa minggu untuk mencerminkan perubahan. Cara membaca laporan tersebut dijelaskan di artikel [cara membaca PageSpeed Insights](/cara-membaca-pagespeed-insights/). Catat tanggal pemasangan CDN agar mudah membandingkan data.

**Cache hit ratio dan beban origin.** Panel CDN biasanya menampilkan persentase permintaan yang dilayani dari cache. Rasio yang tinggi menunjukkan CDN bekerja efektif. Pantau juga penggunaan sumber daya di server asal, seperti prosesor dan bandwidth. Penurunan beban origin menunjukkan bahwa CDN menyerap sebagian besar lalu lintas. Jika rasio rendah, tinjau kembali aturan dan header cache.

## FAQ CDN

### Apa itu CDN secara sederhana?

CDN adalah jaringan server di banyak lokasi yang menyimpan salinan konten website. Ketika pengguna membuka website, konten dikirim dari server terdekat sehingga lebih cepat. CDN juga mengurangi beban server utama dan menambah lapisan keamanan.

### Apakah website kecil perlu CDN?

Website kecil juga bisa mendapat manfaat dari CDN, terutama jika pengunjungnya berasal dari berbagai daerah. Banyak penyedia menawarkan paket gratis yang cukup untuk website kecil. Selain kecepatan, fitur keamanan dan HTTPS otomatis juga sangat membantu.

### Apakah CDN menggantikan hosting?

Tidak. CDN bekerja di atas hosting sebagai lapisan pengiriman. Website tetap membutuhkan server asal untuk menyimpan file asli dan menjalankan aplikasi. CDN hanya menyimpan salinan konten dan melayani permintaan dari lokasi yang dekat dengan pengguna.

### Apakah CDN berpengaruh pada SEO?

CDN dapat mempercepat waktu muat halaman dan memperbaiki metrik seperti TTFB dan LCP. Pengalaman halaman yang lebih baik bermanfaat bagi pengunjung dan merupakan bagian dari sinyal yang diperhatikan Google. Namun, CDN tidak secara langsung menaikkan peringkat tanpa konten yang relevan dan berkualitas.

### Mengapa perubahan di website tidak langsung terlihat setelah memakai CDN?

Hal ini terjadi karena konten lama masih tersimpan di cache CDN atau browser. Lakukan purge cache untuk file atau halaman yang diubah. Untuk jangka panjang, gunakan nama file berversi dan mekanisme purge otomatis.

### Apakah CDN aman untuk toko daring?

CDN aman digunakan untuk toko daring jika dikonfigurasi dengan benar. Pastikan halaman keranjang, pembayaran, dan akun tidak disimpan di cache bersama. Gunakan mode HTTPS penuh dan manfaatkan fitur keamanan seperti WAF.

### Apa perbedaan cache browser dan cache CDN?

Cache browser menyimpan file di perangkat masing-masing pengguna, sehingga hanya bermanfaat bagi pengguna tersebut. Cache CDN menyimpan file di edge server dan bisa dimanfaatkan oleh semua pengguna di wilayah yang sama. Keduanya diatur melalui header `Cache-Control` dan bekerja saling melengkapi.

### Berapa lama TTL yang ideal untuk CDN?

Tidak ada angka yang berlaku untuk semua konten. File statis dengan nama berversi bisa disimpan hingga satu tahun. Halaman HTML publik biasanya menggunakan TTL pendek, dari beberapa menit hingga beberapa jam, disertai mekanisme purge saat konten berubah.

### Bagaimana cara mengetahui apakah konten disajikan dari cache CDN?

Buka panel Network di alat pengembang browser, lalu periksa header respons sebuah file. Banyak CDN menambahkan header status seperti `x-cache` atau `cf-cache-status` dengan nilai `HIT` atau `MISS`. Nilai `HIT` menandakan konten disajikan dari cache.

### Apakah CDN bisa membuat website lebih lambat?

Dalam kondisi tertentu, bisa. Contohnya, jika hampir semua permintaan mengalami cache miss, CDN hanya menambah satu lapisan perjalanan sebelum mencapai server asal. Kondisi ini bisa diperbaiki dengan mengatur header cache, cache key, dan aturan pengecualian dengan benar.

## Kesimpulan

CDN adalah jaringan server tersebar yang mengirimkan konten website dari lokasi terdekat dengan pengguna. Cara kerjanya bertumpu pada cache di edge server, yang mengambil konten dari origin saat dibutuhkan dan menyimpannya untuk permintaan berikutnya. Manfaat utamanya adalah kecepatan, berkurangnya beban server asal, ketahanan terhadap lonjakan trafik, dan keamanan tambahan. Pemasangan CDN relatif mudah, tetapi aturan cache perlu diatur dengan cermat. Konten statis bisa disimpan lama, halaman publik bisa disimpan dengan TTL yang wajar, sedangkan halaman personal harus selalu dikecualikan.

Hindari kesalahan umum seperti menyimpan konten personal, mode HTTPS yang tidak aman, dan alamat origin yang terbuka. Ukur dampak CDN melalui TTFB, Core Web Vitals, dan cache hit ratio. Untuk membaca dampak tersebut dengan benar, gunakan panduan [cara membaca PageSpeed Insights](/cara-membaca-pagespeed-insights/). Jika halaman dinamis Anda masih lambat meski sudah memakai CDN, periksa kinerja basis data melalui artikel [optimasi database MySQL](/optimasi-database-mysql/).
