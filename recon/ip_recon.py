from core.runner import run_bash
from modules.python.geoip import run_geoip

def ip_recon(target):
    print(run_bash("modules/bash/ping.sh",target))
    print(run_bash("modules/bash/whois.sh",target))
    print(run_bash("modules/bash/dns_enum.sh",target))
    print(run_bash("modules/bash/traceroute.sh",target))

    run_geoip(target)