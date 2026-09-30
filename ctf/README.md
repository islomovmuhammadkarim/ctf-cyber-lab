# 🚩 CTF

CTF musobaqalari (picoCTF, CTFtime eventlari va h.k.) topshiriqlari va yechimlari.

> `ctf/` — vaqt bilan cheklangan **musobaqa** topshiriqlari uchun.
> Doimiy platformalar (TryHackMe, HackTheBox, PortSwigger) esa [`writeups/`](../writeups/) da.

## Kategoriyalar

| Kategoriya                            | Papka                    |
| ------------------------------------- | ------------------------ |
| [Web](web/)                           | `ctf/web/`               |
| [Crypto](crypto/)                     | `ctf/crypto/`            |
| [Pwn (Binary Exploitation)](pwn/)     | `ctf/pwn/`               |
| [Reverse Engineering](reverse/)       | `ctf/reverse/`           |
| [Forensics](forensics/)               | `ctf/forensics/`         |
| [OSINT](osint/)                       | `ctf/osint/`             |
| [Misc](misc/)                         | `ctf/misc/`              |
| [Network](network/)                   | `ctf/network/`           |

## Yangi challenge qo‘shish

```text
ctf/<kategoriya>/<event>-<yil>-<challenge-nomi>/
├── README.md      # writeups/_template.md asosidagi yechim
├── solve.py       # (ixtiyoriy) yechim skripti
└── files/         # (ixtiyoriy) challenge fayllari — faqat tarqatishga ruxsat bo‘lsa
```

Misol: `ctf/web/picoctf-2025-cookie-monster/README.md`

> ⚠️ Real flag'ni yozmang — `flag{REDACTED}` ishlating. Faqat tarqatishga ruxsat berilgan challenge fayllarini qo‘shing (ko‘p musobaqalarda fayllarni qayta tarqatish taqiqlangan).
