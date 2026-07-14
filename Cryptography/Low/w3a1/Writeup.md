# Writeup w3a1 — Rekonstruksi Kunci XOR Konfigurasi Malware
**Author:** Abdul Latif
**Kategori:** Cryptography / Malware Analysis

## Inventarisasi File
**Barang Bukti (Asli):**
- `config.bin` (Blob konfigurasi malware yang ter-obfuscate)
- `key_hint.txt` (Catatan analis mengenai infrastruktur C2)
- `decode_stub.c` (Potongan decoder dari laporan analisis — kunci XOR diredaksi)

**Tools/Skrip/Output Analis:**
- `decode_config.py` (Skrip Python untuk merekonstruksi kunci dan mendekode config)

## Langkah-langkah Analisis
1. Analis meninjau `decode_stub.c` dan memahami format kontainer: file terdiri atas rangkaian entri, di mana setiap entri diawali *header* panjang 2-byte (uint16 *little-endian*), diikuti *payload* sepanjang nilai tersebut. Setiap payload di-XOR dengan kunci 4-byte yang berulang (`buf[i] ^= key[i % 4]`).
2. Dari `key_hint.txt`, analis mengetahui bahwa kunci XOR 4-byte merupakan representasi *little-endian* dari nomor port C2 `7080` desimal. Nilai `7080` = `0x1BA8`.
3. Analis menyusun kunci dalam format *little-endian* 4-byte: `[0xA8, 0x1B, 0x00, 0x00]`, konsisten dengan petunjuk bahwa byte pertama adalah `0xA8` (168 desimal).
4. Analis mengimplementasikan skrip `decode_config.py` yang mem-parsing tiap entri (baca panjang → baca payload → XOR dengan kunci berulang) lalu mencetak hasil dekode sebagai UTF-8.
5. Eksekusi skrip mengungkap daftar string konfigurasi C2 (`sistem_kendali_utama`, `jaringan_distribusi_data`, `modul_enkripsi_protokol`, `koneksi_server_cadangan`) dan menyisipkan *flag* di salah satu entri.

**FLAG:** `flag{emotet_xor_config_terbaca}`
