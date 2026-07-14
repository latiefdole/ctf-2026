# Writeup W2-B3 — Konsolidasi Infrastruktur Ancaman
**Author:** Abdul Latif
**Kategori:** OSINT / Recon

## Inventarisasi File
**Barang Bukti (Asli):**
- `index.html`, `robots.txt` (Halaman & disallow list target `3c4819c9-ctf.dsg.id`)
- `whois_dump.txt` (Rekaman WHOIS domain pelaku)
- `linkedin_export.txt`, `attacker_cv.html`, `company_doc.html` (Profil & dokumen)
- `email_thread.txt` (Utas email dengan header mencurigakan)
- `leaked_config.txt` (Konfigurasi bocor berisi `DEPLOY_KEY`)

**Tools/Skrip/Output Analis:**
- `solve_w2b3.py` (Skrip dekripsi XOR berulang)

## Langkah-langkah Analisis
1. Analis membaca `robots.txt` yang membocorkan path tersembunyi: `/whois_dump.txt`, `/leaked_config.txt`, `/company_doc.html`, `/email_thread.txt`. Semua diunduh untuk konsolidasi bukti.
2. Analis menyusun profil pelaku dari korelasi lintas-artefak: nama **Hendra Wicaksono**, alias **RedMist_ID**, domain **redmist-id.net**, berbasis di **Yogyakarta** (WHOIS), domain dibuat tahun **2024**.
3. Target utama ditemukan di `leaked_config.txt`:
   ```
   DEPLOY_KEY=PwMGHhoDUhwQEwZvRQUoDQYpaQFXJhNYBR9FEkZvSwQsQFl7JA==
   KEY_ALGORITHM=custom-xor-b64
   ```
   Base64-decode menghasilkan 37 byte ciphertext yang di-XOR dengan kunci berulang.
4. Analis merekonstruksi kunci XOR dari petunjuk OSINT yang tersebar:
   - `Yogyakarta` (kota dari WHOIS) — 10 char pertama terbukti benar (`flag{h3ndr...`),
   - `2024` (tahun pembuatan domain),
   - `K9mZ` (token bocor, dari X-Mailer-Token `Zm9K0027604071` di `email_thread.txt`).
   Kunci penuh: **`Yogyakarta2024K9mZ`** (18 karakter, berulang).
5. Analis menjalankan dekripsi `byte[i] ^ key[i % 18]`. Seluruh 37 byte terdekripsi bersih menjadi flag yang mengandung identitas pelaku (Hendra, Wicaksono, RedMist, Yogya).

**FLAG:** `flag{h3ndr4_w1c4ks0n0_r3dm1st_y0gy4!}`
