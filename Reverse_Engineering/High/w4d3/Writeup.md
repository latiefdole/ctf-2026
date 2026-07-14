# Writeup w4d3 — VM8 dengan Bytecode Packed & Subrutin
**Author:** Abdul Latif
**Kategori:** Reverse Engineering (Custom VM + Unpacking)

## Inventarisasi File
**Barang Bukti (Asli):**
- `vm8_chall` (Binary ELF 64-bit — VM 8-opcode, bytecode di-*pack*)
- `vm8_spec.txt` (Spesifikasi arsitektur & opcode VM8)
- `xor_key_hint.txt` (Petunjuk konstanta XOR unpacking)
- `disasm.txt` (Dump disassembly rutin unpacking)

## Langkah-langkah Analisis
1. Analis mempelajari `vm8_spec.txt`: VM stack-based dengan memori 256 slot dan 8 opcode — `PUSH`, `XOR`, `ADD`, `STORE <addr>`, `LOAD <addr>`, `CALL <off>`, `RET`, `PRINT`. Spesifikasi memperingatkan bahwa **bytecode dikemas (XOR)** dan binary menerapkan transformasi tambahan pada output — sehingga nilai asli harus dibaca dari `mem[]`, bukan dari stdout.
2. `xor_key_hint.txt` mengarahkan ke konstanta prima antara 100–130 (versi OS oktal→desimal). Namun analis memverifikasi langsung lewat `disasm.txt`: rutin unpacking di `0x1080` melakukan `mov edi, 0x77777777`, `pxor xmm0, xmm1`, dan `xor edx, 0x77` — mengungkap bahwa **kunci XOR sebenarnya `0x77` (119)**. (Petunjuk "prima 100–130" merupakan pengecoh; kunci nyata terbaca di kode.)
3. Analis mengekstrak *packed bytecode* dari `.rodata` (setelah tabel string & jump table, ditandai pola `76 4e 76 1d ...`), sepanjang 238 byte.
4. Analis meng-*unpack* bytecode: `byte ^ 0x77`. Hasilnya menjadi program VM8 yang valid (opcode `0x01`–`0x08`).
5. Analis mengimplementasikan emulator VM8 penuh — termasuk `CALL`/`RET` dengan *call stack* untuk subrutin. Alih-alih memercayai stdout (yang ditransformasi), analis **membaca `mem[]` secara langsung** setelah eksekusi. Isi memori merangkai flag utuh, mengonfirmasi tema "subrutin ter-unpack".

**FLAG:** `flag{vm8_subroutine_unpacked}`
