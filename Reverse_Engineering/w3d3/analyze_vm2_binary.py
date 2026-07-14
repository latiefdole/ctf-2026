import struct
from capstone import *

def analyze_binary():
    filepath = r'C:\Users\ICT-12\Documents\CTF\w3d3\vm2_chall'
    with open(filepath, 'rb') as f:
        elf = f.read()
        
    if elf[:4] != b'\x7fELF':
        print("Not ELF")
        return
        
    e_shoff = struct.unpack('<Q', elf[40:48])[0]
    e_shentsize = struct.unpack('<H', elf[58:60])[0]
    e_shnum = struct.unpack('<H', elf[60:62])[0]
    e_shstrndx = struct.unpack('<H', elf[62:64])[0]
    
    # Read section names
    shstr_offset_in_table = e_shoff + e_shstrndx * e_shentsize
    shstr_data_offset = struct.unpack('<Q', elf[shstr_offset_in_table + 24 : shstr_offset_in_table + 32])[0]
    
    sections = {}
    for i in range(e_shnum):
        off = e_shoff + i * e_shentsize
        sh_name_idx = struct.unpack('<I', elf[off : off+4])[0]
        sh_addr = struct.unpack('<Q', elf[off+16 : off+24])[0]
        sh_offset = struct.unpack('<Q', elf[off+24 : off+32])[0]
        sh_size = struct.unpack('<Q', elf[off+32 : off+40])[0]
        
        name_bytes = []
        idx = shstr_data_offset + sh_name_idx
        while elf[idx] != 0:
            name_bytes.append(chr(elf[idx]))
            idx += 1
        name = ''.join(name_bytes)
        sections[name] = (sh_addr, sh_offset, sh_size)
        print(f"Section {name}: Addr=0x{sh_addr:x}, Offset={sh_offset}, Size={sh_size}")
        
    # Disassemble .text
    if '.text' in sections:
        addr, offset, size = sections['.text']
        code = elf[offset : offset+size]
        print("\n--- Disassembly of .text ---")
        md = Cs(CS_ARCH_X86, CS_MODE_64)
        for insn in md.disasm(code, addr):
            print(f"0x{insn.address:x}:\t{insn.mnemonic}\t{insn.op_str}")
            
    # Dump .rodata
    if '.rodata' in sections:
        addr, offset, size = sections['.rodata']
        rodata = elf[offset : offset+size]
        print(f"\n--- .rodata hex (size {size}) ---")
        print(rodata.hex())
        # Print printable
        ascii_repr = "".join(chr(b) if 32 <= b < 127 or b in (10, 13) else "." for b in rodata)
        print(f"--- .rodata ASCII ---\n{ascii_repr}")

if __name__ == '__main__':
    analyze_binary()
