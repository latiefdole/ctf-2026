# w4d1: Pemeriksa Kredensial — SOLVED ✅

Target: `w4d1/checker.pyc` (Python 3.8 compiled bytecode)

## 🚩 FLAG
```
flag{bytekode_tersembunyi_31}
```

## Analisis & Solusi

### 1. Reverse Engineering Python Bytecode
- Target file `checker.pyc` diidentifikasi sebagai bytecode Python 3.8 berdasarkan magic bytes header `55 0d 0d 0a`.
- Menggunakan decompiler `uncompyle6` untuk merekonstruksi kode sumber Python.

### 2. Algoritma Verifikasi
- Fungsi `check_flag` memverifikasi input pengguna terhadap flag yang dikomparasi setelah didekripsi.
- Skema enkripsi:
  1. Base64-decode terhadap string `V11QVkpTSEVUWl5VVG5FVENCVFxTRF9IWG4CAEw=`.
  2. XOR setiap byte dengan key bernilai integer `49`.
  3. Hasil decoding menghasilkan flag: `flag{bytekode_tersembunyi_31}`.

### 3. Skrip Solusi
Skrip lengkap di [solve_w4d1.py](file:///C:/Users/ICT-12/Documents/CTF/w4d1/solve_w4d1.py).
