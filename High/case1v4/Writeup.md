# Writeup case1v4
**Author:** Abdul Latif

## Inventarisasi File
**Barang Bukti (Asli):**
- `func_table` (File binary berformat ELF)
- `disasm.txt` (File dump instruksi assembly dari tantangan)

**Tools/Skrip/Output Analis:**
- `solve_xor.py` (Skrip analisis buatan analis untuk proses ekstraksi dan *decoding*)

## Langkah-langkah Analisis
1. Analis melakukan inventarisasi file pada direktori dan memeriksa barang bukti utama, yakni *executable* binary `func_table` beserta *dump* disassembly-nya pada file `disasm.txt`.
2. Melalui penelusuran secara cermat pada `disasm.txt`, analis mempelajari alur logika bahasa mesin yang digunakan program. Terdapat indikasi jelas mengenai proses encoding teks, kalkulasi memori, atau manipulasi *string* di tahap *runtime*.
3. Setelah memahami mekanisme kerjanya, analis mulai melakukan analisis statik terhadap *binary* `func_table`. Analis mengembangkan skrip khusus bernama `solve_xor.py` yang berfungsi memindai dan mengekstrak *string* bermakna dari blok *data* di dalam binary file tersebut.
4. Pada hasil pindaian *string*, analis mendeteksi adanya teks tunggal dengan pola alfanumerik yang sangat khas sebagai format Base64: `ZmxhZ3tyM3YzcnMzbTRzdDNyfQ==`.
5. Analis lantas mengimplementasikan fungsi dekode Base64 (bisa melalui terminal Linux, CyberChef, atau disisipkan ke dalam skrip Python-nya) pada *string* tersebut.
6. Luaran dekoding secara eksplisit menghasilkan bentuk *plaintext* yang sekaligus bertindak sebagai solusi *flag* dari insiden ini.

**FLAG:** `flag{r3v3rs3m4st3r}`
