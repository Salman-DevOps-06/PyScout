import requests
from bs4 import BeautifulSoup
import colorama
colorama.init()
G = '\033[92m'#Green
R = '\033[91m'#Red
Y = '\033[93m'#Yellow
r = '\033[0m'#Reset

def Web_Crawler(url,intLink):
    dep2 = []; dplct = [url]; count=1

    print(Y + "Crawling the list of Internal links .....  " + r)
    for link in intLink:
        total = len(intLink)
        progress = int((count / total) * 20)
        print(
            f"[{'#' * progress}{'-' * (20 - progress)}] "
            f"{count}/{total}"
            f" {link}",
            end=""
        )
        if link not in dplct:
            dplct.append(link)
            try:
                resp = requests.get(link)
            except Exception as e: print(R + f"[!] An unexpected error occurred: {e} with link: {link}" + r,end=""); continue
            if resp.status_code in [200,301,302]:
                soup = BeautifulSoup(resp.text, "lxml")
                a = soup.find_all("a")
                for hrf in a:
                    href = hrf.get("href")
                    if href and href.startswith("https://"):
                        dep2.append(href)
        count += 1
        print(end="\r")
    print(f"Home Page:-\n     {url}\nDepth 1:({len(intLink)} pages)\n     {intLink}\nDepth 2:({len(dep2)} pages)\n    {dep2[:100]}")

