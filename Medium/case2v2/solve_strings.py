import string

with open('C:/Users/ICT-12/Documents/CTF/Digital_Forensics/case2v2/kode_akses', 'rb') as f:
    data = f.read()

printable = set(bytes(string.printable, 'ascii'))

current_str = []
for b in data:
    if b in printable:
        current_str.append(chr(b))
    else:
        if len(current_str) > 4:
            s = "".join(current_str)
            if "flag" in s.lower() or "key" in s.lower() or len(s) > 8:
                print(s)
        current_str = []
if len(current_str) > 4:
    print("".join(current_str))
