def xor_bytes(b_arr, key):
    return bytes([b ^ key for b in b_arr])

part1_options = {
    "hex_orig": "756b615f696e757a61",
    "dec_orig": "uka_inuza",
    "hex_rev": "617a756e695f616b75",
    "dec_rev": "azuni_aku",
}

part2_options = [
    "20240101",
    "2024-01-01",
    "20240104",
    "2024-01-04",
    "20240105",
    "2024-01-05",
]

candidates = []

for p1_name, p1_val in part1_options.items():
    # We can compute multiple Part3 variants for each Part1
    p3_variants = []
    
    # If it is a hex string
    if p1_name.startswith("hex"):
        # Variant A: first 5 chars of hex string
        p3_variants.append(xor_bytes(p1_val[:5].encode('ascii'), 0x1F).hex())
        # Variant B: first 5 bytes of decoded hex
        try:
            dec = bytes.fromhex(p1_val).decode('ascii')
            p3_variants.append(xor_bytes(dec[:5].encode('ascii'), 0x1F).hex())
            # Variant C: entire decoded hex
            p3_variants.append(xor_bytes(dec.encode('ascii'), 0x1F).hex())
        except Exception:
            pass
        # Variant D: entire hex string
        p3_variants.append(xor_bytes(p1_val.encode('ascii'), 0x1F).hex())
    else:
        # If it is a decoded string
        # Variant A: first 5 chars of string
        p3_variants.append(xor_bytes(p1_val[:5].encode('ascii'), 0x1F).hex())
        # Variant B: entire string
        p3_variants.append(xor_bytes(p1_val.encode('ascii'), 0x1F).hex())
        # Variant C: first 5 chars of hex-encoded string
        hex_enc = p1_val.encode('ascii').hex()
        p3_variants.append(xor_bytes(hex_enc[:5].encode('ascii'), 0x1F).hex())
        # Variant D: entire hex-encoded string
        p3_variants.append(xor_bytes(hex_enc.encode('ascii'), 0x1F).hex())

    for p2 in part2_options:
        for p3 in set(p3_variants):
            candidates.append(f"flag{{{p1_val}_{p2}_{p3}}}")

# Write all candidates to a file
with open("candidates_list.txt", "w") as f:
    for c in sorted(list(set(candidates))):
        f.write(c + "\n")

print(f"Generated {len(set(candidates))} unique candidates and saved to candidates_list.txt")
