# Cross-Site Scripting (XSS)

O‘quv konspekti. Faqat ruxsat berilgan lab va CTF muhitlarida sinash uchun.

## Nima bu?

Hujumchi kiritgan matn boshqa foydalanuvchi brauzerida **HTML/JavaScript sifatida** bajarilsa, XSS yuzaga keladi. Sabab — foydalanuvchi input'i sahifaga chiqarilishdan oldin to‘g‘ri kodlanmagani (encoding qilinmagani).

## Turlari

| Turi        | Qayerda saqlanadi / qanday yetkaziladi                          |
| ----------- | --------------------------------------------------------------- |
| Reflected   | Input so‘rovda kelib, javobda darhol qaytariladi (masalan, qidiruv natijasi) |
| Stored      | Input serverda saqlanadi va keyin boshqalarga ko‘rsatiladi (izoh, profil) |
| DOM-based   | Zaiflik butunlay klient tomon JS'da, sahifa DOM'ini o‘zgartirishda |

## Ta'siri (impact)

- Session cookie'ni o‘g‘irlash
- Foydalanuvchi nomidan amallar bajarish
- Sahifani soxtalashtirish (defacement, fishing forma)
- Keylogging

## Aniqlash

Input qaytariladigan joyni topib, u **matn** sifatida ko‘rsatilayaptimi yoki **HTML** sifatida talqin qilinayaptimi tekshiriladi. Agar oddiy `<b>test</b>` qalin bo‘lib chiqsa — sahifa input'ni HTML sifatida qabul qilyapti, bu XSS uchun signal.

Test payload'lar odatda `alert()` yoki `console.log()` kabi zararsiz funksiyalar bilan tuziladi — maqsad kod bajarilishini isbotlash, zarar yetkazish emas.

## Himoya (juda muhim)

- **Output encoding** — kontekstga mos (HTML, attribute, JS, URL). Bu asosiy yechim.
- **Content Security Policy (CSP)** — inline skript va tashqi manbalarni cheklaydi.
- Framework'ning avtomatik escaping'idan foydalanish (React, Jinja2 autoescape va h.k.).
- Cookie'ga `HttpOnly` — JS uni o‘qiy olmaydi.
- Input validatsiya (allow-list), lekin bu yolg‘iz yetarli emas — encoding baribir kerak.

## Manbalar

- [PortSwigger — XSS](https://portswigger.net/web-security/cross-site-scripting)
- [OWASP — XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
