import urllib.request
import urllib.error

url_base = "https://5b016909-ctf.dsg.id/"

paths = [
    "private/",
    "private/flag.txt",
    "private/operator.txt",
    "private/note.txt",
    "private/session.txt",
    "archive/",
    "archive/archived_post.html",
    "archive/flag.txt",
    "archive/note.txt",
    "robots.txt",
    "flag.txt",
    "flag",
    "secret",
    "secret.txt",
]

for p in paths:
    url = url_base + p
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            print(f"[+] {p} : {response.status} (Length: {len(response.read())})")
    except urllib.error.HTTPError as e:
        print(f"[-] {p} : {e.code}")
    except Exception as e:
        print(f"[!] {p} : {e}")
