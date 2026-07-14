import re

print('============ INDEX.HTML ============')
with open('index_dl.html', 'r', encoding='utf-8') as f:
    content = f.read()

comments = re.findall(r'<!--(.*?)-->', content, re.DOTALL)
print('HTML Comments:', comments if comments else 'TIDAK ADA')

links = re.findall(r'href="(.*?)"', content)
print('Links:')
for l in links:
    print(' ', l)

metas = re.findall(r'<meta[^>]+>', content)
print('Meta tags:')
for m in metas:
    print(' ', m)

# Check for any hidden text
hidden_spans = re.findall(r'<span[^>]*style="[^"]*color\s*:\s*#[0-9a-fA-F]{6}[^"]*"[^>]*>(.*?)</span>', content, re.DOTALL)
print('Colored spans:', hidden_spans)

print()
print('============ EMAIL_THREAD.TXT ============')
with open('email_thread_dl.txt', 'r', encoding='utf-8') as f:
    email = f.read()
print(email)
