import urllib.request
import urllib.error

url_base = "https://5b016909-ctf.dsg.id/"

filenames = [
    "secret_note.txt", "secret_notes.txt",
    "operational_note.txt", "operational_notes.txt",
    "operator_notes.txt",
    "session_key.txt", "session_keys.txt",
    "forum_archive.html", "forum_archived.html",
    "archived_post.html",
    "private.txt",
    "key.asc", "public_key.asc", "pubkey.asc",
    "encrypted_message.txt", "encrypted.txt", "message.txt",
    "coordination_note.txt", "coordination.txt",
    "intel_report.txt", "intel.txt",
    "sigilum_report.txt", "report.txt",
    "profile.html", "analysis.html",
    "profile.jpg", "avatar.jpg", "avatar.png",
    "photo.jpg", "photo.png",
    "backup.zip", "backup.tar.gz", "backup.tgz",
    ".git/config", ".git/HEAD",
    ".env", ".htaccess",
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
        if e.code != 404:
            print(f"[!] {f} : {e.code}")
    except Exception as e:
        print(f"[ERROR] {f} : {e}")
