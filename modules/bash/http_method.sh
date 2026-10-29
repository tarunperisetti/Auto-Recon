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

# Add HTTPS if no scheme is provided
if [[ "$target" != http://* && "$target" != https://* ]]; then
    target="https://$target"
fi 

echo "[✱] Target : $target"
echo
echo "[*] Checking advertised HTTP methods..."
echo "----------------------------------------"

curl -sS -I -X OPTIONS \
    --connect-timeout 5 \
    --max-time 15 \
    -D - -o /dev/null \
    "$target" 2>/dev/null |
    grep -iE '^(HTTP/|Allow:|Public:)'

status=${PIPESTATUS[0]}

if [ "$status" -ne 0 ]; then
    echo "[!] Request failed. Check the target or network."
    exit 1
fi

echo
echo "[✔] HTTP method check completed."