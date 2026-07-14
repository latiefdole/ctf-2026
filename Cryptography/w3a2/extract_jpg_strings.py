import string

def extract_strings():
    with open(r'C:\Users\ICT-12\Documents\CTF\w3a2\key_source.jpg', 'rb') as f:
        data = f.read()
        
    curr = []
    for b in data:
        if chr(b) in string.printable and b >= 32 and b <= 126:
            curr.append(chr(b))
        else:
            if len(curr) >= 4:
                print(''.join(curr))
            curr = []
    if len(curr) >= 4:
        print(''.join(curr))

if __name__ == '__main__':
    extract_strings()
