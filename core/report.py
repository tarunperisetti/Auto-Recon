import os


def create_report(target, results):
    report_dir = os.path.join("reports", target)
    os.makedirs(report_dir, exist_ok=True)

    for filename, output in results.items():

        file_path = os.path.join(report_dir, filename)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(output if output else "[!] No output received.\n")

        print(f"[✔] Saved: {file_path}")

    print(f"\n[✔] All reports saved in: {report_dir}")