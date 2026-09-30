# Cookie Role (namuna)

<!-- To‘ldirilgan NAMUNA. Real target, flag yoki credential yo‘q — hammasi placeholder. -->

| Maydon         | Qiymat                          |
| -------------- | ------------------------------- |
| **Challenge**  | Cookie Role                     |
| **Category**   | Web                             |
| **Platform**   | Example CTF                     |
| **Difficulty** | Easy                            |
| **Target**     | http://challenge.example/       |
| **Objective**  | Admin sahifadagi flag'ni ochish |
| **Tags**       | web, cookie, access-control, idor |

## TL;DR

Sayt foydalanuvchi rolini oddiy cookie'da (`role=user`) saqlar ekan va uni server
tomonda tekshirmasdan ishonar edi. Cookie'ni `role=admin` ga o‘zgartirib admin
sahifaga kirildi (OWASP A01 — Broken Access Control).

## 1. Reconnaissance

Saytga oddiy user sifatida kirilgach, brauzer devtools → Application → Cookies
bo‘limida quyidagi cookie ko‘rindi:

```text
session=<...>
role=user
```

## 2. Analysis

- `role` cookie'si imzolanmagan (JWT emas, oddiy matn).
- Admin sahifasi (`/admin`) oddiy userga `403 Forbidden` qaytaradi.
- Taxmin: server `/admin` uchun `role` cookie qiymatiga qarab qaror qiladi.

## 3. Exploitation

`role` cookie qiymati `user` dan `admin` ga o‘zgartirildi va `/admin` qayta so‘raldi:

```bash
curl http://challenge.example/admin -b "session=<...>; role=admin"
```

Admin sahifa ochildi va flag ko‘rindi.

## 4. Flag

```text
flag{REDACTED}
```

## 5. Lessons Learned

- **Client tomonда saqlangan ma'lumotga ishonib bo‘lmaydi** — cookie'ni foydalanuvchi
  o‘zgartira oladi.
- Rol/huquq har doim **server tomonда**, ishonchli session ma'lumotiga qarab
  tekshirilishi kerak.
- **Himoya:** rolni server-side session'da saqlash yoki imzolangan token (JWT'ni
  to‘g‘ri tekshirish bilan) ishlatish. Cookie'ga `HttpOnly` va `Secure` qo‘yish.

## References

- [OWASP A01: Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)
- Konspekt: [notes/web-security/owasp-top-10.md](../../../notes/web-security/owasp-top-10.md)
