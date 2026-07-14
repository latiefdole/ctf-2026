import sys, urllib.request, json, time
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('w2a3/lampiran_surat.jpg', 'rb') as f:
    img_data = f.read()

# Try the correct aperisolve endpoint
boundary = b'----CTFBoundary'
part1 = b'--' + boundary + b'\r\nContent-Disposition: form-data; name="file"; filename="lampiran_surat.jpg"\r\nContent-Type: image/jpeg\r\n\r\n'
part2 = b'\r\n--' + boundary + b'--\r\n'
body = part1 + img_data + part2

# Try steghide with the password
part_pw1 = b'--' + boundary + b'\r\nContent-Disposition: form-data; name="steghide"\r\n\r\n'
part_pw2 = b'gelombang_hitam'
part_pw3 = b'\r\n'

# Also try stegseek online via their API
# Or use the correct aperisolve v3 API
req = urllib.request.Request(
    'https://www.aperisolve.com/upload',
    data=body,
    headers={
        'Content-Type': 'multipart/form-data; boundary=' + boundary.decode(),
        'User-Agent': 'Mozilla/5.0'
    }
)
try:
    resp = urllib.request.urlopen(req, timeout=30)
    result = resp.read().decode('utf-8', errors='replace')
    # Look for flag or steghide result
    if 'flag' in result.lower() or 'steghide' in result.lower():
        print('INTERESTING:', result[:2000])
    else:
        print('Response length:', len(result))
        # Try to extract any interesting JSON
        import re
        jsons = re.findall(r'\{[^{}]+\}', result)
        for j in jsons[:5]:
            print(j)
except Exception as e:
    print('Error:', e)
