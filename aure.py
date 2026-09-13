from core.valid import classify_target
from recon.ip_recon import ip_recon
from recon.domain_recon import domain_recon
import pyfiglet 
from colorama import Fore,init

init(autoreset=True)
def banner():
    print(Fore.RED+"="*79)
    print(Fore.RED+pyfiglet.figlet_format("AUTORECON", font="ansi_shadow"))
    print(Fore.RED+"               Basic automatic passive and active reconnassince")
    print(Fore.RED+"="*79)

#-----------------main-----------------

banner()
target = input("\n[+] Enter IP address or Domain name : ")
target_type = classify_target(target)
if target_type == "IP":
    ip_recon(target)
elif target_type == "DOMAIN":
    domain_recon(target)
else:
    print("[!] Invalid Target")