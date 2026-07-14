# Writeup CTF - Digital Forensics: Case 4

**Author**: Abdul Latif

## Daftar File
### Barang Bukti (Asli)
- `pemeriksa_kredensial` (File Executable ELF)

### Tools / Output Analis
- Tool string viewer atau skrip Python ekstraktor string

## Analisis Kasus
Pada `case4`, analis diberikan satu buah file executable ELF Linux bernama `pemeriksa_kredensial`. Program ini tampaknya meminta masukan berupa kredensial dari pengguna, lalu memvalidasi masukan tersebut sebelum memberikan akses. Analis ditugaskan untuk melakukan rekayasa balik (reverse engineering) atau analisis binary untuk menemukan kredensial yang valid (flag).

## Langkah-langkah Penyelesaian

**Langkah 1: Analisis Statis Dasar**
Sebagai langkah pertama yang cepat, analis tidak langsung membongkar instruksi assembly, melainkan mengandalkan analisis statis dengan mengekstrak string teks yang ada di dalam binary. Analis menjalankan perintah pengecekan string untuk membaca blok data yang dapat dicetak (printable strings).

**Langkah 2: Identifikasi Fungsi dan String Kunci**
Dari deretan string yang dihasilkan, analis menemukan nama-nama fungsi internal yang sangat informatif, yaitu `expected_b64`, `reverse_str`, dan `b64_encode`. Di area yang sama, ditemukan juga string Base64 yang mencurigakan yang diduga merupakan nilai perbandingan kredensial di dalam memory:
`fWQza2M0cmNfbjE0aGNfNDYzczRiXzNzcjN2M3J7Z2FsZg==`

**Langkah 3: Rekonstruksi Flag**
Memperhatikan nama fungsi `reverse_str`, analis menyimpulkan alur logika perbandingan pada program. Analis lalu mengambil string Base64 tersebut dan men-decode-nya, yang menghasilkan string terbalik:
`}d3kc4rc_n14hc_463s4b_3sr3v3r{galf`

Terakhir, analis membalik urutan karakter dari string tersebut (reverse string) ke format normal, dan mendapatkan flag secara utuh.

## Flag
FLAG: `flag{r3v3rs3_b4s364_ch41n_cr4ck3d}`
