#!/usr/bin/env python3
"""
w4d3 — VM8: unpack bytecode (XOR 0x77) lalu emulasikan, baca mem[] langsung.

Kunci XOR = 0x77 (119), terbaca langsung dari rutin unpacking di disasm.txt
(`mov edi, 0x77777777`, `xor edx, 0x77`) — bukan "prima 100-130" seperti hint.
Output stdout ditransformasi, jadi flag dibaca dari memori VM setelah eksekusi.
"""
import struct


def get_packed_bytecode(path="vm8_chall"):
    elf = open(path, "rb").read()
    # .rodata @ file offset 8192, size 398
    rodata = elf[8192:8192 + 398]
    # packed bytecode dimulai pada penanda 76 4e 76 1d ... (setelah string & jump table)
    start = rodata.hex().find("764e761d") // 2
    return rodata[start:]


def run(bc):
    pc, stack, mem, calls, steps = 0, [], [0] * 256, [], 0
    while pc < len(bc) and steps < 100000:
        op = bc[pc]; steps += 1
        if op == 0x01:                       # PUSH <val>
            stack.append(bc[pc + 1]); pc += 2
        elif op == 0x02:                     # XOR
            a, b = stack.pop(), stack.pop(); stack.append(a ^ b); pc += 1
        elif op == 0x03:                     # ADD <val>
            stack.append((stack.pop() + bc[pc + 1]) & 0xFF); pc += 2
        elif op == 0x04:                     # STORE <addr>
            mem[bc[pc + 1]] = stack.pop(); pc += 2
        elif op == 0x05:                     # LOAD <addr>
            stack.append(mem[bc[pc + 1]]); pc += 2
        elif op == 0x06:                     # CALL <off>
            calls.append(pc + 2); pc = bc[pc + 1]
        elif op == 0x07:                     # RET
            if not calls:
                break
            pc = calls.pop()
        elif op == 0x08:                     # PRINT (output ditransformasi -> diabaikan)
            pc += 1
        else:
            break
    return bytes(mem)


def main():
    packed = get_packed_bytecode()
    bc = bytes(b ^ 0x77 for b in packed)     # unpack
    mem = run(bc)
    flag = mem.split(b"\x00")[0].decode("latin1")
    print(f"[+] XOR unpack key : 0x77 (119)")
    print(f"[+] FLAG (dari mem): {flag}")


if __name__ == "__main__":
    main()
