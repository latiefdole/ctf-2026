# Writeup w3f1 — Protokol Komunikasi SCADA (SICP)
**Author:** Abdul Latif
**Kategori:** Misc / Protocol Analysis

## Inventarisasi File
**Barang Bukti (Asli):**
- `protocol_log.bin` (Log komunikasi biner protokol SCADA)
- `protocol_spec.txt` (Spesifikasi parsial protokol SICP hasil analisis lalu lintas jaringan)

**Tools/Skrip/Output Analis:**
- `solve_w3f1.py` (Parser protokol biner + decoder base64)

## Langkah-langkah Analisis
1. Analis mempelajari `protocol_spec.txt` dan memetakan **format pesan SICP** (SCADA Industrial Communication Protocol):
   - **Magic:** 2 byte tetap `0xDE 0xAD` (penanda awal pesan)
   - **Type:** 1 byte — `0x01` HEARTBEAT, `0x02` DATA, `0x03` FLAG, `0x04` CLOSE
   - **Length:** 2 byte *big-endian* (panjang payload)
   - **Payload:** sepanjang `Length` byte
2. Analis mengimplementasikan parser (`solve_w3f1.py`) yang menyusuri `protocol_log.bin`: mencari magic `0xDE 0xAD`, membaca `Type` & `Length`, lalu mengekstrak payload, dan melompat ke pesan berikutnya (`offset += 5 + Length`).
3. Analis menelusuri seluruh pesan dalam log. Ditemukan urutan HEARTBEAT (timestamp 4 byte) dan DATA berisi status operasional Bahasa Indonesia (`"Sistem berjalan normal"`, `"Monitoring aktif"`, `"Koneksi stabil"`), diakhiri pesan CLOSE.
4. Analis menemukan **satu-satunya pesan bertipe `0x03` (FLAG)** dengan payload ter-encode Base64:
   `ZmxhZ3twcm90b2tvbF9iaW5lcl90ZXJiYWNhfQ==`
5. Analis melakukan Base64-decode terhadap payload FLAG, menghasilkan *plaintext* flag.

**FLAG:** `flag{protokol_biner_terbaca}`
