import mimetypes

with open('C:/Users/ICT-12/Documents/CTF/Digital_Forensics/case2v2/kode_akses', 'rb') as f:
    header = f.read(100)
    print("Header hex:", header.hex())
    print("Header ascii:", "".join(chr(c) if 32 <= c <= 126 else '.' for c in header))
