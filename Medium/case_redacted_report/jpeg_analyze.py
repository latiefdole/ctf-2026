import struct
import re

with open('profile.jpg', 'rb') as f:
    data = f.read()

print(f'File size: {len(data)} bytes')
print()

# Parse JPEG segments
i = 0
while i < len(data) - 1:
    if data[i] == 0xFF:
        marker = data[i+1]
        if marker == 0xD8:
            print(f'SOI at offset {i}')
            i += 2
            continue
        elif marker == 0xD9:
            print(f'EOI at offset {i}')
            # Check if there's data after EOI
            remaining = data[i+2:]
            if remaining:
                print(f'!!! DATA AFTER EOI: {len(remaining)} bytes !!!')
                try:
                    text = remaining.decode('utf-8', errors='replace')
                    print(f'As text: {repr(text[:500])}')
                except:
                    print(f'Raw hex: {remaining[:100].hex()}')
            break
        elif marker in (0xE0, 0xE1, 0xE2, 0xFE, 0xED):
            length = struct.unpack('>H', data[i+2:i+4])[0]
            segment = data[i+4:i+2+length]
            marker_names = {0xE0: 'APP0/JFIF', 0xE1: 'APP1/EXIF', 0xE2: 'APP2', 0xFE: 'COMMENT', 0xED: 'APP13/IPTC'}
            name = marker_names.get(marker, f'0xFF{marker:02X}')
            print(f'{name} at offset {i}, length {length}')
            if marker == 0xFE:
                comment_text = segment.decode('utf-8', errors='replace')
                print(f'  COMMENT: {repr(comment_text)}')
            if marker == 0xE1:
                strings = re.findall(b'[\x20-\x7e]{6,}', segment)
                for s in strings:
                    print(f'  EXIF string: {s.decode()}')
            i += 2 + length
        else:
            if i+3 < len(data):
                length = struct.unpack('>H', data[i+2:i+4])[0]
            else:
                length = 0
            if length > 0:
                i += 2 + length
            else:
                i += 2
    else:
        i += 1

# Also check all GPS/EXIF tags in raw
print("\n=== FULL STRING SCAN ===")
all_strings = re.findall(b'[\x20-\x7e]{8,}', data)
for s in all_strings:
    decoded = s.decode('ascii')
    # Filter out JPEG noise
    if not all(c in 'QEH()\\' for c in decoded):
        print(f'  {decoded}')
