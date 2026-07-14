import base64
import codecs

with open('C:/Users/ICT-12/Documents/CTF/Digital_Forensics/case2/encoded_memo.txt', 'r') as f:
    data = f.read().strip()

b64_decoded = base64.b64decode(data).decode('utf-8')
rot13_decoded = codecs.decode(b64_decoded, 'rot_13')

print(rot13_decoded)
