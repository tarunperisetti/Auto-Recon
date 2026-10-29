#!/bin/bash

target="$1"

if [ -z "$target" ]; then
    echo "[!] Usage: $0 <domain>"
    exit 1
fi

if ! command -v gobuster >/dev/null 2>&1; then
    echo "[!] Gobuster is not installed."
    echo "[!] Install it with:"
    echo "    sudo apt install gobuster"
    exit 1
fi

echo "[✱] Target: $target"
echo

gobuster dir -u "$target" -w /usr/share/wordlists/dirb/common.txt

echo "[✔] Directory Enumeration completed..."