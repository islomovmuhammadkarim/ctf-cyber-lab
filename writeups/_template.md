# <Challenge / Room / Machine nomi>

<!--
  Shablondan foydalanish:
  1. Faylni nusxalang: writeups/<platforma>/<nomi>.md yoki ctf/<kategoriya>/<event>-<yil>-<nomi>/README.md
  2. <...> bilan belgilangan joylarni to‘ldiring, keraksiz bo‘limlarni o‘chiring.
  3. HECH QACHON real flag, password, token, cookie yoki boshqa credential yozmang.
     Placeholder ishlating: THM{REDACTED}, HTB{REDACTED}, <PASSWORD>, 10.10.x.x
-->

| Maydon         | Qiymat                                                        |
| -------------- | ------------------------------------------------------------- |
| **Challenge**  | <nomi>                                                        |
| **Category**   | <Web / Crypto / Pwn / Reverse / Forensics / OSINT / Misc / Network> |
| **Platform**   | <TryHackMe / HackTheBox / PortSwigger / picoCTF / ...>        |
| **Difficulty** | <Easy / Medium / Hard / Insane>                               |
| **Target**     | <10.10.x.x yoki URL — faqat platforma bergan manzil>          |
| **Objective**  | <nima qilish kerak: user/root flag, admin panelga kirish ...> |
| **Sana**       | <YYYY-MM-DD>                                                  |
| **Tags**       | <sqli, suid, smb, ...>                                        |

## TL;DR

<1–3 gapda: qanday zaiflik topildi va qanday yechildi.>

## 1. Reconnaissance

<Target haqida dastlabki ma'lumot yig‘ish.>

```bash
nmap -sC -sV -oN nmap/initial <TARGET_IP>
```

## 2. Enumeration

<Servislar, directorylar, userlar, versiyalar.>

## 3. Analysis

<Topilgan ma'lumotlar tahlili: qaysi zaiflik (vulnerability) bor va nima uchun.>

## 4. Exploitation

<Zaiflikdan foydalanish bosqichlari. Kod/payload qisqa va tushunarli bo‘lsin.>

## 5. Privilege Escalation

<User → root / Administrator. Kerak bo‘lmasa o‘chiring.>

## 6. Flag

```text
user.txt: <PLATFORM>{REDACTED}
root.txt: <PLATFORM>{REDACTED}
```

> Real flag yozilmaydi.

## 7. Lessons Learned

- <Nimani o‘rgandim?>
- <Qanday himoya (mitigation) bu zaiflikni oldini oladi?>

## References

- <Foydalanilgan manbalar, CVE, maqolalar>
