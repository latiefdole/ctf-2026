def xor_bytes(b_arr, key):
    return bytes([b ^ key for b in b_arr])

part1_options = {
    "hex": "756b615f696e757a61",
    "decoded": "uka_inuza",
}

part2_options = [
    "20240101",
    "2024-01-01",
    "20240104",
    "2024-01-04",
    "20240105",
    "2024-01-05",
]

# Calculate Part3 for each Part1 option
part3_options = {}

# For hex Part1:
# Option A: first 5 chars of hex string
hex_str = part1_options["hex"]
p3_hex_chars = xor_bytes(hex_str[:5].encode('ascii'), 0x1F).hex()
# Option B: first 5 bytes of decoded hex
decoded_str = part1_options["decoded"]
p3_decoded_chars = xor_bytes(decoded_str[:5].encode('ascii'), 0x1F).hex()
# Option C: entire hex string
p3_hex_entire = xor_bytes(hex_str.encode('ascii'), 0x1F).hex()
# Option D: entire decoded string
p3_decoded_entire = xor_bytes(decoded_str.encode('ascii'), 0x1F).hex()

part3_options["hex"] = [p3_hex_chars, p3_decoded_chars, p3_hex_entire, p3_decoded_entire]
part3_options["decoded"] = [p3_hex_chars, p3_decoded_chars, p3_hex_entire, p3_decoded_entire]

candidates = []

for p1_key, p1_val in part1_options.items():
    for p2 in part2_options:
        for p3 in part3_options[p1_key]:
            # Try underscore separator
            candidates.append(f"flag{{{p1_val}_{p2}_{p3}}}")
            candidates.append(f"CTF{{{p1_val}_{p2}_{p3}}}")
            # Try hyphen separator
            candidates.append(f"flag{{{p1_val}-{p2}-{p3}}}")
            candidates.append(f"CTF{{{p1_val}-{p2}-{p3}}}")

# Also try without flag wrapper, just the operational code
for p1_key, p1_val in part1_options.items():
    for p2 in part2_options:
        for p3 in part3_options[p1_key]:
            candidates.append(f"{p1_val}_{p2}_{p3}")
            candidates.append(f"{p1_val}-{p2}-{p3}")

print(f"Generated {len(candidates)} candidates.")
for i, c in enumerate(candidates[:100]):
    print(f"{i+1}: {c}")
if len(candidates) > 100:
    print(f"... and {len(candidates) - 100} more")
