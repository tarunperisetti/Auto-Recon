from core.valid import classify_target
from recon.auto_recon import auto_recon
import socket
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
    exit()

print("""
╔══════════════════════════════════════════════╗
║                 AUTO RECON                   ║
╠══════════════════════════════════════════════╣
║                                              ║
║                PASSIVE RECON                 ║
║                                              ║
║  [1]  WHOIS Information                      ║
║  [2]  Search Engine Recon                    ║
║  [3]  Google Dorking                         ║
║  [4]  Email Enumeration                      ║
║  [5]  IP Information                         ║
║                                              ║
║                ACTIVE RECON                  ║
║                                              ║
║  [6]  DNS Enumeration                        ║
║  [7]  Subdomain Enumeration                  ║
║  [8]  Port Scanning                          ║
║  [9]  Service Enumeration                    ║
║  [10] HTTP Header Analysis                   ║
║  [11] Web Technology Detection               ║
║  [12] Robots & Sitemap Check                 ║
║  [13] SSL/TLS Information                    ║
║  [14] Directory Enumeration                  ║
║                                              ║
║                 OPERATIONS                   ║
║                                              ║
║  [15] Generate Report                        ║
║  [0]  Exit                                   ║
║                                              ║
╚══════════════════════════════════════════════╝
""")

choice = input("[?] Select recon : ")
auto_recon(choice,target)