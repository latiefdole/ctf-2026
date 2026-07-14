import struct

def solve():
    # Path to the ELF binary
    binary_path = "C:/Users/ICT-12/Documents/CTF/w3d1/vm_chall"
    
    with open(binary_path, 'rb') as f:
        elf = f.read()
    
    # 1. Parse ELF to find .rodata section
    header_format = "<16sHHIQQQIHHHHHH"
    parsed_header = struct.unpack(header_format, elf[:64])
    
    e_shoff = parsed_header[6]
    e_shentsize = parsed_header[11]
    e_shnum = parsed_header[12]
    e_shstrndx = parsed_header[13]
    
    # Read section headers to find .rodata
    rodata_offset = None
    rodata_size = None
    
    # First find .shstrtab section
    shstr_sh = struct.unpack("<IIQQQQIIQQ", elf[e_shoff + e_shstrndx * e_shentsize : e_shoff + (e_shstrndx + 1) * e_shentsize])
    shstr_offset = shstr_sh[4]
    shstr_size = shstr_sh[5]
    shstr_table = elf[shstr_offset : shstr_offset + shstr_size]
    
    for i in range(e_shnum):
        offset = e_shoff + i * e_shentsize
        sh_data = elf[offset : offset + e_shentsize]
        sh_parsed = struct.unpack("<IIQQQQIIQQ", sh_data)
        
        name_offset = sh_parsed[0]
        end_name = shstr_table.find(b'\x00', name_offset)
        name = shstr_table[name_offset:end_name].decode('utf-8', errors='ignore')
        
        if name == '.rodata':
            rodata_offset = sh_parsed[4]
            rodata_size = sh_parsed[5]
            break
            
    if rodata_offset is None:
        print("Could not find .rodata section")
        return
        
    rodata = elf[rodata_offset : rodata_offset + rodata_size]
    
    # 2. Locate bytecode array
    # Looking for bytecode starting pattern: PUSH (01), then some printable/byte, PUSH (01), 00, XOR (02), PRINT (03)
    # i.e., 01 XX 01 00 02 03
    bytecode = None
    for i in range(len(rodata) - 6):
        if rodata[i] == 0x01 and rodata[i+2] == 0x01 and rodata[i+3] == 0x00 and rodata[i+4] == 0x02 and rodata[i+5] == 0x03:
            bytecode = rodata[i:]
            break
            
    if bytecode is None:
        print("Could not locate VM bytecode signature")
        return
        
    # 3. Emulate Stack VM
    # Opcodes:
    # 0x01 PUSH <byte>
    # 0x02 XOR
    # 0x03 PRINT
    # 0x04 HALT
    
    stack = []
    output = []
    pc = 0
    
    while pc < len(bytecode):
        opcode = bytecode[pc]
        if opcode == 0x01:  # PUSH
            val = bytecode[pc+1]
            stack.append(val)
            pc += 2
        elif opcode == 0x02:  # XOR
            if len(stack) < 2:
                print("Error: Stack underflow on XOR")
                break
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(v1 ^ v2)
            pc += 1
        elif opcode == 0x03:  # PRINT
            if len(stack) < 1:
                print("Error: Stack underflow on PRINT")
                break
            val = stack.pop()
            output.append(chr(val))
            pc += 1
        elif opcode == 0x04:  # HALT
            break
        else:
            # Reached end of VM instructions or invalid opcode
            break
            
    flag = "".join(output)
    print("Flag:", flag)
    return flag

if __name__ == "__main__":
    solve()
