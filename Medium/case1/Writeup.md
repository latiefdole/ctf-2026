# Writeup case1
**Author:** Abdul Latif

## Inventarisasi File
**Barang Bukti (Asli):**
- `readme (1).txt` (Catatan petunjuk)
- `company_logo.jpg` (File gambar bukti)
- `cipher_text.txt` (Pesan terenkripsi)

**Tools/Skrip/Output Analis:**
- `solve_case1.py` (Skrip analisis otomatis buatan analis)
- `solve_vig.py` (Skrip dekripsi khusus algoritma Vigenere)
- `company_logo - Copy.txt` (Output teks hasil ekstraksi *strings* dari file gambar)

## Langkah-langkah Analisis
1. Analis membaca dan menganalisis file bukti `readme (1).txt`. Pesan di dalamnya mengindikasikan adanya penggunaan "enkripsi klasik" dan memberikan petunjuk kuat bahwa kunci untuk membuka pesan tersembunyi ada di dalam file bukti yang lain.
2. Mematuhi petunjuk tersebut, analis memusatkan perhatian pada file gambar `company_logo.jpg`. Analis memanfaatkan skrip ekstraksi string/tool terminal untuk menarik semua karakter ASCII yang tertanam (embedded) di dalam struktur biner gambar tersebut.
3. Analis meninjau teks hasil ekstraksi dan dengan cepat mengidentifikasi sebuah teks mencurigakan yang berbunyi: `kunci: ARKANA`.
4. Analis kemudian beralih ke file `cipher_text.txt`. Mengingat petunjuk awal soal "enkripsi klasik" dan dengan mempertimbangkan karakteristik ciphertext yang muncul dalam bentuk alfabetis, analis menyimpulkan bahwa algoritma sandi yang dipakai adalah *Vigenere Cipher*.
5. Menggunakan kunci `ARKANA` yang ditemukan di gambar, analis merancang (atau menggunakan) skrip `solve_vig.py` / `solve_case1.py` untuk mengotomatisasi proses *decoding* Vigenere terhadap pesan terenkripsi.
6. Proses eksekusi *script* dekripsi berhasil memunculkan teks "MEMO INTERNAL" beserta informasi sensitif lain yang di dalamnya langsung termuat *flag*.

**FLAG:** `FLAG{V1G3N3R3_4RK4N4_D3CRYPT3D}`
