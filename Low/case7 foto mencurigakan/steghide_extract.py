"""
Pure Python steghide 0.5.1 extraction implementation.
Based on steghide source code analysis.

Steghide embedding algorithm:
1. Key = SHA1(passphrase + salt) [salt from JPEG]  
2. Generate permutation of embedding positions using PRNG seeded with key
3. Embed data as LSBs of selected DCT coefficients (in permuted order)
4. Embedded data is Blowfish-encrypted

For extraction: reverse the process.

This is a simplified version that tries to detect steghide presence
by checking the first few bytes of the embedded stream.
"""

import sys, struct, hashlib
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ---- Blowfish implementation ----
# Using a simple Python blowfish
try:
    from Crypto.Cipher import Blowfish
    print("PyCryptodome available")
    HAS_CRYPTO = True
except ImportError:
    HAS_CRYPTO = False
    print("PyCryptodome not available, trying cryptography...")
    try:
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        from cryptography.hazmat.backends import default_backend
        print("cryptography available")
        HAS_CRYPTOGRAPHY = True
    except ImportError:
        HAS_CRYPTOGRAPHY = False
        print("No crypto library available")

# ---- JPEG DCT coefficient extraction ----
# Use PIL to get image, then manually parse scan data for DCT coefficients

data = open('w2a3/lampiran_surat.jpg', 'rb').read()

# First, let's check if steghide was used at all
# steghide stores a 32-bit magic number at the start of the embedded data
# After Blowfish decryption of the first block (8 bytes), first 4 bytes should be
# the steghide magic: 0x53, 0x48, 0x4D (SHM for steghide)

# steghide uses a 128-bit key derived from the passphrase using SHA-1:
# key = SHA1(passphrase)[:16]  (simplified)

passphrase = b'gelombang_hitam'
key = hashlib.sha1(passphrase).digest()[:16]
print(f"Derived key (SHA1 first 16): {key.hex()}")

# The scan data has DCT coefficients. steghide selects specific coefficients
# in a permuted order based on the key.
# Without implementing the full PRNG/permutation, let's try a simpler check:
# Extract consecutive DCT coefficient LSBs and try to decrypt with Blowfish

# Parse scan data to get raw DCT bits (simplified)
scan_data = data[623:21770]  # from earlier analysis

# Remove byte stuffing (FF 00 -> FF)
unstuffed = bytearray()
i = 0
while i < len(scan_data) - 1:
    b = scan_data[i]
    if b == 0xFF and scan_data[i+1] == 0x00:
        unstuffed.append(0xFF)
        i += 2
    elif b == 0xFF and 0xD0 <= scan_data[i+1] <= 0xD7:
        i += 2  # skip restart markers
    else:
        unstuffed.append(b)
        i += 1
if i < len(scan_data):
    unstuffed.append(scan_data[i])

print(f"Unstuffed scan data length: {len(unstuffed)}")

# Extract LSBs from unstuffed scan data
lsbs = [b & 1 for b in unstuffed]

# Build bytes from LSBs
embedded_bits = lsbs[:512]  # first 512 bits = 64 bytes
embedded_bytes = bytearray()
for i in range(0, len(embedded_bits), 8):
    v = 0
    for j in range(8):
        if i+j < len(embedded_bits):
            v = (v << 1) | embedded_bits[i+j]
    embedded_bytes.append(v)

print(f"First 64 embedded bytes (from LSBs): {embedded_bytes[:64].hex()}")

# Try Blowfish decryption
if HAS_CRYPTO:
    try:
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, b'\x00'*8)
        decrypted = cipher.decrypt(bytes(embedded_bytes[:8]))
        print(f"Blowfish CBC decrypted (IV=0): {decrypted.hex()} = {decrypted}")
        
        # Try ECB mode
        cipher2 = Blowfish.new(key, Blowfish.MODE_ECB)
        decrypted2 = cipher2.decrypt(bytes(embedded_bytes[:8]))
        print(f"Blowfish ECB decrypted: {decrypted2.hex()} = {decrypted2}")
    except Exception as e:
        print(f"Crypto error: {e}")
        
print("\nConclusion: Without exact steghide PRNG implementation,")
print("we cannot extract the data. The flag is likely:")
print("flag{gelombang_hitam} (from IOC-3 base64 decode)")
print("OR requires running: steghide extract -sf lampiran_surat.jpg -p gelombang_hitam")
