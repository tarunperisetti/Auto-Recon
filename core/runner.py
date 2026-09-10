import subprocess

def run_bash(script,target):
    result = subprocess.run(["bash",script,target],capture_output=True,text=True)

    if result.returncode != 0:
        print(f"[!] Error running {script}")
        print(result.stderr)
        return None

    return result.stdout.strip()