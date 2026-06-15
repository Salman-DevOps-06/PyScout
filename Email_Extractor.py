import requests,re
import colorama
colorama.init()
G = '\033[92m'#Green
R = '\033[91m'#Red
Y = '\033[93m'#Yellow
r = '\033[0m'#Reset

def Email_Extractor(url,intLink):
    emails = set(); count=1
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    print(Y + "Extracting emails .....  " + r)
    session = requests.Session()
    response = session.get(url)
    HTML = response.text
    found_emails = re.findall(pattern, HTML)
    for email in found_emails:
        emails.add(email)
    for link in intLink:
        total = len(intLink)
        progress = int((count / total) * 20)
        print(
            f"[{'#' * progress}{'-' * (20 - progress)}] ",
            end=""
        )
        try:
            resp = requests.get(link)
            found_emails = re.findall(pattern, resp.text)
            for email in found_emails:
                emails.add(email)
        except Exception as e: print(f"Error: {e}",end=""); continue
        count += 1; print(end="\r")
    print(f"Emails Found: {len(emails)}")
    for email in emails:
        print(email, end=", ")
