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

print("""
╔══════════════════════════════════════════════╗
║                 AUTO RECON                   ║
╠══════════════════════════════════════════════╣
║                                              ║
║                PASSIVE RECON                 ║
║                                              ║
║  [1]  WHOIS Information                      ║
║  [2]  Shodan Recon                           ║
║  [3]  Google Dorking                         ║
║  [4]  Email Enumeration                      ║
║  [5]  IP Information                         ║
║  [6]  ASN Lookup                             ║
║                                              ║
║                ACTIVE RECON                  ║
║                                              ║
║  [7]  DNS Enumeration                        ║
║  [8]  Subdomain Enumeration                  ║
║  [9]  Port Scanning                          ║
║  [10] Service Enumeration                    ║
║  [11] HTTP Header Analysis                   ║
║  [12] Web Technology Detection               ║
║  [13] HTTP_Method Enumeration                ║
║  [14] Directory Enumeration                  ║
║                                              ║
║                 OPERATIONS                   ║
║                                              ║
║  [15] Generate Report                        ║
║  [0]  Exit                                   ║
║                                              ║
╚══════════════════════════════════════════════╝
""")


while True:
    choice = input("[?] Select recon : ").strip()

    if choice == "0":
        print("[✱] Exiting Auto-Recon. Goodbye!")
        break

    elif choice in [str(i) for i in range(1, 15)]:
        target = input("\n[✱] Enter IP address or Domain name : ")
        target_type = classify_target(target)

        if target_type == "DOMAIN":
            ip = socket.gethostbyname(target)
            print(f"[+] Target IP : {ip}\n")
        elif target_type == "IP":
            domain = socket.gethostbyaddr(target)
            print(f"[+] Target Domain : {domain}\n")
        auto_recon(choice, target)

        input("\n[✱] Press Enter to return to the menu...")

    else:
        print("[✘] Invalid Option")