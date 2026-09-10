#!/bin/bash
target=$1
echo
echo "=========================================="
echo "[+] PING SCAN"
echo "=========================================="

ping -c 4 "$target"

#if [[ $? -eq 0 ]]; then
#    echo "[+] Host is UP"
#else
#    echo "[!] Host is DOWN or blocking ICMP"
#fi