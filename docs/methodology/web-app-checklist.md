# Web Application Testing Checklist

Web ilovani tekshirishda qisqa checklist. Batafsil nazariya: [`notes/web-security/`](../../notes/web-security/).

## Information Gathering

- [ ] Texnologiyalar: server, framework, CMS (`whatweb`, Wappalyzer, HTTP header'lar)
- [ ] `robots.txt`, `sitemap.xml`, `.git/`, `.env`, backup fayllar (`.bak`, `.old`, `~`)
- [ ] Sahifa manba kodi: comment'lar, yashirin maydonlar, JS fayllardagi endpoint'lar
- [ ] Directory va fayl brute force (`gobuster`, `ffuf`)
- [ ] Subdomain va virtual host (`ffuf -H "Host: FUZZ.<domain>"`)

## Authentication

- [ ] Default credential'lar
- [ ] Username enumeration (xato xabarlari yoki javob vaqti farqi)
- [ ] Parol tiklash (password reset) mexanizmi
- [ ] Brute force himoyasi (rate limit, lockout) — faqat ruxsat bo‘lsa
- [ ] JWT: `alg: none`, zaif secret, imzo tekshirilmasligi

## Session Management

- [ ] Cookie flag'lari: `HttpOnly`, `Secure`, `SameSite`
- [ ] Logout'dan keyin session bekor bo‘ladimi?
- [ ] Session ID taxmin qilinadigan emasmi?

## Access Control

- [ ] IDOR: `?id=1` → `?id=2`
- [ ] Oddiy user admin endpoint'larga kira oladimi?
- [ ] HTTP method o‘zgartirish (`GET` ↔ `POST` ↔ `PUT`)

## Input Validation

- [ ] SQL Injection — [`sql-injection.md`](../../notes/web-security/sql-injection.md)
- [ ] XSS (reflected, stored, DOM) — [`xss.md`](../../notes/web-security/xss.md)
- [ ] Command Injection (`; id`, `| id`, `` `id` ``, `$(id)`)
- [ ] SSTI (`{{7*7}}`, `${7*7}`)
- [ ] Path Traversal / LFI (`../../../../etc/passwd`)
- [ ] File upload: kengaytma, `Content-Type`, magic bytes tekshiruvi
- [ ] SSRF (`http://127.0.0.1`, `http://169.254.169.254`)
- [ ] XXE (XML qabul qiladigan endpoint'lar)

## Business Logic

- [ ] Narx yoki miqdorni manfiy / nol qilish
- [ ] Bosqichlarni o‘tkazib yuborish (multi-step jarayonlar)
- [ ] Race condition

## Security Headers

- [ ] `Content-Security-Policy`, `Strict-Transport-Security`, `X-Frame-Options`, `X-Content-Type-Options`
- [ ] Tekshirish uchun: [`tools/web/header-check/`](../../tools/web/header-check/)
