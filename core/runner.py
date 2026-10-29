import subprocess
from pathlib import Path
import re

RESULTS_DIR = Path("results")


def run_bash(script, target):
    safe_target = re.sub(r"[^a-zA-Z0-9_.-]", "_", target)
    target_dir = RESULTS_DIR / safe_target
    target_dir.mkdir(parents=True, exist_ok=True)

    script_name = Path(script).stem
    output_file = target_dir / f"{script_name}.txt"

    print(f"\n[*] Running {script_name}...\n")

    try:
        result = subprocess.run(["bash", script, target],capture_output=True,text=True,timeout=300)

        output = result.stdout
        if result.stderr:
            output += "\n[Errors / Warnings]\n" + result.stderr

        print(output)

        output_file.write_text(
            output or "[!] No output returned.\n",
            encoding="utf-8"
        )

        print(f"\n[✔] Output saved: {output_file}")

    except subprocess.TimeoutExpired:
        print(f"[!] {script_name} timed out.")

    except OSError as error:
        print(f"[!] Could not run script: {error}")
