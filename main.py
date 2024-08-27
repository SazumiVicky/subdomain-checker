try:
    from colorama import Fore, Style, init
    colorama_installed = True
    init()
except ImportError:
    colorama_installed = False
    print("[!] Error: Coloring libraries not installed, no coloring will be used [Check the readme]")

import sublist3r
import requests
import time
import itertools
import threading

def loading_animation(message):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if not loading:
            break
        print(f'\r{message} {c}', end='', flush=True)
        time.sleep(0.1)

def check_subdomain_status(root_domain, subdomains):
    results = []
    for subdomain in subdomains:
        url = f"http://{subdomain}"
        try:
            response = requests.get(url)
            status = response.status_code
        except requests.ConnectionError:
            status = 503
        results.append((root_domain, status, subdomain))
    return results

loading = True
t = threading.Thread(target=loading_animation, args=("Initializing script",))
t.start()
time.sleep(2)
loading = False
t.join()
print("\r" + " " * 30, end='\r') 
root_domain = input("Please enter your root domain: ")
loading = True
t = threading.Thread(target=loading_animation, args=("Please wait",))
t.start()
subdomains = sublist3r.main(root_domain, 40, None, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)
results = check_subdomain_status(root_domain, subdomains)
loading = False
t.join()
print("\r" + " " * 30, end='\r') 
if colorama_installed:
    print(Fore.GREEN + "------------------------------------------------------------")
    print("| ROOT DOMAIN        | STATUS |         SUBDOMAIN          |")
    print("------------------------------------------------------------" + Style.RESET_ALL)
else:
    print("------------------------------------------------------------")
    print("| ROOT DOMAIN        | STATUS |         SUBDOMAIN          |")
    print("------------------------------------------------------------")
active_count = 0
inactive_count = 0
for result in results:
    if colorama_installed:
        status_color = Fore.GREEN if result[1] == 200 else Fore.RED
    else:
        status_color = ""
    if result[1] == 200:
        active_count += 1
    else:
        inactive_count += 1
    print(f"{status_color}| {result[0]:<18} | {result[1]:<6} | {result[2]:<25} |{Style.RESET_ALL if colorama_installed else ''}")
if colorama_installed:
    print(Fore.GREEN + "------------------------------------------------------------" + Style.RESET_ALL)
else:
    print("------------------------------------------------------------")
if colorama_installed:
    print(Fore.CYAN + "------------------------------------------------------------")
    print("| ACTIVE             |        |         INACTIVE           |")
    print("------------------------------------------------------------")
    print(f"| {active_count:<18} |        | {inactive_count:<25} |")
    print("------------------------------------------------------------" + Style.RESET_ALL)
else:
    print("------------------------------------------------------------")
    print("| ACTIVE             |        |         INACTIVE           |")
    print("------------------------------------------------------------")
    print(f"| {active_count:<18} |        | {inactive_count:<25} |")
    print("------------------------------------------------------------")