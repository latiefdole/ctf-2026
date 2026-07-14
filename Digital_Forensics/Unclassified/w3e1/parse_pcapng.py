import struct

def parse_pcapng():
    pcap_path = r'C:\Users\ICT-12\Documents\CTF\w3e1\traffic.pcap'
    with open(pcap_path, 'rb') as f:
        data = f.read()
        
    print(f"Total file size: {len(data)} bytes")
    offset = 0
    packet_idx = 0
    swap = False
    
    while offset < len(data):
        if offset + 8 > len(data):
            print(f"End of file reached with {len(data) - offset} leftover bytes")
            break
            
        try:
            block_type, block_len = struct.unpack('<II' if not swap else '>II', data[offset:offset+8])
        except Exception as e:
            print(f"Error unpacking at offset {offset}: {e}")
            break
            
        if block_len == 0:
            print("Error: Block length is 0, stopping to prevent infinite loop.")
            break
            
        if offset + block_len > len(data):
            print(f"Error: Block length {block_len} at offset {offset} exceeds remaining file size {len(data) - offset}")
            break
            
        block_data = data[offset : offset + block_len]
        
        if block_type == 0x0A0D0D0A: # Section Header Block
            bom = data[offset+8:offset+12]
            if bom == b'\x1a\x2b\x3c\x4d':
                swap = True
                print(f"Offset {offset}: SHB, BOM: Big-endian")
            elif bom == b'\x4d\x3c\x2b\x1a':
                swap = False
                print(f"Offset {offset}: SHB, BOM: Little-endian")
            # Re-read block_len after determining endianness
            block_len = struct.unpack('<I' if not swap else '>I', data[offset+4:offset+8])[0]
            
        elif block_type == 0x00000006: # Enhanced Packet Block
            interface_id, ts_high, ts_low, cap_len, orig_len = struct.unpack(
                '<IIIII' if not swap else '>IIIII', block_data[8:28]
            )
            packet_data = block_data[28 : 28 + cap_len]
            print(f"Offset {offset}: EPB, interface={interface_id}, cap_len={cap_len}")
            
            if len(packet_data) >= 14:
                eth_proto = struct.unpack('>H', packet_data[12:14])[0]
                if eth_proto == 0x0800:
                    ip_data = packet_data[14:]
                    ip_proto = ip_data[9]
                    src_ip = ".".join(map(str, ip_data[12:16]))
                    dst_ip = ".".join(map(str, ip_data[16:20]))
                    ip_header_len = (ip_data[0] & 0x0F) * 4
                    
                    if ip_proto == 6:
                        tcp_data = ip_data[ip_header_len:]
                        src_port, dst_port = struct.unpack('>HH', tcp_data[:4])
                        data_offset = (tcp_data[12] >> 4) * 4
                        payload = tcp_data[data_offset:]
                        print(f"  TCP: {src_ip}:{src_port} -> {dst_ip}:{dst_port}, payload_len={len(payload)}")
                        
                        if payload:
                            # Print first 64 bytes of payload in hex
                            print(f"    Payload (hex): {payload[:64].hex()}")
                            
                            # Check for TLS records
                            if len(payload) >= 5:
                                rec_type, rec_ver, rec_len = struct.unpack('>BHH', payload[:5])
                                if rec_type in (0x14, 0x15, 0x16, 0x17) and rec_ver in (0x0301, 0x0302, 0x0303, 0x0304):
                                    print(f"    Detected TLS Record: Type=0x{rec_type:02x}, Ver=0x{rec_ver:04x}, Len={rec_len}")
        else:
            print(f"Offset {offset}: Type 0x{block_type:08x}, Len {block_len}")
            
        offset += block_len

if __name__ == '__main__':
    parse_pcapng()
