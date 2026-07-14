import binascii

with open("w2a2/encoded_data.txt", "r") as f:
    encoded_hex = f.read().strip()

encoded_bytes = bytes.fromhex(encoded_hex)

keys_to_try = [b"MiraiBot2016", b"Mirai2016"]

for key in keys_to_try:
    decoded = bytes([encoded_bytes[i] ^ key[i % len(key)] for i in range(len(encoded_bytes))])
    print(f"Key: {key}, Decoded: {decoded}")
