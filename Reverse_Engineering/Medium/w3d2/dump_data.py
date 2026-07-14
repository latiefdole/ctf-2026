def dump_and_decrypt():
    with open(r'C:\Users\ICT-12\Documents\CTF\w3d2\antidebug', 'rb') as f:
        elf = f.read()
    
    # Locate .rodata (offset 8192, size 34)
    rodata = elf[8192 : 8192 + 34]
    print(f".rodata hex: {rodata.hex()}")
    # Let's decode strings from .rodata
    print(f".rodata as ascii: {repr(rodata)}")
    
    # Locate .data (offset 12320, size 64)
    # 0x4020 is at offset 12320.
    # 0x4040 is at offset 12320 + (0x4040 - 0x4020) = 12320 + 0x20 = 12352.
    # The data decrypted is 32 bytes from 0x4040.
    data_32 = elf[12352 : 12352 + 32]
    print(f"Encrypted data (at 0x4040) hex: {data_32.hex()}")
    
    # XOR decryption with 0x5a
    decrypted = bytearray()
    for b in data_32:
        decrypted.append(b ^ 0x5a)
        
    print(f"Decrypted data hex: {decrypted.hex()}")
    print(f"Decrypted data string: {decrypted.decode('utf-8', errors='replace')}")

if __name__ == '__main__':
    dump_and_decrypt()
