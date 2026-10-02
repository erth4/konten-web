---
title: "Core Web Vitals: Arti LCP, INP, CLS dan Cara Memperbaikinya"
meta_description: "Pelajari Core Web Vitals (LCP, INP, CLS): ambang batas nilai, cara mengukur di PageSpeed Insights dan Search Console, serta cara memperbaikinya."
slug: "core-web-vitals-lcp-inp-cls"
focus_keyword: "Core Web Vitals"
keywords:
  - core web vitals
  - LCP adalah
  - INP adalah
  - CLS adalah
  - cara memperbaiki LCP
  - cara memperbaiki INP
  - cara memperbaiki CLS
  - page experience
  - pagespeed insights
category: "Performa"
tags: ["Performa Website", "Core Web Vitals", "SEO Teknis", "Web Development"]
date: "2026-10-02"
lang: "id"
---

# Core Web Vitals: Pengertian LCP, INP, CLS dan Cara Memperbaikinya

Pernahkah Anda membuka sebuah website, lalu tombol yang hendak diklik tiba-tiba bergeser karena ada iklan yang muncul? Atau mengetuk menu di ponsel, tetapi halaman diam saja selama beberapa saat? Pengalaman seperti ini menjengkelkan dan membuat banyak orang langsung menutup halaman. Google merangkum pengalaman-pengalaman tersebut ke dalam tiga metrik yang disebut **Core Web Vitals**. Metrik ini menjadi standar untuk menilai kualitas pengalaman pengguna di sebuah halaman web.

Panduan ini membahas Core Web Vitals secara lengkap, mulai dari pengertian hingga cara memperbaikinya. Anda akan memahami arti LCP, INP, dan CLS, ambang batas nilai yang dianggap baik, serta cara mengukurnya dengan alat yang tepat. Kami juga menguraikan penyebab umum skor yang buruk dan teknik perbaikan yang bisa langsung diterapkan. Artikel ini ditujukan untuk pemilik website, pengembang web, dan praktisi SEO. Pembahasannya disertai contoh kode sederhana agar mudah dipraktikkan.

## Daftar Isi

1. [Apa Itu Core Web Vitals?](#apa-itu-core-web-vitals)
2. [Mengapa Core Web Vitals Penting?](#mengapa-core-web-vitals-penting)
3. [Ambang Batas Nilai Core Web Vitals](#ambang-batas-nilai-core-web-vitals)
4. [Data Lapangan dan Data Laboratorium](#data-lapangan-dan-data-laboratorium)
5. [Alat untuk Mengukur Core Web Vitals](#alat-untuk-mengukur-core-web-vitals)
6. [LCP: Largest Contentful Paint](#lcp-largest-contentful-paint)
7. [INP: Interaction to Next Paint](#inp-interaction-to-next-paint)
8. [CLS: Cumulative Layout Shift](#cls-cumulative-layout-shift)
9. [Metrik Pendukung: TTFB, FCP, dan TBT](#metrik-pendukung-ttfb-fcp-dan-tbt)
10. [Alur Kerja Memperbaiki Core Web Vitals](#alur-kerja-memperbaiki-core-web-vitals)
11. [Core Web Vitals pada WordPress dan Framework JavaScript](#core-web-vitals-pada-wordpress-dan-framework-javascript)
12. [Kesalahan Umum Saat Mengoptimasi Core Web Vitals](#kesalahan-umum-saat-mengoptimasi-core-web-vitals)
13. [FAQ Core Web Vitals](#faq-core-web-vitals)
14. [Kesimpulan](#kesimpulan)

## Apa Itu Core Web Vitals?

Core Web Vitals adalah sekumpulan metrik dari Google untuk mengukur pengalaman pengguna saat memuat dan berinteraksi dengan halaman web. Metrik ini merupakan bagian dari inisiatif Web Vitals yang diperkenalkan Google untuk menyederhanakan cara menilai kualitas halaman. Sebelumnya, ada begitu banyak metrik kinerja sehingga pemilik website kesulitan menentukan mana yang paling penting. Core Web Vitals memilih beberapa metrik yang dianggap paling mewakili pengalaman nyata pengguna. Setiap metrik mengukur satu aspek yang berbeda.

Saat ini, Core Web Vitals terdiri dari tiga metrik. Metrik pertama adalah **Largest Contentful Paint (LCP)** yang mengukur kinerja pemuatan. Metrik kedua adalah **Interaction to Next Paint (INP)** yang mengukur responsivitas. Metrik ketiga adalah **Cumulative Layout Shift (CLS)** yang mengukur stabilitas visual. Ketiganya bersama-sama menjawab pertanyaan sederhana: apakah halaman cepat tampil, cepat merespons, dan tidak bergerak-gerak secara mengganggu?

Daftar metrik Core Web Vitals bisa berubah seiring perkembangan pemahaman tentang pengalaman pengguna. Perubahan terbesar sejauh ini terjadi pada Maret 2024. Saat itu, INP resmi menggantikan First Input Delay (FID) sebagai metrik responsivitas. FID hanya mengukur jeda pada interaksi pertama, sedangkan INP mengukur responsivitas di sepanjang kunjungan. Karena itu, INP dianggap lebih mewakili pengalaman nyata pengguna.

## Mengapa Core Web Vitals Penting?

Core Web Vitals penting karena berkaitan langsung dengan kenyamanan pengunjung. Halaman yang lambat tampil membuat pengunjung tidak sabar. Halaman yang lambat merespons membuat pengunjung mengira ada yang rusak. Halaman yang tata letaknya bergeser membuat pengunjung salah klik dan frustrasi. Semua pengalaman buruk ini dapat menurunkan kepercayaan dan membuat pengunjung pergi ke website lain.

Dari sisi SEO, Core Web Vitals merupakan bagian dari sinyal pengalaman halaman yang dipertimbangkan oleh sistem peringkat Google. Google menyatakan bahwa memiliki Core Web Vitals yang baik selaras dengan apa yang ingin dihargai oleh sistem peringkatnya. Namun, Google juga menegaskan bahwa relevansi dan kualitas konten tetap jauh lebih penting. Halaman dengan konten terbaik tetap bisa mendapat peringkat tinggi meskipun pengalaman halamannya belum sempurna. Jadi, Core Web Vitals bukan jalan pintas menuju peringkat pertama, melainkan salah satu faktor pendukung.

Dari sisi bisnis, pengalaman yang lebih baik sering berdampak pada konversi. Pengunjung yang nyaman cenderung membaca lebih banyak halaman, mengisi formulir, atau menyelesaikan pembelian. Banyak perusahaan telah mempublikasikan studi kasus tentang peningkatan bisnis setelah memperbaiki kinerja website. Hasil di setiap website tentu berbeda-beda. Namun, arah hubungannya cukup konsisten: pengalaman yang lebih baik cenderung menghasilkan keterlibatan yang lebih baik.

Bagi pasar Indonesia, faktor ini menjadi semakin penting. Sebagian besar pengguna mengakses internet melalui ponsel dengan spesifikasi dan kualitas jaringan yang beragam. Halaman yang terasa cepat di laptop kantor bisa terasa sangat lambat di ponsel kelas menengah dengan sinyal yang tidak stabil. Core Web Vitals diukur dari pengguna nyata, sehingga kondisi ini tercermin dalam nilai yang Anda dapatkan. Mengoptimasi Core Web Vitals berarti memperhatikan pengunjung yang perangkat dan jaringannya paling terbatas.

## Ambang Batas Nilai Core Web Vitals

Google menetapkan ambang batas untuk setiap metrik Core Web Vitals. Ambang batas ini membagi hasil pengukuran menjadi tiga kategori, yaitu Baik, Perlu Peningkatan, dan Buruk. Berikut tabel ambang batas yang berlaku saat ini.

| Metrik | Baik | Perlu Peningkatan | Buruk |
|---|---|---|---|
| LCP (Largest Contentful Paint) | ≤ 2,5 detik | > 2,5 detik hingga 4 detik | > 4 detik |
| INP (Interaction to Next Paint) | ≤ 200 milidetik | > 200 hingga 500 milidetik | > 500 milidetik |
| CLS (Cumulative Layout Shift) | ≤ 0,1 | > 0,1 hingga 0,25 | > 0,25 |

Ada satu hal penting dalam cara penilaiannya. Google menilai Core Web Vitals berdasarkan persentil ke-75 dari kunjungan halaman. Artinya, sebuah halaman dianggap memenuhi standar jika setidaknya 75 persen kunjungan mengalami nilai dalam kategori Baik. Pendekatan ini memastikan bahwa sebagian besar pengguna mendapat pengalaman yang baik, bukan hanya pengguna dengan perangkat tercepat. Penilaian juga dipisahkan antara perangkat seluler dan desktop.

Sebuah halaman dianggap lulus penilaian Core Web Vitals jika ketiga metrik berada dalam kategori Baik. Jika satu metrik saja berada di kategori Perlu Peningkatan atau Buruk, halaman tersebut belum lulus. Karena itu, penting untuk memperhatikan ketiga metrik secara seimbang. Memperbaiki satu metrik hingga sempurna tidak akan cukup jika metrik lain masih buruk. Prioritaskan metrik yang nilainya paling jauh dari ambang batas.

## Data Lapangan dan Data Laboratorium

Sebelum mulai mengukur, Anda perlu memahami dua jenis data kinerja. Jenis pertama adalah data lapangan atau *field data*. Jenis kedua adalah data laboratorium atau *lab data*. Keduanya sama-sama berguna, tetapi memiliki fungsi yang berbeda. Banyak kebingungan seputar Core Web Vitals berasal dari ketidakpahaman tentang perbedaan ini.

### Data Lapangan

Data lapangan dikumpulkan dari pengguna nyata yang mengunjungi website Anda. Data ini mencerminkan beragam perangkat, jaringan, lokasi, dan cara pengguna berinteraksi. Sumber data lapangan yang paling dikenal adalah Chrome User Experience Report atau CrUX. CrUX mengumpulkan data dari pengguna Chrome yang menyetujui berbagi data penggunaan. Data inilah yang digunakan Google untuk menilai Core Web Vitals sebuah halaman.

Data CrUX yang ditampilkan di PageSpeed Insights merupakan agregat dari periode 28 hari terakhir. Akibatnya, perbaikan yang Anda lakukan hari ini tidak akan langsung terlihat di data lapangan. Butuh waktu hingga beberapa minggu sampai data baru sepenuhnya menggantikan data lama. Hal ini sering membuat pemilik website mengira perbaikannya tidak berhasil. Bersabarlah dan pantau perubahan secara bertahap.

Data lapangan juga hanya tersedia jika halaman atau website memiliki cukup banyak kunjungan. Website baru atau halaman yang jarang dikunjungi sering tidak memiliki data CrUX. Dalam kondisi ini, PageSpeed Insights mungkin menampilkan data tingkat domain atau tidak menampilkan data lapangan sama sekali. Anda masih bisa mengumpulkan data lapangan sendiri dengan memasang skrip pengukuran di website. Cara ini akan dibahas di bagian alat ukur.

### Data Laboratorium

Data laboratorium dihasilkan dari pengujian dalam lingkungan yang terkendali. Alat seperti Lighthouse memuat halaman menggunakan perangkat dan jaringan yang disimulasikan. Hasilnya konsisten dan dapat diulang, sehingga sangat cocok untuk mendiagnosis masalah. Anda bisa langsung melihat efek dari setiap perubahan yang dilakukan. Data laboratorium juga dilengkapi saran perbaikan yang spesifik.

Kelemahannya, data laboratorium tidak selalu mencerminkan pengalaman nyata pengguna. Simulasi menggunakan satu jenis perangkat dan jaringan, sedangkan pengguna nyata sangat beragam. Selain itu, pengujian laboratorium biasanya hanya memuat halaman tanpa melakukan interaksi. Karena itu, INP tidak bisa diukur langsung di Lighthouse. Sebagai gantinya, Lighthouse menggunakan metrik *Total Blocking Time* (TBT) sebagai indikator yang berkaitan dengan responsivitas.

### Mengapa Nilai Keduanya Bisa Berbeda?

Sangat wajar jika nilai di data lapangan dan data laboratorium berbeda. Misalnya, Lighthouse menunjukkan LCP 4 detik, sedangkan data lapangan menunjukkan 2 detik. Perbedaan ini bisa terjadi karena pengguna nyata banyak yang mengunjungi halaman dengan *cache* yang sudah tersimpan. Bisa juga karena mayoritas pengguna Anda memiliki perangkat yang lebih cepat daripada simulasi. Sebaliknya, data lapangan bisa lebih buruk jika banyak pengguna memakai ponsel lama dengan jaringan lambat.

Prinsip yang perlu dipegang adalah sebagai berikut. Gunakan data lapangan untuk mengetahui apakah ada masalah dan seberapa besar dampaknya bagi pengguna. Gunakan data laboratorium untuk mencari tahu penyebab masalah dan menguji perbaikan. Jangan mengejar skor Lighthouse 100 jika data lapangan sudah menunjukkan nilai Baik. Fokuslah pada pengalaman pengguna nyata, karena itulah yang dinilai oleh Google.

## Alat untuk Mengukur Core Web Vitals

Ada banyak alat yang bisa digunakan untuk mengukur Core Web Vitals. Sebagian besar disediakan secara gratis oleh Google. Setiap alat memiliki kegunaan yang berbeda dalam alur kerja optimasi. Anda tidak harus menggunakan semuanya. Pilih alat yang sesuai dengan kebutuhan dan tahap pekerjaan Anda.

**PageSpeed Insights.** Ini adalah alat paling populer untuk memeriksa kinerja satu halaman. Cukup masukkan URL, lalu PageSpeed Insights akan menampilkan data lapangan dari CrUX dan data laboratorium dari Lighthouse. Bagian atas laporan menunjukkan apakah halaman lulus penilaian Core Web Vitals. Bagian bawah menampilkan skor kinerja Lighthouse dan daftar saran perbaikan. Alat ini cocok untuk pemeriksaan cepat dan mendapatkan gambaran awal.

**Laporan Core Web Vitals di Search Console.** Laporan ini menampilkan status Core Web Vitals untuk seluruh website, bukan hanya satu halaman. Halaman-halaman dengan masalah serupa dikelompokkan bersama. Dengan begitu, Anda bisa melihat pola, misalnya semua halaman artikel memiliki masalah CLS yang sama. Laporan ini dipisahkan antara perangkat seluler dan desktop. Setelah memperbaiki masalah, Anda bisa meminta Google memvalidasi perbaikan tersebut.

**Lighthouse di Chrome DevTools.** Lighthouse tersedia langsung di dalam browser Chrome melalui DevTools. Alat ini menjalankan audit kinerja, aksesibilitas, praktik terbaik, dan SEO. Hasilnya bisa diulang berkali-kali saat Anda melakukan perubahan di lingkungan pengembangan. Sebaiknya jalankan Lighthouse di jendela penyamaran agar ekstensi browser tidak memengaruhi hasil. Jalankan juga beberapa kali dan lihat nilai tengahnya, karena hasil bisa sedikit berbeda setiap kali.

**Panel Performance di Chrome DevTools.** Panel ini memberikan analisis paling mendalam tentang apa yang terjadi selama halaman dimuat dan saat pengguna berinteraksi. Anda bisa melihat urutan pemuatan sumber daya, tugas JavaScript yang panjang, dan proses rendering. Versi terbaru panel ini juga menampilkan metrik Core Web Vitals secara langsung saat Anda berinteraksi dengan halaman. Fitur ini sangat berguna untuk mendiagnosis masalah INP. Panel ini memang terlihat rumit bagi pemula, tetapi sangat berharga untuk dipelajari.

**Pustaka web-vitals.** Google menyediakan pustaka JavaScript bernama `web-vitals` untuk mengukur Core Web Vitals dari pengguna nyata. Pustaka ini berukuran kecil dan mudah dipasang. Anda bisa mengirimkan hasil pengukuran ke Google Analytics atau sistem analitik lain. Dengan cara ini, Anda memiliki data lapangan sendiri yang lebih rinci daripada CrUX. Data tersebut juga bisa dipecah berdasarkan halaman, perangkat, atau negara.

Berikut contoh sederhana penggunaan pustaka `web-vitals`:

```js
import { onLCP, onINP, onCLS } from 'web-vitals';

function kirimKeAnalitik(metrik) {
  const data = JSON.stringify({
    nama: metrik.name,
    nilai: metrik.value,
    rating: metrik.rating,
    id: metrik.id,
    halaman: location.pathname,
  });
  // sendBeacon tetap terkirim meskipun pengguna menutup halaman
  navigator.sendBeacon('/api/web-vitals', data);
}

onLCP(kirimKeAnalitik);
onINP(kirimKeAnalitik);
onCLS(kirimKeAnalitik);
```

**WebPageTest dan alat pihak ketiga.** WebPageTest memungkinkan pengujian dari berbagai lokasi, browser, dan kecepatan jaringan. Alat ini menampilkan *waterfall* yang sangat rinci serta rekaman visual proses pemuatan halaman. Anda bisa membandingkan beberapa versi halaman secara berdampingan. Ada juga layanan pemantauan berbayar yang mengumpulkan data pengguna nyata secara terus-menerus. Layanan seperti ini cocok untuk website dengan trafik besar dan kebutuhan pemantauan yang serius.

## LCP: Largest Contentful Paint

### Pengertian LCP

Largest Contentful Paint atau LCP mengukur waktu yang dibutuhkan hingga elemen konten terbesar di area layar pertama selesai ditampilkan. Area layar pertama adalah bagian halaman yang terlihat tanpa perlu menggulir. Elemen terbesar ini biasanya adalah gambar utama, gambar sampul artikel, atau blok teks besar seperti judul. LCP dipilih karena cukup mewakili kapan pengguna merasa konten utama halaman sudah muncul. Semakin cepat LCP, semakin cepat pengguna merasa halaman sudah siap dibaca.

Elemen yang dapat dihitung sebagai LCP meliputi elemen gambar, gambar di dalam SVG, gambar sampul video, dan elemen dengan gambar latar yang dimuat melalui CSS. Elemen teks berukuran besar seperti paragraf atau judul juga bisa menjadi elemen LCP. Browser terus memperbarui kandidat LCP selama halaman dimuat. Begitu pengguna mulai berinteraksi, misalnya menggulir atau mengetuk, pencatatan LCP berhenti. Elemen terakhir yang tercatat sebagai yang terbesar menjadi elemen LCP halaman tersebut.

Langkah pertama memperbaiki LCP adalah mengetahui elemen mana yang menjadi elemen LCP. PageSpeed Insights menampilkan informasi ini di bagian diagnostik. Panel Performance di Chrome DevTools juga menandai elemen LCP pada rekaman pemuatan. Elemen LCP bisa berbeda antara tampilan seluler dan desktop. Pastikan Anda memeriksa keduanya.

### Empat Bagian Penyusun LCP

Waktu LCP dapat dipecah menjadi empat bagian. Memahami keempat bagian ini membantu Anda menemukan di mana waktu paling banyak terbuang. Bagian pertama adalah *Time to First Byte* (TTFB), yaitu waktu sampai byte pertama dokumen HTML diterima browser. Bagian kedua adalah jeda pemuatan sumber daya, yaitu waktu antara TTFB dan saat browser mulai mengunduh gambar LCP. Bagian ketiga adalah durasi pemuatan sumber daya, yaitu lamanya gambar LCP diunduh.

Bagian keempat adalah jeda rendering elemen. Ini adalah waktu antara selesainya pengunduhan gambar dan saat gambar benar-benar tampil di layar. Jeda ini bisa terjadi karena browser masih menunggu CSS atau JavaScript yang memblokir rendering. Untuk elemen LCP berupa teks, bagian kedua dan ketiga tidak berlaku. Pada kasus ini, LCP terutama dipengaruhi oleh TTFB, pemuatan font, dan sumber daya yang memblokir rendering. Panel Performance di Chrome DevTools dapat menampilkan rincian keempat bagian ini.

### Penyebab Umum LCP Lambat

**Server lambat merespons.** Jika server membutuhkan waktu lama untuk mengirim HTML, semua proses lain ikut tertunda. TTFB yang tinggi sering disebabkan oleh hosting yang kurang memadai, kueri basis data yang berat, atau tidak adanya *caching*. Jarak fisik antara server dan pengguna juga berpengaruh. Server yang berada jauh dari Indonesia akan menambah latensi bagi pengguna Indonesia. Masalah ini paling terasa pada website yang dirender secara dinamis di setiap permintaan.

**Gambar LCP ditemukan terlambat.** Browser hanya bisa mengunduh gambar setelah menemukannya. Jika gambar LCP dimuat melalui JavaScript atau sebagai gambar latar CSS, browser menemukannya lebih lambat. Masalah serupa terjadi jika gambar LCP diberi atribut `loading="lazy"`. Atribut tersebut menunda pemuatan hingga gambar dekat dengan area pandang. Untuk gambar di area layar pertama, penundaan ini justru merugikan.

**Ukuran gambar terlalu besar.** Gambar beresolusi tinggi yang tidak dikompres membutuhkan waktu lama untuk diunduh. Masalah ini sangat terasa pada jaringan seluler yang lambat. Banyak website mengunggah foto langsung dari kamera tanpa mengubah ukurannya. Akibatnya, gambar berukuran beberapa megabita ditampilkan di layar ponsel yang kecil. Panduan lengkap mengatasi masalah ini ada di artikel [optimasi gambar website](/optimasi-gambar-website/).

**Sumber daya yang memblokir rendering.** File CSS dan JavaScript tertentu harus diunduh dan diproses sebelum browser bisa menampilkan konten. File CSS yang besar dan banyak skrip sinkron di bagian `<head>` akan menunda tampilan halaman. Bahkan jika gambar LCP sudah selesai diunduh, gambar itu belum bisa tampil sampai sumber daya ini selesai diproses. Hal ini menyebabkan jeda rendering elemen yang panjang. Mengurangi dan menunda sumber daya yang tidak penting dapat mempercepat LCP secara signifikan.

**Rendering di sisi klien.** Pada aplikasi yang sepenuhnya dirender di sisi klien, HTML awal hampir kosong. Konten baru muncul setelah JavaScript diunduh, dijalankan, dan mengambil data dari API. Rangkaian proses ini memperpanjang waktu hingga elemen LCP tampil. Masalah ini sering terjadi pada aplikasi satu halaman. Solusinya biasanya adalah merender konten utama di sisi server atau saat proses build.

### Cara Memperbaiki LCP

**1. Kurangi TTFB.** Gunakan hosting yang memadai dan aktifkan *caching* halaman di sisi server. Gunakan CDN agar konten dikirim dari server yang dekat dengan pengguna. Optimalkan kueri basis data yang lambat dan kurangi proses berat saat membangun halaman. Untuk website yang kontennya jarang berubah, pertimbangkan pembuatan halaman statis. Pembahasan lengkapnya ada di artikel [cara mempercepat loading website](/cara-mempercepat-loading-website/).

**2. Buat gambar LCP mudah ditemukan.** Tuliskan gambar LCP sebagai elemen `<img>` biasa di HTML awal, bukan dimuat melalui JavaScript. Jika gambar LCP harus berupa gambar latar CSS, gunakan petunjuk *preload* agar browser mengunduhnya lebih awal. Jangan memberi atribut `loading="lazy"` pada gambar di area layar pertama. Atribut tersebut sebaiknya hanya digunakan untuk gambar di bagian bawah halaman. Langkah sederhana ini sering memberikan perbaikan yang besar.

**3. Prioritaskan gambar LCP.** Tambahkan atribut `fetchpriority="high"` pada gambar LCP. Atribut ini memberi tahu browser bahwa gambar tersebut penting dan harus diunduh lebih dulu. Secara bawaan, browser sering memberi prioritas rendah pada gambar sampai tata letak selesai dihitung. Dengan petunjuk prioritas, gambar LCP bisa mulai diunduh lebih cepat. Gunakan atribut ini secukupnya, cukup untuk satu atau dua gambar terpenting.

```html
<img
  src="/gambar/sampul-artikel-1200.webp"
  srcset="/gambar/sampul-artikel-600.webp 600w,
          /gambar/sampul-artikel-1200.webp 1200w"
  sizes="(max-width: 768px) 100vw, 768px"
  width="1200" height="630"
  alt="Grafik perbandingan nilai LCP sebelum dan sesudah optimasi"
  fetchpriority="high">
```

**4. Kecilkan ukuran gambar.** Gunakan format modern seperti WebP atau AVIF yang menghasilkan file lebih kecil. Sesuaikan dimensi gambar dengan ukuran tampilannya di layar. Sediakan beberapa ukuran gambar dengan atribut `srcset` agar perangkat kecil mengunduh versi yang lebih kecil. Kompres gambar dengan tingkat kualitas yang masih nyaman dilihat. Semua langkah ini mengurangi durasi pemuatan sumber daya.

**5. Kurangi sumber daya yang memblokir rendering.** Pisahkan CSS yang dibutuhkan untuk area layar pertama, lalu tanam langsung di HTML. Muat sisa CSS secara tidak memblokir. Tambahkan atribut `defer` atau `async` pada skrip yang tidak dibutuhkan untuk tampilan awal. Hapus CSS dan JavaScript yang tidak digunakan. Langkah ini mengurangi jeda rendering elemen.

**6. Gunakan rendering di sisi server atau statis.** Untuk aplikasi berbasis framework JavaScript, render konten utama di server atau saat build. Dengan begitu, HTML awal sudah berisi elemen LCP. Browser dapat langsung menampilkannya tanpa menunggu JavaScript. Framework modern seperti Next.js, Nuxt, dan SvelteKit menyediakan mode rendering ini secara bawaan. Pilih mode yang sesuai untuk setiap jenis halaman.

**7. Optimalkan pemuatan font untuk LCP berbasis teks.** Jika elemen LCP berupa teks, font kustom bisa menunda tampilannya. Gunakan properti `font-display: swap` atau `optional` agar teks tetap tampil dengan font cadangan. Lakukan *preload* untuk file font yang paling penting. Gunakan format WOFF2 dan batasi jumlah varian font. Pertimbangkan juga menggunakan font sistem untuk teks utama.

## INP: Interaction to Next Paint

### Pengertian INP

Interaction to Next Paint atau INP mengukur seberapa cepat halaman merespons interaksi pengguna. Interaksi yang dihitung meliputi klik mouse, ketukan di layar sentuh, dan penekanan tombol keyboard. Menggulir halaman dan mengarahkan kursor tidak dihitung sebagai interaksi untuk INP. INP mengukur waktu dari saat pengguna berinteraksi hingga browser menampilkan perubahan visual berikutnya. Perubahan visual ini adalah umpan balik yang menunjukkan bahwa interaksi telah diterima.

INP memperhatikan hampir semua interaksi yang terjadi selama kunjungan, bukan hanya interaksi pertama. Nilai yang dilaporkan biasanya adalah interaksi dengan jeda terlama. Pada halaman dengan sangat banyak interaksi, beberapa nilai ekstrem diabaikan agar satu kejadian aneh tidak mendominasi. Pendekatan ini membuat INP lebih mencerminkan pengalaman keseluruhan. Halaman yang cepat di awal tetapi lambat setelah pengguna membuka menu atau mengisi formulir akan tetap terdeteksi.

Contoh pengalaman dengan INP buruk sangat mudah dikenali. Pengguna mengetuk tombol "Tambah ke Keranjang", tetapi tidak ada yang terjadi selama hampir satu detik. Pengguna mengetik di kolom pencarian, tetapi huruf-huruf muncul tersendat. Pengguna membuka menu, tetapi menu baru terbuka setelah jeda yang terasa. Dalam semua kasus ini, pengguna sering mengetuk berkali-kali karena mengira ketukan pertama tidak berhasil. Akibatnya, aksi bisa terjadi dua kali atau pengguna menjadi frustrasi.

### Tiga Bagian Penyusun INP

Waktu INP terdiri dari tiga bagian. Bagian pertama adalah jeda input, yaitu waktu dari interaksi hingga *event handler* mulai berjalan. Jeda ini terjadi jika *main thread* browser sedang sibuk mengerjakan tugas lain ketika pengguna berinteraksi. Bagian kedua adalah waktu pemrosesan, yaitu lamanya kode *event handler* dijalankan. Bagian ketiga adalah jeda presentasi, yaitu waktu yang dibutuhkan browser untuk menghitung tata letak dan menggambar perubahan di layar.

Masing-masing bagian membutuhkan pendekatan perbaikan yang berbeda. Jeda input yang panjang menandakan ada tugas lain yang terlalu lama memblokir *main thread*. Waktu pemrosesan yang panjang menandakan kode *event handler* terlalu berat. Jeda presentasi yang panjang menandakan perubahan tampilan terlalu kompleks atau DOM terlalu besar. Panel Performance di Chrome DevTools dapat menunjukkan rincian ketiga bagian ini untuk setiap interaksi. Identifikasi bagian mana yang paling dominan sebelum memilih solusi.

### Memahami Main Thread dan Long Task

Untuk memahami INP, Anda perlu memahami konsep *main thread*. Browser menjalankan sebagian besar pekerjaan halaman di satu jalur utama ini. Pekerjaan tersebut meliputi menjalankan JavaScript, menghitung gaya, menyusun tata letak, dan merespons interaksi pengguna. Karena hanya ada satu jalur, browser tidak bisa merespons interaksi jika jalur tersebut sedang sibuk. Interaksi pengguna harus menunggu hingga tugas yang sedang berjalan selesai.

Tugas yang berjalan lebih dari 50 milidetik disebut *long task* atau tugas panjang. Selama tugas panjang berjalan, halaman tidak dapat merespons interaksi. Semakin banyak dan semakin lama tugas panjang, semakin besar peluang interaksi pengguna tertunda. Tugas panjang biasanya berasal dari JavaScript yang berat. Sumbernya bisa kode milik sendiri, framework, atau skrip pihak ketiga seperti iklan dan analitik.

### Penyebab Umum INP Buruk

**JavaScript yang terlalu banyak.** Semakin banyak JavaScript yang dimuat, semakin banyak pekerjaan yang harus dilakukan *main thread*. Banyak website memuat pustaka besar meskipun hanya menggunakan sebagian kecil fiturnya. Plugin dan widget yang menumpuk juga menambah beban. Pada ponsel kelas menengah, pemrosesan JavaScript bisa beberapa kali lebih lambat daripada di laptop. Inilah alasan INP sering jauh lebih buruk di perangkat seluler.

**Skrip pihak ketiga.** Skrip iklan, pelacak analitik, widget obrolan, dan tombol media sosial sering menjalankan tugas berat. Pemilik website tidak memiliki kendali penuh atas kode skrip tersebut. Satu skrip pihak ketiga yang buruk bisa merusak INP seluruh halaman. Tinjau setiap skrip pihak ketiga dan tanyakan apakah manfaatnya sepadan dengan biayanya. Hapus skrip yang tidak lagi digunakan.

**Event handler yang terlalu berat.** Kode yang dijalankan saat pengguna mengklik sering melakukan terlalu banyak pekerjaan sekaligus. Misalnya, memperbarui banyak bagian halaman, memproses data besar, atau mengirim beberapa permintaan sinkron. Semua pekerjaan itu dilakukan sebelum browser sempat menampilkan umpan balik. Akibatnya, pengguna melihat jeda yang panjang. Pekerjaan yang tidak mendesak sebaiknya ditunda setelah umpan balik visual ditampilkan.

**DOM yang terlalu besar.** DOM adalah struktur elemen HTML di halaman. Semakin banyak elemen, semakin lama browser menghitung gaya dan tata letak setiap kali ada perubahan. Halaman dengan ribuan elemen, seperti daftar produk yang sangat panjang, rentan mengalami jeda presentasi yang tinggi. Kode yang membaca dan mengubah tata letak secara bergantian juga memperburuk masalah. Pola ini dikenal sebagai *layout thrashing*.

### Cara Memperbaiki INP

**1. Pecah tugas panjang.** Bagi pekerjaan besar menjadi potongan-potongan kecil. Setelah setiap potongan selesai, beri kesempatan kepada browser untuk merespons interaksi. Teknik ini disebut *yielding* atau menyerahkan kendali ke *main thread*. Browser modern menyediakan `scheduler.yield()` untuk keperluan ini. Untuk browser yang belum mendukungnya, gunakan `setTimeout` sebagai cadangan.

```js
function serahkanKendali() {
  if ('scheduler' in window && 'yield' in scheduler) {
    return scheduler.yield();
  }
  return new Promise((resolve) => setTimeout(resolve, 0));
}

async function prosesBanyakItem(daftarItem) {
  for (const item of daftarItem) {
    prosesSatuItem(item);
    // beri kesempatan browser merespons klik atau ketikan pengguna
    await serahkanKendali();
  }
}
```

**2. Tampilkan umpan balik lebih dulu.** Saat pengguna mengklik tombol, segera tampilkan perubahan visual sederhana. Contohnya adalah mengubah status tombol menjadi "memproses" atau menampilkan indikator pemuatan. Setelah itu, jalankan pekerjaan berat secara terpisah. Dengan cara ini, pengguna langsung tahu bahwa interaksinya diterima. Nilai INP pun membaik karena perubahan visual terjadi lebih cepat.

**3. Kurangi JavaScript.** Hapus pustaka dan kode yang tidak digunakan. Gunakan teknik *code splitting* agar setiap halaman hanya memuat kode yang benar-benar dibutuhkan. Muat komponen yang jarang digunakan hanya saat diperlukan. Pertimbangkan alternatif yang lebih ringan untuk pustaka besar. Setiap kilobita JavaScript yang dihapus berarti lebih sedikit pekerjaan bagi *main thread*.

**4. Kendalikan skrip pihak ketiga.** Muat skrip pihak ketiga dengan atribut `async` atau `defer`. Tunda pemuatan widget yang tidak dibutuhkan di awal, misalnya widget obrolan, hingga pengguna benar-benar membutuhkannya. Gunakan teknik *facade*, yaitu menampilkan tampilan statis yang ringan dan baru memuat widget asli saat diklik. Teknik ini sering dipakai untuk video YouTube yang disematkan. Audit skrip pihak ketiga secara berkala.

**5. Batasi frekuensi event handler.** Untuk interaksi yang terjadi berulang kali dengan cepat, seperti mengetik di kolom pencarian, gunakan teknik *debounce*. Teknik ini menunda eksekusi kode sampai pengguna berhenti mengetik sejenak. Dengan begitu, pencarian tidak dijalankan pada setiap ketukan tombol. Beban *main thread* berkurang dan interaksi terasa lebih lancar. Teknik serupa bernama *throttle* juga bisa digunakan untuk membatasi frekuensi eksekusi.

**6. Perkecil DOM dan sederhanakan rendering.** Kurangi jumlah elemen HTML yang tidak perlu. Untuk daftar yang sangat panjang, gunakan teknik *virtualization* yang hanya merender item yang terlihat di layar. Properti CSS `content-visibility: auto` dapat membantu browser melewati rendering bagian halaman yang belum terlihat. Hindari membaca dan menulis tata letak secara bergantian dalam satu tugas. Kelompokkan pembacaan tata letak terlebih dahulu, lalu lakukan perubahan setelahnya.

**7. Pindahkan pekerjaan berat ke Web Worker.** Web Worker memungkinkan JavaScript berjalan di jalur terpisah dari *main thread*. Pekerjaan seperti memproses data besar atau melakukan perhitungan rumit bisa dipindahkan ke sana. Dengan begitu, *main thread* tetap bebas merespons interaksi pengguna. Web Worker tidak bisa mengakses DOM secara langsung. Karena itu, teknik ini paling cocok untuk pekerjaan komputasi murni.

## CLS: Cumulative Layout Shift

### Pengertian CLS

Cumulative Layout Shift atau CLS mengukur seberapa sering dan seberapa besar elemen halaman bergeser secara tidak terduga. Pergeseran tata letak terjadi ketika elemen yang sudah terlihat tiba-tiba berpindah posisi. Contohnya adalah teks yang turun karena ada gambar yang baru dimuat di atasnya. Contoh lain adalah tombol yang bergeser karena muncul banner iklan. Pergeseran seperti ini mengganggu pembacaan dan bisa menyebabkan pengguna salah klik.

Berbeda dengan LCP dan INP, nilai CLS tidak diukur dalam satuan waktu. CLS adalah skor tanpa satuan yang dihitung dari dua faktor. Faktor pertama adalah seberapa besar area layar yang terdampak pergeseran. Faktor kedua adalah seberapa jauh elemen tersebut bergeser. Semakin besar area dan semakin jauh pergeserannya, semakin tinggi skor CLS.

Pergeseran tata letak bisa terjadi berkali-kali selama kunjungan. Untuk menghitungnya, pergeseran dikelompokkan ke dalam jendela sesi. Satu jendela sesi berisi pergeseran yang terjadi berdekatan, dengan jeda kurang dari satu detik dan durasi total paling lama lima detik. Nilai CLS yang dilaporkan adalah jendela sesi dengan skor tertinggi. Cara ini membuat CLS tetap adil untuk halaman yang dibuka dalam waktu lama.

Tidak semua pergeseran dihitung dalam CLS. Pergeseran yang terjadi dalam waktu singkat setelah interaksi pengguna dianggap wajar dan tidak dihitung. Contohnya adalah menu yang terbuka setelah tombol diklik, sehingga konten di bawahnya bergeser. Pergeseran semacam itu adalah respons yang diharapkan pengguna. Yang dihitung adalah pergeseran yang terjadi tanpa diduga, terutama saat halaman sedang dimuat.

### Penyebab Umum CLS Tinggi

**Gambar dan video tanpa dimensi.** Jika gambar tidak memiliki atribut lebar dan tinggi, browser tidak tahu berapa ruang yang harus disediakan. Browser awalnya menampilkan teks tanpa ruang untuk gambar. Ketika gambar selesai dimuat, teks di bawahnya terdorong ke bawah. Ini adalah penyebab CLS yang paling umum dan paling mudah diperbaiki. Masalah yang sama berlaku untuk video dan elemen `<iframe>`.

**Iklan, sematan, dan iframe tanpa ruang tetap.** Slot iklan sering dimuat belakangan dan ukurannya bisa berubah-ubah. Jika tidak ada ruang yang disiapkan, kemunculan iklan akan menggeser konten. Hal yang sama terjadi pada sematan media sosial, peta, dan video dari pihak ketiga. Elemen-elemen ini sering dimuat terakhir. Akibatnya, pergeseran terjadi ketika pengguna sudah mulai membaca.

**Konten yang disisipkan secara dinamis.** Banner promosi, pemberitahuan cookie, atau ajakan berlangganan yang muncul di bagian atas halaman sering menyebabkan pergeseran. Konten seperti ini biasanya disisipkan oleh JavaScript setelah halaman tampil. Jika disisipkan di atas konten yang sudah terlihat, semua konten di bawahnya akan terdorong. Masalah serupa terjadi pada konten yang dimuat dari API, seperti daftar produk rekomendasi. Tanpa ruang yang disiapkan, kemunculannya akan menggeser tata letak.

**Font web yang menyebabkan perubahan ukuran teks.** Saat font kustom selesai dimuat, browser mengganti font cadangan dengan font kustom. Jika ukuran kedua font berbeda, teks bisa berubah lebar dan tinggi. Perubahan ini menggeser elemen di sekitarnya. Pergeseran akibat font biasanya kecil, tetapi bisa menumpuk di halaman dengan banyak teks. Masalah ini sering terlewat karena hanya terlihat pada kunjungan pertama sebelum font tersimpan di *cache*.

**Animasi yang mengubah tata letak.** Animasi yang mengubah properti seperti `top`, `left`, `width`, atau `height` memicu perhitungan ulang tata letak. Perubahan ini bisa dihitung sebagai pergeseran tata letak. Animasi seperti ini juga lebih berat bagi browser. Gunakan properti `transform` dan `opacity` untuk animasi. Kedua properti tersebut tidak memengaruhi tata letak elemen lain.

### Cara Memperbaiki CLS

**1. Selalu tentukan dimensi gambar dan video.** Tambahkan atribut `width` dan `height` pada setiap elemen gambar dan video. Browser modern akan menggunakan atribut tersebut untuk menghitung rasio aspek dan menyediakan ruang sebelum gambar dimuat. Gambar tetap bisa responsif dengan menambahkan CSS `height: auto` dan lebar maksimum. Alternatif lain adalah menggunakan properti CSS `aspect-ratio`. Langkah ini saja sering menyelesaikan sebagian besar masalah CLS.

```html
<img src="/gambar/produk.webp" width="800" height="600" alt="Sepatu lari warna biru tampak samping">

<style>
  img { max-width: 100%; height: auto; }
  .video-wrapper { aspect-ratio: 16 / 9; }
</style>
```

**2. Siapkan ruang untuk iklan dan sematan.** Tentukan tinggi minimum untuk slot iklan berdasarkan ukuran iklan yang paling sering tampil. Jika iklan tidak terisi, biarkan ruang tetap ada atau tampilkan konten pengganti. Jangan menciutkan slot iklan yang kosong setelah halaman tampil. Hindari menempatkan iklan di bagian paling atas halaman karena dampak pergeserannya paling besar. Lakukan hal yang sama untuk sematan media sosial dan peta.

**3. Hindari menyisipkan konten di atas konten yang sudah tampil.** Tempatkan banner dan pemberitahuan di posisi yang tidak menggeser konten, misalnya sebagai lapisan di bagian bawah layar. Jika konten harus muncul di bagian atas, siapkan ruangnya sejak awal. Untuk konten yang dimuat dari API, gunakan kerangka pemuatan (*skeleton*) dengan ukuran yang mendekati ukuran akhir. Dengan begitu, kemunculan konten tidak menggeser elemen lain. Prinsipnya adalah ruang harus sudah ada sebelum kontennya datang.

**4. Kelola pemuatan font.** Gunakan `font-display: optional` jika Anda ingin menghindari pergantian font sama sekali. Opsi ini menggunakan font cadangan jika font kustom tidak dimuat cukup cepat. Lakukan *preload* untuk font penting agar lebih cepat tersedia. Gunakan juga properti `size-adjust` dan sejenisnya untuk menyesuaikan ukuran font cadangan agar mendekati font kustom. Dengan begitu, pergantian font tidak menyebabkan perubahan ukuran teks yang berarti.

**5. Gunakan transform untuk animasi.** Ganti animasi yang mengubah posisi atau ukuran dengan animasi berbasis `transform`. Misalnya, gunakan `transform: translateY()` alih-alih mengubah properti `top`. Animasi berbasis `transform` diproses lebih efisien oleh browser. Animasi ini juga tidak memicu perhitungan ulang tata letak elemen lain. Hasilnya, animasi terasa lebih halus dan CLS tidak bertambah.

**6. Manfaatkan back/forward cache.** Browser modern memiliki fitur *back/forward cache* yang menyimpan halaman secara utuh di memori. Saat pengguna menekan tombol kembali, halaman ditampilkan langsung dari memori tanpa dimuat ulang. Fitur ini menghilangkan pergeseran tata letak yang biasanya terjadi saat halaman dimuat ulang. Beberapa praktik dapat membuat halaman tidak memenuhi syarat untuk fitur ini, misalnya penggunaan *event* `unload`. Panel Application di Chrome DevTools dapat menguji apakah halaman Anda memenuhi syarat.

## Metrik Pendukung: TTFB, FCP, dan TBT

Selain tiga metrik utama, ada beberapa metrik pendukung yang membantu mendiagnosis masalah. Metrik-metrik ini bukan bagian dari Core Web Vitals. Namun, metrik ini sering menjadi petunjuk tentang penyebab nilai Core Web Vitals yang buruk. Memahaminya akan membuat proses diagnosis lebih cepat. Berikut tiga metrik pendukung yang paling penting.

**Time to First Byte (TTFB).** TTFB mengukur waktu dari saat permintaan dikirim hingga byte pertama respons diterima. Metrik ini mencakup waktu pengalihan, pencarian DNS, koneksi, dan pemrosesan di server. TTFB yang tinggi akan menunda semua metrik lain, termasuk LCP. Metrik ini sangat dipengaruhi oleh kualitas hosting, *caching*, dan jarak ke server. Perbaiki TTFB terlebih dahulu jika nilainya tinggi.

**First Contentful Paint (FCP).** FCP mengukur waktu hingga konten pertama, seperti teks atau gambar, muncul di layar. Metrik ini menunjukkan kapan pengguna pertama kali melihat tanda bahwa halaman sedang dimuat. FCP yang lambat biasanya disebabkan oleh TTFB tinggi atau sumber daya yang memblokir rendering. Jarak antara FCP dan LCP juga memberi petunjuk. Jika jaraknya jauh, kemungkinan masalah ada pada pemuatan elemen LCP itu sendiri.

**Total Blocking Time (TBT).** TBT mengukur total waktu *main thread* terblokir oleh tugas panjang selama proses pemuatan. Metrik ini diukur di lingkungan laboratorium seperti Lighthouse. TBT tidak sama dengan INP, tetapi keduanya sama-sama dipengaruhi oleh JavaScript yang berat. TBT yang tinggi menandakan risiko INP yang buruk. Gunakan TBT sebagai panduan saat menguji perbaikan di lingkungan pengembangan.

## Alur Kerja Memperbaiki Core Web Vitals

Memperbaiki Core Web Vitals akan lebih efektif jika dilakukan dengan alur kerja yang terstruktur. Banyak tim langsung mencoba berbagai teknik tanpa mengetahui penyebab masalah. Akibatnya, waktu terbuang untuk perbaikan yang tidak berdampak. Alur kerja berikut membantu Anda bekerja secara sistematis. Ulangi alur ini setiap kali ada masalah baru.

**Langkah 1: Identifikasi halaman yang bermasalah.** Buka laporan Core Web Vitals di Search Console. Lihat kelompok halaman dengan status Buruk atau Perlu Peningkatan, dimulai dari perangkat seluler. Catat metrik mana yang bermasalah di setiap kelompok. Pilih contoh URL dari setiap kelompok untuk dianalisis lebih lanjut. Prioritaskan kelompok halaman dengan trafik terbesar.

**Langkah 2: Konfirmasi dengan data lapangan.** Periksa contoh URL di PageSpeed Insights untuk melihat data lapangan yang lebih rinci. Jika Anda memasang pustaka `web-vitals`, gunakan data tersebut untuk melihat pola yang lebih spesifik. Perhatikan apakah masalah terjadi di semua perangkat atau hanya pada kondisi tertentu. Data dari analitik sendiri juga bisa menunjukkan elemen atau interaksi mana yang paling bermasalah. Informasi ini mempersempit area pencarian penyebab.

**Langkah 3: Diagnosis dengan data laboratorium.** Jalankan Lighthouse dan panel Performance di Chrome DevTools untuk contoh URL tersebut. Aktifkan simulasi CPU dan jaringan yang lebih lambat agar kondisinya mendekati perangkat pengguna. Untuk LCP, identifikasi elemen LCP dan lihat bagian mana dari keempat bagian penyusunnya yang paling lama. Untuk INP, rekam interaksi yang lambat dan lihat apakah masalahnya pada jeda input, pemrosesan, atau presentasi. Untuk CLS, gunakan fitur penanda pergeseran tata letak untuk melihat elemen yang bergeser.

**Langkah 4: Terapkan perbaikan yang paling berdampak.** Mulailah dari perbaikan yang paling besar dampaknya dan paling mudah diterapkan. Contohnya adalah menambahkan dimensi gambar, menghapus atribut `loading="lazy"` dari gambar LCP, atau menunda skrip pihak ketiga. Uji setiap perbaikan di lingkungan pengembangan sebelum diterapkan ke website utama. Lakukan perubahan secara bertahap agar efeknya bisa diukur. Catat setiap perubahan beserta tanggal penerapannya.

**Langkah 5: Validasi dan pantau.** Setelah perbaikan diterapkan, klik tombol validasi di laporan Core Web Vitals Search Console. Google akan memantau halaman-halaman terkait selama sekitar 28 hari. Selama periode tersebut, pantau juga data dari analitik Anda sendiri. Jika nilai membaik secara konsisten, validasi akan berhasil. Jika tidak, ulangi proses diagnosis untuk mencari penyebab lain.

**Langkah 6: Cegah kemunduran.** Kinerja website cenderung memburuk seiring waktu karena penambahan fitur, plugin, dan skrip. Tetapkan anggaran kinerja (*performance budget*), misalnya batas ukuran JavaScript atau jumlah permintaan per halaman. Jalankan Lighthouse secara otomatis dalam proses integrasi berkelanjutan jika memungkinkan. Tinjau dampak kinerja setiap kali ada skrip atau fitur baru yang akan ditambahkan. Pencegahan jauh lebih murah daripada perbaikan.

## Core Web Vitals pada WordPress dan Framework JavaScript

### WordPress

WordPress adalah CMS yang paling banyak digunakan, sehingga banyak website menghadapi tantangan Core Web Vitals yang serupa. Penyebab umum masalah di WordPress adalah tema yang berat, terlalu banyak plugin, dan hosting yang kurang memadai. Banyak tema memuat CSS dan JavaScript untuk semua fitur di setiap halaman, meskipun fitur tersebut tidak digunakan. Pembangun halaman (*page builder*) juga sering menghasilkan HTML yang sangat besar. Semua ini berdampak pada LCP dan INP.

Mulailah dengan memilih tema yang ringan dan dikenal memiliki kinerja yang baik. Kurangi jumlah plugin dan hapus plugin yang tidak lagi digunakan. Gunakan plugin *caching* untuk menyajikan halaman statis kepada pengunjung. Plugin optimasi dapat membantu menunda JavaScript, menggabungkan CSS penting, dan mengoptimasi gambar. Namun, uji setiap pengaturan dengan hati-hati karena optimasi yang terlalu agresif bisa merusak tampilan atau fungsi website.

WordPress versi modern juga sudah menyertakan beberapa optimasi bawaan. Contohnya adalah atribut `loading="lazy"` otomatis untuk gambar dan atribut `fetchpriority="high"` untuk gambar yang diperkirakan menjadi elemen LCP. Pastikan versi WordPress, tema, dan plugin selalu diperbarui agar mendapat manfaat dari optimasi terbaru. Gunakan versi PHP yang masih didukung karena versi baru biasanya lebih cepat. Pilih hosting dengan server yang dekat dengan mayoritas pengunjung Anda.

### Framework JavaScript

Website yang dibangun dengan framework seperti Next.js, Nuxt, SvelteKit, atau Vue memiliki tantangan yang berbeda. Masalah utama biasanya terletak pada jumlah JavaScript yang dikirim ke browser. Proses *hydration*, yaitu saat framework menghidupkan kembali halaman yang dirender di server, bisa memblokir *main thread*. Akibatnya, INP bisa buruk meskipun LCP sudah baik. Halaman yang dirender sepenuhnya di sisi klien juga cenderung memiliki LCP yang lambat.

Gunakan rendering di sisi server atau pembuatan halaman statis untuk halaman yang mengutamakan konten. Manfaatkan fitur *code splitting* bawaan framework agar setiap rute hanya memuat kode yang dibutuhkan. Gunakan komponen gambar bawaan framework, seperti `next/image` di Next.js, yang otomatis mengatur ukuran dan format gambar. Pertimbangkan pendekatan yang mengurangi JavaScript di sisi klien, seperti komponen server atau arsitektur *islands*. Ukur dampak setiap dependensi baru sebelum menambahkannya ke proyek.

## Kesalahan Umum Saat Mengoptimasi Core Web Vitals

**Hanya mengejar skor Lighthouse.** Skor Lighthouse adalah data laboratorium, bukan nilai yang digunakan untuk menilai Core Web Vitals. Mendapatkan skor 100 di Lighthouse tidak menjamin data lapangan juga baik. Sebaliknya, skor yang kurang sempurna tidak selalu berarti pengguna mengalami masalah. Fokuslah pada data lapangan dari pengguna nyata. Gunakan Lighthouse sebagai alat diagnosis, bukan sebagai tujuan akhir.

**Menguji hanya di perangkat yang cepat.** Pengembang biasanya menggunakan laptop atau ponsel kelas atas dengan koneksi yang stabil. Kondisi ini sangat berbeda dengan sebagian besar pengguna. Masalah yang tidak terlihat di perangkat pengembang bisa sangat terasa di ponsel kelas menengah. Gunakan simulasi CPU yang lebih lambat di DevTools saat menguji. Jika memungkinkan, uji langsung di ponsel yang mewakili perangkat mayoritas pengguna Anda.

**Memasang lazy load pada semua gambar.** Lazy load sangat berguna untuk gambar di bagian bawah halaman. Namun, memasangnya pada gambar di area layar pertama justru memperlambat LCP. Beberapa plugin dan tema menerapkan lazy load ke semua gambar tanpa pengecualian. Periksa pengaturan tersebut dan kecualikan gambar utama. Perbedaan kecil ini bisa berdampak besar pada nilai LCP.

**Mengabaikan skrip pihak ketiga.** Banyak tim fokus mengoptimasi kode sendiri, tetapi melupakan skrip pihak ketiga. Padahal, skrip iklan, analitik, dan widget sering menjadi penyumbang terbesar masalah INP. Buat daftar semua skrip pihak ketiga beserta tujuannya. Hapus yang tidak lagi dibutuhkan dan tunda pemuatan yang tidak mendesak. Diskusikan dengan tim pemasaran agar keputusan menambah skrip mempertimbangkan dampak kinerja.

**Tidak sabar menunggu data lapangan.** Data lapangan CrUX merupakan agregat 28 hari. Perbaikan yang dilakukan hari ini membutuhkan waktu untuk tercermin sepenuhnya. Banyak pemilik website mengubah strategi terlalu cepat karena mengira perbaikan tidak berhasil. Gunakan data analitik sendiri untuk melihat dampak lebih cepat. Bersabarlah dan pantau tren dalam beberapa minggu.

## FAQ Core Web Vitals

### Apa saja yang termasuk Core Web Vitals?

Core Web Vitals terdiri dari tiga metrik, yaitu Largest Contentful Paint (LCP), Interaction to Next Paint (INP), dan Cumulative Layout Shift (CLS). LCP mengukur kecepatan tampil konten utama. INP mengukur responsivitas terhadap interaksi, sedangkan CLS mengukur stabilitas tata letak.

### Berapa nilai Core Web Vitals yang dianggap baik?

Nilai yang dianggap baik adalah LCP paling lama 2,5 detik, INP paling lama 200 milidetik, dan CLS paling tinggi 0,1. Penilaian didasarkan pada persentil ke-75 dari kunjungan halaman. Ketiga metrik harus berada di kategori Baik agar halaman lulus penilaian.

### Apakah Core Web Vitals memengaruhi peringkat Google?

Core Web Vitals merupakan bagian dari sinyal pengalaman halaman yang dipertimbangkan oleh sistem peringkat Google. Namun, relevansi dan kualitas konten tetap jauh lebih berpengaruh. Core Web Vitals yang baik bermanfaat, tetapi tidak bisa menggantikan konten yang bagus.

### Apa perbedaan INP dan FID?

FID hanya mengukur jeda input pada interaksi pertama pengguna. INP mengukur seluruh waktu hingga perubahan visual berikutnya, dan memperhatikan hampir semua interaksi selama kunjungan. INP menggantikan FID sebagai metrik Core Web Vitals pada Maret 2024.

### Mengapa skor PageSpeed Insights saya berubah-ubah?

Skor kinerja Lighthouse di PageSpeed Insights bisa berbeda setiap kali diuji karena kondisi jaringan dan server berubah-ubah. Perbedaan kecil adalah hal yang wajar. Jalankan pengujian beberapa kali dan perhatikan data lapangan yang lebih stabil.

### Mengapa data lapangan tidak tersedia untuk website saya?

Data lapangan CrUX hanya tersedia jika halaman atau website memiliki cukup banyak kunjungan dari pengguna Chrome. Website baru atau halaman dengan trafik kecil sering belum memiliki data ini. Anda bisa memasang pustaka `web-vitals` untuk mengumpulkan data lapangan sendiri.

## Kesimpulan

Core Web Vitals adalah tiga metrik yang mengukur pengalaman pengguna dari sisi kecepatan tampil, responsivitas, dan stabilitas visual. LCP sebaiknya di bawah 2,5 detik, INP di bawah 200 milidetik, dan CLS di bawah 0,1, diukur pada persentil ke-75 kunjungan. Gunakan data lapangan untuk mengetahui kondisi nyata pengguna, dan data laboratorium untuk mendiagnosis penyebab masalah. Setiap metrik memiliki penyebab dan solusi yang berbeda, sehingga diagnosis yang tepat menjadi kunci. Perbaikan yang paling sering berdampak besar adalah mempercepat server, memprioritaskan gambar utama, mengurangi JavaScript, dan menyediakan ruang untuk setiap elemen.

Ingat bahwa tujuan akhirnya adalah pengalaman pengguna yang baik, bukan sekadar angka yang hijau. Website yang cepat dan stabil membuat pengunjung lebih nyaman dan lebih mungkin kembali. Untuk langkah teknis yang lebih luas, baca panduan [cara mempercepat loading website](/cara-mempercepat-loading-website/). Karena gambar sering menjadi elemen LCP, pelajari juga teknik [optimasi gambar website](/optimasi-gambar-website/) agar halaman Anda tampil lebih cepat di semua perangkat.
