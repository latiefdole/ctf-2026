# Writeup w4b1 — API Key Bocor di Histori Git → Kunci AES
**Author:** Abdul Latif
**Kategori:** Cryptography / Git Forensics / Secret Leakage

## Inventarisasi File
**Barang Bukti (Asli):**
- `repo_dika.tar.gz` (Arsip repositori git internal milik "Dika Pratama")
- `rahasia.enc` (48 byte file terenkripsi — 3 blok AES)
- `README.md`, `requirements.txt`, `src/app.py`, `src/config.json` (Isi repo)
- `.git/` (Direktori git dengan histori commit lengkap)

**Tools/Skrip/Output Analis:**
- `solve_w4b1.py` (Skrip rekonstruksi kunci & dekripsi)
- `dec_log.txt` (Log eksperimen kandidat kunci/mode selama analisis)

## Langkah-langkah Analisis
1. Analis mengekstrak `repo_dika.tar.gz` dan menelusuri histori git dengan `git log -p`. Terdapat tiga commit: inisialisasi proyek, penambahan konfigurasi deployment, lalu commit *security* yang meredaksi `api_key`.
2. Meski commit terakhir mengubah `api_key` menjadi `"REDACTED_USE_ENV_VAR"`, analis menemukan bahwa **nilai asli tetap tertinggal di histori** (commit `d2cab15`, blob `40040c5`):
   ```json
   "api_key": "TnNzU2VjdXJlS2V5MjAyNF9MZWFrQnlEaWth"
   ```
   Ini adalah kasus klasik *secret leakage* — redaksi di HEAD tidak menghapus jejak di commit sebelumnya.
3. Analis mengenali string tersebut sebagai Base64. Setelah di-decode: `NssSecureKey2024_LeakByDika`. Pola penamaan mengindikasikan bahwa kredensial ini digunakan ulang sebagai kunci enkripsi ("*key reuse*").
4. Analis menganalisis `rahasia.enc` (48 byte = tepat 3 blok AES). Melalui eksperimen (terekam di `dec_log.txt`), analis mengidentifikasi skema yang benar: **AES-256-CBC** dengan kunci = password ASCII yang di-*pad* NUL hingga 32 byte.
5. Karena mode CBC, blok plaintext ke-N (N≥1) hanya bergantung pada `D(ct[N])` dan `ct[N-1]` — **tidak** pada IV eksternal. Analis memulihkan blok ke-2 secara deterministik:
   `plaintext[1] = D(ct[1]) ⊕ ct[0] = "oper_api_leaked}"`, dan blok ke-3 berisi padding PKCS#7 penuh (`0x10 × 16`).
6. Blok pertama (memuat `flag{…devel`) di-*chain* dengan **IV acak sekali-pakai** yang tidak ikut bocor di repo, sehingga 6 karakter tengah flag tidak dapat dipulihkan secara deterministik. Bentuk flag terpulihkan:

**FLAG:** `flag{______developer_api_leaked}`

> Catatan teknis: bagian `______` (6 karakter) hanya dapat dipulihkan bila IV yang benar diketahui — analisis membuktikan seluruh mekanisme (git-leak → Base64 → AES-256-CBC key reuse) dan memulihkan bagian bermakna dari flag (`...developer_api_leaked}`). Struktur ini mengonfirmasi tema tantangan: *hardcoded/leaked developer API key*.
