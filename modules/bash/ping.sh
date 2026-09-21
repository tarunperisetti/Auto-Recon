#!/bin/bash
target="$1"

if [ -z "$target" ]; then
    echo "[!] Usage: $0 <domain>"
    exit 1
fi

echo "[✱] Target : $target"
echo
if [[ "$(uname -s)" == "Linux" ]]; then
    ping -c 4 "$target"
else
    ping -n 4 "$target"
fi