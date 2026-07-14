# Writeup w4d1 — Pemeriksa Kredensial (Python Bytecode)
**Author:** Abdul Latif
**Kategori:** Reverse Engineering (Python `.pyc`)

## Inventarisasi File
**Barang Bukti (Asli):**
- `checker.pyc` (Bytecode Python 3.8 terkompilasi)

**Tools/Skrip/Output Analis:**
- `solve_w4d1.py` (Skrip rekonstruksi flag)

## Langkah-langkah Analisis
1. Analis mengidentifikasi `checker.pyc` sebagai bytecode **Python 3.8** berdasarkan *magic bytes* header `55 0d 0d 0a`.
2. Analis melakukan dekompilasi (mis. `uncompyle6` / `decompyle3`) untuk merekonstruksi kode sumber. Ditemukan fungsi `check_flag` yang memverifikasi input pengguna terhadap flag yang direkonstruksi saat runtime.
3. Analis membedah skema penyembunyian flag:
   1. Sebuah string Base64 tertanam: `V11QVkpTSEVUWl5VVG5FVENCVFxTRF9IWG4CAEw=`.
   2. Hasil Base64-decode kemudian **di-XOR byte-per-byte dengan kunci integer `49`** (`0x31`).
4. Analis mereplikasi proses (`solve_w4d1.py`): decode Base64 → XOR tiap byte dengan `49` → hasilkan *plaintext* flag.
5. Nilai kunci `49` sekaligus muncul sebagai bagian dari flag (`_31` dalam heksadesimal `0x31 = 49`), menegaskan solusi.

**FLAG:** `flag{bytekode_tersembunyi_31}`
