import sys, struct
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Pure Python JPEG DCT coefficient extractor (jsteg-style)
# jsteg embeds data in LSBs of non-zero, non-1/-1 DCT coefficients

data = open('w2a3/lampiran_surat.jpg', 'rb').read()

# --- Parse Huffman tables ---
class HuffTable:
    def __init__(self, bits, huffval):
        self.bits = bits
        self.huffval = huffval
        # Build lookup: code -> (length, value)
        self.lookup = {}
        code = 0
        idx = 0
        for length in range(1, 17):
            count = bits[length - 1]
            for _ in range(count):
                self.lookup[code] = (length, huffval[idx])
                idx += 1
                code += 1
            code <<= 1

def parse_dht(seg):
    tables = {}
    pos = 0
    while pos < len(seg):
        tc_th = seg[pos]; pos += 1
        tc = (tc_th >> 4) & 0xF  # 0=DC, 1=AC
        th = tc_th & 0xF          # table id
        bits = list(seg[pos:pos+16]); pos += 16
        total = sum(bits)
        huffval = list(seg[pos:pos+total]); pos += total
        tables[(tc, th)] = HuffTable(bits, huffval)
    return tables

# --- Parse quantization tables ---
def parse_dqt(seg):
    tables = {}
    pos = 0
    while pos < len(seg):
        pq_tq = seg[pos]; pos += 1
        pq = (pq_tq >> 4) & 0xF  # 0=8bit, 1=16bit
        tq = pq_tq & 0xF
        if pq == 0:
            vals = list(seg[pos:pos+64]); pos += 64
        else:
            vals = list(struct.unpack('>64H', seg[pos:pos+128])); pos += 128
        tables[tq] = vals
    return tables

# --- Parse SOS ---
def parse_sos(seg):
    ns = seg[0]
    components = []
    for i in range(ns):
        cs = seg[1 + i*2]
        td_ta = seg[2 + i*2]
        td = (td_ta >> 4) & 0xF  # DC table
        ta = td_ta & 0xF          # AC table
        components.append((cs, td, ta))
    return components

# --- Bitstream reader ---
class BitReader:
    def __init__(self, data):
        self.data = data
        self.pos = 0
        self.buf = 0
        self.bits = 0
    
    def read_bit(self):
        if self.bits == 0:
            while self.pos < len(self.data):
                b = self.data[self.pos]; self.pos += 1
                if b == 0xFF:
                    nb = self.data[self.pos] if self.pos < len(self.data) else 0
                    if nb == 0x00:
                        self.pos += 1  # stuffed byte
                        self.buf = (self.buf << 8) | 0xFF
                        self.bits += 8
                        break
                    elif 0xD0 <= nb <= 0xD7:
                        self.pos += 1  # restart marker
                        continue
                    else:
                        return None  # end of scan
                else:
                    self.buf = (self.buf << 8) | b
                    self.bits += 8
                    break
        if self.bits == 0:
            return None
        self.bits -= 1
        return (self.buf >> self.bits) & 1

    def read_bits(self, n):
        val = 0
        for _ in range(n):
            b = self.read_bit()
            if b is None:
                return None
            val = (val << 1) | b
        return val

    def decode_huffman(self, table):
        code = 0
        for length in range(1, 17):
            bit = self.read_bit()
            if bit is None:
                return None
            code = (code << 1) | bit
            if (length, code) in [(table.lookup[c][0], c) for c in table.lookup if table.lookup[c][0] == length]:
                for c in table.lookup:
                    if table.lookup[c] == (length, code):
                        return table.lookup[c][1]
        return None

# Parse JPEG structure
pos = 0
dqt = {}
dht = {}
sof = None
sos_header = None
scan_start = None

while pos < len(data) - 1:
    if data[pos] != 0xFF:
        pos += 1
        continue
    marker = data[pos+1]
    if marker == 0xD8:
        pos += 2; continue
    if marker == 0xD9:
        break
    if marker in (0xD0,0xD1,0xD2,0xD3,0xD4,0xD5,0xD6,0xD7):
        pos += 2; continue
    if marker == 0xDA:
        length = struct.unpack('>H', data[pos+2:pos+4])[0]
        sos_header = parse_sos(data[pos+4:pos+2+length])
        scan_start = pos + 2 + length
        break
    length = struct.unpack('>H', data[pos+2:pos+4])[0]
    seg = data[pos+4:pos+2+length]
    if marker == 0xDB:
        dqt.update(parse_dqt(seg))
    elif marker == 0xC4:
        dht.update(parse_dht(seg))
    elif marker == 0xC0:
        precision = seg[0]
        height = struct.unpack('>H', seg[1:3])[0]
        width = struct.unpack('>H', seg[3:5])[0]
        ncomp = seg[5]
        sof = (height, width, ncomp, seg[6:6+ncomp*3])
    pos += 2 + length

print(f"Image: {sof[1]}x{sof[0]}, components={sof[2]}")
print(f"DHT tables: {list(dht.keys())}")
print(f"DQT tables: {list(dqt.keys())}")
print(f"SOS components: {sos_header}")
print(f"Scan data starts at: {scan_start}")

# Extract DCT coefficients using simplified approach
# For jsteg detection, extract LSBs of scan stream AC coefficients
scan_data = data[scan_start:]

# Simple approach: collect raw bytes of scan, skip stuffed FF00, extract LSBs
raw_bits = []
i = 0
while i < len(scan_data) - 1:
    b = scan_data[i]
    if b == 0xFF:
        nb = scan_data[i+1]
        if nb == 0x00:  # stuffed
            raw_bits.extend([int(x) for x in f'{0xFF:08b}'])
            i += 2
            continue
        elif 0xD0 <= nb <= 0xD7:  # restart
            i += 2
            continue
        else:
            break
    raw_bits.extend([int(x) for x in f'{b:08b}'])
    i += 1

# Rebuild bytes from raw_bits
raw_bytes = bytearray()
for i in range(0, len(raw_bits) - 7, 8):
    v = 0
    for j in range(8):
        v = (v << 1) | raw_bits[i+j]
    raw_bytes.append(v)

# Now try extracting LSBs from these raw bytes (jsteg method)
lsb_bits = [b & 1 for b in raw_bytes]
hidden = bytearray()
for i in range(0, len(lsb_bits) - 7, 8):
    v = 0
    for j in range(8):
        v = (v << 1) | lsb_bits[i+j]
    hidden.append(v)

flag_pos = hidden.find(b'flag{')
print(f"\nLSB of raw scan bytes ({len(hidden)} bytes):")
if flag_pos != -1:
    print("FLAG FOUND:", hidden[flag_pos:flag_pos+60])
else:
    print("No flag{ found")
    print("First 40:", repr(hidden[:40]))
    # Try searching for 'CTF' or common patterns
    for pat in [b'CTF', b'ctf', b'KEY', b'key', b'{', b'NSS', b'gelom']:
        p = hidden.find(pat)
        if p != -1:
            print(f"Found '{pat}' at {p}:", repr(hidden[p:p+40]))
