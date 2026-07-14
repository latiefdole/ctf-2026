# W3-B2: Analisis Investigasi Kelompok Elang Merah — SOLVED ✅

## 🚩 FLAG
```
flag{elang_merah_rekut}
```

---

## 🔍 Pembongkaran Komponen & Analisis Bukti

Berdasarkan dokumen internal yang dipulihkan (`internal_doc.pdf.txt`), kata sandi operasional untuk identifikasi anggota Kelompok Elang Merah mengikuti format:
> **`elang_<PART2>_<PART3>`**

Berikut adalah cara masing-masing komponen di-decode dari artefak yang tersedia:

### 1. Awalan (`elang`)
* **Sumber:** `attacker_site.html`
* **Analisis:** Ditemukan komentar HTML berupa string Base64:
  `<!-- Base64 token: ZWxhbmc= -->`
* **Hasil Decode:** `ZWxhbmc=` → **`elang`**

### 2. Komponen Kedua (`<PART2>`)
Ada dua kemungkinan analisis untuk komponen kedua ini:
* **Analisis A (Lokasi Geografis - Paling Kuat):**
  * **Sumber:** Metadata EXIF pada `profile_photo.jpg`
  * **Analisis:** Koordinat GPS yang tersimpan dalam foto profil operator adalah:
    `S 0° 30' 5.76", E 117° 9' 13.32"` (Decimal: `-0.5016, 117.1537`).
  * **Lokasi:** Koordinat ini merujuk pada area sekitar **Samarinda**, Kalimantan Timur.
  * **Hasil:** **`samarinda`**

* **Analisis B (Keahlian LinkedIn):**
  * **Sumber:** Profil ekspor LinkedIn operator `linkedin_export.html`
  * **Analisis:** Kolom keahlian khusus mencantumkan string hex `6d65726168`.
  * **Hasil Decode:** `6d65726168` → **`merah`**

### 3. Komponen Ketiga (`<PART3>`)
* **Sumber:** Konfigurasi C2 yang bocor `config_leak.txt` pada bagian `[Auth]`
* **Analisis:** Mencantumkan parameter:
  `passphrase_part3 = cmVrdXQK`
* **Hasil Decode:** `cmVrdXQK` → **`rekut`** (terdapat karakter newline `\n` di akhir byte asli).

---

## 🛠️ Langkah Rekonstruksi

Dengan menggabungkan seluruh bagian di atas:
* **Format:** `elang_` + `<PART2>` + `_` + `<PART3>`
* **Kombinasi Terverifikasi (Keahlian LinkedIn):** `elang` + `merah` + `rekut` = **`elang_merah_rekut`** (Benar)
* **Kombinasi Alternatif (Lokasi Geografis):** `elang` + `samarinda` + `rekut` = **`elang_samarinda_rekut`**
