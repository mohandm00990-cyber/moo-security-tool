#!/usr/bin/env python3
"""
Moo Security Tool V5.0 - GOD MODE
By Moo | For Educational & Authorized Testing Only
"""
import socket, threading, argparse
from datetime import datetime

RED="\033[91m"; GREEN="\033[92m"; CYAN="\033[96m"; YELLOW="\033[93m"; RESET="\033[0m"

def banner():
    print(f"{CYAN}")
    print(r" __  __                  _____                      _ _           ")
    print(r"|  \/  |                / ____|                    (_) |          ")
    print(r"| \  / | ___   ___     | (___   ___  ___ _   _ _ __ _| |_ _   _  ")
    print(r"| |\/| |/ _ \ / _ \     \___ \ / _ \/ __| | | | '__| | __| | | | ")
    print(r"| |  | | (_) | (_) |    ____) |  __/ (__| |_| | |  | | |_| |_| | ")
    print(r"|_|  |_|\___/ \___/     |____/ \___|\___|\__,_|_|  |_|\__|\__, | ")
    print(r"                                                          __/ | ")
    print(r"                      V5.0 - GOD MODE                     |___/  ")
    print(f"{RESET}")

parser = argparse.ArgumentParser(description="Moo Security Tool V5.0")
parser.add_argument("target", help="Target IP/Domain")
parser.add_argument("-p", "--ports", default="1-100", help="Ports: 80 or 20-100 or 21,22,80")
parser.add_argument("-t", "--threads", type=int, default=100, help="Threads (default 100)")
parser.add_argument("-o", "--output", help="Save report to file")
args = parser.parse_args()

banner()
try:
    target_ip = socket.gethostbyname(args.target)
    print(f"{CYAN}[+] Target: {args.target} -> {target_ip}{RESET}")
    print(f"{CYAN}[+] Threads: {args.threads}{RESET}")
except:
    print(f"{RED}[-] Invalid target{RESET}"); exit()

# Parse ports
port_list = []
if "-" in args.ports:
    s,e = args.ports.split("-"); port_list = range(int(s), int(e)+1)
elif "," in args.ports:
    port_list = [int(p) for p in args.ports.split(",")]
else:
    port_list = [int(args.ports)]

open_ports = []
start = datetime.now()

def scan(port):
    try:
        s = socket.socket(); s.settimeout(0.5)
        if s.connect_ex((target_ip, port)) == 0:
            print(f"{GREEN}[+] {port}/tcp open{RESET}")
            open_ports.append(port)
        s.close()
    except: pass

print(f"{YELLOW}[*] Scanning {len(port_list)} ports...{RESET}\n")
threads = []
for port in port_list:
    while threading.active_count() > args.threads:
        pass
    t = threading.Thread(target=scan, args=(port,))
    t.start()
    threads.append(t)
for t in threads: t.join()

print(f"\n{CYAN}========== DONE in {datetime.now()-start} =========={RESET}")
print(f"{GREEN}Found {len(open_ports)} open ports: {open_ports}{RESET}")

if args.output or open_ports:
    fname = args.output or f"scan_{target_ip}.txt"
    with open(fname, "w") as f:
        f.write(f"Report for {args.target} ({target_ip})\nTime: {datetime.now()}\nPorts: {open_ports}\n")
    print(f"{YELLOW}[*] Saved to {fname}{RESET}")
