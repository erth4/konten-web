---
title: "Cara Membaca PageSpeed Insights dan Memperbaiki Skornya"
meta_description: "Pelajari cara membaca hasil PageSpeed Insights: data pengguna nyata, skor Lighthouse, arti setiap metrik dan saran perbaikan, serta alur kerja memperbaikinya."
slug: "cara-membaca-pagespeed-insights"
focus_keyword: "PageSpeed Insights"
keywords:
  - pagespeed insights
  - cara membaca pagespeed insights
  - skor pagespeed
  - lighthouse
  - cara meningkatkan skor pagespeed
  - google pagespeed
  - speed index
  - total blocking time
category: "Performa"
tags: ["Performa Website", "PageSpeed Insights", "Lighthouse", "Core Web Vitals"]
date: "2026-10-02"
lang: "id"
---

# Cara Membaca PageSpeed Insights dan Memperbaiki Skor Kinerja Website

Banyak pemilik website pertama kali mengenal istilah kecepatan website dari angka berwarna merah di **PageSpeed Insights**. Angka itu sering memicu kepanikan, terutama jika skor di perangkat seluler jauh lebih rendah daripada di desktop. Sebagian orang lalu memasang berbagai plugin tanpa memahami apa yang sebenarnya diukur. Hasilnya kadang membaik, kadang justru merusak tampilan website. Padahal, laporan PageSpeed Insights berisi informasi yang sangat jelas jika dibaca dengan benar.

Artikel ini membahas cara membaca laporan PageSpeed Insights bagian demi bagian. Anda akan memahami perbedaan antara data pengguna nyata dan hasil pengujian Lighthouse. Kami juga menjelaskan arti setiap metrik, cara skor kinerja dihitung, dan makna saran perbaikan yang paling sering muncul. Di bagian akhir, ada alur kerja untuk menindaklanjuti laporan beserta kesalahan yang sebaiknya dihindari. Untuk penjelasan mendalam tentang tiga metrik utama, Anda bisa membaca artikel Core Web Vitals.

## Daftar Isi

1. [Apa Itu PageSpeed Insights?](#apa-itu-pagespeed-insights)
2. [Cara Menggunakan PageSpeed Insights](#cara-menggunakan-pagespeed-insights)
3. [Struktur Laporan PageSpeed Insights](#struktur-laporan-pagespeed-insights)
4. [Membaca Data Pengguna Nyata](#membaca-data-pengguna-nyata)
5. [Membaca Skor Kinerja Lighthouse](#membaca-skor-kinerja-lighthouse)
6. [Arti Setiap Metrik Laboratorium](#arti-setiap-metrik-laboratorium)
7. [Memahami Daftar Diagnostik dan Saran Perbaikan](#memahami-daftar-diagnostik-dan-saran-perbaikan)
8. [Membaca Kategori Aksesibilitas, Praktik Terbaik, dan SEO](#membaca-kategori-aksesibilitas-praktik-terbaik-dan-seo)
9. [Mengapa Skor PageSpeed Berubah-ubah?](#mengapa-skor-pagespeed-berubah-ubah)
10. [Perbedaan PageSpeed Insights dan Alat Lain](#perbedaan-pagespeed-insights-dan-alat-lain)
11. [Alur Kerja Menindaklanjuti Laporan](#alur-kerja-menindaklanjuti-laporan)
12. [Contoh Membaca Laporan](#contoh-membaca-laporan)
13. [Fitur Tambahan di Laporan Lighthouse](#fitur-tambahan-di-laporan-lighthouse)
14. [Menggunakan PageSpeed Insights API](#menggunakan-pagespeed-insights-api)
15. [Tips Membaca Laporan untuk Website WordPress](#tips-membaca-laporan-untuk-website-wordpress)
16. [Menyampaikan Hasil Laporan kepada Klien atau Atasan](#menyampaikan-hasil-laporan-kepada-klien-atau-atasan)
17. [Kesalahan Umum Saat Menggunakan PageSpeed Insights](#kesalahan-umum-saat-menggunakan-pagespeed-insights)
18. [Memantau Kinerja secara Berkelanjutan](#memantau-kinerja-secara-berkelanjutan)
19. [FAQ PageSpeed Insights](#faq-pagespeed-insights)
20. [Kesimpulan](#kesimpulan)

## Apa Itu PageSpeed Insights?

PageSpeed Insights adalah alat gratis dari Google untuk menganalisis kinerja sebuah halaman web. Alat ini bisa diakses melalui browser dengan memasukkan alamat halaman yang ingin diuji. Dalam beberapa detik, PageSpeed Insights menampilkan laporan untuk perangkat seluler dan desktop. Laporan tersebut menggabungkan dua sumber data yang berbeda. Sumber pertama adalah data dari pengguna nyata, sedangkan sumber kedua adalah hasil pengujian otomatis dengan Lighthouse.

Banyak orang hanya melihat angka skor besar di bagian tengah laporan. Padahal, angka tersebut hanya sebagian kecil dari informasi yang tersedia. Bagian paling penting justru sering berada di atasnya, yaitu penilaian berdasarkan pengalaman pengguna nyata. Bagian lain yang tidak kalah penting adalah daftar diagnostik yang menunjukkan penyebab masalah. Memahami struktur laporan secara utuh akan membuat Anda mengambil keputusan yang lebih tepat.

PageSpeed Insights juga tersedia sebagai API yang dapat dipanggil dari program. Fitur ini berguna bagi pengembang yang ingin memantau banyak halaman secara otomatis. Hasil API berisi data yang sama dengan tampilan di browser. Banyak alat pemantauan pihak ketiga memanfaatkan API ini. Untuk penggunaan sehari-hari, antarmuka web sudah lebih dari cukup.

## Cara Menggunakan PageSpeed Insights

Menggunakan PageSpeed Insights sangat mudah. Buka situs PageSpeed Insights, lalu masukkan URL lengkap halaman yang ingin diuji. Klik tombol analisis dan tunggu beberapa saat hingga laporan muncul. Secara bawaan, laporan perangkat seluler akan ditampilkan terlebih dahulu. Anda bisa beralih ke laporan desktop melalui tab di bagian atas.

Ada beberapa hal yang perlu diperhatikan saat menguji. Pertama, ujilah halaman yang benar-benar penting, bukan hanya beranda. Halaman artikel, kategori, dan produk sering memiliki masalah yang berbeda. Kedua, ujilah URL versi final yang digunakan pengunjung, termasuk HTTPS dan awalan yang benar. Ketiga, jika baru saja melakukan perubahan, pastikan cache website sudah dibersihkan sebelum menguji.

Perlu diingat bahwa pengujian dilakukan dari server Google, bukan dari komputer Anda. Karena itu, kecepatan internet Anda tidak memengaruhi hasil pengujian. Namun, lokasi server pengujian dan kondisi jaringan saat itu bisa sedikit memengaruhi hasil. Hal ini menjadi salah satu alasan mengapa skor bisa berubah-ubah. Pembahasan tentang fluktuasi skor ada di bagian tersendiri.

## Struktur Laporan PageSpeed Insights

Laporan PageSpeed Insights terdiri dari beberapa bagian utama. Setiap bagian memiliki fungsi yang berbeda dan perlu dibaca dengan cara yang berbeda pula. Secara garis besar, laporan dibagi menjadi bagian data lapangan dan bagian data laboratorium. Bagian data laboratorium kemudian dilengkapi dengan daftar diagnostik dan kategori audit lainnya. Berikut urutan bagian yang biasanya Anda temui dari atas ke bawah.

1. Penilaian Core Web Vitals berdasarkan pengalaman pengguna nyata.
2. Rincian metrik data lapangan, untuk URL tersebut atau untuk seluruh origin.
3. Skor kinerja Lighthouse beserta metrik laboratoriumnya.
4. Tangkapan layar dan rekaman visual proses pemuatan halaman.
5. Daftar diagnostik dan saran perbaikan.
6. Skor kategori aksesibilitas, praktik terbaik, dan SEO.

Urutan ini sebenarnya mencerminkan urutan prioritas dalam membaca laporan. Data pengguna nyata menunjukkan apakah ada masalah yang dialami pengunjung. Data laboratorium membantu menjelaskan penyebab masalah tersebut. Daftar diagnostik memberikan petunjuk tentang apa yang perlu diperbaiki. Mari kita bahas setiap bagian secara lebih rinci.

## Membaca Data Pengguna Nyata

Bagian paling atas laporan menampilkan data dari pengguna nyata yang mengunjungi halaman Anda. Data ini berasal dari Chrome User Experience Report atau CrUX. CrUX mengumpulkan data kinerja dari pengguna Chrome yang mengizinkan berbagi statistik penggunaan. Data tersebut mencerminkan pengalaman pengunjung yang sebenarnya, dengan berbagai perangkat dan kondisi jaringan. Karena itu, bagian ini adalah gambaran paling jujur tentang kinerja website Anda.

### Penilaian Core Web Vitals

Di bagian atas data pengguna nyata, terdapat penilaian apakah halaman lulus atau gagal penilaian Core Web Vitals. Penilaian ini didasarkan pada tiga metrik, yaitu LCP, INP, dan CLS. Halaman dinyatakan lulus jika ketiga metrik berada dalam kategori baik pada persentil ke-75. Artinya, setidaknya tiga perempat kunjungan harus mendapat pengalaman yang baik. Jika satu metrik saja tidak memenuhi ambang batas, penilaian dinyatakan gagal.

Penilaian ini adalah informasi terpenting di seluruh laporan. Jika halaman sudah lulus, sebagian besar pengunjung mendapat pengalaman yang baik, apa pun skor Lighthouse-nya. Jika halaman gagal, Anda tahu metrik mana yang perlu menjadi prioritas. Penilaian ini juga sejalan dengan laporan Core Web Vitals di Google Search Console. Keduanya menggunakan sumber data yang sama.

### Metrik yang Ditampilkan

Selain tiga metrik Core Web Vitals, bagian ini juga menampilkan metrik pendukung. Metrik pendukung tersebut adalah First Contentful Paint dan Time to First Byte. Setiap metrik ditampilkan bersama nilai persentil ke-75 dan diagram batang berwarna. Diagram tersebut menunjukkan persentase kunjungan yang masuk kategori baik, perlu peningkatan, dan buruk. Membaca diagram ini membantu Anda melihat sebaran pengalaman, bukan hanya satu angka.

Sebagai contoh, nilai LCP mungkin tercatat 2,8 detik pada persentil ke-75. Namun, diagram bisa menunjukkan bahwa sebagian besar kunjungan sebenarnya sudah baik, sedangkan sebagian kecil sangat lambat. Pola seperti ini menandakan ada kelompok pengunjung tertentu yang mengalami masalah. Kelompok tersebut mungkin menggunakan jaringan yang lambat atau perangkat lama. Informasi ini membantu menentukan jenis perbaikan yang diperlukan.

### Data URL dan Data Origin

PageSpeed Insights menyediakan dua tingkat data pengguna nyata. Data tingkat URL menunjukkan pengalaman pengguna pada halaman spesifik yang diuji. Data tingkat origin menunjukkan pengalaman pengguna di seluruh halaman dalam domain tersebut. Anda bisa beralih di antara keduanya melalui tab yang tersedia. Data origin berguna untuk melihat kondisi website secara keseluruhan.

Data tingkat URL hanya tersedia jika halaman tersebut memiliki cukup banyak kunjungan dari pengguna Chrome. Halaman baru atau halaman yang jarang dikunjungi sering tidak memiliki data ini. Dalam kondisi tersebut, PageSpeed Insights mungkin hanya menampilkan data origin. Jika website secara keseluruhan juga belum memiliki cukup data, bagian ini tidak akan ditampilkan sama sekali. Ketiadaan data bukan berarti halaman bermasalah, melainkan hanya karena jumlah kunjungan belum memadai.

### Periode Data

Data pengguna nyata di PageSpeed Insights merupakan agregat dari periode 28 hari terakhir. Akibatnya, perbaikan yang Anda lakukan hari ini tidak akan langsung tercermin di bagian ini. Data baru akan bercampur dengan data lama selama beberapa minggu. Perubahan baru akan terlihat penuh setelah sekitar empat minggu. Bersabarlah dan gunakan data laboratorium untuk melihat dampak perubahan secara langsung.

## Membaca Skor Kinerja Lighthouse

Di bawah data pengguna nyata, terdapat bagian diagnosis masalah kinerja yang dihasilkan oleh Lighthouse. Lighthouse adalah alat pengujian otomatis yang memuat halaman dalam lingkungan yang dikendalikan. Hasilnya berupa skor kinerja dari 0 sampai 100 beserta beberapa metrik laboratorium. Skor ini sering menjadi pusat perhatian karena ditampilkan dalam lingkaran berwarna yang mencolok. Namun, memahami cara skor dihitung sangat penting agar tidak salah menafsirkannya.

### Arti Warna Skor

Skor kinerja dibagi ke dalam tiga rentang warna. Skor 90 sampai 100 ditampilkan berwarna hijau dan dianggap baik. Skor 50 sampai 89 ditampilkan berwarna oranye dan dianggap perlu peningkatan. Skor 0 sampai 49 ditampilkan berwarna merah dan dianggap buruk. Rentang warna ini berbeda dari ambang batas Core Web Vitals pada data pengguna nyata.

### Kondisi Pengujian

Pengujian seluler di PageSpeed Insights menyimulasikan perangkat seluler kelas menengah dengan jaringan yang lebih lambat. Prosesor juga diperlambat secara simulasi agar mendekati kemampuan ponsel. Kondisi ini sengaja dibuat cukup berat untuk mewakili sebagian besar pengguna seluler. Pengujian desktop menggunakan kondisi jaringan dan prosesor yang jauh lebih cepat. Itulah sebabnya skor seluler hampir selalu lebih rendah daripada skor desktop.

Perbedaan skor seluler dan desktop adalah hal yang wajar. Jangan membandingkan keduanya secara langsung. Bandingkan skor seluler halaman Anda dengan skor seluler halaman lain atau dengan hasil pengujian sebelumnya. Untuk sebagian besar website di Indonesia, kinerja seluler lebih penting karena mayoritas pengunjung menggunakan ponsel. Karena itu, fokuskan perbaikan pada hasil seluler.

### Cara Skor Dihitung

Skor kinerja Lighthouse dihitung dari beberapa metrik laboratorium yang masing-masing memiliki bobot. Setiap metrik terlebih dahulu diubah menjadi skor berdasarkan perbandingan dengan data dari banyak website nyata. Skor-skor tersebut kemudian digabungkan menggunakan bobot tertentu. Bobot ini dapat berubah antarversi Lighthouse seiring perkembangan pemahaman tentang pengalaman pengguna. Pada versi Lighthouse yang banyak digunakan saat ini, pembagian bobotnya adalah sebagai berikut.

| Metrik | Bobot dalam Skor |
|---|---|
| Total Blocking Time (TBT) | 30% |
| Largest Contentful Paint (LCP) | 25% |
| Cumulative Layout Shift (CLS) | 25% |
| First Contentful Paint (FCP) | 10% |
| Speed Index (SI) | 10% |

Dari tabel tersebut, terlihat bahwa TBT, LCP, dan CLS menyumbang sebagian besar skor. Memperbaiki ketiga metrik ini biasanya memberikan kenaikan skor paling besar. TBT sangat dipengaruhi oleh JavaScript, LCP oleh kecepatan server dan sumber daya utama, dan CLS oleh stabilitas tata letak. Lighthouse juga menyediakan kalkulator skor yang menunjukkan bagaimana perubahan setiap metrik memengaruhi skor akhir. Kalkulator ini dapat diakses melalui tautan di laporan.

## Arti Setiap Metrik Laboratorium

Metrik laboratorium ditampilkan tepat di bawah skor kinerja. Setiap metrik diberi warna sesuai kategorinya. Memahami arti setiap metrik membantu Anda mengetahui bagian mana dari proses pemuatan yang bermasalah. Metrik-metrik ini saling berhubungan, sehingga satu perbaikan bisa memengaruhi beberapa metrik sekaligus. Berikut penjelasan setiap metrik.

**First Contentful Paint (FCP).** FCP mencatat kapan browser pertama kali menggambar konten apa pun, misalnya teks atau gambar, di layar. Metrik ini menunjukkan kapan pengguna pertama kali melihat bahwa halaman sedang dimuat. FCP yang lambat biasanya disebabkan oleh server yang lambat merespons atau sumber daya yang memblokir rendering. Font kustom yang lambat dimuat juga bisa menunda tampilnya teks. Perbaikan di sisi server dan pengurangan CSS yang memblokir sering mempercepat FCP.

**Largest Contentful Paint (LCP).** LCP mengukur waktu hingga elemen konten terbesar di layar pertama selesai ditampilkan. Elemen ini biasanya berupa gambar utama atau blok teks besar. LCP mencerminkan kapan pengguna merasa konten utama sudah tersedia. Laporan Lighthouse menunjukkan elemen mana yang menjadi elemen LCP. Informasi ini sangat penting untuk menentukan langkah perbaikan.

**Total Blocking Time (TBT).** TBT mengukur total waktu ketika *main thread* browser terblokir oleh tugas panjang antara FCP dan saat halaman dianggap interaktif. Selama waktu terblokir, halaman tidak dapat merespons klik atau ketukan pengguna. TBT adalah metrik laboratorium yang berkaitan dengan responsivitas. Nilai TBT yang tinggi menandakan risiko INP yang buruk bagi pengguna nyata. Penyebab utamanya hampir selalu JavaScript yang berat, termasuk skrip pihak ketiga.

**Cumulative Layout Shift (CLS).** CLS mengukur pergeseran tata letak yang tidak terduga selama halaman dimuat. Nilai CLS di laboratorium hanya mencakup pergeseran saat pemuatan awal. Di data pengguna nyata, CLS juga mencakup pergeseran selama pengguna berinteraksi dan menggulir. Karena itu, nilai CLS di laboratorium bisa lebih rendah daripada di data lapangan. Penyebab umumnya adalah gambar tanpa dimensi, iklan, dan konten yang disisipkan secara dinamis.

**Speed Index (SI).** Speed Index mengukur seberapa cepat konten halaman ditampilkan secara visual selama proses pemuatan. Lighthouse merekam proses pemuatan dalam bentuk bingkai video, lalu menghitung seberapa cepat tampilan halaman menjadi lengkap. Halaman yang menampilkan sebagian besar konten sejak awal akan memiliki Speed Index yang baik. Sebaliknya, halaman yang tetap kosong lama lalu tiba-tiba lengkap akan memiliki Speed Index yang buruk. Metrik ini dipengaruhi oleh hal-hal yang sama dengan FCP dan LCP.

## Memahami Daftar Diagnostik dan Saran Perbaikan

Bagian yang paling bermanfaat untuk tindakan nyata adalah daftar diagnostik di bawah metrik. Daftar ini berisi temuan Lighthouse tentang hal-hal yang memperlambat halaman. Banyak temuan disertai perkiraan penghematan waktu atau ukuran data. Anda juga bisa memfilter temuan berdasarkan metrik tertentu, misalnya hanya yang berkaitan dengan LCP. Fitur filter ini sangat membantu untuk memprioritaskan perbaikan.

Setiap temuan bisa diklik untuk melihat detailnya. Detail tersebut biasanya berisi daftar file, elemen, atau skrip yang bermasalah. Bacalah detail ini dengan teliti sebelum melakukan perubahan. Sering kali, masalah utama hanya berasal dari satu atau dua file tertentu. Memperbaiki sumber masalah yang tepat jauh lebih efektif daripada menerapkan optimasi secara acak.

Nama dan pengelompokan temuan dapat berubah seiring pembaruan Lighthouse. Beberapa temuan lama kini digabungkan atau diganti dengan nama yang lebih deskriptif. Meski begitu, inti masalah yang dideteksi tetap sama. Berikut penjelasan temuan-temuan yang paling sering muncul beserta arti dan arah perbaikannya. Gunakan penjelasan ini sebagai panduan saat membaca laporan Anda.

### Temuan yang Berkaitan dengan Pemuatan

**Sumber daya yang memblokir rendering.** Temuan ini menunjukkan file CSS atau JavaScript yang harus selesai dimuat sebelum halaman bisa ditampilkan. Semakin banyak dan semakin besar file tersebut, semakin lama halaman kosong di layar. Arah perbaikannya adalah menunda skrip yang tidak penting dengan atribut `defer` atau `async`. Untuk CSS, pertimbangkan memisahkan gaya penting untuk tampilan awal. Hapus juga file yang sebenarnya tidak digunakan di halaman tersebut.

**Waktu respons server awal yang lambat.** Temuan ini menunjukkan bahwa server membutuhkan waktu terlalu lama untuk mengirim dokumen HTML. Penyebabnya bisa hosting yang kurang memadai, tidak adanya caching halaman, atau proses aplikasi yang berat. Masalah ini memengaruhi semua metrik lain karena browser harus menunggu sebelum bisa mulai bekerja. Arah perbaikannya adalah mengaktifkan caching, menggunakan CDN, dan mengoptimalkan proses di server. Kueri basis data yang lambat juga sering menjadi penyebab, seperti dibahas di artikel optimasi database MySQL.

**Penemuan permintaan LCP.** Temuan ini memeriksa apakah gambar LCP dapat ditemukan oleh browser sejak awal. Gambar yang dimuat melalui JavaScript atau diberi atribut lazy load akan terlambat ditemukan. Lighthouse juga memeriksa apakah gambar tersebut diberi prioritas tinggi. Arah perbaikannya adalah menuliskan gambar utama langsung di HTML, tidak menerapkan lazy load padanya, dan menambahkan `fetchpriority="high"`. Perbaikan ini sering memberikan peningkatan LCP yang besar.

**Hindari rantai permintaan penting.** Temuan ini menunjukkan rangkaian permintaan yang saling bergantung. Misalnya, file CSS memuat file font, yang kemudian memuat file lain. Setiap mata rantai menambah waktu tunggu. Arah perbaikannya adalah memperpendek rantai dengan *preload* untuk sumber daya penting. Kurangi juga ketergantungan sumber daya yang tidak perlu.

**Pengalihan halaman.** Temuan ini muncul jika URL yang diuji mengalami pengalihan sebelum sampai ke halaman akhir. Setiap pengalihan menambah waktu perjalanan bolak-balik antara browser dan server. Arah perbaikannya adalah memastikan tautan langsung mengarah ke URL final. Hindari rantai pengalihan dari HTTP ke HTTPS lalu ke versi dengan atau tanpa www. Pengalihan yang sederhana mempercepat pemuatan di setiap kunjungan.

### Temuan yang Berkaitan dengan Ukuran Sumber Daya

**Perbaikan pengiriman gambar.** Temuan ini mencakup gambar yang terlalu besar dibanding ukuran tampilannya, belum menggunakan format modern, atau belum dikompres dengan baik. Lighthouse menampilkan daftar gambar beserta perkiraan penghematan ukuran. Arah perbaikannya adalah mengubah ukuran gambar, menggunakan format WebP atau AVIF, dan menyediakan beberapa ukuran dengan `srcset`. Gambar sering menjadi sumber penghematan terbesar. Langkah-langkah rincinya dibahas dalam artikel optimasi gambar website.

**Kurangi JavaScript dan CSS yang tidak digunakan.** Temuan ini menunjukkan berapa banyak kode yang dimuat tetapi tidak digunakan di halaman tersebut. Kode yang tidak digunakan tetap harus diunduh dan diproses. Sumbernya sering berasal dari tema, plugin, atau pustaka yang dimuat di semua halaman. Arah perbaikannya adalah memuat kode hanya di halaman yang membutuhkannya. Gunakan juga fitur *code splitting* jika memakai alat build modern.

**Hindari payload jaringan yang sangat besar.** Temuan ini menunjukkan total ukuran semua sumber daya yang diunduh halaman. Halaman yang terlalu besar membutuhkan waktu lama untuk dimuat, terutama di jaringan seluler. Detail temuan menampilkan file-file terbesar. Fokuskan perbaikan pada file-file teratas dalam daftar tersebut. Biasanya, gambar, video, dan bundel JavaScript yang besar menjadi penyebab utama.

**Kompresi teks.** Temuan ini muncul jika file teks seperti HTML, CSS, dan JavaScript dikirim tanpa kompresi. Kompresi Gzip atau Brotli dapat mengecilkan ukuran file teks secara signifikan. Pengaturan ini biasanya dilakukan di server web atau CDN. Sekali diaktifkan, manfaatnya berlaku untuk semua halaman. Temuan ini termasuk perbaikan yang paling mudah dan berdampak besar.

**Masa cache yang terlalu singkat.** Temuan ini menunjukkan file statis yang tidak disimpan cukup lama di cache browser. Akibatnya, pengunjung yang kembali harus mengunduh ulang file yang sama. Arah perbaikannya adalah mengatur header `Cache-Control` dengan masa simpan panjang untuk file statis. Gunakan nama file berversi agar pembaruan tetap terunduh. Perbaikan ini tidak memengaruhi skor kunjungan pertama, tetapi sangat membantu kunjungan berikutnya.

### Temuan yang Berkaitan dengan JavaScript dan Responsivitas

**Minimalkan pekerjaan main thread.** Temuan ini menunjukkan total waktu yang digunakan browser untuk memproses halaman di *main thread*. Rinciannya mencakup evaluasi skrip, perhitungan gaya, tata letak, dan rendering. Waktu yang tinggi menandakan halaman terlalu berat untuk diproses perangkat. Arah perbaikannya adalah mengurangi JavaScript, menyederhanakan CSS, dan memperkecil DOM. Temuan ini sangat berkaitan dengan nilai TBT.

**Kurangi waktu eksekusi JavaScript.** Temuan ini menunjukkan skrip-skrip yang paling lama dijalankan. Daftar tersebut sering menunjukkan skrip pihak ketiga seperti iklan, analitik, atau widget obrolan. Tinjau setiap skrip dan tanyakan apakah keberadaannya benar-benar diperlukan. Tunda pemuatan skrip yang tidak dibutuhkan di awal. Untuk kode sendiri, pecah tugas besar menjadi bagian-bagian kecil.

**Hindari tugas panjang di main thread.** Temuan ini menampilkan daftar tugas yang berjalan lebih dari 50 milidetik. Selama tugas panjang berjalan, halaman tidak bisa merespons interaksi pengguna. Detail temuan menunjukkan skrip mana yang menyebabkan tugas tersebut. Arah perbaikannya adalah memecah tugas panjang dan menyerahkan kendali kepada browser secara berkala. Teknik ini dijelaskan lebih rinci di bagian INP pada artikel Core Web Vitals.

**Ukuran DOM yang berlebihan.** Temuan ini muncul jika halaman memiliki terlalu banyak elemen HTML. DOM yang besar memperlambat perhitungan gaya dan tata letak setiap kali ada perubahan. Masalah ini sering terjadi pada halaman yang dibuat dengan pembangun halaman visual atau daftar produk yang sangat panjang. Arah perbaikannya adalah menyederhanakan struktur HTML dan menghapus elemen yang tidak perlu. Untuk daftar panjang, pertimbangkan paginasi atau pemuatan bertahap.

**Dampak kode pihak ketiga.** Temuan ini merangkum skrip dari domain lain beserta ukuran dan waktu pemrosesannya. Informasi ini membantu Anda melihat seberapa besar beban yang ditambahkan oleh layanan pihak ketiga. Sering kali, skrip pihak ketiga menjadi penyumbang terbesar masalah kinerja. Diskusikan dengan tim pemasaran tentang skrip mana yang masih dibutuhkan. Hapus skrip yang sudah tidak digunakan dan tunda yang tidak mendesak.

### Temuan yang Berkaitan dengan Stabilitas Tata Letak

**Penyebab pergeseran tata letak.** Temuan ini menunjukkan elemen-elemen yang bergeser selama halaman dimuat. Lighthouse sering menyertakan informasi tentang penyebab pergeseran, seperti gambar tanpa dimensi atau font yang berganti. Arah perbaikannya adalah menambahkan atribut `width` dan `height` pada gambar dan video. Siapkan ruang untuk iklan dan konten yang dimuat belakangan. Kelola pemuatan font agar pergantian font tidak mengubah ukuran teks secara drastis.

**Gambar tanpa dimensi eksplisit.** Temuan ini secara khusus menunjukkan gambar yang tidak memiliki atribut lebar dan tinggi. Tanpa atribut tersebut, browser tidak tahu berapa ruang yang harus disediakan. Akibatnya, konten di bawah gambar bergeser saat gambar selesai dimuat. Perbaikan ini sangat mudah dan hampir selalu efektif. Pastikan juga gambar tetap responsif dengan CSS `height: auto`.

**Halaman mencegah pemulihan back/forward cache.** Temuan ini menunjukkan bahwa halaman tidak dapat disimpan di *back/forward cache* browser. Fitur tersebut memungkinkan halaman ditampilkan instan saat pengguna menekan tombol kembali. Detail temuan menjelaskan alasan kegagalannya, seperti penggunaan *event* `unload`. Memperbaiki penyebabnya membuat navigasi kembali terasa jauh lebih cepat. Hal ini juga membantu metrik pengguna nyata.

## Membaca Kategori Aksesibilitas, Praktik Terbaik, dan SEO

Di bagian bawah laporan, PageSpeed Insights juga menampilkan skor untuk tiga kategori lain. Ketiga kategori tersebut adalah aksesibilitas, praktik terbaik, dan SEO. Skor ini tidak berkaitan langsung dengan kecepatan, tetapi tetap berguna untuk menilai kualitas halaman. Setiap kategori berisi daftar pemeriksaan otomatis. Perlu diingat bahwa pemeriksaan otomatis hanya mampu mendeteksi sebagian masalah.

**Aksesibilitas.** Kategori ini memeriksa apakah halaman dapat digunakan oleh orang dengan berbagai kemampuan, termasuk pengguna pembaca layar. Contoh pemeriksaannya adalah teks alternatif pada gambar, kontras warna yang cukup, label pada formulir, dan urutan heading. Skor tinggi menunjukkan bahwa masalah dasar sudah ditangani. Namun, skor 100 tidak menjamin halaman sepenuhnya aksesibel. Pengujian manual dengan pembaca layar dan keyboard tetap diperlukan.

**Praktik terbaik.** Kategori ini memeriksa berbagai aspek kualitas teknis halaman. Contohnya adalah penggunaan HTTPS, tidak adanya galat di konsol browser, dan penggunaan API yang tidak usang. Pemeriksaan juga mencakup gambar yang ditampilkan dengan rasio aspek yang benar. Masalah di kategori ini sering menunjukkan kode yang perlu dirapikan. Beberapa masalah juga berkaitan dengan keamanan.

**SEO.** Kategori ini memeriksa elemen dasar SEO teknis. Contohnya adalah keberadaan judul halaman dan meta description, status HTTP yang benar, tautan yang dapat dirayapi, dan pengaturan robots. Skor tinggi di kategori ini menunjukkan bahwa fondasi teknis sudah benar. Namun, skor ini tidak mengukur kualitas konten atau peluang peringkat. SEO yang sebenarnya jauh lebih luas, seperti dijelaskan dalam artikel apa itu SEO.

## Mengapa Skor PageSpeed Berubah-ubah?

Banyak pemilik website bingung karena skor kinerja bisa berbeda setiap kali diuji. Pengujian pertama mungkin menunjukkan skor 72, sedangkan pengujian berikutnya menunjukkan 65 tanpa ada perubahan apa pun. Variasi seperti ini adalah hal yang wajar. Lighthouse menjalankan pengujian dalam kondisi nyata yang tidak sepenuhnya stabil. Berikut beberapa penyebab umum variasi skor.

**Kondisi jaringan dan server.** Waktu respons server bisa berbeda dari satu permintaan ke permintaan lain. Beban server, kondisi jaringan, dan status cache memengaruhi hasil. Jika server sedang sibuk, waktu respons akan lebih lama dan skor menurun. CDN juga mungkin belum menyimpan file di lokasi tertentu pada pengujian pertama. Akibatnya, pengujian berikutnya bisa lebih cepat.

**Skrip pihak ketiga dan iklan.** Iklan dan skrip pihak ketiga sering memuat konten yang berbeda setiap kali halaman dibuka. Satu kali pengujian mungkin memuat iklan ringan, sedangkan pengujian lain memuat iklan yang berat. Variasi ini memengaruhi TBT, LCP, dan CLS. Halaman dengan banyak skrip pihak ketiga cenderung memiliki skor yang lebih tidak stabil. Mengurangi skrip pihak ketiga juga membuat hasil pengujian lebih konsisten.

**Konten dinamis.** Halaman yang kontennya berubah-ubah, seperti beranda dengan artikel terbaru atau rekomendasi produk, bisa menghasilkan skor berbeda. Gambar utama yang berbeda ukurannya akan memengaruhi LCP. Pengujian A/B yang berjalan di halaman juga dapat menyebabkan variasi. Ketahui elemen dinamis apa saja yang ada di halaman Anda. Hal ini membantu menjelaskan perbedaan hasil.

Cara terbaik menghadapi variasi adalah menjalankan pengujian beberapa kali dan melihat nilai tengahnya. Jangan mengambil kesimpulan dari satu kali pengujian. Catat hasil beberapa pengujian sebelum dan sesudah perubahan. Bandingkan juga dengan data pengguna nyata yang lebih stabil. Fokuslah pada tren, bukan angka tunggal.

## Perbedaan PageSpeed Insights dan Alat Lain

PageSpeed Insights bukan satu-satunya alat untuk mengukur kinerja website. Setiap alat memiliki kegunaan tersendiri dalam alur kerja optimasi. Memahami perbedaannya membantu Anda memilih alat yang tepat untuk setiap situasi. Hasil antaralat juga bisa berbeda karena kondisi pengujian yang tidak sama. Berikut perbandingan singkatnya.

**Lighthouse di Chrome DevTools.** Lighthouse yang dijalankan di browser Anda menggunakan mesin yang sama dengan PageSpeed Insights. Namun, pengujian dilakukan dari komputer dan jaringan Anda sendiri. Hasilnya bisa dipengaruhi oleh ekstensi browser dan aplikasi lain yang sedang berjalan. Keunggulannya, Anda bisa menguji halaman yang belum dipublikasikan, seperti di lingkungan pengembangan. Jalankan di jendela penyamaran agar ekstensi tidak memengaruhi hasil.

**Laporan Core Web Vitals di Search Console.** Laporan ini menggunakan data pengguna nyata yang sama dengan bagian atas PageSpeed Insights. Bedanya, laporan ini mengelompokkan banyak halaman sekaligus berdasarkan masalah yang serupa. Laporan ini sangat cocok untuk melihat kondisi seluruh website. Anda juga bisa meminta validasi setelah melakukan perbaikan. Gunakan laporan ini untuk menentukan prioritas, lalu gunakan PageSpeed Insights untuk menganalisis contoh halaman.

**WebPageTest.** WebPageTest memungkinkan pengujian dari berbagai lokasi, perangkat, dan kecepatan jaringan. Alat ini menampilkan diagram *waterfall* yang sangat rinci. Anda bisa melihat urutan dan durasi setiap permintaan. WebPageTest sangat berguna untuk analisis mendalam ketika laporan PageSpeed Insights belum cukup menjelaskan masalah. Alat ini juga bisa membandingkan beberapa versi halaman.

**Panel Performance di Chrome DevTools.** Panel ini memberikan rekaman sangat rinci tentang apa yang terjadi di browser. Anda bisa melihat setiap tugas JavaScript, perhitungan tata letak, dan proses rendering. Panel ini sangat membantu untuk mendiagnosis masalah responsivitas. Anda juga bisa merekam interaksi nyata, seperti mengklik tombol. Bagi pengembang, panel ini adalah alat diagnosis yang paling kuat.

## Alur Kerja Menindaklanjuti Laporan

Membaca laporan hanyalah langkah awal. Nilai sebenarnya ada pada tindakan yang diambil setelahnya. Banyak orang langsung mencoba memperbaiki semua temuan sekaligus tanpa prioritas. Akibatnya, waktu terbuang untuk perbaikan kecil sementara masalah utama terlewat. Berikut alur kerja yang lebih terarah untuk menindaklanjuti laporan PageSpeed Insights.

**Langkah 1: Mulai dari data pengguna nyata.** Periksa apakah halaman lulus penilaian Core Web Vitals. Jika lulus, perbaikan kinerja mungkin bukan prioritas utama untuk halaman tersebut. Jika gagal, catat metrik mana yang bermasalah. Metrik tersebut menjadi fokus perbaikan. Periksa juga data origin untuk melihat apakah masalahnya terjadi di seluruh website.

**Langkah 2: Hubungkan dengan metrik laboratorium.** Lihat metrik laboratorium yang berkaitan dengan masalah di data pengguna nyata. Jika LCP pengguna nyata buruk, perhatikan LCP dan FCP di laboratorium. Jika INP buruk, perhatikan TBT. Jika CLS buruk, perhatikan CLS laboratorium, meskipun nilainya bisa berbeda. Hubungan ini membantu Anda memilih temuan diagnostik yang paling relevan.

**Langkah 3: Filter dan prioritaskan temuan.** Gunakan filter di daftar diagnostik untuk menampilkan temuan yang berkaitan dengan metrik bermasalah. Urutkan berdasarkan perkiraan dampak. Pilih dua atau tiga temuan teratas yang paling mungkin diperbaiki. Hindari mencoba memperbaiki semua temuan sekaligus. Perbaikan yang terfokus lebih mudah diukur dampaknya.

**Langkah 4: Terapkan perbaikan dan uji ulang.** Terapkan perbaikan di lingkungan pengujian jika memungkinkan. Jalankan Lighthouse beberapa kali untuk melihat dampaknya. Pastikan tidak ada fungsi website yang rusak akibat perubahan. Setelah yakin, terapkan ke website utama. Catat tanggal dan isi perubahan untuk keperluan evaluasi.

**Langkah 5: Pantau data pengguna nyata.** Setelah perbaikan diterapkan, pantau data pengguna nyata selama beberapa minggu. Ingat bahwa data ini merupakan agregat 28 hari. Jika menggunakan Search Console, mulai proses validasi untuk masalah yang sudah diperbaiki. Jika data membaik, lanjutkan ke masalah berikutnya. Jika belum membaik, kembali ke data laboratorium untuk mencari penyebab lain.

## Contoh Membaca Laporan

Agar lebih konkret, berikut contoh cara membaca laporan untuk sebuah halaman artikel blog. Contoh ini bersifat ilustrasi dan angka yang digunakan tidak berasal dari website tertentu. Misalkan data pengguna nyata menunjukkan bahwa halaman gagal penilaian Core Web Vitals karena LCP bernilai 3,4 detik. INP dan CLS sudah berada di kategori baik. Skor kinerja Lighthouse untuk seluler adalah 58.

Langkah pertama adalah fokus pada LCP karena itulah metrik yang membuat halaman gagal. Di bagian laboratorium, LCP tercatat 5,1 detik, sedangkan FCP 2,2 detik. Jarak yang cukup jauh antara FCP dan LCP menunjukkan bahwa elemen LCP dimuat terlambat. Detail temuan menunjukkan bahwa elemen LCP adalah gambar sampul artikel. Temuan penemuan permintaan LCP juga menunjukkan bahwa gambar tersebut diberi atribut lazy load.

Dari temuan lain, terlihat bahwa gambar sampul berukuran sangat besar dan masih menggunakan format JPEG. Langkah perbaikan pun menjadi jelas. Pertama, hapus atribut lazy load dari gambar sampul dan tambahkan prioritas tinggi. Kedua, ubah gambar sampul ke format WebP dengan ukuran yang sesuai dan sediakan versi responsif. Setelah perbaikan, pengujian laboratorium menunjukkan LCP turun signifikan dan skor naik.

Beberapa minggu kemudian, data pengguna nyata menunjukkan LCP sudah berada di kategori baik. Halaman pun lulus penilaian Core Web Vitals. Skor Lighthouse mungkin belum mencapai 90 karena masih ada temuan lain, seperti JavaScript yang tidak digunakan. Namun, pengalaman pengguna sudah membaik secara nyata. Perbaikan berikutnya bisa dijadwalkan sesuai prioritas.

## Fitur Tambahan di Laporan Lighthouse

Selain skor dan daftar temuan, laporan Lighthouse memiliki beberapa fitur tambahan yang sering terlewat. Fitur-fitur ini memberikan konteks visual yang membantu memahami proses pemuatan halaman. Memanfaatkannya bisa mempercepat proses diagnosis. Fitur ini terutama berguna saat temuan diagnostik belum cukup menjelaskan masalah. Berikut beberapa fitur yang patut diketahui.

**Deretan tangkapan layar.** Laporan menampilkan beberapa tangkapan layar yang menggambarkan kondisi halaman dari waktu ke waktu selama pemuatan. Dari deretan ini, Anda bisa melihat kapan halaman mulai menampilkan konten dan kapan konten utama muncul. Halaman yang lama kosong menandakan masalah pada server atau sumber daya yang memblokir rendering. Halaman yang tampil bertahap tetapi gambar utamanya muncul belakangan menandakan masalah pada pemuatan elemen LCP. Gambaran visual ini sering lebih mudah dipahami daripada angka.

**Peta ukuran skrip.** Lighthouse menyediakan tampilan peta yang menggambarkan ukuran setiap file JavaScript dan bagian di dalamnya. Tampilan ini membantu menemukan pustaka atau modul yang paling besar. Anda juga bisa melihat berapa bagian kode yang tidak digunakan. Fitur ini sangat bermanfaat bagi pengembang yang ingin mengurangi ukuran bundel JavaScript. Dari sana, keputusan untuk mengganti atau menunda pustaka tertentu bisa diambil berdasarkan data.

**Tampilan berdasarkan metrik.** Filter metrik di atas daftar temuan memungkinkan Anda hanya menampilkan temuan yang memengaruhi metrik tertentu. Misalnya, pilih LCP untuk melihat temuan yang berkaitan dengan pemuatan konten utama. Pilih TBT untuk melihat temuan yang berkaitan dengan JavaScript. Fitur ini membuat daftar temuan yang panjang menjadi lebih mudah dikelola. Gunakan bersama informasi metrik bermasalah dari data pengguna nyata.

## Menggunakan PageSpeed Insights API

Bagi Anda yang mengelola banyak halaman, menguji satu per satu melalui browser cukup melelahkan. PageSpeed Insights menyediakan API yang bisa dipanggil dari program atau baris perintah. Hasil API berisi data yang sama dengan laporan di browser dalam format JSON. Untuk penggunaan ringan, API dapat dipanggil tanpa kunci. Untuk penggunaan rutin dalam jumlah besar, sebaiknya gunakan kunci API dari Google Cloud.

Berikut contoh pemanggilan API sederhana menggunakan `curl` dan `jq` untuk mengambil skor kinerja seluler. Skor di dalam respons API berupa angka antara 0 dan 1, sehingga perlu dikalikan 100. Respons juga memuat data pengguna nyata di bagian `loadingExperience` jika tersedia. Anda bisa menyimpan hasilnya secara berkala untuk memantau tren kinerja. Skrip seperti ini mudah dijadwalkan untuk berjalan otomatis setiap minggu.

```bash
URL="https://contoh.com/artikel/panduan"
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=${URL}&strategy=mobile" \
  | jq '{
      skor: (.lighthouseResult.categories.performance.score * 100),
      lcp_lab: .lighthouseResult.audits["largest-contentful-paint"].displayValue,
      lcp_p75_pengguna: .loadingExperience.metrics.LARGEST_CONTENTFUL_PAINT_MS.percentile
    }'
```

## Tips Membaca Laporan untuk Website WordPress

Website WordPress memiliki pola masalah yang cukup khas di laporan PageSpeed Insights. Temuan tentang JavaScript dan CSS yang tidak digunakan sering berasal dari plugin dan tema. Banyak plugin memuat file di semua halaman, meskipun fiturnya hanya dipakai di satu halaman. Pembangun halaman visual juga cenderung menghasilkan DOM yang besar. Mengenali pola ini membantu Anda menemukan sumber masalah lebih cepat.

Saat membuka detail temuan, perhatikan alamat file yang tercantum. File dari folder plugin biasanya memiliki nama plugin di dalam alamatnya. Dari situ, Anda bisa mengetahui plugin mana yang paling membebani halaman. Pertimbangkan untuk menonaktifkan plugin yang tidak penting atau mencari alternatif yang lebih ringan. Beberapa plugin optimasi juga menyediakan fitur untuk menonaktifkan file tertentu di halaman yang tidak membutuhkannya.

Untuk temuan waktu respons server yang lambat, periksa apakah plugin caching sudah aktif dan berfungsi. Uji halaman dalam keadaan tidak masuk sebagai administrator, karena halaman untuk pengguna yang masuk biasanya tidak disimpan dalam cache. Jika waktu respons tetap lambat, masalahnya mungkin ada pada hosting atau basis data. Plugin pemantau kueri dapat membantu menemukan kueri yang lambat di lingkungan pengujian. Perbaikan di sisi server sering memberikan dampak paling besar untuk website WordPress.

## Menyampaikan Hasil Laporan kepada Klien atau Atasan

Bagi praktisi SEO atau pengembang, sering kali hasil PageSpeed Insights perlu dijelaskan kepada klien atau atasan yang tidak memiliki latar belakang teknis. Banyak klien hanya melihat angka skor dan merasa khawatir jika warnanya merah. Penjelasan yang baik membantu mereka memahami kondisi sebenarnya dan prioritas perbaikan. Komunikasi yang jelas juga mencegah ekspektasi yang tidak realistis. Berikut beberapa tips menyampaikan hasil laporan.

Mulailah dengan data pengguna nyata, bukan skor Lighthouse. Jelaskan apakah pengunjung saat ini mendapat pengalaman yang baik atau tidak. Gunakan bahasa sederhana, misalnya "konten utama muncul dalam waktu kurang dari tiga detik bagi sebagian besar pengunjung". Hubungkan masalah kinerja dengan dampak bisnis, seperti pengunjung yang meninggalkan halaman sebelum melihat produk. Penjelasan seperti ini lebih mudah dipahami daripada istilah teknis.

Sampaikan rencana perbaikan dalam bentuk prioritas yang jelas. Jelaskan perkiraan usaha dan dampak setiap perbaikan. Ingatkan bahwa skor laboratorium bisa berubah-ubah dan data pengguna nyata butuh waktu untuk berubah. Hindari menjanjikan skor tertentu, karena banyak faktor di luar kendali. Laporan berkala yang menunjukkan tren akan lebih meyakinkan daripada satu angka sesaat.

## Kesalahan Umum Saat Menggunakan PageSpeed Insights

**Mengejar skor 100 dengan segala cara.** Skor 100 bukan tujuan akhir. Beberapa orang menghapus fitur penting, seperti formulir kontak atau analitik, hanya demi skor sempurna. Ada juga yang menerapkan trik yang membuat skor naik tetapi pengalaman pengguna tidak berubah. Fokuslah pada pengalaman pengguna nyata yang tercermin dalam data lapangan. Skor yang cukup baik dengan fungsi lengkap lebih bernilai daripada skor sempurna dengan fungsi yang hilang.

**Hanya menguji beranda.** Beranda sering kali bukan halaman yang paling banyak dikunjungi dari mesin pencari. Pengunjung lebih sering masuk melalui halaman artikel, produk, atau kategori. Halaman-halaman tersebut bisa memiliki masalah yang sangat berbeda. Lakukan pengujian pada setiap jenis templat halaman yang penting. Gunakan laporan Search Console untuk menemukan kelompok halaman yang bermasalah.

**Membandingkan skor seluler dan desktop.** Kondisi pengujian seluler dan desktop sangat berbeda. Wajar jika skor seluler jauh lebih rendah. Membandingkan keduanya secara langsung tidak memberikan informasi yang berguna. Bandingkan skor seluler dengan skor seluler sebelumnya atau dengan pesaing. Prioritaskan perbaikan berdasarkan hasil seluler.

**Mengabaikan data pengguna nyata.** Banyak orang langsung melihat skor Lighthouse dan melewatkan bagian data pengguna nyata. Padahal, data pengguna nyata adalah yang digunakan dalam penilaian Core Web Vitals. Skor laboratorium yang rendah belum tentu berarti pengguna mengalami masalah. Sebaliknya, skor laboratorium yang tinggi belum tentu menjamin pengalaman pengguna baik. Selalu baca kedua bagian secara bersamaan.

**Menerapkan saran tanpa memahami konteksnya.** Tidak semua saran di laporan cocok untuk setiap website. Misalnya, saran untuk menunda JavaScript bisa merusak fungsi tertentu jika diterapkan sembarangan. Bacalah detail setiap temuan dan pahami dampaknya sebelum mengubah sesuatu. Uji perubahan di lingkungan pengujian terlebih dahulu. Perbaikan yang terburu-buru bisa menimbulkan masalah baru.

**Menyimpulkan dari satu pengujian.** Seperti dijelaskan sebelumnya, skor bisa berubah-ubah antarpengujian. Satu hasil pengujian tidak cukup untuk menyimpulkan apakah perubahan berhasil. Jalankan pengujian beberapa kali dan lihat nilai tengahnya. Catat hasilnya secara sistematis. Data yang konsisten lebih bisa dipercaya untuk pengambilan keputusan.

## Memantau Kinerja secara Berkelanjutan

Kinerja website tidak bersifat tetap. Penambahan fitur, plugin, konten, dan skrip baru bisa menurunkan kinerja secara perlahan. Tanpa pemantauan, penurunan ini sering baru disadari setelah cukup parah. Karena itu, pemantauan kinerja perlu dilakukan secara berkelanjutan. Ada beberapa cara untuk melakukannya.

Cara paling sederhana adalah memeriksa laporan Core Web Vitals di Search Console setiap bulan. Laporan ini akan menunjukkan jika ada kelompok halaman yang kinerjanya menurun. Untuk halaman penting, jalankan PageSpeed Insights secara berkala dan catat hasilnya. Bagi tim pengembang, Lighthouse dapat dijalankan secara otomatis setiap kali ada perubahan kode. Alat seperti Lighthouse CI dapat memberi peringatan jika kinerja menurun melewati batas tertentu.

Bagi website dengan trafik yang besar, pertimbangkan untuk mengumpulkan data kinerja dari pengguna nyata secara mandiri. Data ini bisa dikumpulkan dengan pustaka `web-vitals` dan dikirim ke sistem analitik. Dengan data sendiri, Anda bisa melihat kinerja per halaman, per perangkat, atau per wilayah. Data ini juga tersedia lebih cepat daripada agregat 28 hari di CrUX. Pemantauan yang baik membuat Anda bisa bertindak sebelum masalah berdampak besar.

## FAQ PageSpeed Insights

### Berapa skor PageSpeed Insights yang dianggap baik?

Skor kinerja 90 sampai 100 dianggap baik, 50 sampai 89 perlu peningkatan, dan di bawah 50 dianggap buruk. Namun, yang lebih penting adalah penilaian Core Web Vitals dari data pengguna nyata. Halaman dengan skor di bawah 90 tetap bisa memberikan pengalaman yang baik bagi pengguna.

### Mengapa skor seluler lebih rendah daripada desktop?

Pengujian seluler menyimulasikan perangkat kelas menengah dengan jaringan yang lebih lambat dan prosesor yang lebih terbatas. Kondisi ini jauh lebih berat daripada pengujian desktop. Karena itu, skor seluler hampir selalu lebih rendah dan sebaiknya dibandingkan dengan skor seluler juga.

### Apakah skor PageSpeed memengaruhi peringkat Google?

Skor Lighthouse tidak digunakan secara langsung dalam sistem peringkat Google. Yang dipertimbangkan sebagai bagian dari pengalaman halaman adalah data Core Web Vitals dari pengguna nyata. Meski begitu, relevansi dan kualitas konten tetap jauh lebih berpengaruh terhadap peringkat.

### Mengapa data pengguna nyata tidak muncul di laporan?

Data pengguna nyata hanya tersedia jika halaman atau website memiliki cukup banyak kunjungan dari pengguna Chrome. Website baru atau halaman yang jarang dikunjungi sering belum memiliki data ini. Dalam kondisi tersebut, gunakan data laboratorium sebagai panduan.

### Berapa lama perbaikan terlihat di PageSpeed Insights?

Hasil pengujian laboratorium langsung berubah setelah perbaikan diterapkan dan cache dibersihkan. Data pengguna nyata membutuhkan waktu hingga sekitar empat minggu untuk sepenuhnya mencerminkan perubahan. Hal ini karena data tersebut merupakan agregat dari 28 hari terakhir.

### Apakah perlu memperbaiki semua saran di laporan?

Tidak harus. Prioritaskan saran yang berkaitan dengan metrik yang bermasalah di data pengguna nyata dan memiliki perkiraan dampak terbesar. Beberapa saran mungkin tidak relevan atau terlalu berisiko untuk website tertentu. Pertimbangkan manfaat dan usahanya sebelum menerapkan.

### Apa perbedaan PageSpeed Insights dan Lighthouse?

Lighthouse adalah mesin pengujian otomatis yang juga tersedia di Chrome DevTools. PageSpeed Insights menjalankan Lighthouse dari server Google dan menambahkan data pengguna nyata dari CrUX. Karena itu, laporan PageSpeed Insights memberikan gambaran yang lebih lengkap.

### Apakah plugin optimasi bisa langsung menaikkan skor PageSpeed?

Plugin optimasi bisa membantu, misalnya dengan mengaktifkan caching, menunda JavaScript, dan mengoptimasi gambar. Namun, hasilnya sangat bergantung pada sumber masalah di website Anda. Uji setiap pengaturan dengan hati-hati karena optimasi yang terlalu agresif bisa merusak fungsi halaman.

## Kesimpulan

PageSpeed Insights adalah alat yang sangat berguna jika dibaca dengan benar. Mulailah dari bagian data pengguna nyata untuk mengetahui apakah halaman lulus penilaian Core Web Vitals. Gunakan skor dan metrik Lighthouse untuk mendiagnosis penyebab masalah, dengan memahami bahwa skor tersebut adalah hasil pengujian dalam kondisi simulasi. Pelajari daftar diagnostik dan prioritaskan temuan yang berkaitan dengan metrik bermasalah. Ingat bahwa skor bisa berubah-ubah, sehingga pengujian perlu dilakukan beberapa kali.

Tujuan akhirnya bukan skor sempurna, melainkan pengalaman yang baik bagi pengunjung nyata. Terapkan perbaikan secara bertahap, ukur dampaknya, dan pantau kinerja secara berkelanjutan. Untuk menindaklanjuti temuan tentang kecepatan server dan pengiriman file, pelajari artikel CDN. Jika temuan menunjukkan server lambat merespons karena basis data, lanjutkan dengan panduan optimasi database MySQL.
