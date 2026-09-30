# Linux Privilege Escalation — Checklist

Oddiy user shell olingandan keyin `root`ga ko‘tarilish uchun tekshiriladigan joylar. Faqat ruxsat berilgan lab / CTF muhitida.

> Odat: avval avtomatik enumeration (`linpeas.sh`), keyin natijani qo‘lda tekshirish.

## 1. Tizim haqida ma'lumot

```bash
id; whoami; hostname
uname -a; cat /etc/os-release      # kernel va distro versiyasi
cat /etc/passwd; cat /etc/group
```

## 2. `sudo` huquqlari

```bash
sudo -l
```

- Parolsiz ishga tushadigan buyruqlar bormi?
- Ruxsat berilgan buyruqni `root` sifatida boshqa amalga "aylantirib" bo‘ladimi? — [GTFOBins](https://gtfobins.github.io/) tekshiring.

## 3. SUID / SGID fayllar

```bash
find / -perm -4000 -type f 2>/dev/null      # SUID
find / -perm -2000 -type f 2>/dev/null      # SGID
```

Standart bo‘lmagan fayllarni [GTFOBins](https://gtfobins.github.io/) bilan solishtiring.

## 4. Capabilities

```bash
getcap -r / 2>/dev/null
```

`cap_setuid` kabi capability'lar ko‘tarilishga olib kelishi mumkin.

## 5. Cron ishlari

```bash
cat /etc/crontab
ls -la /etc/cron.*
```

- `root` ishga tushiradigan skript sizga yoziladiganmi?
- Skriptda to‘liq yo‘l ko‘rsatilmaganmi (PATH hijacking)?

## 6. Yoziladigan muhim fayllar

```bash
find / -writable -type f 2>/dev/null | grep -vE '^/proc|^/sys'
ls -la /etc/passwd /etc/shadow
```

## 7. Parol va kalitlar qidirish

```bash
grep -rniE 'password|passwd|secret' /var/www 2>/dev/null
ls -la ~/.ssh /root/.ssh 2>/dev/null
cat ~/.bash_history 2>/dev/null
```

> Config fayllardagi credential'lar ko‘pincha eng oson yo‘l.

## 8. Ishlab turgan servislar va portlar

```bash
ps aux
ss -tulpn
```

- `root` nomidan ishlaydigan zaif ichki servis bormi?
- Faqat `localhost` da ochilgan portlar (port forwarding orqali kirsa bo‘ladi)?

## 9. Kernel exploit (oxirgi chora)

`uname -r` bilan kernel versiyasini aniqlab, faqat lab muhitida, ma'lum va tekshirilgan exploit'lardan foydalaning. Real tizimlarda kernel exploit tizimni buzishi mumkin — ehtiyot bo‘ling.

## Foydali vositalar

- [linPEAS](https://github.com/peass-ng/PEASS-ng)
- [GTFOBins](https://gtfobins.github.io/)
- [LinEnum](https://github.com/rebootuser/LinEnum)

## Himoya nuqtai nazaridan

- Keraksiz SUID bit'larni olib tashlash
- `sudo` qoidalarini minimal qilish
- Cron skriptlariga to‘liq yo‘l va to‘g‘ri ruxsatlar
- Config fayllarda parol saqlamaslik
