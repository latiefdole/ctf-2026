import base64

def solve():
    encoded = "V11QVkpTSEVUWl5VVG5FVENCVFxTRF9IWG4CAEw="
    key = 49
    flag = bytes([b ^ key for b in base64.b64decode(encoded)]).decode()
    print("Flag:", flag)
    return flag

if __name__ == "__main__":
    solve()
