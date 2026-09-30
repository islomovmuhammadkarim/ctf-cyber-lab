# header-check

> Berilgan URL javobidagi HTTP xavfsizlik header'larini tekshiruvchi oddiy vosita.

## Maqsadi

Sayt javobida `Content-Security-Policy`, `Strict-Transport-Security`, `X-Frame-Options` kabi muhim xavfsizlik header'lari bor-yo‘qligini va versiyani oshkor qiluvchi (`Server`, `X-Powered-By`) header'larni ko‘rsatadi. Recon va defensiv audit uchun.

## O‘rnatish

```bash
cd tools/web/header-check
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Foydalanish

```bash
python3 header_check.py <url>
python3 header_check.py https://example.com -t 5
```

## Example

```bash
$ python3 header_check.py https://example.com
[*] URL   : https://example.com/
[*] Status: 200

=== Xavfsizlik header'lari ===
[+] Strict-Transport-Security: bor
[-] Content-Security-Policy: YO‘Q  (XSS va injeksiyani cheklaydi)
...
[*] Yetishmayotgan xavfsizlik header'lari: 3/6
```

## Limitations

- Faqat bitta GET so‘rov yuboradi; header'lar sahifadan-sahifaga farq qilishi mumkin.
- Header borligini ko‘rsatadi, lekin uning **qiymati to‘g‘ri sozlanganini** chuqur tekshirmaydi.
- JavaScript orqali qo‘yiladigan sozlamalarni ko‘rmaydi.

## Security notes

- Vosita hech narsani o‘zgartirmaydi — faqat o‘qiydi (GET).
- Baribir faqat sinash huquqingiz bor saytlarda ishlating.
- Hech qanday credential yoki token saqlamaydi.
