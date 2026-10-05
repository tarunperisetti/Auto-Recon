#!/bin/bash

target="$1"

if [ -z "$target" ]; then
    echo "[!] Usage: $0 <domain>"
    exit 1
fi

echo "[✱] Target: $target"
echo

if ! command -v theHarvester >/dev/null 2>&1; then
    echo "[!] theHarvester is not installed."
    echo "[!] Install it with:"
    echo "    sudo apt install theharvester"
    exit 1
fi

echo "[✱] Searching for publicly available email addresses..."
echo

theHarvester -d "$target" -b bing,duckduckgo
