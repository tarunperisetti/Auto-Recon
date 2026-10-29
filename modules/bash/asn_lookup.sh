#!/bin/bash

target="$1"

if [ -z "$target" ];then
    echo "[!] Usage: $0 <domain/IP>"
    exit 1
fi

if ! command -v curl >/dev/null 2>&1; then
    echo "[!] Error: curl is not installed."
    exit 1
fi

if ! command -v jq >/dev/null 2>&1; then
    echo "[!] Error: jq is not installed."
    echo "[*] Install it using: sudo apt install jq"
    exit 1
fi

echo "[✱] Target : $target"
echo

echo "[*] Querying ASN information..."
echo "----------------------------------------"

response=$(curl -fsS --connect-timeout 5 --max-time 15 \
    --get \
    --data-urlencode "search=$target" \
    "https://asn.ipinfo.app/api/json/search/")

if [ $? -ne 0 ] || [ -z "$response" ]; then
    echo "[!] Lookup failed. Check your connection or try later."
    exit 1
fi

if echo "$response" | jq -e 'type == "array"' >/dev/null 2>&1; then
    if [ "$(echo "$response" | jq 'length')" -eq 0 ]; then
        echo "[!] No ASN results found."
        exit 1
    fi

    echo "$response" | jq -r '
        .[] |
        "ASN: AS\(.asn)\nOrganization: \(.name)\n"
    '
else
    echo "[!] Unexpected response from the lookup service."
    exit 1
fi

echo "[+] ASN lookup completed."