import os
import re

dir_path = "downloads"
files = os.listdir(dir_path)

# Let's read all files and search for patterns
flag_pattern = re.compile(r'flag\{.*?\}|CTF\{.*?\}|ctf\{.*?\}', re.IGNORECASE)
under_pattern = re.compile(r'\b[a-zA-Z0-9_]{5,}\b')

for f_name in files:
    path = os.path.join(dir_path, f_name)
    if os.path.isdir(path):
        continue
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
            # Find flag pattern
            flags = flag_pattern.findall(content)
            if flags:
                print(f"[+] Found flag pattern in {f_name}: {flags}")
                
            # Find occurrences of words with underscores
            if "n0ct" in content or "session" in content or "kunci" in content or "epoch" in content:
                print(f"[*] File {f_name} contains keywords.")
                
            # Check for comments or hidden inputs
            comments = re.findall(r'<!--(.*?)-->', content, re.DOTALL)
            if comments:
                print(f"[+] Comments in {f_name}: {comments}")
    except Exception as e:
        print(f"Error reading {f_name}: {e}")
