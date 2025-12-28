# enumeration.py - FINAL: high-risk items in RED

import subprocess
import re
from utils import RED, YELLOW, RESET

def get_all_enum():
    enum = {}

    # Basic info
    basic = []
    basic.append(["Hostname", subprocess.getoutput("hostname").strip()])
    basic.append(["Current User", subprocess.getoutput("whoami").strip()])
    basic.append(["User ID & Groups", subprocess.getoutput("id").strip()])
    basic.append(["OS Release", subprocess.getoutput("cat /etc/os-release | grep PRETTY_NAME | cut -d'=' -f2 | tr -d '\"'").strip()])
    basic.append(["Kernel Version", subprocess.getoutput("uname -a").strip()])
    basic.append(["Architecture", subprocess.getoutput("uname -m").strip()])
    basic.append(["Uptime", subprocess.getoutput("uptime -p").strip()])
    basic.append(["IP Addresses", subprocess.getoutput("ip -o -4 addr show | awk '{print $4}' | tr '\\n' ' '").strip()])
    basic.append(["Sudo Rights", subprocess.getoutput("sudo -l 2>/dev/null || echo 'No sudo'").strip()])
    basic.append(["Sudo Version", subprocess.getoutput("sudo -V 2>/dev/null | head -1").strip()])
    enum["basic"] = basic

    # Users
    users = []
    for line in subprocess.getoutput("cat /etc/passwd").splitlines():
        f = line.split(":")
        if len(f) >= 7 and f[6] not in ["/bin/false", "/usr/sbin/nologin"]:
            users.append([f[0], f[2], f[6]])
    enum["users"] = users or [["No users found"]]

    # SUID Files - HIGH RISK - in RED
    suid = []
    output = subprocess.getoutput("find / -perm -4000 -type f 2>/dev/null | head -30")
    for line in output.splitlines():
        suid.append([f"{RED}{line}{RESET}"])
    enum["suid"] = suid or [[f"{YELLOW}No SUID files found{RESET}"]]

    # Sensitive Data - passwords/secrets in RED
    sensitive = []
    paths = "/etc /var/www /opt /home /root"
    cmd = f"grep -rEi '(pass|pwd|secret|key|token|database|mysql|mariadb|api)' {paths} 2>/dev/null | head -30"
    output = subprocess.getoutput(cmd)
    if output:
        for line in output.splitlines():
            sensitive.append(f"{RED}{line}{RESET}")

    # Critical: password hashes in /etc/passwd
    if subprocess.getoutput("grep -v '^#' /etc/passwd | cut -d: -f2 | grep -v '^x$\\|^\\*$\\|^!$\\|^!!$'"):
        sensitive.append(f"{RED}CRITICAL: Password hashes found in /etc/passwd! (Offline crack risk){RESET}")

    # History - potential passwords in RED
    hist = subprocess.getoutput("cat /home/*/.bash_history /root/.bash_history 2>/dev/null | grep -i 'pass\\|mysql\\|ssh\\|sudo\\|key' | head -10")
    if hist:
        sensitive.append(f"{RED}--- Command history matches (potential passwords/keys) ---{RESET}")
        sensitive.extend(f"{RED}{line}{RESET}" for line in hist.splitlines())

    # .ssh contents
    ssh = subprocess.getoutput("ls -la /home/*/.ssh /root/.ssh 2>/dev/null")
    if ssh:
        sensitive.append("--- .ssh Directory Contents ---")
        sensitive.extend(ssh.splitlines())

    enum["sensitive"] = sensitive or ["No sensitive data found"]

    # Writable Directories - HIGH RISK - in RED
    writable = []
    output = subprocess.getoutput("find / -path /proc -prune -o -type d -perm -o+w 2>/dev/null | head -20")
    for line in output.splitlines():
        writable.append([f"{RED}{line}{RESET}"])
    enum["writable"] = writable or [[f"{YELLOW}No world-writable directories found{RESET}"]]

    # Block Devices
    enum["block"] = subprocess.getoutput("lsblk -o NAME,SIZE,TYPE,MOUNTPOINT").splitlines()

    # Running Processes
    enum["processes"] = subprocess.getoutput("ps au | head -15").splitlines()

    # Defenses
    defenses = []
    defenses.append(["AppArmor", subprocess.getoutput("aa-status --enabled 2>/dev/null || echo 'Not active'")])
    defenses.append(["SELinux", subprocess.getoutput("getenforce 2>/dev/null || echo 'Disabled'")])
    defenses.append(["UFW", subprocess.getoutput("ufw status 2>/dev/null || echo 'Inactive'")])
    defenses.append(["Fail2Ban", subprocess.getoutput("fail2ban-client status 2>/dev/null || echo 'Not installed'")])
    enum["defenses"] = defenses

    # GTFOBins - HIGH RISK - in RED
    gtfobins = []
    high = ["sudo", "vim", "find", "less", "nano", "awk", "perl", "python", "tar"]
    for b in high:
        path = subprocess.getoutput(f"which {b} 2>/dev/null")
        if path:
            gtfobins.append([f"{RED}{b}{RESET}", f"{RED}High Privesc Risk{RESET}"])
    enum["gtfobins"] = gtfobins or [[f"{YELLOW}No high-risk GTFOBins found{RESET}", ""]]

    return enum
