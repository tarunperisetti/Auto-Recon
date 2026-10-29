#!/bin/bash

target="$1"

if [ -z "$target" ];then
    echo "[!] Usage: $0 <domain/IP>"
    exit 1
fi

echo "[✱] Target : $target"
echo

# Resolve a domain to an IP address
if [[ "$target" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    ip="$target"
else
    ip=$(getent ahostsv4 "$target" | awk 'NR==1 {print $1}')
fi

if [ -z "$ip" ]; then
    echo "[!] Could not resolve target to an IPv4 address."
    exit 1
fi

echo "[+] Target IP: $ip"
echo "[*] Querying Shodan InternetDB..."
echo "----------------------------------------"

response=$(curl -fsS --connect-timeout 5 --max-time 15 \
    "https://internetdb.shodan.io/$ip")

if [ $? -ne 0 ] || [ -z "$response" ]; then
    echo "[!] Shodan lookup failed or returned no data."
    exit 1
fi

if command -v jq >/dev/null 2>&1; then
    echo "$response" | jq '{
        ip: .ip,
        ports: .ports,
        hostnames: .hostnames,
        cpes: .cpes,
        tags: .tags,
        vulns: .vulns
    }'
else
    echo "$response"
fi

echo
echo "[✔] Shodan recon completed..."
echo "[*] Results reflect Shodan's available data, not a live scan."