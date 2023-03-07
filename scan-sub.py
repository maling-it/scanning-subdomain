import requests

def find_subdomain(domain, timeout=3):
    wordlist = [
        "admin",
        "api",
        "blog",
        "chat",
        "image",
        "login",
        "mail"
    ]

    for subdomain in wordlist:
        url = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(url)
            status = response.status_code
            print(f"{url} - {status}")
        except requests.exceptions.RequestException:
            pass
        
        url = f"https://{subdomain}.{domain}"
        try:
            response = requests.get(url)
            status = response.status_code
            print(f"{url} - {status}")
        except request.exceptions.RequestExceptions:
            pass

domain = "google.com"
timeout = 4

find_subdomain(domain, timeout)