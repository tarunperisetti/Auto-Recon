import subprocess
from modules.python.geoip import run_geoip

def run_bash(script,target):
    result = subprocess.run(["bash",script,target],capture_output=True,text=True)

    if result.returncode != 0:
        print("[!] Error : ",result.stderr)
        return None

    return result.stdout

print(run_bash("modules/bash/whois.sh",target))
print(run_bash("modules/bash/ping.sh",target))

run_geoip(target)