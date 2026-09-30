# OWASP Juice Shop — Local Lab

[OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) — o‘rganish uchun
ataylab zaif qilib yozilgan zamonaviy web ilova. OWASP Top 10 va boshqa ko‘plab
zaifliklarni xavfsiz, qonuniy muhitda mashq qilish uchun.

## Talablar

- Docker va Docker Compose

## Ishga tushirish

```bash
cd labs/web/juice-shop
docker compose up -d
```

Brauzerda oching: <http://localhost:3000>

To‘xtatish:

```bash
docker compose down
```

## Muhim: xavfsizlik

- Ilova **ataylab zaif** — uni faqat o‘z kompyuteringizda ishga tushiring.
- `docker-compose.yml` da port `127.0.0.1` ga bog‘langan, ya'ni faqat sizning
  mashinangizdan ochiladi. Buni tarmoqqa ochib qo‘ymang.
- Faqat shu ilovaning o‘zini sinang — bu sizning qonuniy sinov maydoningiz.

## Mashq g‘oyalari

- OWASP Top 10 bo‘yicha konspekt: [`notes/web-security/owasp-top-10.md`](../../../notes/web-security/owasp-top-10.md)
- Har bir topilgan zaiflikni [`writeups/_template.md`](../../../writeups/_template.md) asosida yozib boring.
