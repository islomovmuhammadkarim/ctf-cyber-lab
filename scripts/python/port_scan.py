#!/usr/bin/env python3
"""
port_scan.py — oddiy TCP connect port scanner.

Purpose:      Berilgan host'da ochiq TCP portlarni tekshirish (o‘quv maqsadida).
Requirements: Python 3.8+, faqat standard library.
Installation: -
Usage:        python3 port_scan.py <host> [-p 1-1024] [-t 0.5] [-w 100]
Examples:     python3 port_scan.py scanme.nmap.org -p 20-100
Notes:        Faqat O‘ZINGIZGA tegishli yoki YOZMA RUXSAT berilgan host'larni
              skanerlang. Ruxsatsiz skanerlash ko‘p mamlakatda noqonuniy.
              Bu — nmap o‘rnini bosuvchi emas, o‘quv namunasi.
"""

import argparse
import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed


def parse_ports(spec: str) -> list[int]:
    """'20-100' yoki '22,80,443' yoki '80' ko‘rinishini port ro‘yxatiga aylantiradi."""
    ports: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            ports.update(range(int(start), int(end) + 1))
        elif part:
            ports.add(int(part))
    return sorted(p for p in ports if 0 < p <= 65535)


def scan_port(host: str, port: int, timeout: float) -> tuple[int, bool, str]:
    """Bitta portni tekshiradi. (port, ochiqmi, servis nomi) qaytaradi."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        is_open = sock.connect_ex((host, port)) == 0
    try:
        service = socket.getservbyport(port, "tcp") if is_open else ""
    except OSError:
        service = ""
    return port, is_open, service


def main() -> int:
    parser = argparse.ArgumentParser(description="Oddiy TCP connect port scanner (o‘quv).")
    parser.add_argument("host", help="Nishon host (IP yoki domen)")
    parser.add_argument("-p", "--ports", default="1-1024",
                        help="Portlar: '1-1024', '22,80,443' yoki '80' (default: 1-1024)")
    parser.add_argument("-t", "--timeout", type=float, default=0.5,
                        help="Har bir port uchun timeout, soniya (default: 0.5)")
    parser.add_argument("-w", "--workers", type=int, default=100,
                        help="Parallel thread soni (default: 100)")
    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.host)
    except socket.gaierror:
        print(f"[!] Host aniqlanmadi: {args.host}", file=sys.stderr)
        return 1

    ports = parse_ports(args.ports)
    print(f"[*] Nishon : {args.host} ({target_ip})")
    print(f"[*] Portlar: {len(ports)} ta, timeout={args.timeout}s\n")

    open_ports: list[tuple[int, str]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(scan_port, target_ip, p, args.timeout) for p in ports]
        for future in as_completed(futures):
            port, is_open, service = future.result()
            if is_open:
                open_ports.append((port, service))
                print(f"[+] {port:>5}/tcp ochiq   {service}")

    print(f"\n[*] Tugadi. {len(open_ports)} ta ochiq port topildi.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n[!] To‘xtatildi.", file=sys.stderr)
        sys.exit(130)
