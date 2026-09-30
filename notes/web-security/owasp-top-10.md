# OWASP Top 10 (2021)

OWASP Top 10 — web ilovalardagi eng keng tarqalgan xavflar ro‘yxati.

> Ro‘yxat vaqti-vaqti bilan yangilanadi — eng so‘nggi versiyani [owasp.org/Top10](https://owasp.org/Top10/) dan tekshiring.

| #   | Kategoriya                                   | Qisqacha                                                            |
| --- | -------------------------------------------- | ------------------------------------------------------------------- |
| A01 | Broken Access Control                        | User o‘ziga ruxsat berilmagan narsaga kira oladi (IDOR va h.k.)     |
| A02 | Cryptographic Failures                       | Maxfiy ma'lumot himoyasiz yoki zaif shifrlangan                     |
| A03 | Injection                                    | Foydalanuvchi input'i buyruq/so‘rov sifatida bajariladi             |
| A04 | Insecure Design                              | Xavfsizlik dizayn bosqichida hisobga olinmagan                      |
| A05 | Security Misconfiguration                    | Default parol, debug rejim, ortiqcha ochiq sozlamalar               |
| A06 | Vulnerable and Outdated Components           | Eskirgan, ma'lum CVE'si bor kutubxona yoki servislar                |
| A07 | Identification and Authentication Failures   | Autentifikatsiyadagi zaifliklar (zaif session, brute force himoyasi yo‘q) |
| A08 | Software and Data Integrity Failures         | Kod yoki ma'lumot yaxlitligi tekshirilmaydi                         |
| A09 | Security Logging and Monitoring Failures     | Hujumlar qayd etilmaydi va sezilmaydi                               |
| A10 | Server-Side Request Forgery (SSRF)           | Server hujumchi ko‘rsatgan ichki manzilga so‘rov yuboradi           |

## Har biri bo‘yicha himoya (mitigation) asoslari

- **A01:** har bir so‘rovda server tomonda avtorizatsiyani tekshirish; default — rad etish (deny by default).
- **A02:** transportда TLS, maxfiy ma'lumotni kuchli va zamonaviy algoritm bilan saqlash, parollarni `bcrypt`/`argon2` bilan.
- **A03:** parametrlangan so‘rovlar (prepared statements), input validatsiya, output encoding.
- **A05:** keraksiz servis va sahifalarni o‘chirish, default credential'larni almashtirish.
- **A06:** dependency'larni yangilab turish, `pip-audit` / `npm audit` kabi vositalar.
- **A10:** URL'larni allow-list bilan cheklash, ichki tarmoqqa so‘rovlarni bloklash.

## Qayerdan mashq qilish

- [PortSwigger Web Security Academy](https://portswigger.net/web-security) — bepul lablar
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) — local lab
- TryHackMe'dagi OWASP Top 10 xonalari

## Bog‘liq konspektlar

- [SQL Injection](sql-injection.md)
- [Cross-Site Scripting (XSS)](xss.md)
