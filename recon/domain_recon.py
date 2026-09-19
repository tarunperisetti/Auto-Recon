from core.runner import run_bash
from colorama import Fore,init

init(autoreset=True)
def sidebanner(n):
    print(Fore.CYAN+"="*79)
    print(Fore.RED+n)
    print(Fore.CYAN+"="*79)

def domain_recon(target):
    sidebanner("[------------------------------------PING-------------------------------------]")
    print(run_bash("modules/bash/ping.sh",target))
    sidebanner("[------------------------------------WHOIS------------------------------------]")
    print(run_bash("modules/bash/whois.sh",target))
    sidebanner("[-------------------------------DNS ENUMERATION-------------------------------]")
    print(run_bash("modules/bash/dns_enum.sh",target))
    sidebanner("[---------------------------------TRACEROUTE----------------------------------]")
    print(run_bash("modules/bash/traceroute.sh",target))