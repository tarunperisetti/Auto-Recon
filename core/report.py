from pathlib import Path
from datetime import datetime
import re


def create_report(target):
    safe_target = re.sub(r"[^a-zA-Z0-9_.-]", "_", target)
    results_dir = Path("results") / safe_target
    reports_dir = Path("reports")

    if not results_dir.exists() or not list(results_dir.glob("*.txt")):
        print("[!] No saved recon results found.")
        print("[*] Run at least one recon script first.")
        return

    reports_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = reports_dir / f"{safe_target}_{timestamp}.txt"

    with report_file.open("w", encoding="utf-8") as report:
        report.write("=" * 60 + "\n")
        report.write("             AUTO-RECON REPORT\n")
        report.write("=" * 60 + "\n")
        report.write(f"Target: {target}\n")
        report.write(f"Generated: {datetime.now()}\n")
        report.write(f"Scripts recorded: {len(list(results_dir.glob('*.txt')))}\n")

        for result_file in sorted(results_dir.glob("*.txt")):
            report.write("\n\n" + "=" * 60 + "\n")
            report.write(f"MODULE: {result_file.stem.upper()}\n")
            report.write("=" * 60 + "\n\n")
            report.write(result_file.read_text(encoding="utf-8", errors="replace"))

    print(f"\n[✔] Report generated successfully!")
    print(f"[+] Report location: {report_file}")