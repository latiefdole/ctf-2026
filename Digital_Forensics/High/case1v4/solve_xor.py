import string

with open('C:/Users/ICT-12/Documents/CTF/Digital_Forensics/case1v4/func_table', 'rb') as f:
    data = f.read()

xored = bytes([b ^ 0x4f for b in data])

printable = set(bytes(string.printable, 'ascii'))
current_str = []
for b in xored:
    if b in printable:
        current_str.append(chr(b))
    else:
        if len(current_str) > 4:
            s = "".join(current_str)
            if "flag" in s.lower() or "{" in s:
                print(s)
        current_str = []
if len(current_str) > 4:
    print("".join(current_str))

current_str = []
for b in data:
    if b in printable:
        current_str.append(chr(b))
    else:
        if len(current_str) > 4:
            s = "".join(current_str)
            if "flag" in s.lower() or "{" in s:
                print("raw:", s)
        current_str = []
