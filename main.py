import subprocess
from modules.geoip import run_geoip

def run_bash(script,target):
    result = subprocess.run(["bash",script,target],capture_output=True,text=True)

    if result.returncode != 0:
        print("[!] Error : ",result.stderr)
        return None

    return result.stdout

#-----------------main-----------------
ip = input("[+] Enter IP : ")
print(run_bash("scripts/whois.sh",ip))
print(run_bash("scripts/ping.sh",ip))
run_geoip(ip)