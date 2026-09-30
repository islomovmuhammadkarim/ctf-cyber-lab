# Script shabloni

Muhim skriptlarning har biri quyidagi ma'lumotga ega bo‘lishi kerak. Oddiy skript uchun — fayl boshidagi comment/docstring yetarli. Murakkabroq skript uchun — yoniga shu formatdagi `README.md` qo‘shing.

Standart bo‘limlar: **Purpose, Requirements, Installation, Usage, Examples, Notes**.

## Python

```python
#!/usr/bin/env python3
"""
<script-nomi>.py

Purpose:      <Skript nima qiladi.>
Requirements: Python 3.10+, <paketlar yoki "faqat standard library">
Installation: pip install <paket>   (kerak bo‘lmasa: "-")
Usage:        python3 <script-nomi>.py <argumentlar>
Examples:     python3 <script-nomi>.py -t 10.10.x.x
Notes:        Faqat ruxsat berilgan target'larda ishlating.
              Maxfiy qiymatlar environment variable orqali o‘qiladi (os.environ).
"""
```

## Bash

```bash
#!/usr/bin/env bash
# <script-nomi>.sh
#
# Purpose:      <Skript nima qiladi.>
# Requirements: bash 4+, <nmap, curl, ...>
# Installation: sudo apt install <paket>   (kerak bo‘lmasa: "-")
# Usage:        ./<script-nomi>.sh <argumentlar>
# Examples:     ./<script-nomi>.sh 10.10.x.x
# Notes:        Faqat ruxsat berilgan target'larda ishlating.

set -euo pipefail
```

## PowerShell

```powershell
<#
.SYNOPSIS
    <Skript nima qiladi.>
.DESCRIPTION
    Requirements: PowerShell 5.1+ / 7+
    Installation: <kerak bo‘lsa>
    Notes:        Faqat ruxsat berilgan muhitda ishlating.
.EXAMPLE
    .\<script-nomi>.ps1 -Target 10.10.x.x
#>
```

## Nomlash

- Fayl nomi — kebab-case va maqsadni bildiradi: `port-scan.sh`, `jwt-decode.py`.
- Bash skriptlarga bajarish huquqini bering: `chmod +x <script-nomi>.sh`.
