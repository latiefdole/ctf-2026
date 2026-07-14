import hashlib
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_with_key(key, iv, ciphertext):
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext)
        return decrypted
    except Exception:
        return None

def test_candidates():
    # Load encrypted file
    with open(r'C:\Users\ICT-12\Documents\CTF\w3a2\encrypted.bin', 'rb') as f:
        ciphertext = f.read()
        
    # Load IV
    with open(r'C:\Users\ICT-12\Documents\CTF\w3a2\iv.txt', 'r') as f:
        iv_hex = f.read().strip()
    iv = binascii.unhexlify(iv_hex)
    
    print(f"Ciphertext length: {len(ciphertext)}")
    print(f"IV: {iv.hex()}")
    
    # Candidate strings
    candidates = [
        "PenguinOps",
        "AES-KEY-SOURCE",
        "2024:03:15 09:00:00",
        "2024-03-15",
        "Surabaya",
        "surabaya",
        "Indonesia",
        "indonesia",
        "PT Arsip Nasional Digital",
        "Tim Respons Insiden - Divisi Keamanan Informasi",
        # coordinates
        "7.2491, 112.7508",
        "-7.2491, 112.7508",
        "7.2491,112.7508",
        "-7.2491,112.7508",
        "7°14'56.76\" S, 112°45'2.88\" E",
        "7°14'56.76\" S 112°45'2.88\" E",
        # coordinate values raw
        "7 14 56.76 S 112 45 2.88 E",
        # other variants
        "7.2491",
        "112.7508",
        "-7.2491",
        "7.249100, 112.750800",
        "-7.249100, 112.750800",
        "7.249100,112.750800",
        "-7.249100,112.750800",
    ]
    
    # Let's add more candidates:
    # Latitude: 7/1, 14/1, 5676/100, S
    # Longitude: 112/1, 45/1, 288/100, E
    candidates.extend([
        "7/1 14/1 5676/100 S 112/1 45/1 288/100 E",
        "7/1, 14/1, 5676/100, S, 112/1, 45/1, 288/100, E",
        "7, 14, 56.76, S, 112, 45, 2.88, E",
        "7,14,56.76,S,112,45,2.88,E",
    ])
    
    # Try raw strings (truncated to 16 bytes or padded with 0)
    for c in candidates:
        # Padded with null bytes to 16 bytes
        k_pad = c.encode('utf-8')
        if len(k_pad) < 16:
            k_pad = k_pad.ljust(16, b'\x00')
        elif len(k_pad) > 16:
            k_pad = k_pad[:16]
            
        # Try raw
        dec = decrypt_with_key(k_pad, iv, ciphertext)
        if dec and (b'flag' in dec or b'ctf' in dec or b'{' in dec or all(32 <= b < 127 for b in dec)):
            print(f"[RAW-PAD] Key candidate '{c}' -> {dec}")
            
        # Try MD5
        k_md5 = hashlib.md5(c.encode('utf-8')).digest()
        dec = decrypt_with_key(k_md5, iv, ciphertext)
        if dec and (b'flag' in dec or b'ctf' in dec or b'{' in dec or all(32 <= b < 127 for b in dec)):
            print(f"[MD5] Key candidate '{c}' -> {dec}")
            
        # Try SHA-256 (truncated to 16 bytes)
        k_sha256 = hashlib.sha256(c.encode('utf-8')).digest()[:16]
        dec = decrypt_with_key(k_sha256, iv, ciphertext)
        if dec and (b'flag' in dec or b'ctf' in dec or b'{' in dec or all(32 <= b < 127 for b in dec)):
            print(f"[SHA256-16] Key candidate '{c}' -> {dec}")
            
        # Try SHA-1 (truncated to 16 bytes)
        k_sha1 = hashlib.sha1(c.encode('utf-8')).digest()[:16]
        dec = decrypt_with_key(k_sha1, iv, ciphertext)
        if dec and (b'flag' in dec or b'ctf' in dec or b'{' in dec or all(32 <= b < 127 for b in dec)):
            print(f"[SHA1-16] Key candidate '{c}' -> {dec}")

if __name__ == '__main__':
    test_candidates()
