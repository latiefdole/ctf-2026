# Fragmen kode - ditemukan di memori perangkat IoT yang dikompromikan
# PT Telematika Sentral - Unit Forensik

key = b"????"

with open("data.bin", "rb") as f:
    data = f.read()

out = bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
final = out.hex()

with open("encoded_data.txt", "w") as f:
    f.write(final)
