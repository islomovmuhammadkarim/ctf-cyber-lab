# CTF Cyber Lab

> CTF, pentest va kiberxavfsizlik bo‘yicha vositalar, skriptlar, tadqiqotlar, konspektlar va amaliy writeuplar jamlanmasi.

![License](https://img.shields.io/badge/license-MIT-blue)
![Focus](https://img.shields.io/badge/focus-CTF%20%7C%20Pentest%20%7C%20Web%20Security-red)

---

## 🧭 Navigatsiya

- [🎯 Maqsad](#-maqsad)
- [🔎 Tezkor qidiruv](#-tezkor-qidiruv)
- [📂 Repository strukturasi](#-repository-strukturasi)
- [🚩 CTF](#-ctf)
- [🧰 Tools](#-tools)
- [📜 Scripts](#-scripts)
- [📚 Notes](#-notes)
- [📝 Writeups](#-writeups)
- [🧪 Labs](#-labs)
- [📖 Docs](#-docs)
- [📊 Lab statistikasi](#-lab-statistikasi)
- [🔐 Security](#-security)
- [🤝 Contribution](#-contribution)
- [📄 License](#-license)

---

## 🎯 Maqsad

Ushbu repository kiberxavfsizlikni amaliy o‘rganish, CTF topshiriqlarini bajarish va foydali security vositalari hamda bilimlarni **bitta tartibli joyda** saqlash uchun yaratilgan.

Asosiy yo‘nalishlar:

- CTF (Capture The Flag)
- Web Security
- Penetration Testing
- Linux va Networking
- Privilege Escalation
- Active Directory
- Python / Bash / PowerShell skriptlar
- Security tools
- Writeuplar, konspektlar va tadqiqotlar

---

## 🔎 Tezkor qidiruv

“Men nima izlayapman va uni qayerdan topaman?”

| Men izlayapman                   | Qayerdan topaman                                               |
| -------------------------------- | -------------------------------------------------------------- |
| Web CTF challenge                | [`ctf/web/`](ctf/web/)                                         |
| Crypto CTF challenge             | [`ctf/crypto/`](ctf/crypto/)                                   |
| Pwn / binary exploitation        | [`ctf/pwn/`](ctf/pwn/)                                         |
| Reverse engineering              | [`ctf/reverse/`](ctf/reverse/)                                 |
| Forensics (pcap, memory, disk)   | [`ctf/forensics/`](ctf/forensics/)                             |
| OSINT                            | [`ctf/osint/`](ctf/osint/)                                     |
| Linux privilege escalation       | [`notes/privilege-escalation/`](notes/privilege-escalation/)   |
| Web security konspektlari        | [`notes/web-security/`](notes/web-security/)                   |
| Active Directory                 | [`notes/active-directory/`](notes/active-directory/)           |
| Linux buyruqlari va konspektlar  | [`notes/linux/`](notes/linux/)                                 |
| Networking asoslari              | [`notes/networking/`](notes/networking/)                       |
| Python script                    | [`scripts/python/`](scripts/python/)                           |
| Bash script                      | [`scripts/bash/`](scripts/bash/)                               |
| PowerShell script                | [`scripts/powershell/`](scripts/powershell/)                   |
| Nmap / enumeration tools         | [`tools/enumeration/`](tools/enumeration/)                     |
| Web security tools               | [`tools/web/`](tools/web/)                                     |
| Exploitation tools               | [`tools/exploitation/`](tools/exploitation/)                   |
| TryHackMe writeup                | [`writeups/tryhackme/`](writeups/tryhackme/)                   |
| HackTheBox writeup               | [`writeups/hackthebox/`](writeups/hackthebox/)                 |
| PortSwigger Web Academy writeup  | [`writeups/portswigger/`](writeups/portswigger/)               |
| Local lab muhitlari              | [`labs/`](labs/)                                               |
| Pentest methodology / checklist  | [`docs/methodology/`](docs/methodology/)                       |
| Yangi writeup uchun shablon      | [`writeups/_template.md`](writeups/_template.md)               |
| Yangi tool uchun shablon         | [`tools/_template.md`](tools/_template.md)                     |
| Yangi script uchun shablon       | [`scripts/_template.md`](scripts/_template.md)                 |

> 💡 GitHub'da repository ichidan qidirish uchun `t` tugmasini bosing (file finder) yoki yuqoridagi qidiruv maydoniga `repo:islomovmuhammadkarim/ctf-cyber-lab <so‘z>` yozing.

---

## 📂 Repository strukturasi

```text
ctf-cyber-lab/
├── README.md              # Bosh sahifa va navigatsiya
├── LICENSE                # MIT License
├── .gitignore             # Git'ga tushmasligi kerak bo‘lgan fayllar
│
├── ctf/                   # CTF musobaqalari: challenge fayllari va yechimlar
│   ├── web/  crypto/  pwn/  reverse/
│   └── forensics/  osint/  misc/  network/
│
├── tools/                 # O‘zim yozgan yoki moslashtirgan security tools
│   ├── _template.md
│   └── enumeration/  web/  network/  exploitation/  automation/
│
├── scripts/               # Kichik, bir martalik yoki yordamchi skriptlar
│   ├── _template.md
│   └── python/  bash/  powershell/
│
├── notes/                 # Mavzu bo‘yicha konspektlar va cheat sheetlar
│   └── linux/  networking/  web-security/
│       privilege-escalation/  active-directory/  general/
│
├── writeups/              # Platformalardagi room/machine/lab writeuplari
│   ├── _template.md
│   └── tryhackme/  hackthebox/  portswigger/  other/
│
├── labs/                  # Local lab muhitlari (Docker, VM, konfiguratsiya)
│   └── web/  linux/  windows/  network/
│
└── docs/
    └── methodology/       # Pentest metodologiya va checklistlar
```

**Nomlash qoidalari (naming convention):**

- Papka va fayl nomlari — `kichik-harf-va-chiziqcha` (kebab-case): `sql-injection-basics.md`, `blue.md`.
- Bo‘sh papkalardagi `.gitkeep` — faqat papkani Git'da saqlash uchun. Papkaga birinchi fayl qo‘shilgach, uni o‘chirish mumkin.

---

## 🚩 CTF

Bu bo‘limda **CTF musobaqalari** (masalan, picoCTF, CTFtime eventlari) topshiriqlari va ularning yechimlari saqlanadi.

| Kategoriya          | Papka                                  | Tavsif                                        |
| ------------------- | -------------------------------------- | --------------------------------------------- |
| Web                 | [`ctf/web/`](ctf/web/)                 | SQLi, XSS, SSTI, auth bypass va h.k.          |
| Crypto              | [`ctf/crypto/`](ctf/crypto/)           | Klassik shifrlar, RSA, XOR, hash              |
| Pwn                 | [`ctf/pwn/`](ctf/pwn/)                 | Buffer overflow, ROP, format string           |
| Reverse Engineering | [`ctf/reverse/`](ctf/reverse/)         | Binary tahlil, decompile, crackme             |
| Forensics           | [`ctf/forensics/`](ctf/forensics/)     | PCAP, memory dump, disk image, steganography  |
| OSINT               | [`ctf/osint/`](ctf/osint/)             | Ochiq manbalardan ma'lumot yig‘ish            |
| Misc                | [`ctf/misc/`](ctf/misc/)               | Boshqa kategoriyalarga tushmaydiganlar        |
| Network             | [`ctf/network/`](ctf/network/)         | Protokollar, trafik tahlili                   |

**Yangi challenge qo‘shish:**

```text
ctf/<kategoriya>/<event>-<yil>-<challenge-nomi>/
├── README.md      # writeups/_template.md asosida yozilgan yechim
├── solve.py       # (ixtiyoriy) yechim skripti
└── files/         # (ixtiyoriy) challenge fayllari — faqat ruxsat berilgan bo‘lsa
```

Misol: `ctf/web/picoctf-2025-cookie-monster/README.md`

> **`ctf/` va `writeups/` farqi:** `ctf/` — vaqt bilan cheklangan musobaqa (event) topshiriqlari. `writeups/` — doimiy platformalardagi room, machine va lablar (TryHackMe, HackTheBox, PortSwigger).

---

## 🧰 Tools

Bu bo‘limda o‘zim yozgan yoki moslashtirgan, qayta ishlatiladigan **security tools** saqlanadi.

| Kategoriya     | Papka                                              | Misol                                  |
| -------------- | -------------------------------------------------- | -------------------------------------- |
| Enumeration    | [`tools/enumeration/`](tools/enumeration/)         | Port / service / subdomain enumeration |
| Web            | [`tools/web/`](tools/web/)                         | Directory fuzzing, header tekshiruv    |
| Network        | [`tools/network/`](tools/network/)                 | Packet tahlil, sniffing yordamchilari  |
| Exploitation   | [`tools/exploitation/`](tools/exploitation/)       | PoC va exploit yordamchilari           |
| Automation     | [`tools/automation/`](tools/automation/)           | Recon pipeline, report generatsiya     |

Har bir tool alohida papkada va bir xil formatda bo‘ladi:

```text
tools/<kategoriya>/<tool-nomi>/
├── README.md          # tools/_template.md asosida
├── requirements.txt   # (Python bo‘lsa) faqat kerakli dependency'lar
└── <tool-nomi>.py
```

README ichida: **Tool nomi, Maqsadi, O‘rnatish, Foydalanish, Example, Limitations, Security notes**. Shablon: [`tools/_template.md`](tools/_template.md).

---

## 📜 Scripts

Kichik, yordamchi yoki bir martalik skriptlar (tool darajasiga yetmaganlar).

| Til        | Papka                                            |
| ---------- | ------------------------------------------------ |
| Python     | [`scripts/python/`](scripts/python/)             |
| Bash       | [`scripts/bash/`](scripts/bash/)                 |
| PowerShell | [`scripts/powershell/`](scripts/powershell/)     |

Har bir muhim skript boshida (docstring yoki comment) yoki yonidagi README'da quyidagilar bo‘ladi: **Purpose, Requirements, Installation, Usage, Examples, Notes**. Shablon: [`scripts/_template.md`](scripts/_template.md).

> Skript kattalashib, bir nechta fayl va dependency talab qila boshlasa — uni `tools/` ga ko‘chiring.

---

## 📚 Notes

Mavzu bo‘yicha konspektlar, cheat sheetlar va tadqiqotlar.

| Mavzu                 | Papka                                                          |
| --------------------- | -------------------------------------------------------------- |
| Linux                 | [`notes/linux/`](notes/linux/)                                 |
| Networking            | [`notes/networking/`](notes/networking/)                       |
| Web Security          | [`notes/web-security/`](notes/web-security/)                   |
| Privilege Escalation  | [`notes/privilege-escalation/`](notes/privilege-escalation/)   |
| Active Directory      | [`notes/active-directory/`](notes/active-directory/)           |
| General               | [`notes/general/`](notes/general/)                             |

Fayl nomi mavzuni aniq aytsin: `notes/web-security/sql-injection.md`, `notes/linux/file-permissions.md`.

---

## 📝 Writeups

TryHackMe, HackTheBox, PortSwigger va boshqa platformalardagi room / machine / lab writeuplari.

| Platforma            | Papka                                              |
| -------------------- | -------------------------------------------------- |
| TryHackMe            | [`writeups/tryhackme/`](writeups/tryhackme/)       |
| HackTheBox           | [`writeups/hackthebox/`](writeups/hackthebox/)     |
| PortSwigger Academy  | [`writeups/portswigger/`](writeups/portswigger/)   |
| Boshqa               | [`writeups/other/`](writeups/other/)               |

Har bir writeup [`writeups/_template.md`](writeups/_template.md) asosida yoziladi:

```text
Challenge · Category · Platform · Difficulty · Target · Objective

1. Reconnaissance
2. Enumeration
3. Analysis
4. Exploitation
5. Privilege Escalation
6. Flag
7. Lessons Learned
```

> ⚠️ HackTheBox **active** machine'lar uchun writeup'ni machine retire bo‘lgunicha public qilmang — bu platforma qoidalariga zid. Real flag va parollarni yozmang, o‘rniga `THM{REDACTED}` kabi placeholder ishlating.

---

## 🧪 Labs

O‘zim ko‘targan local lab muhitlari: Docker compose fayllari, VM sozlamalari, zaif (vulnerable) ilovalar konfiguratsiyasi.

| Lab turi | Papka                              |
| -------- | ---------------------------------- |
| Web      | [`labs/web/`](labs/web/)           |
| Linux    | [`labs/linux/`](labs/linux/)       |
| Windows  | [`labs/windows/`](labs/windows/)   |
| Network  | [`labs/network/`](labs/network/)   |

> Zaif lablarni faqat izolyatsiyalangan tarmoqda (host-only / internal network) ishga tushiring, internetga ochmang.

---

## 📖 Docs

[`docs/methodology/`](docs/methodology/) — pentest bosqichlari, recon checklist, reporting va umumiy ish metodologiyasi.

---

## 📊 Lab statistikasi

| Bo‘lim          | Soni |
| --------------- | ---- |
| CTF Challenges  | 0    |
| Writeups        | 0    |
| Security Tools  | 0    |
| Scripts         | 0    |
| Notes           | 0    |
| Labs            | 0    |

> Raqamlar repository'dagi haqiqiy fayllarga mos (oxirgi yangilanish: 2026-09-30). Kontent qo‘shilgach, jadvalni yangilashni unutmang — kelajakda uni avtomatik hisoblaydigan skript qo‘shish rejalashtirilgan.

---

## 🔐 Security

Bu repository **public**. Shuning uchun quyidagi qoidalar majburiy:

1. **Secrets commit qilinmaydi** — password, API key, token, cookie, session ID, SSH private key, VPN (`.ovpn`) fayllari.
2. **`.env` ishlating** — maxfiy qiymatlar faqat local `.env` faylida turadi (u `.gitignore` da). Namuna kerak bo‘lsa, bo‘sh qiymatli `.env.example` qo‘shing.
3. **Real credentials saqlanmaydi** — writeup va notes'larda `REDACTED`, `<PASSWORD>`, `10.10.x.x` kabi placeholder ishlating.
4. **Faqat ruxsat berilgan targetlar** — TryHackMe, HackTheBox, PortSwigger, CTF platformalari yoki o‘zingizning local lablaringiz.
5. **Qonuniylik** — security testing faqat qonuniy va yozma ruxsat berilgan muhitda o‘tkaziladi. Bu repository'dagi materiallar faqat ta'lim maqsadida.
6. **Commit'dan oldin tekshiring** — `git diff --staged` ni ko‘zdan kechiring. Agar secret tasodifan push qilingan bo‘lsa, uni darhol **revoke / rotate** qiling: Git tarixidan o‘chirish yetarli emas.

> Xavfsizlik muammosi topsangiz, public issue ochmasdan repository egasiga to‘g‘ridan-to‘g‘ri xabar bering.

---

## 🤝 Contribution

Hissa qo‘shish ochiq! Quyidagilarni qo‘shishingiz mumkin:

- 🧰 yangi **tool** → `tools/<kategoriya>/<tool-nomi>/`
- 📜 yangi **script** → `scripts/<til>/`
- 📚 yangi **note** → `notes/<mavzu>/`
- 📝 yangi **CTF writeup** → `ctf/<kategoriya>/` yoki `writeups/<platforma>/`

**Qoidalar:**

1. Tegishli shablondan foydalaning (`writeups/_template.md`, `tools/_template.md`, `scripts/_template.md`).
2. [🔐 Security](#-security) bo‘limidagi qoidalarga to‘liq rioya qiling — secret yoki real credential bo‘lgan PR qabul qilinmaydi.
3. Keraksiz dependency qo‘shmang; `requirements.txt` da faqat haqiqatan kerakli paketlar bo‘lsin.
4. Kod ishlaydigan va tushunarli bo‘lsin; zararli (malicious) yoki ruxsatsiz hujumga mo‘ljallangan kod qabul qilinmaydi.
5. Fork → yangi branch → o‘zgarish → Pull Request. PR tavsifida nima qo‘shilganini qisqa yozing.

Barcha o‘zgarishlar repository egasi tomonidan ko‘rib chiqiladi va uning security hamda quality talablariga mos kelishi shart.

---

## 📄 License

Ushbu loyiha [MIT License](LICENSE) ostida tarqatiladi.
