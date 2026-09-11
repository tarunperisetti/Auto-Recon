from core.runner import run_bash

def domain_recon(target):
    print(run_bash("modules/bash/ping.sh",target))
    print(run_bash("modules/bash/whois.sh",target))