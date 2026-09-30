#!/usr/bin/env python3
"""
header_check.py — HTTP xavfsizlik header'larini tekshiradi.

Purpose:      Berilgan URL javobidagi muhim xavfsizlik header'lari bor-yo‘qligini
              ko‘rsatadi (defensiv tekshiruv / bug bounty recon).
Requirements: Python 3.8+, requests
Installation: pip install -r requirements.txt
Usage:        python3 header_check.py <url>
Examples:     python3 header_check.py https://example.com
Notes:        Faqat GET so‘rov yuboradi, hech narsani o‘zgartirmaydi. Baribir
              faqat sinash huquqingiz bor saytlarda ishlating.
"""

import argparse
import sys

try:
    import requests
except ImportError:
    print("[!] 'requests' kerak: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

# header -> nima uchun kerakligi
SECURITY_HEADERS = {
    "Strict-Transport-Security": "HTTPS'ni majburiy qiladi (HSTS)",
    "Content-Security-Policy": "XSS va injeksiyani cheklaydi",
    "X-Frame-Options": "Clickjacking'dan himoya (frame ichiga olishni cheklaydi)",
    "X-Content-Type-Options": "MIME-sniffing'ni to‘xtatadi (nosniff)",
    "Referrer-Policy": "Referrer ma'lumot oqishini cheklaydi",
    "Permissions-Policy": "Brauzer imkoniyatlarini (kamera, mikrofon) cheklaydi",
}

# oshkor qilmaslik ma'qul bo‘lgan header'lar
INFO_LEAK_HEADERS = ["Server", "X-Powered-By", "X-AspNet-Version"]


def check(url: str, timeout: float) -> int:
    try:
        resp = requests.get(url, timeout=timeout, allow_redirects=True)
    except requests.RequestException as exc:
        print(f"[!] So‘rov muvaffaqiyatsiz: {exc}", file=sys.stderr)
        return 1

    headers = {k.lower(): v for k, v in resp.headers.items()}
    print(f"[*] URL   : {resp.url}")
    print(f"[*] Status: {resp.status_code}\n")

    print("=== Xavfsizlik header'lari ===")
    missing = 0
    for name, purpose in SECURITY_HEADERS.items():
        if name.lower() in headers:
            print(f"[+] {name}: bor")
        else:
            print(f"[-] {name}: YO‘Q  ({purpose})")
            missing += 1

    print("\n=== Ma'lumot oshkor qiluvchi header'lar ===")
    for name in INFO_LEAK_HEADERS:
        if name.lower() in headers:
            print(f"[!] {name}: {headers[name.lower()]}  (versiyani yashirish tavsiya etiladi)")

    print(f"\n[*] Yetishmayotgan xavfsizlik header'lari: {missing}/{len(SECURITY_HEADERS)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="HTTP xavfsizlik header'larini tekshirish.")
    parser.add_argument("url", help="To‘liq URL, masalan https://example.com")
    parser.add_argument("-t", "--timeout", type=float, default=10.0, help="Timeout (default: 10s)")
    args = parser.parse_args()

    url = args.url
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return check(url, args.timeout)


if __name__ == "__main__":
    sys.exit(main())
