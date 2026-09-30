# Example Room (namuna)

<!--
  Bu — writeup qanday ko‘rinishi kerakligini ko‘rsatuvchi TO‘LDIRILGAN NAMUNA.
  Haqiqiy writeup yozganда writeups/_template.md dan nusxa oling.
  Bu yerda hech qanday real target, flag yoki credential yo‘q — hammasi placeholder.
-->

| Maydon         | Qiymat                          |
| -------------- | ------------------------------- |
| **Challenge**  | Example Room                    |
| **Category**   | Web                             |
| **Platform**   | TryHackMe                       |
| **Difficulty** | Easy                            |
| **Target**     | 10.10.x.x                       |
| **Objective**  | Web ilovadagi zaiflik orqali user va root flag'ni topish |
| **Sana**       | 2026-09-30                      |
| **Tags**       | web, enumeration, misconfig     |

## TL;DR

Ochiq web port topildi, directory enumeration orqali yashirin sahifa aniqlandi,
noto‘g‘ri sozlangan huquqlar orqali tizimga kirildi va oddiy privesc bilan root olindi.

## 1. Reconnaissance

```bash
nmap -sC -sV -oN nmap/detailed 10.10.x.x
```

Natija: `22/tcp` (SSH) va `80/tcp` (HTTP) ochiq.

## 2. Enumeration

Web serverni directory enumeration:

```bash
gobuster dir -u http://10.10.x.x -w /usr/share/wordlists/dirb/common.txt
```

`/hidden` yo‘li topildi — unda konfiguratsiya sahifasi bor edi.

## 3. Analysis

Konfiguratsiya sahifasi autentifikatsiyasiz ochiq (Security Misconfiguration — OWASP A05).
Undan servis haqidagi ma'lumot va login uchun ipuchi olindi.

## 4. Exploitation

Topilgan ma'lumot yordamida web panelga kirildi va SSH orqali dastlabki shell olindi.

```text
user.txt: THM{REDACTED}
```

## 5. Privilege Escalation

```bash
sudo -l
```

Bir buyruq parolsiz `root` sifatida ishga tushar ekan; [GTFOBins](https://gtfobins.github.io/)
yordamida undan shell olindi.

```text
root.txt: THM{REDACTED}
```

## 6. Flag

Ikkala flag ham topildi (yuqorida REDACTED ko‘rinishida — real qiymat repository'ga yozilmaydi).

## 7. Lessons Learned

- Directory enumeration'ni to‘liq wordlist bilan bajarish muhim.
- `sudo -l` — privesc'da eng birinchi tekshiriladigan joy.
- **Himoya:** ichki sahifalarga autentifikatsiya qo‘yish, `sudo` qoidalarini minimal saqlash.

## References

- [GTFOBins](https://gtfobins.github.io/)
- [OWASP A05: Security Misconfiguration](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)
