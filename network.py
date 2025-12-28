# network.py - Beautiful network topology diagram (fixed)

import subprocess

def get_network_diagram():
    hostname = subprocess.getoutput("hostname").strip()
    public_ip = subprocess.getoutput("curl -s ifconfig.me || echo 'No Internet'").strip()
    gateway = subprocess.getoutput("ip route | grep default | awk '{print $3}'").strip() or "Unknown"

    interfaces = []
    brief = subprocess.getoutput("ip -brief a").strip()
    for line in brief.splitlines()[1:]:
        parts = line.split()
        if len(parts) < 3 or parts[1] != "UP":
            continue
        dev = parts[0]
        ip = subprocess.getoutput(f"ip -4 addr show {dev} | awk '/inet / {{print $2}}' | cut -d'/' -f1").strip()
        if ip:
            interfaces.append({"dev": dev, "ip": ip})

    diag = f"""
                                      {{ Internet }}
                                Public IP: {public_ip}
                                           ↓
                               Physical Host Machine
                                           │
                  ┌────────────────────────┼────────────────────────┐
                  │                        │                        │
                  ↓                        ↓                        ↓
"""
    for iface in interfaces:
        diag += f"              Internet Access Network\n"
        diag += f"                  │\n"
        diag += f"                {iface['dev']}\n"
        diag += f"                 {iface['ip']}\n"
        diag += f"                  │\n"

    diag += f"                  ↓\n"
    diag += f"                      {hostname} (Multi-homed Virtual Machine)\n\n"

    diag += "    Network Summary:\n"
    diag += f"      • Hostname : {hostname}\n"
    diag += f"      • Public IP : {public_ip}\n"
    diag += f"      • Default Gateway : {gateway}\n"
    diag += f"      • Active Interfaces: {len(interfaces)}\n"
    for iface in interfaces:
        diag += f"         → {iface['dev']}: {iface['ip']}\n"

    return diag
