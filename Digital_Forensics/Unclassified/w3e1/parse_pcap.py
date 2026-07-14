import struct

def parse_pcap():
    pcap_path = r'C:\Users\ICT-12\Documents\CTF\w3e1\traffic.pcap'
    with open(pcap_path, 'rb') as f:
        data = f.read()
        
    if len(data) < 24:
        print("Invalid PCAP file")
        return
        
    magic = data[:4]
    if magic == b'\xa1\xb2\xc3\xd4':
        swap = False
    elif magic == b'\xd4\xc3\xb2\xa1':
        swap = True
    else:
        print(f"Unknown magic: {magic.hex()}")
        return
        
    link_type = struct.unpack('<I' if not swap else '>I', data[20:24])[0]
    print(f"PCAP Magic: {magic.hex()}, LinkType: {link_type}")
    
    offset = 24
    packet_idx = 0
    while offset < len(data):
        if offset + 16 > len(data):
            break
        ts_sec, ts_usec, inclen, origlen = struct.unpack('<IIII' if not swap else '>IIII', data[offset:offset+16])
        offset += 16
        
        packet_data = data[offset : offset + inclen]
        offset += inclen
        
        print(f"\n--- Packet {packet_idx} (Len: {inclen} bytes) ---")
        # Assuming Ethernet (LinkType 1)
        if link_type == 1:
            if len(packet_data) < 14:
                print("Truncated Ethernet frame")
                continue
            eth_proto = struct.unpack('>H', packet_data[12:14])[0]
            if eth_proto == 0x0800: # IPv4
                ip_data = packet_data[14:]
                if len(ip_data) < 20:
                    print("Truncated IP packet")
                    continue
                ip_proto = ip_data[9]
                src_ip = ".".join(map(str, ip_data[12:16]))
                dst_ip = ".".join(map(str, ip_data[16:20]))
                ip_header_len = (ip_data[0] & 0x0F) * 4
                
                if ip_proto == 6: # TCP
                    tcp_data = ip_data[ip_header_len:]
                    if len(tcp_data) < 20:
                        print("Truncated TCP segment")
                        continue
                    src_port, dst_port = struct.unpack('>HH', tcp_data[:4])
                    data_offset = (tcp_data[12] >> 4) * 4
                    payload = tcp_data[data_offset:]
                    print(f"IP: {src_ip}:{src_port} -> {dst_ip}:{dst_port} (TCP)")
                    if payload:
                        print(f"TCP Payload length: {len(payload)} bytes")
                        # Print first 64 bytes of payload in hex
                        print(f"Payload (hex): {payload[:64].hex()}")
                        # Print ASCII if printable
                        ascii_repr = "".join(chr(b) if 32 <= b < 127 or b in (10, 13) else "." for b in payload[:128])
                        print(f"Payload (ASCII):\n{ascii_repr}")
                else:
                    print(f"IP: {src_ip} -> {dst_ip} (Proto: {ip_proto})")
            else:
                print(f"Ethernet Proto: 0x{eth_proto:04x}")
        else:
            print(f"Raw data (first 64 bytes): {packet_data[:64].hex()}")
            
        packet_idx += 1

if __name__ == '__main__':
    parse_pcap()
