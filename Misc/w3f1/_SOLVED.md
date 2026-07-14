# w3f1: SCADA Industrial Communication Protocol — SOLVED ✅

Target: `w3f1/protocol_log.bin` (binary log file)

## 🚩 FLAG
```
flag{protokol_biner_terbaca}
```

## Analisis & Solusi

### 1. Spesifikasi Protokol (SICP)
Berdasarkan spesifikasi di [protocol_spec.txt](file:///C:/Users/ICT-12/Documents/CTF/w3f1/protocol_spec.txt):
- **Magic**: `0xDE 0xAD` (2 byte)
- **Type**: `0x03` = FLAG (1 byte)
- **Length**: 2 byte (big-endian)
- **Payload**: `<Length>` byte (mengandung flag yang di-base64-encode)

### 2. Solusi Pemrosesan
Menggunakan skrip penuntas [solve_w3f1.py](file:///C:/Users/ICT-12/Documents/CTF/w3f1/solve_w3f1.py):
- Membaca file log biner `protocol_log.bin`.
- Mencari magic number `0xDE 0xAD`.
- Jika ditemukan tipe pesan `0x03` (FLAG), membaca payload sepanjang `Length` byte.
- Melakukan base64-decode terhadap payload.
- Hasil decoding menghasilkan flag: `flag{protokol_biner_terbaca}`
