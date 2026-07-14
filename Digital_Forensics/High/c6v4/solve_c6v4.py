import struct

def rol(val, r_bits, max_bits=32):
    return ((val << r_bits) & (2**max_bits - 1)) | (val >> (max_bits - r_bits))

def ror(val, r_bits, max_bits=32):
    return ((val >> r_bits) & (2**max_bits - 1)) | (val << (max_bits - r_bits))

def encrypt(pt):
    pt_bytes = bytes.fromhex(pt)
    B, A = struct.unpack('>II', pt_bytes)
    C = B ^ rol(A, 5) ^ 0xdeadbeef
    D = A ^ rol(C, 5) ^ 0xcafebabe
    E = C ^ rol(D, 5) ^ 0x13371337
    F = D ^ rol(E, 5) ^ 0xabcdabcd
    return struct.pack('>II', F, E).hex().upper()

def decrypt(ct):
    ct_bytes = bytes.fromhex(ct)
    F, E = struct.unpack('>II', ct_bytes)
    D = F ^ rol(E, 5) ^ 0xabcdabcd
    C = E ^ rol(D, 5) ^ 0x13371337
    A = D ^ rol(C, 5) ^ 0xcafebabe
    B = C ^ rol(A, 5) ^ 0xdeadbeef
    return struct.pack('>II', B, A)

print("Test Vector Check:")
print("Expected: 4E5414112E3C54F8")
print("Actual:   " + encrypt("0102030405060708"))

with open('C:/Users/ICT-12/Documents/CTF/Digital_Forensics/c6v4/ciphertext.txt', 'r') as f:
    cts = f.read().splitlines()

pt = b''
for ct in cts:
    if ct.strip():
        pt += decrypt(ct.strip())

print("Decrypted PT:", pt)
