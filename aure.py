from core.valid import classify_target
from recon.ip_recon import ip_recon
from recon.domain_recon import domain_recon
import socket
import pyfiglet 
from colorama import Fore,init

init(autoreset=True)
def banner():
    print(Fore.RED+"="*79)
    print(Fore.RED+pyfiglet.figlet_format("AUTORECON", font="ansi_shadow"))
    print(Fore.RED+"               Basic automatic passive and active reconnassince")
    print(Fore.RED+"="*79)

def resolve(target):
    return socket.gethostbyname(target)

#-----------------main-----------------

banner()
target = input("\n[+] Enter IP address or Domain name : ")
target_type = classify_target(target)

if target_type == "DOMAIN":
    ip = resolve(target)
    print(f"[+] Target ip : {ip}")

if target_type == "IP":
    ip_recon(target)
elif target_type == "DOMAIN":
    domain_recon(target)
else:
    print("[!] Invalid Target")