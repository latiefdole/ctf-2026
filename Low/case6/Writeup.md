# Writeup Case 6

**Author:** Abdul Latif

## Daftar Barang Bukti (Asli)
- `perangkat_lunak_terkunci`

## Langkah-Langkah Penyelesaian:
1. **Identifikasi File**: Barang bukti utama adalah file `perangkat_lunak_terkunci` yang teridentifikasi sebagai executable Linux (ELF) 64-bit.
2. **Ekstraksi String**: Untuk menyelesaikannya, analis membuat skrip Python sebagai tool kustom (pengganti utilitas `strings`) guna mengekstrak karakter-karakter ASCII dari dalam binary tersebut.
3. **Pencarian Pola**: Dari output skrip buatan analis, ditemukan string menarik seperti "=== Verifikasi Lisensi PT Digital Solusi ===" dan sebuah string heksadesimal mencurigakan: `666c61677b6833785f737472316e675f6c3163336e73335f637234636b33647d`.
4. **Dekode Heksadesimal**: Analis kemudian mendekode string heksadesimal tersebut menggunakan fungsi konversi heksadesimal ke teks ASCII.
5. **Mendapatkan Flag**: Hasil dekode heksadesimal mengungkap string flag yang dicari.

**FLAG:** `flag{h3x_str1ng_l1c3ns3_cr4ck3d}`
