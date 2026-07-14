# Writeup Case 5v4

**Author:** Abdul Latif

## Daftar Barang Bukti (Asli)
- `hint.txt`
- `dokumen_biasa.bin`
- `rahasia.zip`

## Langkah-Langkah Penyelesaian:
1. **Analisis Petunjuk**: Barang bukti yang diberikan antara lain `hint.txt`, `dokumen_biasa.bin`, dan `rahasia.zip`. Dari `hint.txt` diketahui bahwa terdapat gabungan dua format dan ada nilai tak biasa pada piksel warna tertentu.
2. **Inspeksi File Polyglot**: Melalui analisis header pada `dokumen_biasa.bin`, diketahui bahwa file tersebut adalah file polyglot berawalan header PNG dan berakhiran ZIP. File `rahasia.zip` sendiri diproteksi dengan enkripsi AES.
3. **Ekstraksi Piksel Gambar**: Untuk menyelesaikannya, analis membuat skrip Python (menggunakan library Pillow) untuk membaca data piksel RGB gambar. Ditemukan bahwa pada 17 piksel pertama channel Merah (Red) memiliki nilai selain 128 (background), yaitu `139 133 142...`.
4. **Mendapatkan Password ZIP**: Berdasarkan petunjuk rumus kombinasi warna, analis memodifikasi skrip untuk melakukan kalkulasi `R + (B - 86) * 16 - 32` pada 17 piksel pertama, dan berhasil mengungkap password yaitu `kunci_tersembunyi`.
5. **Mengekstrak File ZIP**: Analis kemudian menggunakan modul Python `pyzipper` di dalam skripnya untuk mengekstrak isi barang bukti `rahasia.zip` menggunakan password tersebut.
6. **Mendapatkan Flag**: Hasil ekstraksi menghasilkan file `flag.txt` yang di dalamnya terdapat flag asli.

**FLAG:** `flag{polyglot_lsb_stego_aes256}`
