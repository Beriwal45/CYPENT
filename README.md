# CYPENT - Cybersecurity Penetration Testing Tool

**CYPENT** is a comprehensive local machine enumeration and vulnerability scanner designed for security professionals to gather system intelligence and identify potential security weaknesses during authorized penetration tests.

## 🚀 Features

- **System Enumeration**: Hostname, OS, kernel, users, sudo rights
- **Network Analysis**: Open ports, services, IP addresses, topology
- **Vulnerability Detection**: SUID/SGID files, world-writable directories
- **Security Assessment**: Defense status (AppArmor, SELinux, UFW, Fail2Ban)
- **Credential Hunting**: Sensitive data and SSH key discovery
- **GTFOBins Identification**: High-risk privilege escalation binaries
- **Process Monitoring**: Running services and applications

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Beriwal45/CYPENT.git
cd CYPENT

# Run directly
sudo python3 main.py
```

## 🎯 Usage

### Basic Scan
```bash
sudo python3 main.py --target <IP_ADDRESS> --scan
```

### Scan Examples
```bash
# Scan local machine
sudo python3 main.py --target 127.0.0.1 --scan

# Scan specific network target
sudo python3 main.py --target 192.168.1.100 --scan

# Full enumeration with all modules
sudo python3 main.py --target <IP> --full
```

## 📋 Output Sections

The tool generates a structured report with these sections:
1. **System Information** - OS, kernel, users, sudo configuration
2. **Open Ports & Services** - Network services and processes
3. **User Accounts** - All system users with shells
4. **SUID/SGID Files** - Potentially dangerous executables
5. **Sensitive Data** - Configuration files, SSH keys, credentials
6. **Writable Directories** - World-writable locations
7. **Security Defenses** - Firewall, SELinux, AppArmor status
8. **GTFOBins Binaries** - Known privilege escalation vectors
9. **Network Topology** - Network interfaces and routing

## ⚠️ Legal & Ethical Use

**This tool is for authorized security assessments only.**

✅ **Permitted Use:**
- Testing your own systems
- Authorized penetration tests with written permission
- Educational environments
- Security research

❌ **Prohibited Use:**
- Unauthorized system access
- Testing systems without permission
- Malicious activities
- Violating laws or regulations

**You are solely responsible for using this tool ethically and legally.**

## 🐛 Troubleshooting

**Common Issues:**
```bash
# Permission denied
sudo python3 main.py

# Python not found
python3 --version
# Install: sudo apt install python3

# Missing dependencies
pip install -r requirements.txt
```
## 📄 License

MIT License - See [LICENSE](https://github.com/Beriwal45/CYPENT/blob/main/LICENSE) file for details.

## 👨💻 Author

**Beriwal45** - [GitHub Profile](https://github.com/Beriwal45)


