#!/bin/bash
target="$1"

if [ -z "$target" ]; then
    echo "[!] Usage: $0 <domain>"
    exit 1
fi

echo "[+] Target : $target"
echo
echo "----------------NS RECORDS-----------------"
dig "$target" NS +short
echo
echo "----------------MX RECORD------------------"
dig "$target" MX +short
echo
echo "----------------TXT RECORD-----------------"
dig "$target" TXT +short