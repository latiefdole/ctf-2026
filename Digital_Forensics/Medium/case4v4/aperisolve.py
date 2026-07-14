import sys, urllib.request
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('w2a3/lampiran_surat.jpg', 'rb') as f:
    img_data = f.read()

boundary = b'----CTFBoundary7MA4YWxk'
part1 = b'--' + boundary + b'\r\n'
part1 += b'Content-Disposition: form-data; name="file"; filename="lampiran_surat.jpg"\r\n'
part1 += b'Content-Type: image/jpeg\r\n\r\n'
part2 = b'\r\n--' + boundary + b'--\r\n'
body = part1 + img_data + part2

req = urllib.request.Request(
    'https://aperisolve.fr/api/upload',
    data=body,
    headers={
        'Content-Type': 'multipart/form-data; boundary=' + boundary.decode(),
        'User-Agent': 'Mozilla/5.0'
    }
)
try:
    resp = urllib.request.urlopen(req, timeout=30)
    result = resp.read().decode('utf-8', errors='replace')
    print('Aperisolve result:', result[:3000])
except Exception as e:
    print('Error:', e)
