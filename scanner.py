# scanner.py - FINAL: Shows ALL open ports from ss -tulnp (perfect match)

import subprocess
import re
from utils import print_info

def run_port_scan():
    print_info("Detecting open ports & services using ss -tulnp...")
    ports = []

    output = subprocess.getoutput("ss -tulnp")
    lines = output.splitlines()[1:]  # skip header

    seen = set()
    for line in lines:
        if "LISTEN" not in line:
            continue

        # Split the line properly (ss output has variable spacing)
        parts = re.split(r'\s+', line.strip())

        if len(parts) < 6:
            continue

        proto = parts[0].upper()
        local_addr = parts[4]  # Local Address:Port

        # Extract port
        if ':' in local_addr:
            port_str = local_addr.split(":")[-1]
            if port_str == '*':
                continue
            if not port_str.isdigit():
                continue
            port = int(port_str)
        else:
            continue

        # Avoid duplicates
        if (port, proto) in seen:
            continue
        seen.add((port, proto))

        # Extract process and PID
        process = "Unknown"
        pid = "Unknown"
        if len(parts) > 6 and "users:((" in parts[-1]:
            process_part = parts[-1]
            match = re.search(r'"([^"]+)"', process_part)
            if match:
                process = match.group(1)
            pid_match = re.search(r'pid=(\d+)', process_part)
            if pid_match:
                pid = pid_match.group(1)

        ports.append([str(port), proto, process, f"N/A (PID: {pid})"])

    # Sort by port
    ports.sort(key=lambda x: int(x[0]))

    if not ports:
        ports.append(["N/A", "TCP", "No open ports", ""])

    return ports
