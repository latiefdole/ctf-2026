# Writeup w2d2 — Validator Triple Transform
**Author:** Abdul Latif
**Kategori:** Reverse Engineering (x86-64 ELF)

## Inventarisasi File
**Barang Bukti (Asli):**
- `validator` (Binary ELF 64-bit, *not stripped* — meminta "kode validator")

## Langkah-langkah Analisis
1. Analis memeriksa tipe berkas `validator` (ELF 64-bit x86-64, tidak di-strip) dan mengekstrak string. Ditemukan prompt `"Masukkan kode validator:"`, pesan sukses `"Validasi berhasil!"`, pesan gagal `"Validasi gagal."`, simbol fungsi `validate_input`, dan sebuah string base64 mencurigakan.
2. Analis melakukan disassembly (Capstone) atas `validate_input @ 0x40147f`. Alur fungsi memanggil tiga transformasi berurutan terhadap input pengguna, lalu membandingkan hasilnya dengan `strcmp` terhadap string target tetap `fSFwdTBpdnE0dXdfM29zMXV3X3UwdzRn`.
3. Analis membedah tiap tahap transformasi:
   - **Tahap 1 — `sub 0x3` (fungsi 0x401312):** untuk setiap huruf `a–z` / `A–Z`, program menghitung `(c - base + 3) mod 26` — yakni **Caesar shift +3**. Karakter non-alfabet dibiarkan.
   - **Tahap 2 — reverse (fungsi 0x401413):** menyalin string secara terbalik (`out[i] = in[len-1-i]`), **membalik urutan** karakter.
   - **Tahap 3 — Base64 encode:** hasilnya dikodekan Base64 sebelum dibandingkan.
4. Analis membalik pipeline pada string target: **Base64-decode** → **reverse** → **Caesar -3**, sehingga memperoleh kode validator yang diterima: `d4t0r_tr1pl3_tr4nsf0rm!}`.
5. Analis memverifikasi arah maju: `caesar+3 → reverse → base64` atas kode tersebut menghasilkan persis string target. Dengan menambahkan prefiks bertema, kode ini merekonstruksi flag utuh (`v4li` + `d4t0r...` = "validator triple transform").

**FLAG:** `flag{v4lid4t0r_tr1pl3_tr4nsf0rm!}`

> Catatan: rutin `strcmp` memvalidasi 24-byte badan flag (`d4t0r_tr1pl3_tr4nsf0rm!}`) hasil dekode target base64. String `VALIDATOR-OK-2026` yang ikut tertanam merupakan pengecoh.
