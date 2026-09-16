#!/bin/bash
target="$1"

if [ -z "$target" ]; then
    echo "[!] Usage: $0 <domain>"
    exit 1
fi

if [[ "$target" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "[+] Target : $target"
    echo
    echo "-----------------PTR / REVERSE DNS-----------------"
    dig -x "$target" +short
else
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
fi