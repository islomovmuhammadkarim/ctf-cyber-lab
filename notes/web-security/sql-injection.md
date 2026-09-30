# SQL Injection (SQLi)

O‘quv konspekti. Faqat ruxsat berilgan lab va CTF muhitlarida (PortSwigger, TryHackMe, DVWA va shu kabilar) sinash uchun.

## Nima bu?

Foydalanuvchi kiritgan ma'lumot SQL so‘roviga alohida ajratilmasdan qo‘shilsa, so‘rov mantiqi buziladi. Sabab — ma'lumot va kod bir-biridan ajratilmaganligi.

```php
// Zaif namuna
$query = "SELECT * FROM users WHERE username = '$user'";
```

## Ildiz sabab

Ma'lumot (user input) va kod (SQL) aralashib ketishi. Yechim — ularni ajratish: **parametrlangan so‘rovlar (prepared statements)**.

## Aniqlash belgilari (detection)

Zaiflik bor-yo‘qligini sinashda quyidagi belgilarga qaraladi:

| Kuzatilishi mumkin bo‘lgan holat        | Nimadan darak beradi           |
| --------------------------------------- | ------------------------------ |
| Bitta tirnoq kiritilganda ilova xatosi  | Input so‘roq ichiga tushyapti  |
| Rost/yolg‘on shartlarda javob farqi     | Boolean-based ehtimoli         |
| Javob vaqtining sezilarli kechikishi    | Time-based ehtimoli            |

## Turlari (tasnif)

| Turi             | Natija qanday olinadi                     |
| ---------------- | ----------------------------------------- |
| In-band (UNION)  | To‘g‘ridan-to‘g‘ri sahifada ko‘rinadi     |
| Error-based      | Xato xabarlari orqali                     |
| Blind (boolean)  | Faqat rost/yolg‘on farqi orqali           |
| Blind (time)     | Faqat javob vaqti orqali                  |
| Out-of-band      | Tashqi kanal (masalan DNS) orqali         |

## Metodologiya (yuqori daraja)

1. Input nuqtalarini aniqlash (URL parametri, forma, header, cookie).
2. Zaiflik borligini oddiy probe bilan tasdiqlash.
3. So‘rov strukturasini tushunish (ustunlar soni, chiqadigan joy).
4. `information_schema` orqali sxemani o‘rganish.
5. Kerakli ma'lumotni ajratib olish.

> Aniq payload zanjirlarini har bir lab o‘z darsligida beradi (masalan PortSwigger). Bu yerda maqsad — mexanizmni tushunish, tayyor hujum quroli emas.

## `sqlmap`

Avtomatlashtirilgan test uchun, faqat ruxsat berilgan target'da:

```bash
sqlmap -u "http://<LAB_TARGET>/item?id=1" --batch
```

## Himoya (juda muhim)

- **Prepared statements / parametrlangan so‘rovlar** — asosiy yechim:

  ```python
  cur.execute("SELECT * FROM users WHERE username = %s", (user,))
  ```

- ORM'dan to‘g‘ri foydalanish (xom so‘rovlarni aralashtirmaslik).
- Input validatsiya (allow-list).
- Eng kam huquqли DB user (least privilege).
- Xato xabarlarini foydalanuvchiga ko‘rsatmaslik.

## Manbalar

- [PortSwigger — SQL Injection](https://portswigger.net/web-security/sql-injection)
- [OWASP — SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
