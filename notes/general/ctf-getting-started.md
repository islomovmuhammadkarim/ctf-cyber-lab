# CTF — Boshlash uchun qo‘llanma

CTF (Capture The Flag) — kiberxavfsizlik bo‘yicha musobaqa. Maqsad — topshiriqlarni yechib, yashirin **flag** (masalan `flag{...}`) ni topish.

## CTF turlari

| Turi        | Tavsif                                                             |
| ----------- | ------------------------------------------------------------------ |
| Jeopardy    | Kategoriyalarga bo‘lingan mustaqil topshiriqlar (eng keng tarqalgan) |
| Attack-Defense | Har bir jamoa o‘z servisini himoya qilib, boshqalarnikiga hujum qiladi |
| King of the Hill | Bitta tizimni egallab, ushlab turish                           |

## Kategoriyalar

| Kategoriya          | Nima haqida                                    | Konspekt                                       |
| ------------------- | ---------------------------------------------- | ---------------------------------------------- |
| Web                 | Web ilova zaifliklari                          | [`notes/web-security/`](../web-security/)      |
| Crypto              | Shifrlash, kodlash, hash                        | —                                              |
| Pwn (Binary)        | Binary exploitation, xotira xatolari            | —                                              |
| Reverse Engineering | Binary'ni tahlil qilib mantiqini tushunish      | —                                              |
| Forensics           | PCAP, memory dump, disk, steganography          | —                                              |
| OSINT               | Ochiq manbalardan ma'lumot yig‘ish             | —                                              |
| Misc                | Aralash topshiriqlar                            | —                                              |

## Zarur asosiy vositalar

```text
Web:       browser devtools, Burp Suite, ffuf/gobuster, curl
Crypto:    CyberChef, Python (pycryptodome), hashcat/john
Pwn:       gdb (+pwndbg/gef), pwntools, checksec
Reverse:   Ghidra, radare2/rizin, strings, ltrace/strace
Forensics: Wireshark, binwalk, exiftool, volatility, steghide
Umumiy:    Linux, Python, hex editor, base64/hex bilan ishlash
```

## Ish jarayoni (workflow)

1. Topshiriqni diqqat bilan o‘qing — matnda ipuchi (hint) bo‘ladi.
2. Kategoriyani va berilgan fayl/URL turini aniqlang (`file`, `strings`).
3. Osonroq va aniqroq yo‘ldan boshlang.
4. Har bir qadamni yozib boring — keyin writeup uchun asqotadi.
5. Flag topilgach, uni [`writeups/_template.md`](../../writeups/_template.md) asosida hujjatlashtiring (real flag'ni `REDACTED` bilan).

## Platformalar

| Platforma              | Nima uchun yaxshi                                 |
| ---------------------- | ------------------------------------------------- |
| [picoCTF](https://picoctf.org/) | Boshlovchilar uchun, doim ochiq             |
| [TryHackMe](https://tryhackme.com/) | Bosqichma-bosqich yo‘naltirilgan xonalar |
| [HackTheBox](https://www.hackthebox.com/) | Realroq mashinalar                  |
| [CTFtime](https://ctftime.org/) | Jonli musobaqalar taqvimi                   |
| [OverTheWire](https://overthewire.org/wargames/) | Linux/asoslar wargame'lari |

## Maslahatlar

- Boshlovchi bo‘lsangiz — picoCTF va TryHackMe'dan boshlang.
- Bitta topshiriqqa juda uzoq tiqilib qolmang; boshqasiga o‘tib, keyin qayting.
- Boshqalarning writeup'larini o‘qing — eng tez o‘rganish usuli.
- Barcha ishni [🔐 Security](../../README.md#-security) qoidalariga rioya qilib bajaring.
