# Write-up CTF Digital Forensics: Kasus Laporan Redacted (INC-2025-Q4-0041)

**Author:** Abdul Latif
**Kategori:** Digital Forensics / SIGINT

---

## 1. Deskripsi Kasus

Kasus ini berkisar pada laporan insiden (INC-2025-Q4-0041) yang sudah diredaksi (redacted). Kita diberikan beberapa file terkait laporan tersebut, termasuk halaman web dan catatan korespondensi email, serta catatan mentah dari investigasi pribadi penulis laporan, Rizal Hakim (EMP-8847). Tujuan kita adalah mencari informasi yang disembunyikan/dieksfiltrasi.

## 2. Inventarisasi File

**Barang Bukti (Asli):**
- `index_dl.html` (Halaman utama blog peneliti keamanan)
- `redacted_report.html` (Laporan insiden yang sudah diredaksi)
- `email_thread_dl.txt` (Arsip korespondensi email terkait laporan)
- `profile.jpg` (Foto avatar Rizal Hakim)
- `notes_raw.html` (Data rekaman mentah/raw signal dari investigasi)
- `operator_note.txt` (Catatan petunjuk dari operator SIGINT)
- `signal.txt` (Sampel sinyal yang disadap)
- `static_noise.txt` (Data *noise*/gangguan)

**Tools/Skrip/Output Analis:**
- `analyze_redacted.py`, `analyze2.py`, `analyze3.py` (Skrip python buatan analis untuk mengecek metadata dan elemen HTML tersembunyi).
- `jpeg_analyze.py` (Skrip analis untuk membaca metadata EXIF JPEG).
- `signal_raw.py` (Skrip python buatan analis untuk mengekstrak pesan morse dari file HTML).

## 3. Metodologi / Langkah Penyelesaian (Step-by-Step)

**Langkah 1: Analisis Laporan dan Email**
Barang bukti awal berupa `redacted_report.html` dan `email_thread_dl.txt` diperiksa. Pada laporan, terdapat banyak informasi yang diredaksi (seperti nama klien dan ID karyawan target: EMP-8847). Analis membuat skrip ekstraksi untuk mencari data tersembunyi atau *zero-width spaces* di dalam HTML, namun tidak ditemukan *flag* di sana. 

**Langkah 2: Menghubungkan Bukti Tambahan**
Analis menemukan petunjuk tambahan berupa `notes_raw.html` yang secara eksplisit menyebutkan "Catatan Investigasi Pribadi - Rizal Hakim" untuk "INC-2025-Q4-0041". Di dalamnya terdapat dua blok sinyal. Berdasarkan `operator_note.txt`, analis diminta untuk fokus pada data sinyal (`signal.txt`) dan mengabaikan gangguan (`static_noise.txt`). 

**Langkah 3: Pembuatan Skrip Ekstraktor**
Melihat adanya format titik dan garis pada `notes_raw.html`, analis menyimpulkan bahwa data tersebut disandikan menggunakan Sandi Morse (*Morse Code*). Analis kemudian menggunakan skrip `signal_raw.py` yang dibuatnya untuk mem-parsing tag HTML spesifik dan mengekstrak sinyal tersebut.

**Langkah 4: Decoding Sandi Morse**
Terdapat dua sinyal yang di-*decode* oleh analis:
- **Sinyal A:** `-... ..- -.- .- -. / ..-. .-.. .- --. / .. -. .. -.-.--` yang berarti `BUKAN FLAG INI!`
- **Sinyal B:** `.-. .---- --.. ....- .-.. / .... ....- -.- .---- -- / ...-- -- .--. / ---.. ---.. ....- --... -.-.--` yang berarti `R1Z4L H4K1M 3MP 8847!`

**Langkah 5: Konfirmasi Flag**
Sinyal B dengan jelas mengungkap identitas asli dan ID karyawan dari target (Rizal Hakim / EMP-8847), yang juga diredaksi pada laporan. Ini adalah *flag* yang dicari.

## 4. Hasil Analisis / Flag

**Flag:** `flag{R1Z4L_H4K1M_3MP_8847!}`
