# Writeup CTF - Digital Forensics: Case 2v4

**Author**: Abdul Latif

## Daftar File
### Barang Bukti (Asli)
- `readme (2).txt`
- `params.txt`

### Tools / Skrip Analis
- `solve.py` (Skrip Python yang dibuat oleh analis untuk dekripsi)

## Analisis Kasus
Barang bukti yang diberikan terdiri dari dua file yaitu `readme (2).txt` dan `params.txt`. File `readme (2).txt` menyatakan bahwa terdapat dua ciphertext yang dihasilkan dari pesan yang sama dan menggunakan modulus ($n$) yang sama, namun dengan eksponen enkripsi yang berbeda ($e_1 = 17$ dan $e_2 = 65537$). Ini merupakan indikasi kuat adanya kerentanan kriptografi RSA yang dikenal sebagai **Common Modulus Attack**.

## Langkah-langkah Penyelesaian

**Langkah 1: Menyiapkan Metodologi Serangan**
Berdasarkan parameter yang ada di `params.txt`, $e_1$ dan $e_2$ adalah bilangan prima yang relatif koprima ($gcd(e_1, e_2) = 1$). Oleh karena itu, analis dapat menggunakan algoritma *Extended Euclidean* untuk mencari nilai $a$ dan $b$ sehingga memenuhi persamaan:
$a \cdot e_1 + b \cdot e_2 = 1$

Setelah mendapatkan nilai $a$ dan $b$, ciphertext dapat didekripsi untuk memulihkan pesan asli ($m$) dengan persamaan:
$m = (c_1^a \cdot c_2^b) \pmod n$

**Langkah 2: Pembuatan Skrip Eksploitasi**
Untuk menyelesaikan kasus ini, analis membuat skrip python `solve.py` yang bertugas untuk membaca parameter $n, e_1, e_2, c_1, c_2$ dari file `params.txt`. Skrip ini melakukan perhitungan invers modular jika nilai pangkat ($a$ atau $b$) bernilai negatif, kemudian mengkalkulasi pesan $m$ dan mengonversi nilai desimal/hex tersebut kembali menjadi teks ASCII.

**Langkah 3: Eksekusi dan Mendapatkan Flag**
Setelah analis menjalankan `solve.py`, skrip berhasil memulihkan pesan asli secara utuh dari kedua ciphertext yang saling terkait. Hasil akhirnya menampilkan teks berisi flag dari soal.

## Flag
FLAG: `flag{modulus_bersama_terekspos}`
