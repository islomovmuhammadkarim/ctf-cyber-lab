#!/usr/bin/env python3
"""
solve.py — "Base Decode" namuna challenge yechimi.

Qatlamma-qatlam Base32 -> Base64 dekod qiladi.
Real CTF'da cipher.txt o‘rniga challenge bergan faylни qo‘ying.
"""
import base64

# Namuna: "flag{REDACTED}" ni ikki qatlam kodlab ko‘rsatamiz.
sample = "flag{REDACTED}"
layer1 = base64.b64encode(sample.encode())      # ichki qatlam: Base64
cipher = base64.b32encode(layer1)               # tashqi qatlam: Base32

print(f"[*] Kodlangan (Base32): {cipher.decode()}")

# --- Dekod ---
step1 = base64.b32decode(cipher)                # Base32 yechish
flag = base64.b64decode(step1).decode()         # Base64 yechish
print(f"[+] Flag: {flag}")
