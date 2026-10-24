#!/usr/bin/env python3
# Moo Security Tool - V3.0 Kali Edition
# By: mohandm00990-cyber

import socket
import sys
from datetime import datetime
import subprocess

# الالوان
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

def banner():
    print(f"{GREEN}{BOLD}")
    print(r"""
 __  __                ____                       _            
|  \/  | ___   ___     / ___|  ___  ___ _   _ _ __(_) |_ _   _   
| |\/| |/ _ \ / _ \    \___ \ / _ \/ __| | | | '__| | __| | | |  
| |  | | (_) | (_) |    ___) |  __/ (__| |_| | |  | | |_| |_| |  
|_|  |_|\___/ \___/    |____/ \___|\__,_|_|  |_|\__|\__, |  
                                                        |___/   
                    V3.0 - Kali Edition
    """)
    print(f"{RESET}{CYAN}  [+] GitHub: mohandm00990-cyber/moo-security-tool{RESET}\n")

def port_scanner(target):
    print(f"{YELLOW}[*] Scanning Target: {target}{RESET}")
    print(f"{YELLOW}[*] Time Started: {datetime.now()}{RESET}\n")
    
    try:
        for port in [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 8080]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"{GREEN}[+] Port {port}: Open{RESET}")
            else:
                print(f"{RED}[-] Port {port}: Closed{RESET}")
            s.close()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] You Stopped The Scan!{RESET}")
        sys.exit()
    except socket.gaierror:
        print(f"{RED}[!] Hostname Could Not Be Resolved!{RESET}")
        sys.exit()

if __name__ == "__main__":
    banner()
    if len(sys.argv) < 2:
        target = input(f"{BLUE}[?] Enter IP / Domain to scan: {RESET}")
    else:
        target = sys.argv[1]
    
    port_scanner(target)
    print(f"\n{GREEN}{BOLD}[*] Scan Finished!{RESET}")
