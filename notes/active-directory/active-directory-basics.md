# Active Directory — Asoslar

Active Directory (AD) — Windows domenlarida foydalanuvchi, kompyuter va resurslarni markazlashgan boshqarish tizimi. Pentest'da tez-tez uchraydi.

> Faqat ruxsat berilgan lab muhitida (masalan, o‘zingiz ko‘targan domen yoki HackTheBox/TryHackMe AD lablari).

## Asosiy tushunchalar

| Termin              | Ma'nosi                                                        |
| ------------------- | -------------------------------------------------------------- |
| Domain              | Ob'ektlar (user, kompyuter) guruhi, bitta ma'muriyat ostida    |
| Domain Controller (DC) | AD ma'lumotlar bazasini yurituvchi server                   |
| Forest              | Bir yoki bir nechta domenning eng yuqori to‘plami              |
| OU (Organizational Unit) | Ob'ektlarni tartiblash uchun konteyner                    |
| GPO (Group Policy Object) | Domen bo‘ylab sozlamalarni qo‘llash                       |
| LDAP                | AD'ga so‘rov yuborish protokoli (389/636)                      |
| Kerberos            | AD'ning asosiy autentifikatsiya protokoli (88)                 |

## Kerberos qisqacha

1. User paroli asosida DC'dan **TGT** (Ticket Granting Ticket) oladi.
2. TGT bilan aniq servis uchun **TGS** (Service Ticket) so‘raydi.
3. TGS'ni servisga ko‘rsatib kiradi.

Bu jarayondagi ba'zi zaif nuqtalar pentest'da o‘rganiladi (quyida).

## Enumeration (ruxsat berilgan muhitda)

```bash
# Domen va userlar (kirish huquqi bilan)
enum4linux -a <DC_IP>
# LDAP orqali
ldapsearch -x -H ldap://<DC_IP> -b "dc=example,dc=com"
```

`BloodHound` + `SharpHound` — AD'dagi huquq munosabatlarini grafik ko‘rinishda ko‘rsatadi va hujum yo‘llarini topadi.

## Ko‘p uchraydigan hujum kontseptsiyalari (yuqori daraja)

| Nomi                | G‘oyasi (qisqacha)                                                   |
| ------------------- | -------------------------------------------------------------------- |
| Kerberoasting       | Servis akkaunt ticketlarini olib, offline parol tekshirish           |
| AS-REP Roasting     | Pre-auth talab qilinmaydigan akkauntlardan foydalanish               |
| Pass-the-Hash       | Parol o‘rniga NTLM hash bilan autentifikatsiya                       |
| Pass-the-Ticket     | O‘g‘irlangan Kerberos ticket bilan kirish                            |
| ACL abuse           | Ob'ektlar ustidagi noto‘g‘ri huquqlardan foydalanish                 |

> Bu yerda maqsad — mexanizmni tushunish. Aniq bajarish qadamlari mos lab darsliklarida (masalan TryHackMe AD yo‘nalishi) beriladi.

## Foydali vositalar

- [BloodHound](https://github.com/BloodHoundAD/BloodHound)
- [Impacket](https://github.com/fortra/impacket)
- [CrackMapExec / NetExec](https://github.com/Pennyw0rth/NetExec)

## Himoya nuqtai nazaridan

- Servis akkauntlarга kuchli, uzun parollar (Kerberoasting'ni qiyinlashtiradi)
- Least privilege va muntazam ACL audit
- LAPS bilan local administrator parollarини boshqarish
- Monitoring: g‘ayrioddiy ticket so‘rovlarini kuzatish
