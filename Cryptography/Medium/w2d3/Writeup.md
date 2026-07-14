# Writeup w2d3 — Dekripsi Darurat
**Author:** Abdul Latif
**Kategori:** Cryptography / Reverse Engineering

## Inventarisasi File
**Barang Bukti (Asli):**
- `dekripsi_darurat` (Binary ELF 64-bit, tidak di-strip — meminta "kunci pemulihan")
- `indonesian_phrases.txt` (Wordlist berisi 188 frasa bahasa Indonesia)

## Langkah-langkah Analisis
1. Analis memeriksa tipe berkas `dekripsi_darurat` dan memastikan bahwa file tersebut merupakan *executable* ELF 64-bit (`x86-64`, *not stripped*). Ketika dijalankan, program meminta input berupa **"Masukkan kunci pemulihan:"**.
2. Karena binary tidak di-strip, analis melakukan ekstraksi *string* pada segmen data. Ditemukan beberapa untai penting: fungsi `verify_key`, pesan sukses `"Verifikasi berhasil. Menampilkan kunci dekripsi darurat..."`, pesan gagal `"Kunci pemulihan tidak valid."`, dan yang paling krusial — untai *flag* yang tertanam langsung di dalam biner.
3. Program membandingkan input pengguna terhadap sebuah kunci rahasia melalui rutin `verify_key`. Analis menautkan berkas pendamping `indonesian_phrases.txt` sebagai *dictionary* kandidat kunci pemulihan.
4. Frasa **"langit biru nusantara"** (baris ke-103 pada wordlist) merupakan kunci pemulihan yang valid — hal ini dikuatkan oleh kemunculan *flag* dalam bentuk *leetspeak* dari frasa yang sama persis di dalam binary.
5. Setelah verifikasi kunci berhasil, program menampilkan *flag* dekripsi darurat. Bentuk flag adalah transformasi *leet* dari "langit biru nusantara": huruf `a→4`, `i→1`.

**FLAG:** `flag{l4ng1t_b1ru_nus4nt4r4!}`
