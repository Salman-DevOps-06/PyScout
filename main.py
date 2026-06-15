from Link_Extractor import *
from Web_Crawler import *
from Email_Extractor import *
from Header_Check import *
from Robot_Analyzer import *
from JS_Analyzer import *
import colorama
colorama.init()
# color define
G = '\033[92m'#Green
R = '\033[91m'#Red
Y = '\033[93m'#Yellow
r = '\033[0m'#Reset

try:
    parts = []
    url = input("Enter the URL (starts with http/https): ")
    raw_parts = url.split("/")
    for raw in raw_parts: parts.append(raw+'/')
    if parts[0]=="http:/" or parts[0]=="https:/" or parts[0]=="ftp:/":
        if len(parts)>=3:
            print(G + "****************** Valid Url ******************" + r)
        else: print(R + "###############################\n#         Invalid Url         #\n###############################" + r); sys.exit()
    else:
        print(R + "###############################\n#         Invalid Url         #\n###############################" + r); sys.exit()
except requests.exceptions.Timeout:
    print(R + "[!] Error: The server took too long to respond!" + r); sys.exit()
except requests.exceptions.ConnectionError:
    print(R + "[!] Error: The server did not respond!" + r); sys.exit()
except Exception as e:
    print(R + f"[!] An unexpected error occurred: {e}" + r); sys.exit()

links = Link_Extractor(url=url)
Web_Crawler(url=url,intLink=links)
Email_Extractor(url=url,intLink=links)
Header_Check(url=url)
Robots_Analyzer(url=url)
JS_Analyzer(url=url)

input("Press any key to exit...")