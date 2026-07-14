import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

data = open('w2a3/lampiran_surat.jpg', 'rb').read()

# Check for common stego tools signatures in JPEG data
# steghide embeds data after specific signature

# Look for 'flag{' pattern directly
flag_pos = data.find(b'flag{')
if flag_pos != -1:
    print('Found flag{ at:', flag_pos)
    print('Flag:', data[flag_pos:flag_pos+50])

# Look for known stego tool signatures
# steghide: uses custom format, not directly readable
# outguess: embedded in DCT coefficients
# jsteg: LSB of DCT coefficients

# Let's check if there's a ZIP/RAR embedded
zip_sig = data.find(b'PK\x03\x04')
print('ZIP signature at:', zip_sig)

rar_sig = data.find(b'Rar!')
print('RAR signature at:', rar_sig)

# Check for base64 encoded data embedded in comments or EXIF UserComment
# Look for ASCII that looks like base64 or flag
import re
# Scan for printable long strings anywhere in the file
ascii_strings = re.findall(b'[ -~]{8,}', data)
print('\nLong strings in JPEG:')
for s in ascii_strings:
    decoded = s.decode('ascii', 'ignore')
    print(repr(decoded))
