# Writeup w3b3 — Operator Bayangan "n0ct4lys1s"
**Author:** Abdul Latif
**Kategori:** OSINT / Recon (Hard)

## Inventarisasi File
**Barang Bukti (Asli):**
- `index.html`, `profil.html`, `analisis.html` (Halaman navigasi target `5b016909-ctf.dsg.id`)
- `forum_post.html` (Post forum — komentar HTML: epoch `1704067200`, UID-9182)
- `pgp_pubkey.asc` (Kunci publik PGP operator)
- `profile_analysis.txt` (Profil perilaku operator)
- `persona_cross.json` (3 alias: n0ct4lys1s, azure_ghost_77, azknight)
- `operator_note.txt` (**Formula kode operasional**)
- `decoy_token.txt` (Jebakan: `N0CT-4LYS-1S99`)
- `robots.txt` → mengungkap `/archive/` (accessible) & `/private/` (403)
- `archive_archived_post.html` (Berisi kunci sesi)

**Tools/Skrip/Output Analis:**
- `solve.py`, `downloader.py`, `bypass_403.py`, `probe*.py` (Crawler & solver)

## Langkah-langkah Analisis
1. Analis meng-crawl target dan memetakan 6+ artefak publik. `robots.txt` membocorkan `/archive/` (dapat diakses) dan `/private/` (403 Forbidden). Analis mengunduh isi `/archive/`.
2. Dari `operator_note.txt`, analis menemukan **formula kode operasional**:
   ```
   Kode = <Part1>_<Part2>_<Part3>
   Part1 = kunci sesi (dari arsip forum)
   Part2 = konversi epoch join ke format YYYYMMDD
   Part3 = XOR(Part1_pertama_5_char_as_bytes, key_byte=0x1F) lalu hex-encode
   ```
3. **Part1 — kunci sesi:** dari `/archive/archived_post.html`: `756b615f696e757a61`. Sebagai heksadesimal, decode ASCII → `uka_inuza`.
4. **Part2 — epoch → tanggal:** epoch `1704067200` = **2024-01-01 00:00:00 UTC** → **`20240101`**.
5. **Part3 — komputasi XOR:** ambil 5 byte pertama dari Part1 (`u`,`k`,`a`,`_`,`i` = `0x75,0x6b,0x61,0x5f,0x69`), XOR masing-masing dengan `0x1F`, lalu hex-encode → `6a747e4076`.
6. Analis merangkai kode operasional sesuai format flag. `decoy_token.txt` (`N0CT-4LYS-1S99`) sengaja diabaikan sebagai pengecoh.

**FLAG:** `flag{uka_inuza_20240101_6a747e4076}`

> Catatan: Part1 dapat berupa nilai heksadesimal mentah (`756b615f696e757a61`) maupun bentuk ter-decode (`uka_inuza`); kandidat utama menggunakan bentuk ter-decode. Kandidat alternatif didokumentasikan di `_ANALYSIS.md`.
