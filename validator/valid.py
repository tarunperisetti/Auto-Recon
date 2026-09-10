import ipaddress
import re

def classify_target(target):
    target = target.strip()
    try:
        ipaddress.ip_address(target)
        return "IP"
    except ValueError:
        pass

    domain_pattern = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    if re.match(domain_pattern,target):
        return "DOMAIN"

    return "INVALID"