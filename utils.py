# utils.py - No duplicate headings (section only in display.py)

RED = '\033[91m'
ORANGE = '\033[93m'
YELLOW = '\033[33m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

def banner():
    print(f"{GREEN}╔══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║                 CYPENT - Local Vulnerability Scanner         ║{RESET}")
    print(f"{GREEN}║                   Python-based • Dynamic • Fast               ║{RESET}")
    print(f"{GREEN}║                     December 2025 Edition                    ║{RESET}")
    print(f"{GREEN}╚══════════════════════════════════════════════════════════════╝{RESET}\n")

def print_info(msg):
    print(f"{GREEN}[+] {msg}{RESET}")

def print_section(title):
    line = "═" * 80
    print(f"\n{GREEN}{line}{RESET}")
    print(f"{BLUE}                    {title}{RESET}")
    print(f"{GREEN}{line}{RESET}\n")

def print_box_table(headers, rows):
    if not rows:
        rows = [["No data found"]]

    col_widths = [max(len(str(row[i])) for row in rows + [headers]) for i in range(len(headers))]
    total_width = sum(col_widths) + 3 * (len(headers) - 1) + 4

    print(f"{GREEN}+{'-' * (total_width - 2)}+{RESET}")
    header_line = "| " + " | ".join(f"{BLUE}{str(h).ljust(w)}{RESET}" for h, w in zip(headers, col_widths)) + " |"
    print(header_line)
    print(f"{GREEN}+{'=' * (total_width - 2)}+{RESET}")
    for row in rows:
        row_line = "| " + " | ".join(str(item).ljust(w) for item, w in zip(row, col_widths)) + " |"
        print(row_line)
    print(f"{GREEN}+{'-' * (total_width - 2)}+{RESET}\n")
