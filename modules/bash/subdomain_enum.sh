#!/bin/bash
target="$1"

if [ -z "$target" ];then
    echo "[!] Usage: $0 <domain/IP>"
    exit 1
fi

if ! command -v subfinder >/dev/null 2>&1; then
    echo "[!] Error: subfinder is not installed."
    exit 1
fi

echo "[✱] Target : $target"
echo
subfinder -d "$target" -silent

echo "[✔] Subdomain Enumeration completed..."