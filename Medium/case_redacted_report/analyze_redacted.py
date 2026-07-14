import re

with open('redacted_report.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract redacted spans content
pattern = r'class="redacted"[^>]*>([^<]*)<'
redacted = re.findall(pattern, content)
print('=== REDACTED CONTENT ===')
for r in redacted:
    print(repr(r))

# HTML Comments
comment_pattern = r'<!--(.*?)-->'
comments = re.findall(comment_pattern, content, re.DOTALL)
print('\n=== HTML COMMENTS ===')
for c in comments:
    print(repr(c.strip()))

# All text inside tags that might be hidden
print('\n=== FULL RAW CONTENT ===')
print(content)
