# 🔍 Auto-Recon

Auto-Recon is a simple automated reconnaissance tool designed to help security researchers and penetration testers collect basic information about a target.

The project automates common reconnaissance tasks and organizes the results so they can be reviewed easily.

> ⚠️ **Disclaimer:** Use this tool only on systems you own or have explicit permission to test.

---

## 🚀 Features

Auto-Recon can be used for tasks such as:

- 🔎 Domain reconnaissance
- 🌐 DNS enumeration
- 📡 Port scanning
- 🛠️ Service detection
- 🌍 Web server information gathering
- 📋 HTTP header analysis
- 🔗 Subdomain enumeration
- 📊 Collecting reconnaissance results
- 📁 Organizing scan outputs

More features may be added as the project develops.

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

## ▶️ Usage

Run the main program:

```bash
python3 aure.py
```

Follow the instructions shown by the program and provide the target domain or IP address.

### Example

```text
Target: example.com
```

Auto-Recon will then perform the configured reconnaissance tasks and collect the results.

---

## 📂 Project Structure

```text
Auto-Recon/
│
├── aure.py
├── requirements.txt
│
├── core/
│   ├── valid.py
│   ├── runner.py
│   └── report.py
│
├── modules/
│   └── bash/
│       ├── dns_enum.sh
│       ├── http_headers.sh
│       ├── google_dorking.sh
│       ├── nmap_os.sh
│       ├── nmap_service.sh 
│       ├── ping.sh
│       ├── subdomains_enum.sh
│       ├── traceroute.sh
│       ├── whatweb.sh
│       └── whois.sh
│
└── results/
    └── ...
```

---

## 📊 Results

The reconnaissance results can be saved and organized for later analysis.

Typical information may include:

```text
Ports
Services
Web Server
HTTP Headers
Subdomains
DNS Information
```

The collected information can also be used to generate a report.

---

## 🛠️ Technologies Used

- **Python** — Main application
- **Bash** — Reconnaissance scripts
- **Nmap** — Port and service scanning
- **Curl** — HTTP requests and web information gathering
- **Linux** — Development and testing environment

---

## ⚠️ Disclaimer

This project is intended for **educational purposes and authorized security testing only**.

Do not use Auto-Recon against systems, networks, or domains without proper authorization.

The developer is not responsible for misuse of this tool.

---

## 👨‍💻 Author

**Tarun Perisetti**

GitHub:  https://github.com/tarunperisetti

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!