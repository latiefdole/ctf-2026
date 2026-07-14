def search_disk():
    img_path = r'C:\Users\ICT-12\Documents\CTF\w3e2\forensic_disk.img'
    with open(img_path, 'rb') as f:
        data = f.read()
        
    print(f"Disk image loaded. Size: {len(data)} bytes")
    
    # Search for ascii string "kunci_rahasia.txt"
    target = b"kunci_rahasia.txt"
    idx = 0
    while True:
        idx = data.find(target, idx)
        if idx == -1:
            break
        print(f"\nFound target at offset: {idx} (0x{idx:x})")
        # Print surrounding bytes (128 bytes before and after)
        start = max(0, idx - 128)
        end = min(len(data), idx + 128)
        context = data[start:end]
        print(f"Context hex:\n{context.hex()}")
        # Print printable ASCII representation of context
        ascii_repr = "".join(chr(b) if 32 <= b < 127 else "." for b in context)
        print(f"Context ASCII:\n{ascii_repr}")
        idx += len(target)

if __name__ == '__main__':
    search_disk()
