import struct

def decode_config():
    # Reconstruct the 4-byte XOR key: 7080 in decimal is 0x1ba8.
    # In little-endian 4-byte integer: [0xa8, 0x1b, 0x00, 0x00]
    key = [0xa8, 0x1b, 0x00, 0x00]
    
    with open(r'C:\Users\ICT-12\Documents\CTF\w3a1\config.bin', 'rb') as f:
        data = f.read()
        
    offset = 0
    while offset < len(data):
        if offset + 2 > len(data):
            break
        # Read 2-byte length (little endian uint16)
        length = struct.unpack('<H', data[offset:offset+2])[0]
        offset += 2
        
        if offset + length > len(data):
            print(f"[!] Warning: Truncated entry at offset {offset}, expected {length} bytes")
            break
            
        buf = bytearray(data[offset:offset+length])
        offset += length
        
        # XOR decode
        decoded = bytearray()
        for i in range(len(buf)):
            decoded.append(buf[i] ^ key[i % 4])
            
        try:
            decoded_str = decoded.decode('utf-8', errors='replace')
            print(decoded_str)
        except Exception as e:
            print(f"[!] Decode error: {e}")

if __name__ == '__main__':
    decode_config()
