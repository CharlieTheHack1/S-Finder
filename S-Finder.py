import requests

#colours used
red = '\033[31m'

print()
print (red+"""
███████╗      ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝      ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
███████╗█████╗█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
╚════██║╚════╝██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
███████║      ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚══════╝      ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝                                                              
"""+red)

print("\033[96m Coded By - Charlie : The Hacker")
print(" Instagram 1 : https://instagram.com/7.7.7.7_hacker ")
print(" Instagram 2 : https://instagram.com/7.7.7.7_hacker ")
print(" Twitter  https://twitter.com/CharlieTheHack1 \033[0m")
print()
domain = input("Enter domain: ")
file = open('wordlist.txt','r')
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
