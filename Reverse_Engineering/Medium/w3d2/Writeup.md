# Writeup w3d2 — Anti-Debug & Data Terenkripsi
**Author:** Abdul Latif
**Kategori:** Reverse Engineering (Anti-Debugging)

## Inventarisasi File
**Barang Bukti (Asli):**
- `antidebug` (Binary ELF 64-bit PIE, **stripped** — menerapkan proteksi anti-debug `ptrace`)

**Tools/Skrip/Output Analis:**
- `analyze_elf.py` (Parser header ELF + disassembler Capstone `.text`)
- `dump_data.py` (Ekstraksi & dekripsi blob data terenkripsi)

## Langkah-langkah Analisis
1. Analis mengidentifikasi `antidebug` sebagai ELF 64-bit PIE yang di-*strip*. String `"Tidak dapat dieksekusi."` mengindikasikan adanya *guard* anti-debug — program menolak berjalan bila mendeteksi debugger (`ptrace(PTRACE_TRACEME)` yang gagal → sudah di-trace).
2. Alih-alih menjalankan binary di bawah debugger (yang akan diblokir), analis memilih **analisis statik**. Dengan `analyze_elf.py`, analis mem-parsing tabel section dan men-disassembly `.text` untuk menemukan lokasi data terenkripsi dan konstanta XOR.
3. Analis menemukan blob 32 byte terenkripsi pada segmen `.data` di alamat virtual `0x4040` (file offset 12352), serta operasi dekripsi berupa **XOR byte-per-byte dengan konstanta `0x5A`**.
4. Analis mengekstrak blob tersebut (`dump_data.py`) dan menerapkan `byte ^ 0x5A` pada setiap byte.
5. Hasil dekripsi langsung menghasilkan *plaintext* flag — sekaligus mengonfirmasi bahwa proteksi `ptrace` dapat dilewati sepenuhnya lewat pendekatan statik tanpa mengeksekusi program.

**FLAG:** `flag{antidebug_ptrace_terlewati}`
