import requests
import colorama
colorama.init()
G = '\033[92m'#Green
R = '\033[91m'#Red
Y = '\033[93m'#Yellow
r = '\033[0m'#Reset

def Robots_Analyzer(url):
    disallow_paths = []
    try:
        domain = url.split("/")[0] + "//" + url.split("/")[2]
        robots_url = domain + "/robots.txt"
        print(Y + "Analyzing robots.txt ..... " + r)
        resp = requests.get(robots_url)
        if resp.status_code != 200: print("[!] robots.txt not found")
        print("[+] robots.txt discovered")
        for line in resp.text.splitlines():
            line = line.strip()
            if line.lower().startswith("disallow:"):
                path = line.split(":", 1)[1].strip()
                if path: disallow_paths.append(path)
        if disallow_paths:
            print("\nInteresting Paths:")
            for path in disallow_paths: print(f"    {path}")
        else: print("[!] No disallowed paths found")
    except Exception as e:
        print(R + f"[!] An unexpected error occurred: {e}" + r)