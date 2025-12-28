# main.py - FINAL: shows all detection steps

from utils import banner, print_info
from scanner import run_port_scan
from enumeration import get_all_enum
from network import get_network_diagram
from display import display_results

def main():
    banner()
    
    print_info("Detecting open ports & services using ss -tulnp...")
    print_info("Enumerating users with login shells...")
    print_info("Finding SUID/SGID files...")
    print_info("Searching for sensitive data & credentials (passwords, keys, tokens)...")
    print_info("Checking world-writable directories...")
    print_info("Listing block devices...")
    print_info("Capturing running processes...")
    print_info("Checking security defenses (AppArmor, SELinux, UFW, Fail2Ban)...")
    print_info("Identifying GTFOBins abusable binaries...")
    print_info("Generating network topology diagram...")
    print_info("Collecting system information (hostname, OS, kernel, IPs, sudo rights, etc.)...\n")

    ports = run_port_scan()
    enum_data = get_all_enum()
    diag = get_network_diagram()
    display_results({"ports": ports, **enum_data}, diag)

if __name__ == "__main__":
    main()
