import struct
import base64

def solve():
    log_path = "C:/Users/ICT-12/Documents/CTF/w3f1/protocol_log.bin"
    with open(log_path, 'rb') as f:
        data = f.read()

    offset = 0
    while offset < len(data):
        if offset + 5 > len(data):
            break
        magic = data[offset:offset+2]
        if magic != b'\xde\xad':
            next_magic = data.find(b'\xde\xad', offset + 1)
            if next_magic == -1:
                break
            offset = next_magic
            continue
            
        msg_type = data[offset+2]
        length = struct.unpack('>H', data[offset+3:offset+5])[0]
        
        if offset + 5 + length > len(data):
            break
        
        payload = data[offset+5:offset+5+length]
            
        if msg_type == 3:
            flag_b64 = payload.decode('ascii')
            flag = base64.b64decode(flag_b64).decode('utf-8')
            return flag
            
        offset += 5 + length
    return None

if __name__ == "__main__":
    flag = solve()
    print("Flag:", flag)
