# Writeup w3b2 — Investigasi Kelompok "Elang Merah"
**Author:** Abdul Latif
**Kategori:** OSINT / Recon

## Inventarisasi File
**Barang Bukti (Asli):**
- `index.html`, `tentang.html`, `kasus_aktif.html` (Halaman situs target)
- `attacker_site.html` (Situs pelaku — berisi komentar HTML tersembunyi)
- `internal_doc.pdf.txt` (Dokumen internal — mendefinisikan format passphrase)
- `linkedin_export.html` (Ekspor profil LinkedIn operator)
- `profile_photo.jpg` (Foto profil — berisi metadata EXIF GPS)
- `config_leak.txt` (Konfigurasi C2 bocor)
- `whois_record.txt`, `email_thread.txt` (Artefak pendukung)

## Langkah-langkah Analisis
1. Dari `internal_doc.pdf.txt`, analis menetapkan **format passphrase operasional**: `elang_<PART2>_<PART3>`. Tiga komponen ini harus dipulihkan dari artefak terpisah.
2. **Awalan (`elang`)** — pada `attacker_site.html` ditemukan komentar HTML: `<!-- Base64 token: ZWxhbmc= -->`. Decode Base64 `ZWxhbmc=` → **`elang`**.
3. **Komponen kedua (`<PART2>`)** — analis menelusuri `linkedin_export.html`, kolom keahlian memuat string hex `6d65726168`. Decode hex → **`merah`**. (Analisis EXIF GPS pada `profile_photo.jpg` memberi koordinat Samarinda sebagai jalur alternatif, namun jalur LinkedIn yang terverifikasi benar.)
4. **Komponen ketiga (`<PART3>`)** — dari `config_leak.txt` bagian `[Auth]`: `passphrase_part3 = cmVrdXQK`. Decode Base64 → **`rekut`** (byte asli diakhiri newline `\n`).
5. Analis merangkai ketiga komponen: `elang` + `_` + `merah` + `_` + `rekut`.

**FLAG:** `flag{elang_merah_rekut}`
