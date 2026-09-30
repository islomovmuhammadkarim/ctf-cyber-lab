#!/usr/bin/env python3
"""
hash_identify.py — hash turini uzunligi va shakli bo‘yicha taxmin qiladi.

Purpose:      CTF/forensics'da uchragan hash qaysi algoritmga o‘xshashini aniqlash.
Requirements: Python 3.8+, faqat standard library.
Installation: -
Usage:        python3 hash_identify.py <hash>
              echo <hash> | python3 hash_identify.py -
Examples:     python3 hash_identify.py 5f4dcc3b5aa765d61d8327deb882cf99
Notes:        Bu — taxmin, aniq javob emas. Bir xil uzunlikdagi bir nechta
              algoritm bo‘lishi mumkin. Ular ro‘yxatda birga ko‘rsatiladi.
"""

import re
import sys

# (uzunlik, hex bo‘lishi shart, nomlar) — soddalashtirilgan qoidalar to‘plami.
RULES = [
    (32,  True,  ["MD5", "NTLM", "MD4"]),
    (40,  True,  ["SHA-1"]),
    (56,  True,  ["SHA-224"]),
    (64,  True,  ["SHA-256", "SHA3-256"]),
    (96,  True,  ["SHA-384"]),
    (128, True,  ["SHA-512", "SHA3-512"]),
]

HEX_RE = re.compile(r"^[a-fA-F0-9]+$")


def identify(h: str) -> list[str]:
    """Hash uchun ehtimoliy algoritm nomlari ro‘yxatini qaytaradi."""
    h = h.strip()
    guesses: list[str] = []

    # Prefiksga qarab aniqlanadigan formatlar
    if h.startswith("$2a$") or h.startswith("$2b$") or h.startswith("$2y$"):
        return ["bcrypt"]
    if h.startswith("$1$"):
        return ["md5crypt (Unix)"]
    if h.startswith("$5$"):
        return ["sha256crypt (Unix)"]
    if h.startswith("$6$"):
        return ["sha512crypt (Unix)"]
    if h.startswith("$argon2"):
        return ["Argon2"]

    is_hex = bool(HEX_RE.match(h))
    for length, need_hex, names in RULES:
        if len(h) == length and (is_hex if need_hex else True):
            guesses.extend(names)

    return guesses


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2

    raw = sys.stdin.read() if sys.argv[1] == "-" else sys.argv[1]

    for line in raw.splitlines():
        h = line.strip()
        if not h:
            continue
        guesses = identify(h)
        if guesses:
            print(f"{h}\n  -> {', '.join(guesses)} (uzunlik: {len(h)})\n")
        else:
            print(f"{h}\n  -> Aniqlanmadi (uzunlik: {len(h)})\n")

    print("Eslatma: bu taxmin. Aniqroq uchun `hashid` yoki `hash-identifier` ishlating.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
