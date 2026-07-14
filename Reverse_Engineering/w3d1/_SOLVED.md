# w3d1: Validator Terselubung — SOLVED ✅

Target: `w3d1/vm_chall` (ELF 64-bit binary)

## 🚩 FLAG
```
flag{vm_stack_berjalan}
```

## Analisis & Solusi

### 1. Reverse Engineering Kontrol Alur (x86_64)
- Program menerima argumen pertama (`argv[1]`) dan membandingkannya dengan string `"buka_vm"` menggunakan `strcmp`.
- Jika argumen bernilai `"buka_vm"`, program melanjutkan eksekusi ke interpreter VM internal.

### 2. Spesifikasi Bytecode VM
Berdasarkan spesifikasi di [vm_spec.txt](file:///C:/Users/ICT-12/Documents/CTF/w3d1/vm_spec.txt):
- `0x01 PUSH <byte>`
- `0x02 XOR`
- `0x03 PRINT`
- `0x04 HALT`

### 3. Ekstraksi Bytecode dari `.rodata`
Bytecode terletak di bagian `.rodata` dengan pola:
```
01 66 01 00 02 03
01 6c 01 00 02 03
...
```
- Setiap karakter di-decode dengan melakukan `PUSH <char_byte>`, `PUSH 0x00`, `XOR`, dan `PRINT`.
- Diakhiri dengan opcode `0x04` (HALT).

### 4. Eksekusi Emulasi
Menggunakan skrip penuntas [solve_w3d1.py](file:///C:/Users/ICT-12/Documents/CTF/w3d1/solve_w3d1.py):
- Mengekstrak bytecode dari ELF segment `.rodata`.
- Mengemulasikan stack VM.
- Hasil decoding menghasilkan flag: `flag{vm_stack_berjalan}`
