from core.valid import classify_target
from recon.ip_recon import ip_recon
from recon.domain_recon import domain_recon

#-----------------main-----------------

target = input("[+] Enter IP address or Domain name : ")
target_type = classify_target(target)
if target_type == "IP":
    ip_recon(target)
elif target_type == "DOMAIN":
    domain_recon(target)
else:
    print("[!] Invalid Target")