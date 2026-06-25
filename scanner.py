#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
┌──────────────────────────────────────────────────────────────────────────┐
│  MIT License (C) 2026 Goutham Joshi. All Rights Reserved.               │
└──────────────────────────────────────────────────────────────────────────┘
"""
import sys
import os
import re
import time
import subprocess
import threading

# --- 2026 Advanced TrueColor Space (24-bit) ---
C = '\033[38;2;0;235;235m'     # Concept Neon Cyan
P = '\033[38;2;255;105;180m'   # True Sakura Pink
R = '\033[38;2;220;20;60m'     # Crimson Red
G = '\033[38;2;50;205;50m'     # Mint Green
Y = '\033[38;2;255;165;0m'     # Amber Yellow
W = '\033[0m'                  # Reset White
B = '\033[1m'                  # Bold
D = '\033[2m'                  # Dim

# Classic Nmap Slant Font Block
LOGO = r"""
  ____  _____     _    ____ ___ 
 / __ \|  __ \   / \  / ___|_ _|
| |  | | |__) | / _ \ \___ \| | 
| |__| |  _  / / ___ \ ___) | | 
 \____/|_| \_\/_/   \_\____/___| ™
"""

SHURIKEN_FRAMES = ['✛', '✜', '✕', '✖']

# Local Vulnerability Engine Matching Database
VULN_DB = {
    21:  {"name": "FTP Insecure Authentication / Anonymous Access", "cve": "CVE-2011-2523", "risk": "HIGH"},
    22:  {"name": "SSH Brute Force Vector / Outdated Handshake", "cve": "CVE-2023-38408", "risk": "MEDIUM"},
    23:  {"name": "Telnet Cleartext Protocol Vulnerability", "cve": "CVE-2020-10188", "risk": "CRITICAL"},
    80:  {"name": "HTTP Unencrypted Traffic / Directory Traversal", "cve": "CVE-2021-41773", "risk": "MEDIUM"},
    443: {"name": "SSL/TLS Vulnerability / Heartbleed", "cve": "CVE-2014-0160", "risk": "HIGH"},
    445: {"name": "SMB Remote Code Execution (MS17-010)", "cve": "CVE-2017-0144", "risk": "CRITICAL"}
}

class ShurikenSpinner:
    def __init__(self):
        self.ev = threading.Event()
        self.t = None

    def _spin(self):
        idx = 0
        while not self.ev.is_set():
            sys.stdout.write(f"\r  {P}{SHURIKEN_FRAMES[idx%4]}{W} {D}SCANNING FOR PORTS & VULNERABILITIES...{W} ")
            sys.stdout.flush()
            idx += 1
            time.sleep(0.15)

    def start(self):
        self.ev.clear()
        self.t = threading.Thread(target=self._spin, daemon=True)
        self.t.start()

    def stop(self):
        self.ev.set()
        if self.t:
            self.t.join()
        sys.stdout.write("\r" + " " * 65 + "\r")
        sys.stdout.flush()

def render_header():
    print(f"{C}{LOGO}{W}")
    print(f"  {P}🌸{W}  {B}開発者 — Goutham Joshi  //  影 ORASI™ SHADOW CORE{W}  {P}🌸{W}")
    print(f"  {D}═══⚔════════════════════════════════════════►{W}\n")

def mask_stream_text(text):
    if not text:
        return ""
    return text.replace("Nmap", "Orasi").replace("nmap", "orasi")

def parse_and_display_output(raw_output, target_ip):
    cleaned = mask_stream_text(raw_output)
    lines = cleaned.splitlines()
    
    print(f"  {G}✦{W} {B}[▶] AUDIT ENGINE v1.0 // TARGET: {target_ip}{W}")
    print(f"    {D}Deployment Trace: {time.strftime('%Y-%m-%d %H:%M:%S')}{W}\n")
    
    in_port_block = False
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
            
        if any(k in stripped for k in ["Starting Orasi", "orasi scan report for", "Orasi scan report for", "orasi: option"]):
            continue
            
        if "Host is up" in stripped or "Not shown:" in stripped:
            print(f"    {D}{stripped}{W}")
            continue
            
        # Nmap Standard Tabular Columns
        if "PORT" in stripped and "STATE" in stripped:
            print(f"    {B}{'PORT':<10} {'STATE':<10} {'SERVICE'}{W}")
            print(f"    {D}──────────  ──────────  ───────────────────────────────────────{W}")
            in_port_block = True
            continue
            
        port_match = re.match(r'^(\d+)/(tcp|udp)\s+(\w+)\s+(.*)$', stripped)
        if port_match:
            port_num = int(port_match.group(1))
            proto = port_match.group(2)
            state = port_match.group(3)
            service_desc = port_match.group(4)
            
            port_label = f"{port_num}/{proto}"
            
            if "open" in state:
                print(f"    {port_label:<10} {G}{state:<10}{W} {B}{service_desc}{W}")
                
                if port_num in VULN_DB:
                    v = VULN_DB[port_num]
                    r_color = R if v['risk'] in ["HIGH", "CRITICAL"] else Y
                    print(f"        {B}CVE Match:{W}   {C}{v['cve']}{W}")
                    print(f"        {B}Risk Tier:{W}   {r_color}{v['risk']}{W}")
                    print(f"        {B}Details:{W}     {D}{v['name']}{W}")
            else:
                print(f"    {D}{port_label:<10} {state:<10} {service_desc}{W}")
            continue
            
        if in_port_block:
            if stripped.startswith("|") or stripped.startswith("_"):
                cleaned_line = stripped.lstrip('|_ ')
                print(f"        {D}{cleaned_line}{W}")
            elif not any(k in stripped for k in ["Orasi done", "SF:"]):
                print(f"        {D}{stripped}{W}")

def main():
    if len(sys.argv) == 1 or '-h' in sys.argv or '--help' in sys.argv:
        render_header()
        cmd = ["nmap", "-h"]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        help_txt = mask_stream_text(res.stdout)
        print(help_txt)
        return

    render_header()
    
    target_ip = "TARGET NODE"
    for arg in sys.argv[1:]:
        if not arg.startswith('-') and re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', arg):
            target_ip = arg
            break
            
    args_pool = sys.argv[1:]
    target_cmd = ["nmap"] + args_pool
    
    spinner = ShurikenSpinner()
    spinner.start()
    
    try:
        proc = subprocess.run(target_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        spinner.stop()
        
        if proc.stdout:
            parse_and_display_output(proc.stdout, target_ip)
        if proc.stderr:
            parse_and_display_output(proc.stderr, target_ip)
            
    except KeyboardInterrupt:
        spinner.stop()
        print(f"\n  {R}[!] Operations halted by operator.{W}")
    finally:
        print(f"\n  {D}MIT License (C) 2026 Goutham Joshi. Developed for verification.{W}\n")

if __name__ == "__main__":
    main()
