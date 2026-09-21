import requests

def run_geoip(ip):
    
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url, timeout=5).json()

    if response["status"] != "success":
        return None
    
    return response