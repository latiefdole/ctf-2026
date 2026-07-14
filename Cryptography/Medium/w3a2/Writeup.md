# Writeup w3a2 — Kunci AES dari Metadata EXIF
**Author:** Abdul Latif
**Kategori:** Cryptography / Digital Forensics (EXIF)

## Inventarisasi File
**Barang Bukti (Asli):**
- `encrypted.bin` (File terenkripsi AES-128-CBC dari workstation terkompromi)
- `key_source.jpg` (Foto berlabel "kunci" yang ditemukan di direktori yang sama)
- `iv.txt` (Initialization Vector dalam bentuk hex)
- `readme (1).txt` (Catatan respons insiden)

**Tools/Skrip/Output Analis:**
- `extract_exif.py` / `extract_jpg_strings.py` (Ekstraksi metadata & string dari foto)
- `solve_aes.py` (Skrip *brute-forcing* kandidat kunci)
- `decrypt_flag.py` (Skrip dekripsi final)

## Langkah-langkah Analisis
1. Dari `readme (1).txt`, analis mengetahui bahwa **kunci AES-128 diturunkan dari metadata EXIF foto** `key_source.jpg`, sementara IV tersimpan di `iv.txt` (`4f2a8b1c9d3e7f0a5b6c2d4e8f1a3b7c`).
2. Analis mengekstrak metadata EXIF dari foto dan mengidentifikasi dua field kunci: `Artist = PenguinOps` dan `DateTimeOriginal = 2024:03:15 09:00:00`.
3. Analis merekonstruksi *key material* dengan menggabungkan kedua field memakai pemisah `|`, menghasilkan string sumber: `PenguinOps|2024:03:15 09:00:00`.
4. Karena AES-128 membutuhkan kunci 16 byte, analis melakukan hashing SHA-256 atas string sumber lalu mengambil **16 byte pertama** sebagai kunci AES-128.
5. Dengan kunci hasil derivasi, IV dari `iv.txt`, dan mode **AES-CBC**, analis mendekripsi `encrypted.bin` melalui `decrypt_flag.py`. Setelah *unpadding* PKCS#7, plaintext mengungkap flag.

**FLAG:** `flag{exif_kunci_aes_tersimpan}`
