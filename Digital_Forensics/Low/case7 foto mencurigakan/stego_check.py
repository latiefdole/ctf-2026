import re

# Check all files for zero-width characters, invisible unicode, etc.
files = ['index_dl.html', 'redacted_report.html', 'email_thread_dl.txt']

for fname in files:
    print(f'\n=== {fname} ===')
    with open(fname, 'rb') as f:
        raw = f.read()
    
    # Zero-width chars: U+200B, U+200C, U+200D, U+FEFF, U+2060
    zw_chars = [b'\xe2\x80\x8b', b'\xe2\x80\x8c', b'\xe2\x80\x8d', b'\xef\xbb\xbf', b'\xe2\x81\xa0']
    zw_names = ['ZWSP', 'ZWNJ', 'ZWJ', 'BOM/ZWNBSP', 'WJ']
    
    for zw, name in zip(zw_chars, zw_names):
        count = raw.count(zw)
        if count > 0:
            positions = [i for i in range(len(raw)) if raw[i:i+len(zw)] == zw]
            print(f'  {name} found {count} times at positions: {positions[:20]}')
    
    # Any non-ASCII non-whitespace chars
    non_ascii = [(i, raw[i]) for i in range(len(raw)) if raw[i] > 127]
    if non_ascii:
        print(f'  Non-ASCII bytes: {len(non_ascii)} occurrences')
        # Group by byte value
        from collections import Counter
        byte_counts = Counter(b for _, b in non_ascii)
        for byte_val, cnt in byte_counts.most_common(10):
            print(f'    0x{byte_val:02X}: {cnt} times')
    
    # Check for unusual whitespace (tabs, multiple spaces that might encode data)
    with open(fname, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    
    trailing_spaces = []
    for i, line in enumerate(lines):
        stripped = line.rstrip('\n\r')
        if stripped != stripped.rstrip():
            trailing = len(stripped) - len(stripped.rstrip())
            trailing_spaces.append((i+1, trailing))
    
    if trailing_spaces:
        print(f'  Lines with trailing whitespace: {len(trailing_spaces)}')
        for linenum, count in trailing_spaces[:10]:
            print(f'    Line {linenum}: {count} trailing spaces')
        
        # Could be whitespace steganography - decode as binary
        bits = ''.join('1' if t > 1 else '0' for _, t in trailing_spaces)
        if len(bits) >= 8:
            text = ''
            for j in range(0, len(bits) - 7, 8):
                byte = int(bits[j:j+8], 2)
                if 32 <= byte <= 126:
                    text += chr(byte)
            if text:
                print(f'    Whitespace stego decode: {repr(text)}')
