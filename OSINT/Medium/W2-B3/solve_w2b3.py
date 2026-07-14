import base64

def decrypt_deploy_key():
    # Ciphertext base64 dari leaked_config.txt
    ciphertext_b64 = "PwMGHhoDUhwQEwZvRQUoDQYpaQFXJhNYBR9FEkZvSwQsQFl7JA=="
    ciphertext = base64.b64decode(ciphertext_b64)
    
    # Kunci yang direkonstruksi: "Yogyakarta2024K9mZ"
    key = "Yogyakarta2024K9mZ"
    
    # Dekripsi menggunakan XOR berulang
    decrypted = []
    for i in range(len(ciphertext)):
        decrypted.append(ciphertext[i] ^ ord(key[i % len(key)]))
        
    flag = bytes(decrypted).decode('utf-8', errors='ignore')
    return flag

if __name__ == "__main__":
    flag = decrypt_deploy_key()
    print("Flag:", flag)
