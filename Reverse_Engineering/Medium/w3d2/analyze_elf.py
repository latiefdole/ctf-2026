import struct
import sys
from capstone import *

def analyze_elf(filepath):
    with open(filepath, 'rb') as f:
        elf = f.read()
    
    # Verify ELF magic
    if elf[:4] != b'\x7fELF':
        print("Not an ELF file")
        return
        
    # ELF64 Header structure
    # e_type: 16, e_machine: 17-18, e_version: 19-22, e_entry: 24-31, e_phoff: 32-39, e_shoff: 40-47
    e_entry = struct.unpack('<Q', elf[24:32])[0]
    e_shoff = struct.unpack('<Q', elf[40:48])[0]
    e_shentsize = struct.unpack('<H', elf[58:60])[0]
    e_shnum = struct.unpack('<H', elf[60:62])[0]
    e_shstrndx = struct.unpack('<H', elf[62:64])[0]
    
    print(f"Entry point: 0x{e_entry:x}")
    print(f"Section header table offset: {e_shoff}")
    print(f"Number of section headers: {e_shnum}")
    
    # Read section names
    shstr_offset_in_table = e_shoff + e_shstrndx * e_shentsize
    shstr_data_offset = struct.unpack('<Q', elf[shstr_offset_in_table + 24 : shstr_offset_in_table + 32])[0]
    
    sections = {}
    for i in range(e_shnum):
        off = e_shoff + i * e_shentsize
        sh_name_idx = struct.unpack('<I', elf[off : off+4])[0]
        sh_type = struct.unpack('<I', elf[off+4 : off+8])[0]
        sh_flags = struct.unpack('<Q', elf[off+8 : off+16])[0]
        sh_addr = struct.unpack('<Q', elf[off+16 : off+24])[0]
        sh_offset = struct.unpack('<Q', elf[off+24 : off+32])[0]
        sh_size = struct.unpack('<Q', elf[off+32 : off+40])[0]
        
        # Extract section name
        name_bytes = []
        idx = shstr_data_offset + sh_name_idx
        while elf[idx] != 0:
            name_bytes.append(chr(elf[idx]))
            idx += 1
        name = ''.join(name_bytes)
        sections[name] = (sh_addr, sh_offset, sh_size)
        print(f"Section {i}: {name} - Addr: 0x{sh_addr:x}, Offset: {sh_offset}, Size: {sh_size}")
        
    if '.text' in sections:
        addr, offset, size = sections['.text']
        code = elf[offset : offset + size]
        
        print("\n--- Disassembling .text section ---")
        md = Cs(CS_ARCH_X86, CS_MODE_64)
        for insn in md.disasm(code, addr):
            print(f"0x{insn.address:x}:\t{insn.mnemonic}\t{insn.op_str}")

if __name__ == '__main__':
    analyze_elf(r'C:\Users\ICT-12\Documents\CTF\w3d2\antidebug')
