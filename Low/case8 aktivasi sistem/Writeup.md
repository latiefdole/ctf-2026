# Writeup Case 8

**Author:** Abdul Latif

## Daftar Barang Bukti (Asli)
- `aktivasi_sistem`

## Langkah-Langkah Penyelesaian:
1. **Analisis Binary**: Barang bukti yang diberikan adalah file `aktivasi_sistem`, yang merupakan file executable pemeriksa "Kode Aktivasi".
2. **Ekstraksi Teks (Strings)**: Untuk menyelesaikannya, analis menulis sebuah skrip Python (tool kustom) yang berfungsi mengekstrak string ASCII dari binary tersebut untuk mencari indikasi kunci atau kode yang tertanam.
3. **Pencarian Petunjuk Kriptografi**: Berdasarkan output dari skrip analis, ditemukan referensi ke `xor_decode` serta sebuah string ciphertext yang tampak diacak (contohnya `<6;=!)k4=6i`).
4. **Bruteforce Kunci XOR**: Analis menambahkan logika bruteforce ke dalam skripnya untuk mencari kunci single-byte XOR. Dengan menggunakan format flag yang diketahui (selalu diawali dengan `flag{`), analis melakukan operasi XOR antara karakter pertama ciphertext (`<`) dengan karakter `f`.
5. **Dekripsi Payload Lengkap**: Hasil dari operasi tersebut mengungkapkan bahwa kunci XOR yang digunakan adalah nilai desimal 90 (karakter `Z`). Skrip analis kemudian digunakan untuk mendekode sisa ciphertext menggunakan kunci tersebut.
6. **Mendapatkan Flag**: Skrip yang dijalankan analis mencetak hasil dekripsi secara utuh yang berisi flag asli.

**FLAG:** `flag{s1ngl3_byt3_x0r_4ct1v4t3d}`
