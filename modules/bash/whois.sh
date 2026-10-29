#!/bin/bash
target="$1"

if [ -z "$target" ]; then
    echo "[!] Usage: $0 <domain>"
    exit 1
fi

if ! command -v whois >/dev/null 2>&1; then
    echo "[!] Error: whois is not installed."
    exit 1
fi

echo "[✱] Target : $target"
echo
whois "$target"

echo "[✔] WHOIS recon is completed..."