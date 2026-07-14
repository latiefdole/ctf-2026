Catatan Teknis - Sistem Keamanan Akses
======================================
Divisi IT Security PT Nusantara Sistem

File encrypted_note.enc berisi data rahasia yang dienkripsi menggunakan AES-128 CBC.

Prosedur derivasi kunci:
  1. Ambil passphrase dari session yang terekam
  2. Hitung SHA-256 dari passphrase (encoding: UTF-8)
  3. Gunakan 16 byte pertama sebagai kunci AES-128
  4. Untuk IV: hitung SHA-256 dari (passphrase + "iv"), gunakan 16 byte pertama

Catatan: Passphrase adalah string yang diketik pengguna pada sesi keyboard yang
terekam dalam file PCAP. Perhatikan adanya koreksi pengetikan (backspace) dalam
sesi tersebut - gunakan string akhir yang berhasil dimasukkan (setelah koreksi).
