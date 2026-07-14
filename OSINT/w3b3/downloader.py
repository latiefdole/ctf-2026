import urllib.request
import re
import os

url_base = "https://5b016909-ctf.dsg.id/"
files = [
    "",
    "index.html",
    "forum_post.html",
    "profil.html",
    "analisis.html",
    "pgp_pubkey.asc",
    "profile_analysis.txt",
    "persona_cross.json",
    "operator_note.txt",
    "decoy_token.txt",
    "robots.txt",
    "archive/archived_post.html",
]

os.makedirs("downloads", exist_ok=True)

for f in files:
    url = url_base + f
    out_name = os.path.join("downloads", f.replace("/", "_") if f else "index_root.html")
    print(f"Downloading {url} to {out_name}...")
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as response:
            html = response.read()
            with open(out_name, "wb") as out:
                out.write(html)
            print("  Success")
    except Exception as e:
        print(f"  Failed: {e}")
