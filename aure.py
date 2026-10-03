from core.valid import classify_target
from recon.ip_recon import ip_recon
from recon.domain_recon import domain_recon
import socket
from core.report import create_report
import pyfiglet 
from colorama import Fore,init

init(autoreset=True)
def banner():
    print(Fore.CYAN+"="*79)
    print(Fore.RED+pyfiglet.figlet_format("AUTORECON", font="ansi_shadow"))
    print(Fore.RED+"               Basic automatic passive and active reconnassince")
    print(Fore.CYAN+"="*79)

#-----------------main-----------------

banner()
target = input("\n[✱] Enter IP address or Domain name : ")
target_type = classify_target(target)

if target_type == "DOMAIN":
    ip = socket.gethostbyname(target)
    print(f"[+] Target IP : {ip}\n")
elif target_type == "IP":
    domain = socket.gethostbyaddr(target)
    print(f"[+] Target Domain : {domain}\n")
else:
    print("[✘] Invalid Target")