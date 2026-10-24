#!/usr/bin/env python3
import socket
import threading
from datetime import datetime

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print(f"{CYAN}==================================={RESET}")
print(f"{CYAN}  Moo Security Tool V4.0 - ULTIMATE {RESET}")
print(f"{CYAN}==================================={RESET}")

target = input(f"\n{YELLOW}Enter Target IP/Domain: {RESET}").strip()
if not target:
    print(f"{RED}No target!{RESET}")
    exit()

target = target.split()[0]
try:
    target_ip = socket.gethostbyname(target)
    print(f"{CYAN}\n[+] Target: {target} -> {target_ip}{RESET}")
except:
    print(f"{RED}[-] Could not resolve host{RESET}")
    exit()

open_ports = []
start_time = datetime.now()

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            try:
                s.send(b'HEAD / HTTP/1.0\r\n\r\n')
                banner = s.recv(1024).decode().strip().split('\n')[0]
            except:
                banner = "Unknown Service"
            print(f"{GREEN}[+] Port {port}: Open  -> {banner}{RESET}")
            open_ports.append(f"Port {port}: Open - {banner}")
        s.close()
    except:
        pass

print(f"{YELLOW}\n[*] Scanning... (Fast Mode){RESET}\n")
threads = []
ports = [21,22,23,25,53,80,110,139,443,445,3306,8080,8443,8888,9000]
for port in ports:
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

end_time = datetime.now()
total = end_time - start_time
print(f"\n{CYAN}========== SCAN DONE =========={RESET}")
print(f"{CYAN}Time: {total}{RESET}")
print(f"{GREEN}Open Ports Found: {len(open_ports)}{RESET}")

if open_ports:
    filename = f"scan_{target_ip}.txt"
    with open(filename, "w") as f:
        f.write(f"Scan Report for {target} ({target_ip})\nDate: {end_time}\n\n")
        for p in open_ports:
            f.write(p + "\n")
    print(f"{YELLOW}[*] Results saved to {filename}{RESET}")
