---
title: "Optimasi Database MySQL: Cara Mempercepat Query Website"
meta_description: "Panduan optimasi database MySQL untuk website: membaca EXPLAIN, membuat index yang tepat, menemukan query lambat, paginasi efisien, dan pengaturan InnoDB."
slug: "optimasi-database-mysql"
focus_keyword: "optimasi database MySQL"
keywords:
  - optimasi database mysql
  - mempercepat query mysql
  - index mysql
  - explain mysql
  - slow query log
  - query lambat
  - optimasi mysql wordpress
  - innodb buffer pool
category: "Performa"
tags: ["Performa Website", "MySQL", "Database", "PHP"]
date: "2026-10-02"
lang: "id"
---

# Optimasi Database MySQL: Cara Menemukan dan Mempercepat Query yang Lambat

Website dinamis hampir selalu bergantung pada basis data. Setiap kali pengunjung membuka halaman artikel, daftar produk, atau riwayat pesanan, aplikasi mengambil data dari basis data. Jika pengambilan data itu lambat, seluruh halaman ikut lambat. Pengunjung harus menunggu sebelum browser menerima apa pun dari server. Itulah sebabnya basis data yang lambat sering menjadi penyebab tersembunyi di balik waktu respons server yang tinggi.

Panduan ini membahas **optimasi database MySQL** dari sudut pandang pengembang dan pengelola website. Anda akan belajar cara menemukan query yang lambat, membaca hasil `EXPLAIN`, dan membuat index yang benar-benar membantu. Kami juga membahas pola query yang sering menjadi masalah, seperti query di dalam perulangan dan paginasi dengan offset besar. Selain itu, ada pembahasan tentang pengaturan InnoDB, caching, dan kasus khusus di WordPress. Contoh kode menggunakan PHP dan PDO, tetapi prinsipnya berlaku untuk bahasa pemrograman lain.

## Daftar Isi

1. [Mengapa Basis Data Memengaruhi Kecepatan Website?](#mengapa-basis-data-memengaruhi-kecepatan-website)
2. [Langkah Pertama: Ukur Sebelum Mengoptimasi](#langkah-pertama-ukur-sebelum-mengoptimasi)
3. [Membaca Hasil EXPLAIN](#membaca-hasil-explain)
4. [Memahami dan Membuat Index yang Tepat](#memahami-dan-membuat-index-yang-tepat)
5. [Memperbaiki Pola Query yang Bermasalah](#memperbaiki-pola-query-yang-bermasalah)
6. [Merancang Skema Tabel yang Efisien](#merancang-skema-tabel-yang-efisien)
7. [Mengatur Konfigurasi MySQL dan InnoDB](#mengatur-konfigurasi-mysql-dan-innodb)
8. [Menambahkan Lapisan Cache](#menambahkan-lapisan-cache)
9. [Optimasi Database untuk WordPress](#optimasi-database-untuk-wordpress)
10. [Keamanan dan Optimasi Berjalan Bersama](#keamanan-dan-optimasi-berjalan-bersama)
11. [Perawatan Rutin Basis Data](#perawatan-rutin-basis-data)
12. [Jenis Index Lain yang Perlu Diketahui](#jenis-index-lain-yang-perlu-diketahui)
13. [Transaksi dan Penguncian](#transaksi-dan-penguncian)
14. [Mengelola Koneksi dari Aplikasi PHP](#mengelola-koneksi-dari-aplikasi-php)
15. [Replikasi untuk Beban Baca yang Besar](#replikasi-untuk-beban-baca-yang-besar)
16. [Memantau Kesehatan Server Basis Data](#memantau-kesehatan-server-basis-data)
17. [Kesalahan Umum dalam Optimasi Database](#kesalahan-umum-dalam-optimasi-database)
18. [Mengoptimasi JOIN dan Subquery](#mengoptimasi-join-dan-subquery)
19. [Contoh Kasus Optimasi](#contoh-kasus-optimasi)
20. [Checklist Optimasi Database MySQL](#checklist-optimasi-database-mysql)
21. [FAQ Optimasi Database MySQL](#faq-optimasi-database-mysql)
22. [Kesimpulan](#kesimpulan)

## Mengapa Basis Data Memengaruhi Kecepatan Website?

Ketika pengunjung meminta sebuah halaman dinamis, server menjalankan kode aplikasi untuk membangun halaman tersebut. Di tengah proses itu, aplikasi biasanya mengirim beberapa query ke basis data. Server tidak bisa mengirim halaman sebelum semua data yang dibutuhkan tersedia. Jika satu query membutuhkan waktu satu detik, pengunjung harus menunggu setidaknya satu detik. Jika ada puluhan query yang masing-masing lambat, waktu tunggu bisa menjadi sangat panjang.

Masalah basis data juga cenderung memburuk seiring waktu. Query yang cepat saat tabel berisi seribu baris bisa menjadi sangat lambat ketika tabel berisi jutaan baris. Website yang awalnya terasa cepat perlahan menjadi lambat tanpa ada perubahan kode. Pemilik website sering mengira masalahnya ada pada hosting, padahal penyebabnya adalah query yang tidak efisien. Mengoptimasi basis data sejak dini mencegah masalah ini.

Basis data yang lambat juga memengaruhi kapasitas server secara keseluruhan. Query berat memakan prosesor, memori, dan akses disk. Saat banyak pengunjung datang bersamaan, query-query tersebut saling berebut sumber daya. Akibatnya, semua permintaan menjadi lambat, termasuk yang sebenarnya ringan. Dalam kondisi terburuk, server basis data bisa kewalahan dan website tidak dapat diakses.

Dari sisi pengalaman pengguna, dampak basis data terlihat pada metrik *Time to First Byte*. Metrik ini mengukur waktu hingga browser menerima byte pertama dari server. TTFB yang tinggi akan menunda semua tahap berikutnya, termasuk tampilnya konten utama. Penjelasan tentang metrik ini dapat dibaca di artikel Core Web Vitals. Caching halaman dan CDN memang bisa menutupi masalah ini untuk halaman publik, tetapi halaman dinamis tetap bergantung pada kecepatan basis data.

## Langkah Pertama: Ukur Sebelum Mengoptimasi

Kesalahan paling umum dalam optimasi basis data adalah menebak-nebak. Banyak pengembang langsung menambahkan index atau mengubah konfigurasi tanpa mengetahui query mana yang sebenarnya lambat. Hasilnya, waktu terbuang untuk mengoptimasi query yang tidak bermasalah. Bahkan, perubahan yang keliru bisa memperlambat bagian lain dari aplikasi. Karena itu, langkah pertama selalu mengukur.

### Mengaktifkan Slow Query Log

MySQL menyediakan fitur *slow query log* untuk mencatat query yang berjalan lebih lama dari batas tertentu. Fitur ini adalah alat paling dasar untuk menemukan query bermasalah. Anda dapat mengaktifkannya melalui file konfigurasi atau secara langsung dengan perintah SQL. Tentukan batas waktu dengan variabel `long_query_time`, misalnya satu detik atau kurang. Query yang melebihi batas tersebut akan dicatat ke dalam file log.

```sql
-- Aktifkan slow query log tanpa restart (berlaku sampai server dimulai ulang)
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 0.5;
SET GLOBAL slow_query_log_file = '/var/log/mysql/mysql-slow.log';

-- Opsional: catat juga query yang tidak menggunakan index
SET GLOBAL log_queries_not_using_indexes = 'ON';
```

Agar pengaturan tetap berlaku setelah server dimulai ulang, tambahkan pengaturan yang sama ke file konfigurasi MySQL. Perhatikan bahwa mencatat terlalu banyak query bisa menghasilkan file log yang sangat besar. Gunakan batas waktu yang wajar dan pantau ukuran file log. Pengaturan `log_queries_not_using_indexes` sebaiknya diaktifkan sementara saja karena bisa mencatat banyak query kecil. Setelah data terkumpul, analisis log tersebut untuk menemukan pola.

### Menganalisis Log

File slow query log bisa sangat panjang dan sulit dibaca secara manual. Alat seperti `mysqldumpslow` yang disertakan dengan MySQL dapat meringkas log berdasarkan pola query. Alat lain yang populer adalah `pt-query-digest` dari Percona Toolkit. Alat-alat ini mengelompokkan query yang mirip dan menghitung total waktu yang dihabiskan. Fokuskan perhatian pada query yang paling banyak menghabiskan waktu secara total.

Perlu diingat bahwa query paling lambat belum tentu yang paling penting untuk diperbaiki. Query yang membutuhkan lima detik tetapi hanya dijalankan sekali sehari mungkin kurang berdampak. Sebaliknya, query yang membutuhkan 50 milidetik tetapi dijalankan ribuan kali per menit bisa menjadi beban utama. Karena itu, lihatlah total waktu, yaitu durasi dikalikan frekuensi. Prioritaskan query dengan total waktu terbesar.

### Memantau dari Sisi Aplikasi

Selain dari sisi basis data, pemantauan juga bisa dilakukan dari sisi aplikasi. Banyak framework menyediakan alat untuk menampilkan daftar query yang dijalankan setiap halaman beserta durasinya. Di WordPress, plugin pemantau query dapat menampilkan informasi serupa di lingkungan pengembangan. Layanan pemantauan aplikasi juga dapat melacak query lambat di lingkungan produksi. Pendekatan ini membantu mengetahui halaman mana yang menjalankan query bermasalah.

## Membaca Hasil EXPLAIN

Setelah menemukan query yang lambat, langkah berikutnya adalah memahami mengapa query tersebut lambat. MySQL menyediakan perintah `EXPLAIN` untuk menampilkan rencana eksekusi sebuah query. Rencana ini menunjukkan bagaimana MySQL akan mencari data, index mana yang digunakan, dan berapa banyak baris yang diperkirakan diperiksa. Dengan membaca hasil `EXPLAIN`, Anda bisa mengetahui sumber masalah. Cukup tambahkan kata `EXPLAIN` di depan query yang ingin dianalisis.

```sql
EXPLAIN
SELECT id, total, dibuat_pada
FROM pesanan
WHERE pelanggan_id = 1024
ORDER BY dibuat_pada DESC
LIMIT 20;
```

Hasil `EXPLAIN` ditampilkan dalam bentuk tabel dengan beberapa kolom. Tidak semua kolom sama pentingnya bagi pemula. Fokuslah pada beberapa kolom utama yang paling sering mengungkap masalah. Kolom-kolom tersebut adalah `type`, `possible_keys`, `key`, `rows`, dan `Extra`. Berikut penjelasan setiap kolom tersebut.

**Kolom type.** Kolom ini menunjukkan cara MySQL mengakses tabel. Nilai `ALL` berarti MySQL memindai seluruh tabel dari awal hingga akhir, yang sangat lambat untuk tabel besar. Nilai `index` berarti MySQL memindai seluruh index, yang sedikit lebih baik tetapi tetap bisa berat. Nilai `range` berarti MySQL hanya memindai rentang tertentu dari index. Nilai `ref`, `eq_ref`, dan `const` menunjukkan akses yang sangat efisien menggunakan index.

**Kolom possible_keys dan key.** Kolom `possible_keys` menunjukkan index yang bisa digunakan untuk query tersebut. Kolom `key` menunjukkan index yang benar-benar dipilih oleh MySQL. Jika `key` bernilai kosong, artinya MySQL tidak menggunakan index sama sekali. Kondisi ini sering menjadi penyebab utama query lambat. Jika `possible_keys` berisi beberapa pilihan tetapi `key` kosong, MySQL mungkin menilai index tidak cukup membantu.

**Kolom rows.** Kolom ini menunjukkan perkiraan jumlah baris yang harus diperiksa MySQL. Angka yang sangat besar dibanding jumlah baris yang dikembalikan menandakan query tidak efisien. Misalnya, query yang hanya mengembalikan 20 baris tetapi memeriksa satu juta baris jelas perlu diperbaiki. Perlu diingat bahwa angka ini adalah perkiraan berdasarkan statistik tabel. Statistik yang usang bisa membuat perkiraan kurang akurat.

**Kolom Extra.** Kolom ini berisi informasi tambahan tentang cara query dijalankan. Nilai `Using index` adalah kabar baik karena MySQL bisa menjawab query hanya dari index tanpa membaca tabel. Nilai `Using filesort` berarti MySQL harus mengurutkan hasil secara terpisah karena tidak bisa memanfaatkan urutan index. Nilai `Using temporary` berarti MySQL membuat tabel sementara, biasanya untuk `GROUP BY` atau `DISTINCT`. Kedua nilai terakhir bukan selalu masalah, tetapi patut diperhatikan pada query yang lambat.

### EXPLAIN ANALYZE

MySQL versi 8.0 menyediakan perintah `EXPLAIN ANALYZE` yang benar-benar menjalankan query dan menampilkan waktu nyata setiap tahap. Berbeda dengan `EXPLAIN` biasa yang hanya menampilkan perkiraan, perintah ini menunjukkan berapa lama setiap langkah sebenarnya berlangsung. Informasi ini sangat membantu untuk menemukan bagian query yang paling lambat. Karena query benar-benar dijalankan, berhati-hatilah menggunakannya pada query yang mengubah data. Gunakan pada query `SELECT` di lingkungan pengujian jika memungkinkan.

## Memahami dan Membuat Index yang Tepat

Index adalah struktur data yang membantu MySQL menemukan baris dengan cepat tanpa memindai seluruh tabel. Cara kerjanya mirip dengan indeks di bagian belakang buku. Daripada membaca seluruh buku untuk mencari sebuah istilah, Anda melihat indeks untuk mengetahui halamannya. Pada mesin penyimpanan InnoDB, sebagian besar index menggunakan struktur B-tree yang menyimpan nilai secara berurutan. Struktur ini sangat efisien untuk pencarian nilai tertentu, rentang nilai, dan pengurutan.

### Kolom Mana yang Perlu Diberi Index?

Kolom yang sering digunakan dalam klausa `WHERE`, `JOIN`, dan `ORDER BY` adalah kandidat utama untuk diberi index. Contohnya adalah kolom kunci asing seperti `pelanggan_id`, kolom status, atau kolom tanggal. Kolom yang memiliki banyak nilai unik biasanya lebih bermanfaat diberi index. Kolom dengan sangat sedikit variasi nilai, seperti kolom jenis kelamin, jarang bermanfaat jika diberi index sendirian. Namun, kolom seperti itu bisa berguna sebagai bagian dari index gabungan.

Jangan memberi index pada semua kolom secara membabi buta. Setiap index memakan ruang penyimpanan dan harus diperbarui setiap kali data ditambah, diubah, atau dihapus. Terlalu banyak index akan memperlambat operasi tulis. Index yang tidak pernah digunakan juga hanya menjadi beban. Buatlah index berdasarkan pola query yang benar-benar dijalankan aplikasi.

### Index Gabungan dan Aturan Prefiks Kiri

Index gabungan atau *composite index* adalah index yang mencakup lebih dari satu kolom. Index ini sangat berguna untuk query yang memfilter dan mengurutkan berdasarkan beberapa kolom sekaligus. Urutan kolom di dalam index gabungan sangat penting. MySQL dapat menggunakan index gabungan mulai dari kolom paling kiri. Prinsip ini dikenal sebagai aturan prefiks kiri.

Misalnya, terdapat index gabungan pada kolom `(pelanggan_id, dibuat_pada)`. Index ini dapat digunakan untuk query yang memfilter berdasarkan `pelanggan_id` saja. Index ini juga dapat digunakan untuk query yang memfilter berdasarkan `pelanggan_id` dan mengurutkan berdasarkan `dibuat_pada`. Namun, index ini tidak efektif untuk query yang hanya memfilter berdasarkan `dibuat_pada`. Karena itu, susun urutan kolom berdasarkan pola query yang paling sering digunakan.

```sql
-- Index gabungan untuk query riwayat pesanan per pelanggan
ALTER TABLE pesanan
  ADD INDEX idx_pelanggan_tanggal (pelanggan_id, dibuat_pada);
```

Sebagai panduan umum, letakkan kolom yang difilter dengan kesamaan nilai di bagian kiri. Setelah itu, letakkan kolom yang digunakan untuk rentang nilai atau pengurutan. Pada contoh di atas, `pelanggan_id` difilter dengan tanda sama dengan, sedangkan `dibuat_pada` digunakan untuk pengurutan. Susunan ini memungkinkan MySQL langsung menemukan pesanan milik pelanggan tertentu dalam urutan tanggal. Hasilnya, tidak diperlukan pengurutan tambahan yang mahal.

### Covering Index

*Covering index* adalah index yang memuat semua kolom yang dibutuhkan sebuah query. Dengan covering index, MySQL dapat menjawab query hanya dengan membaca index, tanpa membaca baris data di tabel. Hal ini ditunjukkan dengan keterangan `Using index` di kolom `Extra` hasil `EXPLAIN`. Covering index sangat efektif untuk query yang sering dijalankan dan hanya membutuhkan sedikit kolom. Namun, menambahkan terlalu banyak kolom ke index akan memperbesar ukurannya.

### Kondisi yang Membuat Index Tidak Terpakai

Ada beberapa pola penulisan query yang membuat MySQL tidak dapat menggunakan index dengan efektif. Pola-pola ini cukup umum dan sering tidak disadari oleh pengembang. Mengenalinya membantu Anda menulis query yang lebih efisien. Berikut beberapa pola yang perlu dihindari. Setiap pola disertai alternatif yang lebih baik.

**Menggunakan fungsi pada kolom yang diindeks.** Query seperti `WHERE YEAR(dibuat_pada) = 2025` membuat MySQL harus menghitung fungsi untuk setiap baris. Akibatnya, index pada `dibuat_pada` tidak bisa dimanfaatkan secara langsung. Alternatifnya, tulis kondisi sebagai rentang, misalnya `WHERE dibuat_pada >= '2025-01-01' AND dibuat_pada < '2026-01-01'`. Dengan rentang seperti ini, MySQL dapat menggunakan index secara efisien. Prinsip yang sama berlaku untuk fungsi lain seperti `DATE()` atau `LOWER()`.

**Pencarian dengan wildcard di awal.** Kondisi `LIKE '%kopi'` atau `LIKE '%kopi%'` tidak dapat memanfaatkan index B-tree biasa. MySQL harus memeriksa setiap nilai untuk menemukan kecocokan. Sebaliknya, `LIKE 'kopi%'` masih bisa menggunakan index karena awalan sudah diketahui. Untuk pencarian teks bebas, pertimbangkan index `FULLTEXT` atau mesin pencari khusus. Pilihan ini jauh lebih efisien untuk fitur pencarian.

**Perbedaan tipe data.** Jika kolom bertipe teks tetapi dibandingkan dengan angka, MySQL mungkin perlu mengonversi nilai di setiap baris. Konversi ini dapat mencegah penggunaan index. Contohnya adalah kolom nomor telepon bertipe `VARCHAR` yang dibandingkan dengan angka tanpa tanda kutip. Pastikan tipe data nilai pembanding sama dengan tipe data kolom. Gunakan *prepared statement* dengan tipe parameter yang tepat.

**Kondisi OR pada kolom berbeda.** Kondisi seperti `WHERE email = ? OR telepon = ?` kadang membuat MySQL kesulitan memilih index. Pada beberapa kasus, MySQL dapat menggabungkan dua index, tetapi tidak selalu efisien. Alternatifnya, pecah menjadi dua query yang digabungkan dengan `UNION`. Setiap bagian dapat menggunakan index masing-masing. Periksa hasil `EXPLAIN` untuk memastikan pendekatan mana yang lebih baik.

## Memperbaiki Pola Query yang Bermasalah

Selain index, cara aplikasi menulis dan menjalankan query sangat memengaruhi kinerja. Banyak masalah kinerja berasal dari pola query yang tidak efisien, bukan dari kurangnya index. Pola-pola ini sering muncul tanpa disadari, terutama saat menggunakan ORM atau pustaka yang menyembunyikan query sebenarnya. Mengenali pola bermasalah membantu Anda memperbaikinya sejak tahap pengembangan. Berikut pola-pola yang paling sering ditemui.

### Hindari SELECT *

Query `SELECT *` mengambil semua kolom dari tabel, padahal aplikasi sering hanya membutuhkan beberapa kolom. Kolom yang tidak diperlukan tetap harus dibaca, dikirim melalui jaringan, dan disimpan di memori aplikasi. Jika tabel memiliki kolom teks panjang, seperti isi artikel atau deskripsi produk, bebannya menjadi cukup besar. Selain itu, `SELECT *` mencegah MySQL memanfaatkan covering index. Sebutkan kolom yang benar-benar dibutuhkan secara eksplisit.

### Atasi Masalah N+1

Masalah N+1 terjadi ketika aplikasi menjalankan satu query untuk mengambil daftar data, lalu menjalankan satu query tambahan untuk setiap item dalam daftar tersebut. Contohnya, aplikasi mengambil 50 artikel, lalu menjalankan 50 query terpisah untuk mengambil nama penulis setiap artikel. Total query menjadi 51, padahal bisa diselesaikan dengan satu atau dua query saja. Masalah ini sering muncul saat menggunakan ORM dengan pemuatan relasi secara malas. Pada halaman dengan banyak item, jumlah query bisa mencapai ratusan.

Berikut contoh masalah N+1 dalam PHP dan cara memperbaikinya. Pada versi yang bermasalah, query penulis dijalankan di dalam perulangan. Pada versi yang diperbaiki, semua penulis diambil sekaligus dengan satu query menggunakan klausa `IN`. Hasilnya kemudian dipetakan berdasarkan ID penulis. Jumlah query turun dari 51 menjadi 2, berapa pun jumlah artikelnya.

```php
<?php
// Versi bermasalah: 1 query artikel + 1 query per artikel (N+1)
$artikel = $pdo->query('SELECT id, judul, penulis_id FROM artikel ORDER BY id DESC LIMIT 50')
               ->fetchAll(PDO::FETCH_ASSOC);
foreach ($artikel as &$a) {
    $stmt = $pdo->prepare('SELECT nama FROM penulis WHERE id = ?');
    $stmt->execute([$a['penulis_id']]);
    $a['nama_penulis'] = $stmt->fetchColumn();
}
unset($a);

// Versi diperbaiki: 2 query, berapa pun jumlah artikelnya
$artikel = $pdo->query('SELECT id, judul, penulis_id FROM artikel ORDER BY id DESC LIMIT 50')
               ->fetchAll(PDO::FETCH_ASSOC);
$idPenulis = array_values(array_unique(array_column($artikel, 'penulis_id')));
$namaPenulis = [];
if ($idPenulis !== []) {
    $placeholder = implode(',', array_fill(0, count($idPenulis), '?'));
    $stmt = $pdo->prepare("SELECT id, nama FROM penulis WHERE id IN ($placeholder)");
    $stmt->execute($idPenulis);
    $namaPenulis = $stmt->fetchAll(PDO::FETCH_KEY_PAIR);
}
foreach ($artikel as &$a) {
    $a['nama_penulis'] = $namaPenulis[$a['penulis_id']] ?? null;
}
unset($a);
```

Jika menggunakan ORM, manfaatkan fitur pemuatan relasi di awal atau *eager loading*. Hampir semua ORM populer menyediakan fitur ini dengan sintaks yang sederhana. Alternatif lain adalah menggunakan `JOIN` jika data yang dibutuhkan tidak terlalu banyak. Pantau jumlah query per halaman menggunakan alat debug di lingkungan pengembangan. Jumlah query yang naik seiring jumlah item adalah tanda jelas masalah N+1.

### Gunakan Paginasi yang Efisien

Paginasi dengan `LIMIT` dan `OFFSET` adalah cara yang paling umum untuk membagi data ke dalam beberapa halaman. Cara ini bekerja baik untuk halaman-halaman awal. Namun, untuk halaman yang jauh, misalnya halaman ke-5.000, MySQL tetap harus membaca dan membuang semua baris sebelumnya. Semakin besar offset, semakin lambat query. Masalah ini sering muncul pada halaman arsip, daftar produk, atau API yang mengembalikan data dalam jumlah besar.

Alternatif yang lebih efisien adalah paginasi berbasis kunci atau *keyset pagination*. Alih-alih melompati sejumlah baris, query mengambil baris setelah nilai terakhir dari halaman sebelumnya. Dengan index yang tepat, MySQL bisa langsung menuju posisi tersebut. Kecepatan query pun tetap stabil, berapa pun jauhnya halaman. Kekurangannya, pengguna tidak bisa langsung melompat ke nomor halaman tertentu.

```php
<?php
/**
 * Mengambil satu halaman riwayat pesanan dengan keyset pagination.
 * Kursor berisi tanggal dan id pesanan terakhir dari halaman sebelumnya.
 * Index yang dibutuhkan: (pelanggan_id, dibuat_pada, id).
 */
function ambilPesanan(PDO $pdo, int $pelangganId, ?array $kursor, int $jumlah = 20): array
{
    if ($jumlah < 1 || $jumlah > 100) {
        throw new InvalidArgumentException('Jumlah per halaman harus antara 1 dan 100.');
    }

    $sql = 'SELECT id, total, dibuat_pada FROM pesanan WHERE pelanggan_id = :pelanggan';
    $param = [':pelanggan' => $pelangganId];

    if ($kursor !== null) {
        $sql .= ' AND (dibuat_pada < :tgl OR (dibuat_pada = :tgl2 AND id < :id))';
        $param[':tgl'] = $kursor['dibuat_pada'];
        $param[':tgl2'] = $kursor['dibuat_pada'];
        $param[':id'] = $kursor['id'];
    }

    $sql .= ' ORDER BY dibuat_pada DESC, id DESC LIMIT ' . $jumlah;

    $stmt = $pdo->prepare($sql);
    $stmt->execute($param);
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}
```

Pada contoh di atas, kolom `id` ikut digunakan sebagai pembeda ketika ada beberapa pesanan dengan tanggal yang sama. Tanpa kolom pembeda ini, sebagian data bisa terlewat atau muncul dua kali. Nilai `$jumlah` sudah divalidasi sebagai bilangan bulat dalam rentang tertentu sebelum disisipkan ke query. Semua nilai lain dikirim sebagai parameter untuk mencegah injeksi SQL. Sesuaikan nama tabel dan kolom dengan skema Anda.

### Kurangi Query yang Tidak Perlu

Banyak aplikasi menjalankan query yang sama berulang kali dalam satu permintaan. Contohnya adalah mengambil pengaturan website atau data pengguna yang sedang masuk di beberapa bagian kode. Simpan hasil query tersebut di variabel atau cache permintaan agar tidak diambil ulang. Periksa juga apakah ada query yang hasilnya tidak pernah digunakan. Kode lama sering menyisakan query yang sudah tidak relevan.

### Gabungkan Operasi Tulis

Memasukkan data satu baris per query sangat lambat jika jumlahnya banyak. Setiap query membutuhkan perjalanan bolak-balik ke server basis data dan komit transaksi sendiri. Gabungkan beberapa baris dalam satu perintah `INSERT` dengan beberapa nilai sekaligus. Alternatifnya, bungkus banyak operasi tulis dalam satu transaksi. Kedua cara ini dapat mempercepat proses impor atau pembaruan massal secara signifikan.

### Hati-hati dengan COUNT pada Tabel Besar

Menampilkan jumlah total data, seperti "12.345 produk ditemukan", membutuhkan query `COUNT`. Pada tabel InnoDB yang besar, `COUNT(*)` tanpa kondisi yang didukung index bisa cukup lambat. Hal ini karena InnoDB tidak menyimpan jumlah baris secara langsung. Jika angka pasti tidak terlalu penting, pertimbangkan menampilkan perkiraan atau menyimpan jumlah di tabel ringkasan. Untuk paginasi berbasis kunci, Anda bahkan bisa menghindari kebutuhan menghitung total.

## Merancang Skema Tabel yang Efisien

Kinerja basis data juga sangat dipengaruhi oleh rancangan skema tabel. Skema yang baik membuat query lebih sederhana dan index lebih efektif. Sebaliknya, skema yang kurang baik bisa membuat query rumit dan lambat, seberapa pun bagusnya index. Mengubah skema pada tabel besar yang sudah berjalan juga cukup berisiko. Karena itu, perhatikan rancangan skema sejak awal pengembangan.

**Pilih tipe data yang tepat.** Gunakan tipe data sekecil mungkin yang masih mampu menampung nilai yang dibutuhkan. Misalnya, gunakan `TINYINT` untuk status dengan sedikit pilihan dan `INT` untuk ID yang tidak akan melebihi batasnya. Tipe data yang lebih kecil membuat baris dan index lebih ringkas. Index yang lebih kecil lebih mudah dimuat seluruhnya ke memori. Namun, jangan terlalu pelit hingga nilai di masa depan tidak muat.

**Gunakan tipe tanggal yang sesuai.** Simpan tanggal dan waktu dengan tipe `DATE`, `DATETIME`, atau `TIMESTAMP`, bukan sebagai teks. Tipe tanggal memungkinkan perbandingan rentang yang efisien dan memanfaatkan index dengan baik. Menyimpan tanggal sebagai teks dengan format yang tidak konsisten membuat query sulit dan lambat. Perhatikan juga zona waktu yang digunakan aplikasi dan basis data. Konsistensi zona waktu mencegah kesalahan data yang sulit dilacak.

**Gunakan set karakter utf8mb4.** Set karakter `utf8mb4` mendukung seluruh karakter Unicode, termasuk emoji dan aksara dari berbagai bahasa. Set karakter ini adalah bawaan di MySQL 8.0. Menggunakan set karakter yang sama di seluruh tabel dan koneksi mencegah konversi yang tidak perlu. Perbedaan set karakter atau *collation* antara dua kolom yang di-*join* bisa membuat index tidak digunakan. Pastikan kolom yang saling berhubungan memiliki set karakter dan collation yang sama.

**Seimbangkan normalisasi dan denormalisasi.** Normalisasi berarti memecah data ke dalam beberapa tabel untuk menghindari duplikasi. Pendekatan ini menjaga konsistensi data dan memudahkan pembaruan. Namun, normalisasi yang berlebihan bisa membutuhkan banyak `JOIN` untuk menampilkan satu halaman. Dalam kasus tertentu, menyimpan sebagian data secara terduplikasi atau dalam tabel ringkasan bisa mempercepat query baca. Keputusan ini perlu mempertimbangkan pola baca dan tulis aplikasi.

**Pisahkan data besar yang jarang dibaca.** Kolom berisi teks atau data biner yang sangat besar memperberat setiap baris. Jika kolom tersebut jarang dibutuhkan, pertimbangkan memindahkannya ke tabel terpisah. Dengan begitu, query yang sering dijalankan tidak perlu membaca data besar tersebut. File seperti gambar dan dokumen sebaiknya tidak disimpan di dalam basis data. Simpan file di sistem berkas atau layanan penyimpanan objek, lalu simpan alamatnya di basis data.

## Mengatur Konfigurasi MySQL dan InnoDB

Selain query dan skema, konfigurasi server MySQL juga memengaruhi kinerja. Konfigurasi bawaan MySQL dirancang aman untuk berbagai kondisi, tetapi belum tentu optimal untuk server Anda. Penyesuaian konfigurasi sebaiknya dilakukan setelah query dan index sudah diperbaiki. Konfigurasi yang bagus tidak bisa menyelamatkan query yang buruk. Berikut beberapa pengaturan yang paling berpengaruh.

**innodb_buffer_pool_size.** Buffer pool adalah area memori tempat InnoDB menyimpan data dan index yang sering diakses. Semakin besar buffer pool, semakin banyak data yang bisa dibaca langsung dari memori tanpa mengakses disk. Pada server yang khusus menjalankan basis data, buffer pool biasanya diberi porsi besar dari total memori. Pada server yang juga menjalankan web server dan PHP, ukurannya harus disesuaikan agar tidak kekurangan memori. Pantau rasio pembacaan dari memori dibanding dari disk untuk menilai kecukupan ukurannya.

**Jumlah koneksi.** Pengaturan `max_connections` menentukan berapa banyak koneksi yang dapat dilayani bersamaan. Nilai yang terlalu rendah menyebabkan galat koneksi saat trafik tinggi. Nilai yang terlalu tinggi bisa menghabiskan memori karena setiap koneksi membutuhkan sumber daya. Pada aplikasi PHP, setiap proses PHP biasanya membuka koneksinya sendiri. Sesuaikan jumlah proses PHP dan batas koneksi MySQL agar seimbang.

**Query cache tidak lagi tersedia.** Versi lama MySQL memiliki fitur *query cache* yang menyimpan hasil query. Fitur ini sudah dihapus pada MySQL 8.0 karena sering menimbulkan masalah skalabilitas. Jika Anda membaca panduan lama yang menyarankan pengaturan query cache, abaikan untuk MySQL versi modern. Caching hasil query sebaiknya dilakukan di tingkat aplikasi. Pembahasan tentang hal ini ada di bagian berikutnya.

**Perbarui statistik tabel.** MySQL menggunakan statistik tentang distribusi data untuk memilih rencana eksekusi terbaik. Statistik yang usang bisa membuat MySQL memilih index yang kurang tepat. Perintah `ANALYZE TABLE` memperbarui statistik tersebut. InnoDB biasanya memperbarui statistik secara otomatis, tetapi setelah perubahan data besar, menjalankannya secara manual bisa membantu. Perintah `OPTIMIZE TABLE` dapat membangun ulang tabel untuk merapikan ruang, tetapi jalankan dengan hati-hati karena bisa memakan waktu dan mengunci tabel.

**Gunakan versi yang masih didukung.** Setiap versi MySQL membawa perbaikan kinerja dan keamanan. Versi yang sudah tidak didukung tidak lagi menerima perbaikan celah keamanan. Rencanakan pembaruan versi secara berkala dengan pengujian yang memadai. Periksa perubahan perilaku yang mungkin memengaruhi aplikasi. Pembaruan versi sering memberikan peningkatan kinerja tanpa mengubah kode.

## Menambahkan Lapisan Cache

Query yang paling cepat adalah query yang tidak perlu dijalankan. Banyak data di website tidak berubah setiap detik, sehingga hasil query bisa disimpan sementara. Dengan cache, aplikasi bisa mengambil data dari memori yang jauh lebih cepat daripada basis data. Beban basis data pun berkurang drastis. Ada beberapa tingkat cache yang bisa dimanfaatkan.

**Object cache.** Sistem seperti Redis atau Memcached menyimpan hasil query atau objek aplikasi di memori. Aplikasi memeriksa cache terlebih dahulu sebelum menjalankan query. Jika data ditemukan, query ke basis data tidak perlu dijalankan. Jika tidak, aplikasi menjalankan query lalu menyimpan hasilnya di cache. Atur masa berlaku yang sesuai dan hapus cache ketika data aslinya berubah.

**Caching halaman.** Untuk halaman publik yang sama bagi semua pengunjung, seluruh halaman HTML bisa disimpan dalam cache. Dengan cara ini, tidak ada query basis data yang dijalankan untuk sebagian besar kunjungan. Caching halaman bisa dilakukan di server maupun di CDN. Penjelasan tentang caching di CDN dapat dibaca di artikel CDN. Pendekatan ini sangat efektif untuk blog dan website berita.

**Tabel ringkasan.** Untuk laporan atau statistik yang membutuhkan perhitungan berat, pertimbangkan membuat tabel ringkasan. Tabel ini berisi hasil perhitungan yang diperbarui secara berkala, misalnya setiap jam. Halaman laporan cukup membaca dari tabel ringkasan yang kecil. Pendekatan ini jauh lebih cepat daripada menghitung ulang dari data mentah setiap kali halaman dibuka. Pastikan pengguna memahami bahwa data mungkin tertunda sedikit.

## Optimasi Database untuk WordPress

WordPress menggunakan MySQL atau MariaDB sebagai basis datanya. Struktur tabel WordPress dirancang fleksibel agar bisa menampung berbagai jenis konten dan plugin. Fleksibilitas ini kadang dibayar dengan kinerja, terutama pada website besar. Banyak masalah kinerja WordPress berasal dari plugin yang menulis query kurang efisien. Berikut beberapa area yang perlu diperhatikan.

**Opsi yang dimuat otomatis.** Tabel `wp_options` menyimpan pengaturan website dan plugin. Sebagian opsi ditandai untuk dimuat otomatis di setiap permintaan halaman. Seiring waktu, plugin bisa menyimpan data besar sebagai opsi yang dimuat otomatis. Akibatnya, setiap permintaan harus memuat data yang tidak selalu dibutuhkan. Periksa ukuran total opsi yang dimuat otomatis dan tinjau opsi berukuran besar dari plugin yang sudah tidak digunakan.

**Tabel metadata.** Tabel seperti `wp_postmeta` menyimpan data tambahan dalam bentuk pasangan kunci dan nilai. Struktur ini sangat fleksibel, tetapi query yang memfilter berdasarkan nilai metadata bisa sangat lambat pada data besar. Toko daring dengan banyak produk dan atribut paling sering mengalami masalah ini. Hindari query yang memfilter banyak kondisi metadata sekaligus. Untuk kebutuhan kompleks, pertimbangkan tabel khusus atau solusi pencarian yang lebih efisien.

**Revisi, transient, dan data sisa.** WordPress menyimpan revisi artikel yang bisa menumpuk menjadi sangat banyak. Data sementara atau *transient* yang sudah kedaluwarsa juga bisa tertinggal di basis data. Plugin yang sudah dihapus sering meninggalkan tabel dan data. Bersihkan data-data ini secara berkala dengan hati-hati. Pastikan cadangan basis data sudah tersedia sebelum pembersihan dimulai.

**Object cache persisten.** Secara bawaan, object cache WordPress hanya bertahan selama satu permintaan. Dengan Redis atau Memcached, object cache bisa bertahan di antara permintaan. Hasilnya, banyak query berulang tidak perlu dijalankan lagi. Fitur ini sangat bermanfaat untuk website dinamis seperti toko WooCommerce dan forum. Fitur ini sering sudah tersedia di layanan hosting WordPress terkelola.

**Pantau query per halaman.** Gunakan plugin pemantau query di lingkungan pengembangan atau pengujian. Plugin ini menampilkan jumlah query, durasi, dan asal query untuk setiap halaman. Dari data ini, Anda bisa mengetahui plugin atau tema mana yang paling membebani basis data. Jangan biarkan plugin pemantau aktif di website produksi untuk pengunjung umum. Gunakan informasi tersebut untuk memutuskan perbaikan atau penggantian plugin.

## Keamanan dan Optimasi Berjalan Bersama

Optimasi basis data tidak boleh mengorbankan keamanan. Salah satu praktik terpenting adalah selalu menggunakan *prepared statement* untuk query yang melibatkan input pengguna. Prepared statement memisahkan struktur query dari data, sehingga mencegah injeksi SQL. Selain lebih aman, prepared statement juga memudahkan MySQL mengenali query yang sama dengan parameter berbeda. Contoh-contoh kode di artikel ini menggunakan pendekatan tersebut.

Batasi juga hak akses akun basis data yang digunakan aplikasi. Akun aplikasi sebaiknya hanya memiliki hak yang benar-benar dibutuhkan, seperti membaca dan menulis tabel tertentu. Jangan menggunakan akun administrator basis data untuk aplikasi. Jangan membuka port basis data ke internet jika tidak diperlukan. Prinsip keamanan dasar lainnya dibahas di artikel keamanan siber.

## Perawatan Rutin Basis Data

Basis data membutuhkan perawatan rutin agar tetap sehat dan cepat. Data terus bertambah, pola penggunaan berubah, dan query baru ditambahkan seiring pengembangan aplikasi. Tanpa perawatan, kinerja bisa menurun perlahan tanpa disadari. Perawatan rutin juga membantu mendeteksi masalah sebelum berdampak besar. Berikut kegiatan perawatan yang dianjurkan.

**Tinjau slow query log secara berkala.** Jadikan peninjauan slow query log sebagai kegiatan rutin, misalnya setiap minggu atau setiap bulan. Query baru yang lambat sering muncul setelah ada fitur baru atau pertumbuhan data. Query bermasalah yang ditemukan lebih awal biasanya lebih mudah ditangani. Catat query yang sudah diperbaiki beserta perubahan yang dilakukan. Catatan ini berguna bagi tim di masa depan.

**Hapus index yang tidak digunakan.** Seiring waktu, beberapa index mungkin tidak lagi digunakan karena query berubah. Index yang tidak digunakan tetap membebani operasi tulis dan memakan ruang. MySQL menyediakan tabel di skema `sys` yang dapat menunjukkan index yang tidak pernah digunakan sejak server dimulai. Periksa data tersebut setelah server berjalan cukup lama. Hapus index hanya setelah yakin tidak ada query penting yang membutuhkannya.

**Arsipkan data lama.** Tabel yang terus membesar, seperti log aktivitas atau riwayat transaksi lama, bisa memperlambat query. Pertimbangkan untuk memindahkan data lama ke tabel arsip atau penyimpanan terpisah. Data aktif yang lebih sedikit membuat index lebih kecil dan query lebih cepat. Pastikan kebijakan arsip sesuai dengan kebutuhan bisnis dan aturan penyimpanan data. Untuk data pribadi, perhatikan juga ketentuan masa penyimpanan dalam regulasi yang berlaku.

**Uji cadangan dan pemulihan.** Cadangan basis data wajib dilakukan secara rutin. Namun, cadangan hanya berguna jika bisa dipulihkan dengan benar. Uji proses pemulihan secara berkala di lingkungan terpisah. Ukur juga berapa lama waktu pemulihan agar Anda siap jika terjadi masalah. Proses pencadangan sebaiknya dijadwalkan pada waktu trafik rendah agar tidak mengganggu kinerja.

## Jenis Index Lain yang Perlu Diketahui

Selain index biasa, MySQL menyediakan beberapa jenis index lain dengan fungsi khusus. Memahami jenis-jenis ini membantu Anda memilih alat yang tepat untuk setiap kebutuhan. Setiap jenis memiliki kelebihan dan batasan masing-masing. Gunakan sesuai pola query yang dihadapi. Berikut beberapa jenis yang paling sering digunakan.

**Primary key.** Setiap tabel InnoDB sebaiknya memiliki primary key. InnoDB menyimpan baris data secara berurutan berdasarkan primary key. Index lain di tabel tersebut juga menyimpan nilai primary key sebagai penunjuk ke baris data. Karena itu, primary key yang ringkas, seperti bilangan bulat yang bertambah otomatis, membuat semua index lebih kecil. Primary key yang panjang atau acak bisa memperbesar index dan memperlambat penyisipan data.

**Unique index.** Unique index memastikan tidak ada nilai ganda di kolom tertentu, misalnya alamat email pengguna. Selain menjaga integritas data, unique index juga mempercepat pencarian berdasarkan kolom tersebut. MySQL tahu bahwa paling banyak hanya ada satu baris yang cocok. Gunakan unique index untuk kolom yang memang harus unik. Jangan mengandalkan pemeriksaan di aplikasi saja untuk menjaga keunikan data.

**Fulltext index.** Fulltext index dirancang untuk pencarian teks di kolom berisi kalimat atau paragraf. Index ini memungkinkan pencarian kata kunci yang jauh lebih efisien daripada `LIKE` dengan wildcard di awal. Pencarian dilakukan dengan sintaks `MATCH ... AGAINST`. Fitur ini cocok untuk pencarian artikel atau produk sederhana. Untuk kebutuhan pencarian yang lebih canggih, mesin pencari khusus mungkin lebih sesuai.

## Transaksi dan Penguncian

InnoDB mendukung transaksi yang menjamin sekumpulan operasi berhasil seluruhnya atau dibatalkan seluruhnya. Transaksi sangat penting untuk operasi seperti pembayaran atau pengurangan stok. Namun, transaksi juga melibatkan penguncian baris agar data tetap konsisten. Penguncian yang terlalu lama dapat membuat query lain menunggu. Kondisi ini bisa menurunkan kinerja secara keseluruhan, terutama saat trafik tinggi.

Jaga agar transaksi sesingkat mungkin. Jangan melakukan proses yang lama, seperti memanggil API eksternal atau mengirim email, di dalam transaksi yang sedang terbuka. Siapkan semua data yang dibutuhkan sebelum memulai transaksi. Pastikan query di dalam transaksi menggunakan index agar hanya mengunci baris yang diperlukan. Query tanpa index bisa mengunci jauh lebih banyak baris daripada yang dibutuhkan.

## Mengelola Koneksi dari Aplikasi PHP

Pada aplikasi PHP tradisional, setiap permintaan biasanya membuka koneksi baru ke basis data dan menutupnya di akhir permintaan. Membuka koneksi membutuhkan waktu, terutama jika basis data berada di server berbeda. Pada trafik tinggi, jumlah koneksi bersamaan juga bisa melampaui batas yang diizinkan MySQL. Karena itu, pengelolaan koneksi perlu diperhatikan. Ada beberapa pendekatan yang bisa dipertimbangkan.

Koneksi persisten di PDO memungkinkan proses PHP menggunakan kembali koneksi yang sudah terbuka. Pendekatan ini mengurangi waktu membuka koneksi baru. Namun, koneksi persisten juga membawa risiko, seperti status sesi yang tertinggal dari permintaan sebelumnya. Gunakan dengan hati-hati dan pastikan jumlah koneksi tetap terkendali. Untuk arsitektur yang lebih besar, *connection pooler* di antara aplikasi dan basis data bisa menjadi solusi yang lebih teratur.

## Replikasi untuk Beban Baca yang Besar

Ketika satu server basis data tidak lagi mampu menangani beban, replikasi bisa menjadi pilihan. Dengan replikasi, data dari server utama disalin ke satu atau lebih server replika. Aplikasi dapat mengarahkan query baca ke replika, sementara query tulis tetap ke server utama. Pendekatan ini mengurangi beban server utama secara signifikan. Replika juga bisa berfungsi sebagai cadangan jika server utama bermasalah.

Perlu dipahami bahwa replikasi biasanya memiliki sedikit jeda. Data yang baru ditulis ke server utama mungkin belum langsung tersedia di replika. Untuk data yang harus selalu terbaru, seperti saldo atau status pembayaran, baca dari server utama. Replikasi juga menambah kerumitan infrastruktur dan biaya. Pastikan query dan index sudah dioptimasi sebelum memutuskan menambah server.

## Memantau Kesehatan Server Basis Data

Selain memantau query, pantau juga kondisi server basis data secara keseluruhan. Metrik penting meliputi penggunaan prosesor, memori, kapasitas disk, dan jumlah koneksi aktif. Lonjakan penggunaan prosesor sering menandakan query berat yang baru muncul. Disk yang hampir penuh bisa menyebabkan basis data berhenti menerima data. Atur peringatan otomatis agar masalah segera diketahui.

Pantau juga waktu respons query secara rata-rata dan pada persentil tinggi. Rata-rata saja bisa menyembunyikan sebagian kecil query yang sangat lambat. Grafik dari waktu ke waktu membantu melihat tren penurunan kinerja. Banyak layanan basis data terkelola menyediakan dasbor pemantauan bawaan. Untuk server yang dikelola sendiri, gunakan alat pemantauan sumber terbuka yang sesuai.

## Kesalahan Umum dalam Optimasi Database

**Menambah index tanpa analisis.** Menambahkan index secara acak dengan harapan query menjadi cepat jarang berhasil. Index yang tidak sesuai dengan pola query tidak akan digunakan. Terlalu banyak index justru memperlambat operasi tulis. Selalu analisis query dengan `EXPLAIN` sebelum menambahkan index. Uji kembali setelah index ditambahkan untuk memastikan perbaikannya.

**Mengubah konfigurasi tanpa memahami dampaknya.** Banyak panduan di internet menyarankan angka konfigurasi tertentu tanpa konteks. Angka yang cocok untuk satu server belum tentu cocok untuk server lain. Konfigurasi yang keliru bisa menyebabkan server kehabisan memori atau tidak stabil. Ubah satu pengaturan pada satu waktu dan ukur dampaknya. Simpan catatan pengaturan sebelumnya agar mudah dikembalikan jika ada masalah.

**Menguji dengan data yang terlalu sedikit.** Query yang cepat di lingkungan pengembangan dengan sedikit data bisa sangat lambat di produksi. Masalah kinerja basis data sering baru terlihat ketika data sudah besar. Jika memungkinkan, uji dengan data yang ukurannya mendekati data produksi. Gunakan data yang sudah dianonimkan untuk menjaga privasi. Pengujian seperti ini membantu menemukan masalah sebelum berdampak pada pengguna.

**Mengandalkan cache untuk menutupi query buruk.** Cache sangat membantu, tetapi tidak menyelesaikan akar masalah. Ketika cache kedaluwarsa atau dibersihkan, query lambat tetap harus dijalankan. Pada saat trafik tinggi, banyak permintaan bisa menjalankan query lambat secara bersamaan ketika cache kosong. Kondisi ini bisa membebani basis data secara tiba-tiba. Perbaiki query terlebih dahulu, lalu gunakan cache sebagai lapisan tambahan.

## Mengoptimasi JOIN dan Subquery

Query yang menggabungkan beberapa tabel sangat umum dalam aplikasi web. Contohnya adalah menampilkan pesanan beserta nama pelanggan dan daftar produknya. Jika dirancang dengan baik, `JOIN` bisa sangat efisien. Namun, `JOIN` tanpa index yang tepat bisa membuat MySQL memeriksa kombinasi baris dalam jumlah sangat besar. Berikut beberapa prinsip untuk mengoptimasi query semacam ini.

Pastikan kolom yang digunakan untuk menghubungkan tabel memiliki index. Biasanya, kolom kunci asing seperti `pelanggan_id` di tabel pesanan perlu diberi index. Tanpa index, MySQL harus memindai seluruh tabel untuk setiap baris yang digabungkan. Pastikan juga tipe data dan collation kedua kolom sama. Perbedaan tipe data bisa membuat index tidak digunakan.

Filter data sedini mungkin. Semakin sedikit baris yang terlibat dalam penggabungan, semakin cepat query berjalan. Letakkan kondisi penyaringan yang selektif pada tabel yang tepat. Periksa urutan penggabungan yang dipilih MySQL melalui hasil `EXPLAIN`. Biasanya, optimizer MySQL sudah cukup pintar memilih urutan yang baik selama index tersedia.

Subquery di klausa `WHERE` kadang bisa ditulis ulang menjadi `JOIN` atau `EXISTS`. MySQL versi modern sudah mampu mengoptimasi banyak bentuk subquery secara otomatis. Namun, subquery yang bergantung pada baris luar atau *correlated subquery* tetap bisa lambat. Subquery seperti ini dijalankan berulang kali untuk setiap baris. Bandingkan hasil `EXPLAIN` dari beberapa bentuk penulisan untuk memilih yang paling efisien.

## Contoh Kasus Optimasi

Untuk memberikan gambaran utuh, berikut contoh kasus optimasi yang bersifat ilustrasi. Sebuah toko daring mengeluhkan halaman riwayat pesanan yang semakin lambat. Halaman tersebut menampilkan 20 pesanan terbaru milik pelanggan yang sedang masuk. Awalnya, halaman terasa cepat ketika toko masih baru. Setelah beberapa tahun, tabel pesanan berisi jutaan baris dan halaman menjadi sangat lambat.

Langkah pertama adalah memeriksa slow query log. Ditemukan query yang mengambil pesanan berdasarkan `pelanggan_id` dan mengurutkannya berdasarkan `dibuat_pada`. Hasil `EXPLAIN` menunjukkan kolom `type` bernilai `ALL` dan kolom `Extra` berisi `Using filesort`. Artinya, MySQL memindai seluruh tabel lalu mengurutkan hasilnya secara terpisah. Kolom `rows` menunjukkan perkiraan jutaan baris yang diperiksa.

Langkah kedua adalah menambahkan index gabungan pada `(pelanggan_id, dibuat_pada)`. Setelah index ditambahkan, hasil `EXPLAIN` menunjukkan `type` bernilai `ref` dan `Using filesort` hilang. Jumlah baris yang diperiksa turun drastis menjadi hanya puluhan. Query yang sebelumnya lambat kini selesai dalam waktu sangat singkat. Halaman riwayat pesanan kembali terasa cepat.

Langkah ketiga adalah memeriksa kode aplikasi di halaman tersebut. Ditemukan bahwa nama produk untuk setiap pesanan diambil dengan query terpisah di dalam perulangan. Pola N+1 ini diganti dengan satu query menggunakan klausa `IN`. Kolom yang diambil juga dibatasi hanya yang ditampilkan di halaman. Setelah semua perbaikan, jumlah query di halaman turun drastis dan waktu respons server menjadi stabil.

## Checklist Optimasi Database MySQL

1. Slow query log aktif dan ditinjau secara berkala.
2. Query diprioritaskan berdasarkan total waktu, bukan hanya durasi tunggal.
3. Query lambat dianalisis dengan EXPLAIN sebelum diubah.
4. Index dibuat berdasarkan pola query nyata, termasuk index gabungan dengan urutan kolom yang tepat.
5. Tidak ada fungsi pada kolom berindeks di klausa WHERE.
6. Query hanya mengambil kolom yang dibutuhkan.
7. Masalah N+1 sudah diatasi dengan pemuatan data sekaligus.
8. Paginasi data besar menggunakan pendekatan berbasis kunci.
9. Tipe data dan set karakter kolom sudah sesuai dan konsisten.
10. Ukuran buffer pool InnoDB sudah disesuaikan dengan memori server.
11. Cache aplikasi digunakan untuk data yang jarang berubah.
12. Semua query dengan input pengguna menggunakan prepared statement.
13. Cadangan dibuat rutin dan proses pemulihan sudah diuji.

## FAQ Optimasi Database MySQL

### Bagaimana cara mengetahui query MySQL yang lambat?

Aktifkan slow query log dengan batas waktu yang sesuai, lalu analisis log tersebut menggunakan alat seperti `mysqldumpslow` atau `pt-query-digest`. Dari sisi aplikasi, gunakan alat debug atau pemantauan yang menampilkan durasi setiap query. Fokuskan perbaikan pada query yang paling banyak menghabiskan waktu secara keseluruhan.

### Apakah menambahkan index selalu mempercepat query?

Tidak selalu. Index hanya membantu jika sesuai dengan pola query, termasuk urutan kolom pada index gabungan. Index juga memperlambat operasi tulis dan memakan ruang penyimpanan. Gunakan `EXPLAIN` untuk memastikan index benar-benar digunakan.

### Apa perbedaan EXPLAIN dan EXPLAIN ANALYZE?

`EXPLAIN` menampilkan rencana eksekusi berdasarkan perkiraan tanpa menjalankan query. `EXPLAIN ANALYZE` menjalankan query dan menampilkan waktu nyata setiap tahap. Perintah kedua tersedia di MySQL 8.0 dan memberikan informasi yang lebih akurat.

### Mengapa query cepat di laptop tetapi lambat di server produksi?

Penyebab paling umum adalah perbedaan jumlah data. Query yang memindai seluruh tabel tetap cepat jika tabelnya kecil, tetapi menjadi lambat ketika data membesar. Perbedaan konfigurasi server dan beban dari pengguna lain juga berpengaruh.

### Apakah perlu pindah dari MySQL ke basis data lain agar lebih cepat?

Untuk sebagian besar website, MySQL sudah lebih dari cukup jika query, index, dan konfigurasinya dioptimasi dengan baik. Banyak masalah kinerja berasal dari cara penggunaan, bukan dari jenis basis data. Pertimbangkan teknologi lain hanya jika ada kebutuhan khusus yang jelas.

### Seberapa sering perlu menjalankan OPTIMIZE TABLE?

Pada InnoDB, `OPTIMIZE TABLE` umumnya tidak perlu dijalankan secara rutin. Perintah ini bermanfaat setelah penghapusan data dalam jumlah besar untuk merapikan ruang. Jalankan pada waktu trafik rendah karena prosesnya bisa memakan waktu dan memengaruhi akses tabel.

## Kesimpulan

Optimasi database MySQL dimulai dari pengukuran, bukan tebakan. Aktifkan slow query log, temukan query dengan total waktu terbesar, lalu analisis dengan `EXPLAIN`. Buat index berdasarkan pola query nyata, perhatikan aturan prefiks kiri pada index gabungan, dan hindari pola yang membuat index tidak terpakai. Perbaiki pola query bermasalah seperti `SELECT *`, N+1, dan paginasi dengan offset besar. Rancang skema dengan tipe data yang tepat dan sesuaikan konfigurasi InnoDB dengan kapasitas server.

Tambahkan lapisan cache untuk data yang jarang berubah, tetapi jangan gunakan cache untuk menutupi query yang buruk. Lakukan perawatan rutin dan selalu utamakan keamanan dengan prepared statement. Untuk melihat dampak perbaikan pada pengalaman pengguna, ukur waktu respons server melalui panduan cara membaca PageSpeed Insights. Untuk halaman publik, kombinasikan basis data yang cepat dengan caching di CDN.
