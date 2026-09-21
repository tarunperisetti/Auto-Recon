#!/bin/bash
target="$1"

if [ -z "$target" ]; then
    echo "[!] Usage: $0 <domain>"
    exit 1
fi

echo "[✱] Target: $target"
echo

echo "[+] Indexed pages:"
echo "https://www.google.com/search?q=site%3A$target"

echo
echo "[+] PDFs:"
echo "https://www.google.com/search?q=site%3A$target+filetype%3Apdf"

echo
echo "[+] Documents:"
echo "https://www.google.com/search?q=site%3A$target+filetype%3Adoc"

echo
echo "[+] Spreadsheets:"
echo "https://www.google.com/search?q=site%3A$target+filetype%3Axls"

echo
echo "[+] Login pages:"
echo "https://www.google.com/search?q=site%3A$target+%28inurl%3Alogin+OR+inurl%3Asignin%29"

echo
echo "[+] Subdomains:"
echo "https://www.google.com/search?q=site%3A*.$target"

echo
echo "[+] Directory listings:"
echo "https://www.google.com/search?q=site%3A$target+%22index+of%22"

echo
echo "[+] Configuration-related files:"
echo "https://www.google.com/search?q=site%3A$target+%28filetype%3Ayml+OR+filetype%3Ajson+OR+filetype%3Axml%29"