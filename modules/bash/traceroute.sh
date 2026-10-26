#!/bin/bash

target="$1"

if [ -z "$target" ];then
    echo "[!] Usage: $0 <domain/IP>"
    exit 1
fi

echo "[✱] Target : $target"
echo

if command -v traceroute >/dev/null 2>&1; then
    traceroute -m 15 -w 2 "$target"
elif command -v tracepath >/dev/null 2>&1; then
    tracepath "$target"
else
    echo "[!] Neither traceroute nor tracepath is installed."
    echo "[!] Install traceroute using:"
    echo "    sudo apt install traceroute"
    exit 1
fi

echo
echo "[+] Traceroute completed."