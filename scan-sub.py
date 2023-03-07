# import requests

# def find_subdomain(domain, timeout=3):
#     wordlist = [
#         "admin",
#         "api",
#         "blog",
#         "chat",
#         "image",
#         "login",
#         "mail"
#     ]

#     for subdomain in wordlist:
#         url = f"http://{subdomain}.{domain}"
#         try:
#             response = requests.get(url)
#             status = response.status_code
#             print(f"{url} - {status}")
#         except requests.exceptions.RequestException:
#             pass
        
#         url = f"https://{subdomain}.{domain}"
#         try:
#             response = requests.get(url)
#             status = response.status_code
#             print(f"{url} - {status}")
#         except request.exceptions.RequestExceptions:
#             pass

# domain = "google.com"
# timeout = 4

# find_subdomain(domain, timeout)


import requests

domain = input("Enter domain: ")
file = open('list.txt','r')
content = file.read()

subdomains = content.splitlines()

for subdomain in subdomains:
	url1 = f"http://{subdomain}.{domain}"
	url2 = f"https://{subdomain}.{domain}"
	try:
		requests.get(url1)
		print(f"Discovered URL: {url1}")
		requests.get(url2)
		print(f"Discovered URL: {url2}")
	except requests.ConnectionError:
		pass
