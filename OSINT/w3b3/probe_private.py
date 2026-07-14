import urllib.request
import urllib.error

url_base = "https://5b016909-ctf.dsg.id/private/"

filenames = [
    "",
    "index.html",
    "index.php",
    "operator_note.txt",
    "decoy_token.txt",
    "profile_analysis.txt",
    "persona_cross.json",
    "session.txt",
    "key.txt",
    "flag.txt",
    "flag",
    "credentials.txt",
    "config.php",
    "config.html",
    "auth.txt",
    "secret.txt",
    "admin.txt",
    "admin.php",
    "note.txt",
    "notes.txt",
    "memo.txt",
    "run.sh",
    "setup.sh",
]

for f in filenames:
    url = url_base + f
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(f"[+] {f} : {response.status} (Length: {len(body)})")
            if len(body) < 1000:
                print(body.decode(errors='replace')[:200])
    except urllib.error.HTTPError as e:
        print(f"[-] {f} : {e.code}")
    except Exception as e:
        print(f"[!] {f} : {e}")
