import requests
from colorama import Fore

def run_geoip(ip):
    def geo_lookup(ip):
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=5).json()
        if response["status"] != "success":
            return None
        return response

    data = geo_lookup(ip)
    print(f"[✱] Target : {ip}")
    if data:
        print(f"[+] Country        : {data.get('country')}")
        print(f"[+] Region         : {data.get('regionName')}")
        print(f"[+] City           : {data.get('city')}")
        print(f"[+] ISP            : {data.get('isp')}")
        print(f"[+] Organization   : {data.get('org')}")
        print(f"[+] ASN            : {data.get('as')}")
        print(f"[+] Timezone       : {data.get('timezone')}")
        print(f"[+] Latitude       : {data.get('lat')}")
        print(f"[+] Longitude      : {data.get('lon')}")
    else:
        print(Fore.RED + "[-] Unable to retrieve Geo Location")