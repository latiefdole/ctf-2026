# Writeup w4a1 — Serangan Wiener (Kunci Privat RSA Kecil)
**Author:** Abdul Latif
**Kategori:** Cryptography / RSA

## Inventarisasi File
**Barang Bukti (Asli):**
- `pubkey.txt` (Kunci publik RSA: modulus `n` ~1024-bit dan eksponen `e` sangat besar)
- `ciphertext.txt` (Ciphertext `c` hasil enkripsi RSA)

**Tools/Skrip/Output Analis:**
- `solve_w4a1.py` (Implementasi serangan Wiener via *continued fractions*)

## Langkah-langkah Analisis
1. Analis membaca `pubkey.txt` dan mengamati anomali: eksponen publik `e` berukuran hampir sebesar modulus `n`. Kondisi `e ≈ n` merupakan indikator kuat bahwa eksponen privat `d` bernilai **kecil**.
2. Analis mengidentifikasi kerentanan sebagai **Wiener's Attack**. Teorema Wiener menyatakan bila `d < (1/3)·n^(1/4)`, maka `d` dapat dipulihkan secara efisien dari fraksi berkelanjutan (*continued fractions*) dari `e/n`.
3. Analis menghitung koefisien *continued fraction* dari `e/n` dan menghasilkan deret *convergents* `k/d` secara berurutan.
4. Untuk tiap *convergent*, analis menebak `φ(n) = (e·d − 1) / k`, lalu menyusun persamaan kuadrat `x² − (n − φ(n) + 1)·x + n = 0` untuk menguji apakah akarnya menghasilkan faktorisasi `p·q = n` yang valid.
5. *Convergent* yang benar memulihkan `d = 1124952985623315647`. Analis mendekripsi `c` dengan `m = c^d mod n`, kemudian mengonversi `m` ke bytes untuk memperoleh flag.

**FLAG:** `flag{wiener_kunci_kecil_terekspos}`
