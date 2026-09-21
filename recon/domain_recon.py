from core.runner import run_bash
from colorama import Fore,init

init(autoreset=True)
def sidebanner(n):
    print(Fore.CYAN+"="*82)
    print(Fore.RED+n)
    print(Fore.CYAN+"="*82)

def domain_recon(target):
    results = {}

#------------------------------active-recon-------------------------------------------------------
    sidebanner("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ACTIVE-RECONNAISSANCE]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
    
    sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PING<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
    results["ping.txt"] = run_bash("modules/bash/ping.sh",target)
    print(results["ping.txt"])
    sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TRACEROUTE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
    results["traceroute.txt"] = run_bash("modules/bash/traceroute.sh",target)
    print(results["traceroute.txt"])
    sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>NMAP SERVICE SCAN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
    results["nmap_service.txt"] = run_bash("modules/bash/nmap_service.sh",target)
    print(results["nmap_service.txt"])
    sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>NMAP OS SCAN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
    results["nmap_os.txt"] = run_bash("modules/bash/nmap_os.sh",target)
    print(results["nmap_os.txt"])
    sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>HHTP HEADERS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
    results["http_headers.txt"] = run_bash("modules/bash/http_headers.sh",target)
    print(results["http_headers.txt"])
    sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WHATWEB<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
    results["whatweb.txt"] = run_bash("modules/bash/whatweb.sh",target)
    print(results["whatweb.txt"])

#----------------------------passive-recon------------------------------------------------------- 
    sidebanner("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[PASSIVE-RECONNAISSANCE]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")

    sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WHOIS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
    results["whois.txt"] = run_bash("modules/bash/whois.sh",target)
    print(results["whois.txt"])
    sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>DNS ENUMERATION<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
    results["dns_enum.txt"] = run_bash("modules/bash/dns_enum.sh",target)
    print(results["dns_enum.txt"])
    sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>GOOGLE-DORKING<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
    results["google_dorking.txt"] = run_bash("modules/bash/google_dorking.sh",target)
    print(results["google_dorking.txt"])
    sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>SUBDOMAINS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
    results["subdomain.txt"] = run_bash("modules/bash/subdomain_enum.sh",target)
    print(results["subdomain.txt"])