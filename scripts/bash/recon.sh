#!/usr/bin/env bash
#
# recon.sh — CTF/lab uchun oddiy dastlabki recon avtomatlashtiruvchi.
#
# Purpose:      Bitta host uchun nmap skanerlarini ishga tushirib, natijani
#               tartibli papkaga saqlaydi. Qo‘lda takrorlanadigan ishни qisqartiradi.
# Requirements: bash 4+, nmap. (Ixtiyoriy: gobuster web enumeration uchun.)
# Installation: sudo apt install nmap
# Usage:        ./recon.sh <TARGET_IP_yoki_domen> [natija_papkasi]
# Examples:     ./recon.sh 10.10.10.10
#               ./recon.sh target.thm ~/work/target
# Notes:        Faqat O‘ZINGIZGA tegishli yoki YOZMA RUXSAT/platforma bergan
#               target'larda ishlating. Ruxsatsiz skanerlash noqonuniy.

set -euo pipefail

if [[ $# -lt 1 ]]; then
    echo "Foydalanish: $0 <TARGET> [natija_papkasi]" >&2
    exit 1
fi

TARGET="$1"
OUTDIR="${2:-recon-${TARGET}}"

if ! command -v nmap >/dev/null 2>&1; then
    echo "[!] nmap topilmadi. O‘rnating: sudo apt install nmap" >&2
    exit 1
fi

mkdir -p "${OUTDIR}/nmap"
echo "[*] Nishon : ${TARGET}"
echo "[*] Natija : ${OUTDIR}"
echo

# 1-bosqich: barcha TCP portlarni tez topish
echo "[*] 1/3  Barcha portlarni tezkor skanerlash..."
nmap -p- --min-rate 1000 -T4 -oN "${OUTDIR}/nmap/all-ports.txt" "${TARGET}" >/dev/null

# Topilgan ochiq portlarni ajratib olish
OPEN_PORTS=$(grep -oE '^[0-9]+/tcp' "${OUTDIR}/nmap/all-ports.txt" \
    | cut -d/ -f1 | paste -sd, -)

if [[ -z "${OPEN_PORTS}" ]]; then
    echo "[!] Ochiq TCP port topilmadi."
    exit 0
fi
echo "[+] Ochiq portlar: ${OPEN_PORTS}"

# 2-bosqich: topilgan portlarga batafsil (servis + versiya + default skriptlar)
echo "[*] 2/3  Batafsil skanerlash (-sC -sV)..."
nmap -sC -sV -p "${OPEN_PORTS}" -oN "${OUTDIR}/nmap/detailed.txt" "${TARGET}" >/dev/null
echo "[+] Saqlandi: ${OUTDIR}/nmap/detailed.txt"

# 3-bosqich: agar web port bo‘lsa, eslatma chiqarish
echo "[*] 3/3  Web port tekshiruvi..."
if grep -qE '^(80|443|8080|8443)/tcp' "${OUTDIR}/nmap/all-ports.txt"; then
    echo "[+] Web port topildi. Keyingi qadam sifatida directory enumeration:"
    echo "      gobuster dir -u http://${TARGET} -w <wordlist> -o ${OUTDIR}/gobuster.txt"
else
    echo "[-] Standart web port topilmadi."
fi

echo
echo "[*] Recon tugadi. Natijalar: ${OUTDIR}/"
