#!/bin/bash
target="$1"

if [ -z "$target" ];then
    echo "[!] Usage: $0 <domain/IP>"
    exit 1
fi

echo "[✱] Target : $target"
echo
echo "------------------HTTP------------------"
curl -I -L "http://$target"
echo "-----------------HTTPS------------------"
curl -I -L "https://$target"