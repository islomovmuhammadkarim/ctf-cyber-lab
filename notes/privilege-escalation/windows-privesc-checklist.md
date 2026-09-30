# Windows Privilege Escalation — Checklist

Windows'da past huquqli userdan yuqori huquqlarga ko‘tarilishda tekshiriladigan joylar. Faqat ruxsat berilgan lab / CTF muhitida.

> Odat: avval avtomatik enumeration (`winPEAS.exe` yoki `PowerUp.ps1`), keyin qo‘lda tekshirish.

## 1. Tizim va user haqida

```cmd
whoami /all
systeminfo
hostname
```

- `whoami /priv` — yoqilgan imtiyozlar (`SeImpersonatePrivilege` va h.k.).
- `systeminfo` — OS versiyasi va patch darajasi.

## 2. Foydalanuvchilar va guruhlar

```cmd
net user
net localgroup administrators
```

## 3. Ishlab turgan servislar

```cmd
wmic service get name,pathname,startmode
```

Tekshiriladigan zaifliklar:

- **Unquoted service path** — yo‘lda bo‘sh joy bor va tirnoqqa olinmagan.
- **Weak service permissions** — servisni o‘zgartirish huquqi bor (`accesschk`).
- **Writable binary** — servis ishlatadigan `.exe` sizga yoziladigan.

## 4. Muhim joylardagi credential'lar

```cmd
reg query HKLM /f password /t REG_SZ /s
dir /s *.config *.xml *.txt 2>nul | findstr /i pass
cmdkey /list
```

- Saqlangan RDP / Windows credential'lar
- `unattend.xml`, `sysprep.xml` fayllari
- PowerShell tarixi

## 5. Scheduled tasks

```cmd
schtasks /query /fo LIST /v
```

Yuqori huquq bilan ishga tushadigan, sizga yoziladigan skript bormi?

## 6. AlwaysInstallElevated

```cmd
reg query HKCU\Software\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\Software\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

Ikkalasi ham `0x1` bo‘lsa — MSI paketlari yuqori huquq bilan o‘rnatiladi.

## 7. Token impersonation

`SeImpersonatePrivilege` yoqilgan bo‘lsa (ko‘pincha servis akkauntlarida), "Potato" oilasidagi texnikalar orqali ko‘tarilish mumkin — faqat lab muhitida.

## Foydali vositalar

- [winPEAS](https://github.com/peass-ng/PEASS-ng)
- [PowerUp / PrivescCheck](https://github.com/itm4n/PrivescCheck)
- [accesschk (Sysinternals)](https://learn.microsoft.com/sysinternals/downloads/accesschk)

## Himoya nuqtai nazaridan

- Service path'larni tirnoqqa olish, ruxsatlarni cheklash
- `AlwaysInstallElevated` ni yoqmaslik
- Config va skript fayllarda parol saqlamaslik
- Least privilege: servislarga minimal huquq
