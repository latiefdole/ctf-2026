import re
import base64

with open('redacted_report.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Semua text di dalam span.redacted
redacted = re.findall(r'class="redacted"[^>]*>(.*?)</span>', content, re.DOTALL)
print('=== ISI SPAN REDACTED ===')
for i, r in enumerate(redacted):
    print(f'  [{i+1}] {repr(r)}')

# 2. Semua HTML comments
comments = re.findall(r'<!--(.*?)-->', content, re.DOTALL)
print('\n=== HTML COMMENTS ===')
if comments:
    for c in comments:
        print(repr(c.strip()))
else:
    print('  (tidak ada komentar HTML)')

# 3. Hidden elements
hidden = re.findall(r'display\s*:\s*none|visibility\s*:\s*hidden', content)
print('\n=== HIDDEN ELEMENTS ===')
if hidden:
    for h in hidden:
        print(f'  {h}')
else:
    print('  (tidak ada)')

# 4. Semua data-* attributes
data_attrs = re.findall(r'data-[\w-]+="([^"]+)"', content)
print('\n=== DATA ATTRIBUTES ===')
for d in data_attrs:
    print(f'  {d}')

# 5. Check any base64-ish strings
b64_candidates = re.findall(r'[A-Za-z0-9+/]{20,}={0,2}', content)
print('\n=== POSSIBLE BASE64 ===')
for b in b64_candidates:
    try:
        dec = base64.b64decode(b + '==').decode('utf-8')
        if all(32 <= ord(c) < 127 for c in dec) and len(dec) > 5:
            print(f'  {b} -> {dec}')
    except:
        pass

# 6. Print all links/hrefs
links = re.findall(r'href="([^"]+)"', content)
print('\n=== ALL LINKS ===')
for l in links:
    print(f'  {l}')

# 7. Any meta tags
metas = re.findall(r'<meta[^>]+>', content)
print('\n=== META TAGS ===')
for m in metas:
    print(f'  {m}')
