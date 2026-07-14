# Writeup w3d3 — VM v2 dengan JMP Trap
**Author:** Abdul Latif
**Kategori:** Reverse Engineering (Custom VM)

## Inventarisasi File
**Barang Bukti (Asli):**
- `vm2_chall` (Binary ELF 64-bit — VM v2 "Pelindung Payload Elang")
- `vm2_spec.txt` (Spesifikasi opcode VM v2)

**Tools/Skrip/Output Analis:**
- `analyze_vm2_binary.py` (Parser section + disassembler + dump `.rodata`)
- `simulate_vm2.py` (Emulator VM v2 dengan penanganan JMP signed)

## Langkah-langkah Analisis
1. Analis membaca `vm2_spec.txt` dan memetakan enam opcode: `0x01 PUSH <byte>`, `0x02 POP`, `0x03 XOR`, `0x04 PRINT`, `0x05 JMP <offset signed>`, `0x06 HALT`. Poin krusial: **offset JMP adalah signed 8-bit** (nilai > 127 = lompat mundur).
2. Dengan `analyze_vm2_binary.py`, analis mengurai header ELF, men-disassembly `.text`, dan mendump `.rodata`. Program memerlukan password sebagai `argv[1]` sebelum menjalankan interpreter.
3. Analis mengekstrak *bytecode* VM (247 byte) dari `.rodata` mulai offset internal `0x40`.
4. Analis mengimplementasikan emulator (`simulate_vm2.py`) yang menangani **JMP dengan aritmetika PC signed** (`pc = pc + 2 + offset`, offset dikoreksi ke rentang -128..127). Tanpa penanganan tanda ini, alur eksekusi akan tersesat — inilah "JMP trap" yang menjadi tema tantangan.
5. Analis menjalankan emulasi mode operand mentah. Dengan penanganan lompatan yang benar, urutan `PRINT` merangkai flag secara utuh (mode *lookup* menghasilkan sampah, mengonfirmasi mode mentah yang benar).

**FLAG:** `flag{vm2_jmp_trap_diatasi}`
