from core.valid import classify_target
from core.report import create_report
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

choice = input("[?] Select recon : ")

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

auto_recon(choice,target)

if choice not in ("0", "15"):
    print("\n[+] Selected reconnaissance completed!")

    report_choice = input(
        "\n[?] Do you want to generate a report now? (y/n): "
    ).strip().lower()

    if report_choice in ("y", "yes"):
        create_report(target)
    else:
        print("\n[*] Report generation skipped.")
        print("[+] Your saved results are available for later.")