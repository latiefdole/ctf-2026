import sys, urllib.request, json
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Try the correct aperisolve API v3
# Based on their GitHub: POST /upload with multipart form
# then GET /{hash} for results

import uuid, hashlib

with open('w2a3/lampiran_surat.jpg', 'rb') as f:
    img_data = f.read()

# Compute SHA256 of image for potential hash lookup
sha256 = hashlib.sha256(img_data).hexdigest()
print('Image SHA256:', sha256)

# Try to fetch existing result if already analyzed
result_url = f'https://www.aperisolve.com/{sha256}'
try:
    req = urllib.request.Request(result_url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req, timeout=15)
    result = resp.read().decode('utf-8', errors='replace')
    print('Existing result length:', len(result))
    if 'steghide' in result.lower() or 'flag' in result.lower():
        # Extract relevant portion
        idx = result.lower().find('steghide')
        if idx >= 0:
            print('Steghide section:', result[max(0,idx-100):idx+500])
except Exception as e:
    print('Fetch existing result error:', e)

# Also try fetching the JSON result
try:
    json_url = f'https://www.aperisolve.com/json/{sha256}'
    req2 = urllib.request.Request(json_url, headers={'User-Agent': 'Mozilla/5.0'})
    resp2 = urllib.request.urlopen(req2, timeout=15)
    result2 = resp2.read().decode('utf-8', errors='replace')
    print('JSON result:', result2[:2000])
except Exception as e:
    print('JSON fetch error:', e)
