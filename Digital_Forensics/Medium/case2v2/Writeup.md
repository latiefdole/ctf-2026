# Writeup case2v2
**Author:** Abdul Latif

## Inventarisasi File
**Barang Bukti (Asli):**
- `kode_akses` (File executable tanpa ekstensi/format ELF)

**Tools/Skrip/Output Analis:**
- `analyze.py` (Skrip penganalisa buatan analis)
- `decode.py` (Skrip dekripsi buatan analis)
- `solve_strings.py` (Skrip alat pengekstraksi string buatan analis)

## Langkah-langkah Analisis
1. Analis menginspeksi wujud fisik file barang bukti `kode_akses`. Melalui pengecekan *magic bytes* atau eksekusi perintah tipe file, analis mengonfirmasi bahwa file ini adalah sebuah *executable binary* dalam format ELF (Executable and Linkable Format).
2. Analis berasumsi bahwa file eksekusi ini memiliki *hardcoded strings* di dalam komponen memorinya. Sebagai solusinya, analis membuat serangkaian program pembantu (skrip Python seperti `solve_strings.py` / `analyze.py`) guna membongkar keseluruhan karakter ASCII yang dapat dicerna visual manusia layaknya *tools* `strings`.
3. Analis menyaring ratusan baris *output* hasil ekstraksi string, dan atensinya tertuju pada sebuah gumpalan teks Base64 yang tidak wajar: `ZmxhZ3trMGQzXzRrczNzX2swbXB1dDFuZDAhfQ==`.
4. Menyimpulkan bahwasanya teks tersebut menyimpan informasi rahasia (*encoded*), analis menyusun skrip kecil tambahan (`decode.py`) ataupun mengeksekusi konversi Base64 melalui perintah *shell*.
5. Transformasi *decoding* langsung menelanjangi wujud teks orisinal yang notabenenya adalah letak *flag* jawaban bagi sesi investigasi ini.

**FLAG:** `flag{k0d3_4ks3s_k0mput1nd0!}`
