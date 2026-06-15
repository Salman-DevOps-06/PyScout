import requests,sys
import colorama
colorama.init()
G = '\033[92m'#Green
R = '\033[91m'#Red
Y = '\033[93m'#Yellow
r = '\033[0m'#Reset

def Header_Check(url):
    # send request and get response
    print(Y + f"Checking the Headers ....." + r)
    session = requests.Session()
    try:
        response = session.get(url, timeout=(10, 20))
        header = response.headers
        # checking security headers
        security_header = [
            "Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options",
            "X-XSS-Protection", "Strict-Transport-Security", "Referrer-Policy",
        ]
        print("Headers: ")
        for i in security_header:
            if header.get(i) is None:
                print(R + f"[!] Missing Header: {i}" + r)
            else:
                print(G + f"[+] Header: {i}" + r)
    except requests.exceptions.Timeout:
        print(R + "[!] Error: The server took too long to respond!" + r); sys.exit()
    except requests.exceptions.ConnectionError:
        print(R + "[!] Error: The server did not respond!" + r); sys.exit()
    except Exception as e:
        print(R + f"[!] An unexpected error occured: {e}" + r); sys.exit()
