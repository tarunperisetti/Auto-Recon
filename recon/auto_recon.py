from core.runner import run_bash
from modules.python.geoip import run_geoip
from colorama import Fore,init

init(autoreset=True)
def sidebanner(n):
    print(Fore.CYAN+"="*82)
    print(Fore.RED+n)
    print(Fore.CYAN+"="*82)

#------------------------------active-recon-------------------------------------------------------
def auto_recon(choice,target):

    match choice:

        case "1":
            sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WHOIS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
            run_bash("modules/bash/whois.sh",target) 
        case "2":
            sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WHOIS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]") 
        case "3":  
            sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>GOOGLE-DORKING<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
            run_bash("modules/bash/google_dorking.sh",target)
        case "4":
            sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>EMAIL-ENUMERATION<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
            run_bash("modules/bash/email_enum.sh",target)
        case "5":
            sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>IP INFO<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]") 
            run_geoip(target)
        case "6":
            sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>DNS-ENUMERATION<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
            run_bash("modules/bash/dns_enum.sh",target)
        case "7":
            sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>SUBDOMAINS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
            run_bash("modules/bash/subdomain_enum.sh",target)
        case "8":    
            sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>NMAP BASIC SCAN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
            run_bash("modules/bash/nmap_os.sh",target)
        case "9":
            sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>NMAP SERVICE SCAN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
            run_bash("modules/bash/nmap_service.sh",target)
        case "10":   
            sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>HHTP HEADERS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
            run_bash("modules/bash/http_headers.sh",target)
        case "11":    
            sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WHATWEB<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
            run_bash("modules/bash/whatweb.sh",target)
         
            sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TRACEROUTE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
            run_bash("modules/bash/traceroute.sh",target) 

            

            sidebanner("[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PING<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<]")
            run_bash("modules/bash/ping.sh",target) 
    