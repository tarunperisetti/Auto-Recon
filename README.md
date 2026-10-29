## 🔍 Auto-Recon

A simple Python-based reconnaissance tool that organizes passive and active reconnaissance tasks through a menu-driven interface. 
It uses Python to validate the target and route the selected option to the reconnaissance modules.

> **Use responsibly:** Run this tool only against systems you own or
> have explicit permission to assess. Active checks such as port
> scanning, service enumeration, and directory enumeration send traffic
> to the target.

## Features

### Passive Reconnaissance

-   **WHOIS Information** --- retrieve publicly available domain registration information.
-   **Shodan Recon** --- look up information available through the Shodan InternetDB service.
-   **Google Dorking** --- perform search-engine reconnaissance using search operators.
-   **Email Enumeration** --- search for publicly available email-related information.
-   **IP Information** --- retrieve IP/geolocation-related information through the project's Python module.
-   **ASN Lookup** --- look up Autonomous System Number information.

### Active Reconnaissance

-   **DNS Enumeration** --- query DNS-related information.
-   **Subdomain Enumeration** --- look for subdomains.
-   **Port Scanning** --- check for reachable ports.
-   **Service Enumeration** --- identify services associated with discovered ports.
-   **HTTP Header Analysis** --- inspect HTTP response headers.
-   **Web Technology Detection** --- identify technologies used by a website.
-   **HTTP Method Enumeration** --- check HTTP methods advertised or accepted by the target.
-   **Directory Enumeration** --- check for discoverable web paths and directories.

## 📂 Project Structure

``` text
auto_recon/
├── core/
│   ├── results/             # Results-related directory
│   ├── runner.py            # Helper for running commands/scripts
│   └── valid.py             # Target validation/classification
├── modules/
│   ├── bash/
│   │   ├── asn_lookup.sh
│   │   ├── dir_enum.sh
│   │   ├── dns_enum.sh
│   │   ├── email_enum.sh
│   │   ├── google_dorking.sh
│   │   ├── http_headers.sh
│   │   ├── http_method.sh
│   │   ├── nmap_basic.sh
│   │   ├── nmap_service.sh
│   │   ├── shodan_recon.sh
│   │   ├── subdomain_enum.sh
│   │   ├── whatweb.sh
│   │   └── whois.sh
│   └── python/
│       └── geoip.py
├── recon/
│   └── auto_recon.py        # Reconnaissance menu/dispatcher
├── aure.py                  # Main entry point
├── README.md
└── requirements.txt        
```

---

## 🧰 Requirements

Before running Auto-Recon, make sure you have:

- Python 3
- Bash
- Nmap
- Curl
- subfinder
- whatweb

Some modules may require additional security tools.

### Recommended OS

Auto-Recon is mainly designed for:

- Kali Linux
- Parrot OS
- Other Linux distributions

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/tarunperisetti/Auto-Recon.git
```

Go into the project directory:

```bash
cd Auto-Recon
```

Install the required Python packages:

```bash
pip3 install -r requirements.txt
```

Make sure the required Bash scripts have execute permission:

```bash
chmod +x modules/bash/*.sh
```

---
## Example Workflow

1.  Start the program with `python3 aure.py`.
2.  Select a reconnaissance option. 
3.  Enter the authorized domain or IP address.
4.  Review the output and any results saved by that module.
5.  Select **0 --- Exit** to close the program.

## 📊 Results

The project includes `core/results/` .
Check the implementation of `core/runner.py` and `recon/auto_recon.py` to confirm: - where module outputs are saved; - whether errors and standard output are both captured.

## Limitations

-   Results depend on the tools, data sources, network access, and target responses available to each module.
-   Public lookup services may return incomplete or outdated information.
-   A missing result does not prove that a host, service, email address, or subdomain does not exist.
-   Active scans may trigger security monitoring or affect target systems; use appropriate authorization and conservativ settings.

## ⚠️ Disclaimer

This project is intended for learning, authorized security testing, and reconnaissance of systems for which you have permission. The user is responsible for complying with applicable laws, policies, and service terms.

## 👨‍💻 Author

Tarun Perisetti
GitHub: https://github.com/tarunperisetti

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!