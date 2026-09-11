import subprocess

def run_bash(script,target):
    result = subprocess.run(["bash",script,target],capture_output=True,text=True)

    print("Return code:", result.returncode)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
     
    if result.returncode != 0:
        print(f"[!] Error running {script}")
        return None

    return result.stdout.strip()