def xor_bytes(b_arr, key):
    return bytes([b ^ key for b in b_arr])

# Define the variants of Part 1
part1_variants = {
    "uka_inuza": {
        "raw": "uka_inuza",
        "hex": "756b615f696e757a61",
        "part3_raw": xor_bytes(b"uka_i", 0x1F).hex(),
        "part3_hex": xor_bytes(b"756b6", 0x1F).hex()
    },
    "azuni_aku": {
        "raw": "azuni_aku",
        "hex": "617a756e695f616b75",
        "part3_raw": xor_bytes(b"azuni", 0x1F).hex(),
        "part3_hex": xor_bytes(b"617a7", 0x1F).hex()
    },
    "n0ct4lys1s": {
        "raw": "n0ct4lys1s",
        "hex": "n0ct4lys1s".encode('ascii').hex(),
        "part3_raw": xor_bytes(b"n0ct4", 0x1F).hex(),
        "part3_hex": None
    }
}

dates = {
    "Epoch Join (UTC)": "20240101",
    "Post #1 (UTC)": "20240104",
    "Post #1 (WIB)": "20240105"
}

# Generate flag candidates categorized by hypothesis
output = []
output.append("# Flag Candidates by Hypothesis\n")

for name, info in part1_variants.items():
    output.append(f"## Hypothesis: Key is '{name}'")
    
    # 1. Using decoded string (raw)
    output.append("### Option A: Using Decoded String")
    for date_desc, date_val in dates.items():
        flag = f"flag{{{info['raw']}_{date_val}_{info['part3_raw']}}}"
        output.append(f"- **{date_desc}**: `{flag}`")
    
    # 2. Using hex string
    output.append("\n### Option B: Using Hex Representation")
    for date_desc, date_val in dates.items():
        flag = f"flag{{{info['hex']}_{date_val}_{info['part3_raw']}}}"
        output.append(f"- **{date_desc}**: `{flag}`")
        if info['part3_hex']:
            flag_hex_part3 = f"flag{{{info['hex']}_{date_val}_{info['part3_hex']}}}"
            output.append(f"  - (Alt Part3): `{flag_hex_part3}`")
    output.append("\n" + "="*40 + "\n")

with open("grouped_candidates.md", "w") as f:
    f.write("\n".join(output))

print("Grouped candidates written to grouped_candidates.md")
