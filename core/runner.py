import subprocess
from pathlib import Path
from datetime import datetime
import re

def run_bash(script_path, target):
    safe_target = re.sub(r"[^a-zA-Z0-9.-]", "_", target)
    output_dir = Path("results") / safe_target
    output_dir.mkdir(parents=True, exist_ok=True)

    script_name = Path(script_path).stem
    output_file = output_dir / f"{script_name}.txt"

    try:
        result = subprocess.run(["bash", script_path, target],capture_output=True,text=True,timeout=300)

        output = result.stdout
        if result.stderr:
            output += "\n[STDERR]\n" + result.stderr

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(f"Target: {target}\n")
            file.write(f"Script: {script_name}\n")
            file.write(f"Date: {datetime.now().isoformat()}\n")
            file.write(f"Exit code: {result.returncode}\n\n")
            file.write(output)

        print(output)
        print(f"\n[✔] Output saved to: {output_file}")

    except subprocess.TimeoutExpired:
        print("[!] Script timed out after 300 seconds.")
    except OSError as error:
        print(f"[!] Could not run script: {error}")
