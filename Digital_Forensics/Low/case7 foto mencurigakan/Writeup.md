# Write-up CTF Digital Forensics: Kasus 7 (Foto Mencurigakan)

**Author:** Abdul Latif
**Kategori:** Digital Forensics / Steganography

---

## 1. Deskripsi Kasus

Pada kasus ini, kita diberikan sebuah file gambar yang diduga digunakan sebagai sarana komunikasi rahasia oleh seorang karyawan di PT Cahaya Digital. Berdasarkan instruksi singkat dari tim SOC (Security Operations Center), file gambar tersebut dicurigai mengandung muatan data atau file tersembunyi yang disisipkan melalui teknik steganografi.

## 2. Inventarisasi File

**Barang Bukti (Asli) dari CTF:**
- `readme_analis.txt` (Catatan pengantar dari tim SOC)
- `foto_kantor.jpg` (File gambar utama yang dicurigai mengandung muatan tersembunyi)

**Tools/Skrip/Output Analis (Bukan Bukti Asli):**
- `steghide.zip` dan folder ekstraksinya (Aplikasi pihak ketiga `steghide` yang diunduh dan digunakan analis untuk ekstraksi data)
- `steghide_extract.py`, `stego_check.py` (Skrip Python buatan analis untuk mengotomatisasi ekstraksi)
- `hidden.txt` (File output hasil ekstraksi payload oleh analis)

## 3. Metodologi / Langkah Penyelesaian (Step-by-Step)

**Langkah 1: Analisis Catatan Awal**
Analis mulai dengan membaca `readme_analis.txt` yang secara spesifik menyebutkan bahwa foto `foto_kantor.jpg` mungkin memiliki file tersembunyi di dalamnya. Ini adalah petunjuk kuat ke arah teknik steganografi.

**Langkah 2: Menyiapkan Tool Analisis**
Karena ekstensi file adalah `.jpg`, salah satu algoritma/program steganografi yang paling umum digunakan adalah **Steghide**. Analis mengunduh tool `steghide` (`steghide.zip`) dan menempatkannya di lingkungan kerja lokal untuk dioperasikan (mengingat tool ini bukan bawaan dari tantangan).

**Langkah 3: Mengekstrak Data Tersembunyi**
Analis menjalankan perintah `steghide extract -sf foto_kantor.jpg -p ""` (menggunakan kata sandi kosong, yang merupakan vektor serangan awal paling standar pada CTF steganografi). Proses ini berhasil mendeteksi dan mengekstrak sebuah file teks tersembunyi ke direktori aktif.

**Langkah 4: Mendapatkan Flag**
File hasil ekstraksi tersebut diberi nama `hidden.txt`. Saat isi file dibaca, di dalamnya langsung tercetak teks dengan format flag standar. 

## 4. Hasil Analisis / Flag

Analis sukses mengungkap data komunikasi tersembunyi di dalam gambar.

**Flag:** `flag{st3gh1d3_k4nt0r_2026_f0und}`
