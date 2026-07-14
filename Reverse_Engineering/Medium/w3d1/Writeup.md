# Writeup w3d1 — VM Stack Sederhana
**Author:** Abdul Latif
**Kategori:** Reverse Engineering (Custom VM)

## Inventarisasi File
**Barang Bukti (Asli):**
- `vm_chall` (Binary ELF 64-bit — interpreter VM internal)
- `vm_spec.txt` (Spesifikasi opcode VM)

**Tools/Skrip/Output Analis:**
- `solve_w3d1.py` (Ekstraksi bytecode dari `.rodata` + emulator stack VM)

## Langkah-langkah Analisis
1. Analis melakukan *reverse* alur kontrol x86-64. Program membaca `argv[1]` dan membandingkannya (`strcmp`) dengan `"buka_vm"`; bila cocok, eksekusi berlanjut ke interpreter VM internal.
2. Dari `vm_spec.txt`, analis memetakan empat opcode: `0x01 PUSH <byte>`, `0x02 XOR`, `0x03 PRINT`, `0x04 HALT`.
3. Analis mengurai header ELF untuk menemukan section `.rodata`, lalu memindai *bytecode* VM berdasarkan pola tanda tangan `01 XX 01 00 02 03` (PUSH char, PUSH 0x00, XOR, PRINT).
4. Setiap karakter flag diproduksi lewat pola `PUSH <char> ; PUSH 0x00 ; XOR ; PRINT` — karena XOR dengan `0x00` bersifat identitas, byte yang di-push adalah karakter flag apa adanya, diakhiri `0x04 HALT`.
5. Analis mengemulasikan stack VM via `solve_w3d1.py`, dan hasil `PRINT` berurutan merangkai flag.

**FLAG:** `flag{vm_stack_berjalan}`
