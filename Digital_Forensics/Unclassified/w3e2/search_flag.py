def search_flag():
    img_path = r'C:\Users\ICT-12\Documents\CTF\w3e2\forensic_disk.img'
    with open(img_path, 'rb') as f:
        data = f.read()
        
    print(f"Searching for 'flag{{'...")
    idx = data.find(b"flag{")
    if idx != -1:
        print(f"Found 'flag{{' at offset {idx} (0x{idx:x})")
        print(data[idx:idx+100])
        
    print("Searching for hex '666c61677b'...")
    idx = data.find(b"666c61677b")
    if idx != -1:
        print(f"Found '666c61677b' at offset {idx} (0x{idx:x})")
        print(data[idx:idx+100])

if __name__ == '__main__':
    search_flag()
