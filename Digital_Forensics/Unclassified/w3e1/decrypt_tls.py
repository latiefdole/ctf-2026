import struct
import hashlib
import hmac
import math
from Crypto.Cipher import AES

# HKDF functions for SHA-384 (TLS 1.3 TLS_AES_256_GCM_SHA384)
def hkdf_expand(prk, info, length):
    hash_len = 48  # SHA-384
    n = math.ceil(length / hash_len)
    t = b""
    t_prev = b""
    for i in range(1, n + 1):
        t_prev = hmac.new(prk, t_prev + info + bytes([i]), hashlib.sha384).digest()
        t += t_prev
    return t[:length]

def hkdf_expand_label(secret, label, context, length):
    # HkdfLabel structure:
    # uint16 length
    # uint8 label_len ("tls13 " + label)
    # opaque label
    # uint8 context_len
    # opaque context
    hkdf_label = struct.pack('>H', length)
    full_label = b"tls13 " + label.encode('utf-8')
    hkdf_label += struct.pack('>B', len(full_label))
    hkdf_label += full_label
    hkdf_label += struct.pack('>B', len(context))
    hkdf_label += context
    return hkdf_expand(secret, hkdf_label, length)

def derive_key_iv(secret):
    key = hkdf_expand_label(secret, "key", b"", 32)
    iv = hkdf_expand_label(secret, "iv", b"", 12)
    return key, iv

def decrypt_tls_record(ciphertext_with_tag, key, write_iv, seq_num, record_header):
    # Nonce derivation: write_iv ^ seq_num
    seq_bytes = struct.pack('>Q', seq_num)
    nonce = bytearray(write_iv)
    for i in range(8):
        nonce[4 + i] ^= seq_bytes[i]
    nonce = bytes(nonce)
    
    # In AES-GCM, the last 16 bytes is the tag
    ciphertext = ciphertext_with_tag[:-16]
    tag = ciphertext_with_tag[-16:]
    
    # AAD is the 5-byte record header
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    cipher.update(record_header)
    
    try:
        decrypted = cipher.decrypt_and_verify(ciphertext, tag)
        # In TLS 1.3, the decrypted payload has trailing padding (0x00) and the real content type at the end
        # Find the last non-zero byte
        idx = len(decrypted) - 1
        while idx >= 0 and decrypted[idx] == 0:
            idx -= 1
        if idx < 0:
            return None, None
        real_type = decrypted[idx]
        content = decrypted[:idx]
        return content, real_type
    except Exception as e:
        # print(f"Decryption failed for seq {seq_num}: {e}")
        return None, None

def parse_keys():
    keys_path = r'C:\Users\ICT-12\Documents\CTF\w3e1\sslkeys.txt'
    client_secret = None
    server_secret = None
    with open(keys_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                label, client_random, secret_hex = parts
                if label == "CLIENT_TRAFFIC_SECRET_0":
                    client_secret = bytes.fromhex(secret_hex)
                elif label == "SERVER_TRAFFIC_SECRET_0":
                    server_secret = bytes.fromhex(secret_hex)
    return client_secret, server_secret

def decrypt_traffic():
    client_secret, server_secret = parse_keys()
    if not client_secret or not server_secret:
        print("Failed to find secrets in sslkeys.txt")
        return
        
    client_key, client_iv = derive_key_iv(client_secret)
    server_key, server_iv = derive_key_iv(server_secret)
    
    print(f"Client Write Key: {client_key.hex()}")
    print(f"Client Write IV:  {client_iv.hex()}")
    print(f"Server Write Key: {server_key.hex()}")
    print(f"Server Write IV:  {server_iv.hex()}")
    
    pcap_path = r'C:\Users\ICT-12\Documents\CTF\w3e1\traffic.pcap'
    with open(pcap_path, 'rb') as f:
        data = f.read()
        
    offset = 0
    swap = False
    
    # We will process TCP payloads. To correctly keep track of TLS records, we can reassemble or parse TLS records directly from the packet payload.
    # Since each packet contains one or more complete TLS records, we can extract them packet-by-packet.
    
    client_seq = 0
    server_seq = 0
    
    while offset < len(data):
        if offset + 8 > len(data):
            break
        block_type, block_len = struct.unpack('<II' if not swap else '>II', data[offset:offset+8])
        if block_type == 0x0A0D0D0A:
            bom = data[offset+8:offset+12]
            if bom == b'\x1a\x2b\x3c\x4d':
                swap = True
            elif bom == b'\x4d\x3c\x2b\x1a':
                swap = False
            block_len = struct.unpack('<I' if not swap else '>I', data[offset+4:offset+8])[0]
            
        elif block_type == 0x00000006:
            block_data = data[offset : offset + block_len]
            interface_id, ts_high, ts_low, cap_len, orig_len = struct.unpack(
                '<IIIII' if not swap else '>IIIII', block_data[8:28]
            )
            packet_data = block_data[28 : 28 + cap_len]
            
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
                        
                        # Process TCP payload for TLS records
                        # A packet payload might contain multiple TLS records or be part of a stream.
                        # For this challenge, the records are aligned to packet boundaries.
                        # Let's parse records from the payload:
                        p_off = 0
                        while p_off + 5 <= len(payload):
                            rec_type, rec_ver, rec_len = struct.unpack('>BHH', payload[p_off:p_off+5])
                            # Check if valid TLS record type (0x14-0x17) and version (0x0300-0x0304)
                            if rec_type in (0x14, 0x15, 0x16, 0x17) and rec_ver in (0x0301, 0x0302, 0x0303, 0x0304):
                                if p_off + 5 + rec_len > len(payload):
                                    break
                                record_header = payload[p_off : p_off+5]
                                record_data = payload[p_off+5 : p_off+5+rec_len]
                                
                                if rec_type == 0x17: # Application Data (encrypted)
                                    # Try decrypting as client
                                    dec, r_type = decrypt_tls_record(record_data, client_key, client_iv, client_seq, record_header)
                                    if dec is not None:
                                        print(f"\n[Client -> Server] (Seq {client_seq}) Real Type: 0x{r_type:02x}")
                                        print(f"Decrypted: {dec.decode('utf-8', errors='replace')}")
                                        client_seq += 1
                                    else:
                                        # Try decrypting as server
                                        dec, r_type = decrypt_tls_record(record_data, server_key, server_iv, server_seq, record_header)
                                        if dec is not None:
                                            print(f"\n[Server -> Client] (Seq {server_seq}) Real Type: 0x{r_type:02x}")
                                            # Try decoding as string or print hex
                                            try:
                                                print(f"Decrypted: {dec.decode('utf-8')}")
                                            except Exception:
                                                print(f"Decrypted (hex): {dec.hex()}")
                                            server_seq += 1
                                p_off += 5 + rec_len
                            else:
                                break
                                
        offset += block_len

if __name__ == '__main__':
    decrypt_traffic()
