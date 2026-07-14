# Writeup w3a3 — Substitusi + Transposisi (Known-Plaintext)
**Author:** Abdul Latif
**Kategori:** Cryptography / Classical Cipher

## Inventarisasi File
**Barang Bukti (Asli):**
- `cipher_info.txt` (Deskripsi cipher dua tahap hasil analisis malware)
- `samples.txt` (5 pasangan plaintext/ciphertext untuk analisis *known-plaintext*)
- `target.txt` (Ciphertext target yang harus didekripsi)

**Tools/Skrip/Output Analis:**
- `reconstruct_cipher.py` (Merekonstruksi tabel substitusi & lebar transposisi)
- `decrypt_target.py` (Mendekripsi ciphertext target)

## Langkah-langkah Analisis
1. Analis mempelajari `cipher_info.txt` dan menetapkan bahwa cipher terdiri dari dua langkah berurutan: **(1) substitusi monoalfabetik** dengan tabel rahasia tetap, lalu **(2) transposisi kolom** dengan lebar `W`, di-*pad* dengan `_` bila panjang bukan kelipatan `W`.
2. Analis menentukan lebar kolom `W`. Dari panjang sampel (mis. `hello_world` = 11 karakter di-*pad* menjadi 12), analis menyimpulkan **W = 4**.
3. Untuk setiap pasangan sampel, analis melakukan *un-transpose* ciphertext (membaca kembali kolom-demi-kolom menjadi urutan hasil substitusi), lalu menyandingkan tiap huruf plaintext dengan huruf hasil substitusinya untuk membangun tabel pemetaan.
4. Kelima pasangan sampel cukup untuk memulihkan **seluruh 26 huruf** tabel substitusi tanpa konflik:
   - Plain : `abcdefghijklmnopqrstuvwxyz`
   - Cipher: `qwertyuiopasdfghjklzxcvbnm`
   (yakni *keyboard/QWERTY substitution alphabet*).
5. Analis menerapkan proses balikan pada `target.txt` (`y_iwqsettlqokkouh_is`): *un-transpose* (W=4) → `ysqu_eohitk_wtkiqlos`, kemudian substitusi balik (cipher→plain) menghasilkan plaintext yang menjadi flag.

**FLAG:** `flag{cipher_berhasil}`

> Catatan: plaintext hasil dekripsi adalah `flag_cipher_berhasil` (garis bawah sebagai pemisah kata), yang direpresentasikan dalam format flag sebagai `flag{cipher_berhasil}`.
