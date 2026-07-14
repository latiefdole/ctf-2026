def vigenere_decrypt(ct, key):
    pt = ""
    k_idx = 0
    for c in ct:
        if c.isalpha():
            offset = 65 if c.isupper() else 97
            pt += chr((ord(c) - offset - (ord(key[k_idx % len(key)].upper()) - 65)) % 26 + offset)
            k_idx += 1
        else:
            pt += c
    return pt

with open('C:/Users/ICT-12/Documents/CTF/Digital_Forensics/case1/cipher_text.txt', 'r') as f:
    ct = f.read()

print(vigenere_decrypt(ct, 'ARKANA'))
