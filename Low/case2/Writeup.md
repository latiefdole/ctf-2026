# Writeup case2
**Author:** Abdul Latif

## Inventarisasi File
**Barang Bukti (Asli):**
- `analyst_note.txt` (Catatan investigasi dari soal)
- `encoded_memo.txt` (File memo rahasia)
- `server_log.txt` (Log server jaringan)

**Tools/Skrip/Output Analis:**
- `solve_case2.py` (Skrip Python untuk dekoding bertingkat buatan analis)

## Langkah-langkah Analisis
1. Analis mengawali respons insiden dengan mengevaluasi `analyst_note.txt`. Di dalamnya tertera petunjuk eksplisit untuk berfokus pada file `encoded_memo.txt`, beserta sebuah detail teknis penting bahwa terdapat "DUA LAPISAN encoding umum" (*double layered encoding*).
2. Analis meninjau struktur data dari `encoded_memo.txt`. Berdasarkan *character set* alfanumerik (A-Z, a-z, 0-9) dan kehadiran karakter *padding* ekor ganda (`==`), analis menetapkan bahwa lapisan *encoding* pertama adalah Base64.
3. Setelah analis melakukan proses decoding Base64 secara manual/dengan skrip, teks keluaran masih berbentuk acak, namun tetap mempertahankan bentuk jarak spasi dan tanda bacanya. Pola ini mengarah pada *cipher* substitusi *shift* klasik: ROT13.
4. Guna merampingkan alur kerjanya, analis merancang skrip python `solve_case2.py`. Skrip ini mengimplementasikan dua tahapan logika secara otomatis: membaca file -> melakukan pembalikan Base64 -> melakukan pembalikan ROT13 (atau sejenis algoritma Caesar shift).
5. Analis menjalankan skrip tersebut. Eksekusi ini merestorasi status *memo* sepenuhnya menjadi pesan *plaintext* yang bisa dibaca dan membeberkan *flag* secara gamblang di badan pesan.

**FLAG:** `flag{d0ubl3_l4y3r_m3m0_d3c0d3d}`
