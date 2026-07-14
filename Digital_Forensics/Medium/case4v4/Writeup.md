# Writeup CTF - Digital Forensics: Case 4v4

**Author**: Abdul Latif

## Daftar File
### Barang Bukti (Asli)
- `assembly_note.txt`
- `city_map.txt`
- `foto_1.jpg`
- `foto_2.jpg`
- `foto_3.jpg`

### Tools / Skrip / Output Analis
- `aperisolve.py`, `aperisolve2.py`, `aperisolve3.py` (Skrip analis untuk steganografi)
- `gps_parse.py`, `jpeg_analyze.py`, `jpeg_dct_extract.py` (Skrip analis untuk metadata dan DCT)
- `jawa_cities.txt`, `profile.jpg` (Data tambahan / output yang digunakan analis)

## Analisis Kasus
Barang bukti utama pada `case4v4` terdiri dari tiga buah foto (`foto_1.jpg`, `foto_2.jpg`, `foto_3.jpg`) serta dua buah catatan yaitu `assembly_note.txt` dan `city_map.txt`. Berdasarkan petunjuk, masing-masing foto menyimpan bagian (potongan) flag yang disembunyikan menggunakan teknik berbeda pada metadatanya (obfuskasi ringan, reversed string, dan Base64). Potongan-potongan tersebut harus disusun mengikuti urutan letak geografis kota pengambilan foto (dari utara ke selatan) dengan format perakitan: `{bagian3}_{bagian2}_{bagian1}`.

## Langkah-langkah Penyelesaian

**Langkah 1: Ekstraksi Lokasi dari EXIF Metadata**
Analis membuat skrip Python `gps_parse.py` untuk membaca data EXIF GPS dari ketiga gambar dan menentukan lokasinya. Hasilnya adalah:
- `foto_1.jpg`: Berlokasi di Surabaya (Selatan).
- `foto_2.jpg`: Berlokasi di Bandung (Tengah).
- `foto_3.jpg`: Berlokasi di Medan (Utara).

**Langkah 2: Ekstraksi String dari Tiap Foto**
Selanjutnya, analis menggunakan skrip pembaca metadata untuk menginspeksi nilai-nilai aneh yang tertanam:
- **Foto 3 (Medan)**: Analis menemukan string `dGltdXIzMw==`. Ini adalah format Base64. Setelah didecode, didapatkan hasil **`timur33`**.
- **Foto 2 (Bandung)**: Terdapat metadata bertuliskan `22tarab`. Sesuai dengan teknik reversed string, analis membalik urutan karakternya menjadi **`barat22`**.
- **Foto 1 (Surabaya)**: Pada field `XPComment`, analis menemukan data heksadesimal `\x06\x07\x12\x01\x12JJ`. Sesuai petunjuk "obfuskasi ringan", analis melakukan operasi bitwise XOR pada byte tersebut dengan kunci karakter `s` (ASCII 115) dan berhasil mendapatkan string **`utara99`**.

**Langkah 3: Penggabungan Flag**
Dengan panduan file `city_map.txt`, urutan kota dari paling utara ke selatan adalah: Medan, Bandung, lalu Surabaya.
- Bagian 1 (Medan, Foto 3) = `timur33`
- Bagian 2 (Bandung, Foto 2) = `barat22`
- Bagian 3 (Surabaya, Foto 1) = `utara99`

Instruksi format penggabungan adalah `{bagian3}_{bagian2}_{bagian1}`. Merakit potongan tersebut (berarti Foto 3 untuk bagian 3, Foto 2 untuk bagian 2, dan Foto 1 untuk bagian 1) akan menghasilkan gabungan: `timur33_barat22_utara99`.

Maka flag final yang didapatkan adalah benar.

## Flag
FLAG: `flag{timur33_barat22_utara99}`
