"""
W3-B3: Operator Bayangan - FINAL SOLVER
Flag format: flag{t3ks_c4mpur_angka_dipisah_underscore}
"""

from datetime import datetime, timezone

# Part1: kunci sesi
part1_hex = "756b615f696e757a61"
part1_decoded = bytes.fromhex(part1_hex).decode('ascii')  # "uka_inuza"
print(f"Kunci sesi (raw): {part1_hex}")
print(f"Kunci sesi (decoded): {part1_decoded}")

# Part2: epoch -> YYYYMMDD
epoch = 1704067200
dt = datetime.fromtimestamp(epoch, tz=timezone.utc)
part2 = dt.strftime("%Y%m%d")
print(f"Epoch {epoch} -> {dt} -> Part2: {part2}")

# Part3: XOR(Part1_pertama_5_char_as_bytes, key_byte=0x1F) hex-encode
# Interpretation: Part1 is hex string, decode to bytes, take first 5 bytes
part1_bytes = bytes.fromhex(part1_hex)
first5 = part1_bytes[:5]  # b'uka_i'
xored = bytes([b ^ 0x1F for b in first5])
part3 = xored.hex()
print(f"First 5 bytes: {first5} -> XOR 0x1F -> Part3: {part3}")

print("\n" + "="*60)
print("FLAG CANDIDATES (coba dari atas ke bawah):")
print("="*60)

flags = [
    f"flag{{{part1_hex}_{part2}_{part3}}}",
    f"flag{{{part1_decoded}_{part2}_{part3}}}",
]

# Also try with first 5 chars of hex STRING as ASCII
first5_str = part1_hex[:5]  # "756b6"
xored_str = bytes([b ^ 0x1F for b in first5_str.encode('ascii')])
part3_str = xored_str.hex()

flags.append(f"flag{{{part1_hex}_{part2}_{part3_str}}}")
flags.append(f"flag{{{part1_decoded}_{part2}_{part3_str}}}")

for i, f in enumerate(flags, 1):
    print(f"  [{i}] {f}")
