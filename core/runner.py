import subprocess

def run_bash(script,target):
    result = subprocess.run(["bash",script,target],capture_output=True,text=True)
   
    if result.returncode != 0:
        print(f"[!] Error running {script}")

        if result.stderr.strip():
            print(result.stderr.strip())

        return None

    return result.stdout.strip()