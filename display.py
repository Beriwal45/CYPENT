# display.py - Show ss -tulpn style open ports

import subprocess
from utils import print_section, print_box_table

def display_results(data, network_diag):
    time = subprocess.getoutput("date +'%Y-%m-%d %H:%M:%S'").strip()

    print_section("CYPENT FULL ENUMERATION REPORT")
    print(f"Scan Time: {time}\n")

    print_section("SYSTEM INFORMATION")
    print_box_table(["Field", "Details"], data["basic"])

    print_section("OPEN PORTS & SERVICES")
    print_box_table(["Port", "Protocol", "Process", "User (PID)"], data["ports"])

    print_section("USERS")
    print_box_table(["Username", "UID", "Shell"], data["users"])

    print_section("SUID FILES")
    print_box_table(["Path"], data["suid"])

    print_section("SENSITIVE DATA & CREDENTIALS")
    for line in data["sensitive"]:
        print(line)

    print_section("WRITABLE DIRECTORIES")
    print_box_table(["Path"], data["writable"])

    print_section("BLOCK DEVICES")
    for line in data["block"]:
        print(line)

    print_section("RUNNING PROCESSES")
    for line in data["processes"]:
        print(line)

    print_section("DEFENSES")
    print_box_table(["Defense", "Status"], data["defenses"])

    print_section("GTFOBINS ABUSABLE BINARIES")
    print_box_table(["Binary", "Risk"], data["gtfobins"])

    print_section("NETWORK TOPOLOGY")
    print(network_diag)
