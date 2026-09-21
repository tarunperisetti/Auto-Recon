#!/bin/bash
target="$1"

if [ -z "$target" ]; then
    echo "[!] Usage: $0 <domain>"
    exit 1
fi

echo "[✱] Target : $target"
echo
whois "$target"