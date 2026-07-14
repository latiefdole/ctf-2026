import hashlib
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_flag():
    # 1. Reconstruct the key string: <Artist>|<DateTimeOriginal>
    artist = "PenguinOps"
    datetime_orig = "2024:03:15 09:00:00"
    key_str = f"{artist}|{datetime_orig}"
    print(f"Key source string: {key_str}")
    
    # Compute SHA-256 and take the first 16 bytes
    key = hashlib.sha256(key_str.encode('utf-8')).digest()[:16]
    print(f"Derived AES-128 Key (hex): {key.hex()}")
    
    # 2. Load IV
    with open(r'C:\Users\ICT-12\Documents\CTF\w3a2\iv.txt', 'r') as f:
        iv_hex = f.read().strip()
    iv = binascii.unhexlify(iv_hex)
    print(f"IV (hex): {iv.hex()}")
    
    # 3. Load encrypted data
    with open(r'C:\Users\ICT-12\Documents\CTF\w3a2\encrypted.bin', 'rb') as f:
        ciphertext = f.read()
    print(f"Ciphertext (hex): {ciphertext.hex()}")
    
    # 4. Decrypt using AES-CBC
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    print(f"Decrypted raw bytes: {decrypted}")
    
    # Unpad (if padded, standard PKCS7)
    try:
        plaintext = unpad(decrypted, AES.block_size).decode('utf-8')
        print(f"Decrypted plaintext: {plaintext}")
    except Exception as e:
        print(f"Unpadding failed: {e}")
        # Try decoding raw in case it's not standard padding
        print(f"Decoded raw: {decrypted.decode('utf-8', errors='replace')}")

if __name__ == '__main__':
    decrypt_flag()
