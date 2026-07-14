import urllib.request
import urllib.parse
import http.cookiejar

url = "https://1c8df2b4-ctf.dsg.id/login"
data = urllib.parse.urlencode({'username': 'kepalaops', 'password': 'surabaya'}).encode('utf-8')

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

try:
    req = urllib.request.Request(url, data=data)
    response = opener.open(req)
    print(f"Login status: {response.getcode()}")
    print("Cookies:")
    for cookie in cj:
        print(f"{cookie.name}: {cookie.value}")
        
    dashboard_req = urllib.request.Request("https://1c8df2b4-ctf.dsg.id/")
    dashboard_resp = opener.open(dashboard_req)
    print("\nDashboard:")
    print(dashboard_resp.read().decode('utf-8')[:500])
except Exception as e:
    print(f"Error: {e}")
