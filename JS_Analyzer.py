import requests
from bs4 import BeautifulSoup
import colorama
colorama.init()
# color define
G = '\033[92m'  # Green
R = '\033[91m'  # Red
Y = '\033[93m'  # Yellow
r = '\033[0m'   # Reset

def JS_Analyzer(url):
    print(Y + "Analyzing JavaScript files ..... " + r)
    session = requests.Session()
    response = session.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    domain = url.split("/")[0] + "//" + url.split("/")[2]
    js_files = set()
    keywords = [
        "/api/",
        "/api/v1/",
        "/admin/",
        "/dashboard/",
        "/upload/",
        "/login",
        "/auth"
    ]
    findings = {}
    scripts = soup.find_all("script")
    for script in scripts:
        src = script.get("src")
        if not src:
            continue
        # Convert relative URLs to absolute URLs
        if src.startswith("/"):
            src = domain + src
        elif not src.startswith("http"):
            continue
        js_files.add(src)
    if len(js_files) == 0:
        print("[!] No JavaScript files discovered")
        return
    print(f"[+] JavaScript files discovered: {len(js_files)}")
    for js in js_files:
        try:
            resp = requests.get(js)
            if resp.status_code != 200:
                continue
            content = resp.text.lower()
            matched_keywords = []
            for keyword in keywords:
                if keyword.lower() in content:
                    matched_keywords.append(keyword)
            if matched_keywords:
                findings[js] = matched_keywords
        except Exception as e:
            print(f"[!] Error: {e}")
            continue
    if len(findings) == 0:
        print("[+] No interesting JavaScript findings")
        return
    print("\n[!] Interesting JavaScript Findings\n")
    for js, matched_keywords in findings.items():
        print(f"File: {js}")
        for keyword in set(matched_keywords):
            print(f"    -> {keyword}")
        print()