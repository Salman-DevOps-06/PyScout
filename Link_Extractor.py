import requests
from bs4 import BeautifulSoup
import colorama
colorama.init()
G = '\033[92m'#Green
R = '\033[91m'#Red
Y = '\033[93m'#Yellow
r = '\033[0m'#Reset

def Link_Extractor(url):
    links = []; int_link=[]; ext_link=[]

    session = requests.Session()
    print(Y + "Connecting to the URL.....  " + r, end=" ")
    response = session.get(url, timeout=(5, 10))
    print(f"[{response.status_code}]")
    HTML = response.text
    soup = BeautifulSoup(HTML, "lxml")
    a = soup.find_all("a")
    for link in a:
        href = link.get("href")
        if href and href.startswith("https://"):
            links.append(href)
            try:
                if href.split("/")[2].endswith(url.split("/")[2]):
                    int_link.append(href)
                else: ext_link.append(href)
            except IndexError: pass
    print(f"Internal links: {len(int_link)} \nExternal links: {len(ext_link)} \nTotal links: {len(links)}")
    return int_link