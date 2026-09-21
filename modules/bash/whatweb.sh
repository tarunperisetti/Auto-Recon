#!/bin/bash
target="$1"

if [ -z "$target" ];then
    echo "[!] Usage: $0 <domain/IP>"
    exit 1
fi

echo "[✱] Target : $target"
echo
echo "------------------HTTP------------------"
whatweb -a 1 "http://$target"