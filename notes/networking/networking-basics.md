# Networking Basics

## OSI va TCP/IP modeli

| # | OSI qatlami   | TCP/IP       | Misol protokollar            | Qurilma / tushuncha |
| - | ------------- | ------------ | ---------------------------- | ------------------- |
| 7 | Application   | Application  | HTTP, DNS, FTP, SMTP, SSH    | —                   |
| 6 | Presentation  | Application  | TLS, encoding                | —                   |
| 5 | Session       | Application  | NetBIOS, RPC                 | —                   |
| 4 | Transport     | Transport    | TCP, UDP                     | Port                |
| 3 | Network       | Internet     | IP, ICMP                     | Router, IP manzil   |
| 2 | Data Link     | Link         | Ethernet, ARP                | Switch, MAC manzil  |
| 1 | Physical      | Link         | Kabel, Wi-Fi signal          | Hub                 |

## TCP va UDP

| TCP                                         | UDP                                   |
| ------------------------------------------- | ------------------------------------- |
| Ulanishga asoslangan (3-way handshake)      | Ulanishsiz                            |
| Ishonchli, tartib kafolatlangan             | Tez, lekin kafolatsiz                 |
| HTTP, SSH, FTP, SMB                         | DNS, DHCP, SNMP, TFTP                 |

**3-way handshake:** `SYN` → `SYN-ACK` → `ACK`.
Nmap `-sS` (SYN scan) handshake'ni oxirigacha yakunlamaydi — shuning uchun tezroq.

## Muhim portlar

| Port        | Servis        | Port   | Servis          |
| ----------- | ------------- | ------ | --------------- |
| 20/21       | FTP           | 389    | LDAP            |
| 22          | SSH           | 443    | HTTPS           |
| 23          | Telnet        | 445    | SMB             |
| 25          | SMTP          | 636    | LDAPS           |
| 53          | DNS           | 1433   | MSSQL           |
| 80          | HTTP          | 3306   | MySQL           |
| 88          | Kerberos      | 3389   | RDP             |
| 110         | POP3          | 5432   | PostgreSQL      |
| 111         | RPCbind       | 5985   | WinRM (HTTP)    |
| 135         | MSRPC         | 6379   | Redis           |
| 139         | NetBIOS       | 8080   | HTTP alternativ |
| 143         | IMAP          | 27017  | MongoDB         |
| 161 (UDP)   | SNMP          |        |                 |

## IP manzillar va subnetting

Private diapazonlar (RFC 1918):

- `10.0.0.0/8`
- `172.16.0.0/12`
- `192.168.0.0/16`

| CIDR | Subnet mask       | Host soni |
| ---- | ----------------- | --------- |
| /24  | 255.255.255.0     | 254       |
| /25  | 255.255.255.128   | 126       |
| /26  | 255.255.255.192   | 62        |
| /27  | 255.255.255.224   | 30        |
| /28  | 255.255.255.240   | 14        |
| /30  | 255.255.255.252   | 2         |

Formula: host soni = 2^(32 − CIDR) − 2.

## DNS

| Yozuv  | Vazifasi                          |
| ------ | --------------------------------- |
| A      | Domain → IPv4                     |
| AAAA   | Domain → IPv6                     |
| CNAME  | Domain → boshqa domain (alias)    |
| MX     | Pochta serveri                    |
| TXT    | Matn (SPF, verification, ba'zan flag 🙂) |
| NS     | Name server                       |
| PTR    | IP → domain (reverse)             |

```bash
dig <domain> ANY
dig axfr <domain> @<nameserver>     # zone transfer
nslookup <domain>
host -t mx <domain>
```

## Foydali vositalar

| Vosita       | Vazifasi                                   |
| ------------ | ------------------------------------------ |
| `nmap`       | Port va servis scan                        |
| `wireshark`  | Trafikni grafik tahlil qilish              |
| `tcpdump`    | CLI orqali trafik yozib olish              |
| `netcat`     | TCP/UDP ulanish, listener                  |
| `traceroute` | Paket yo‘lini ko‘rish                      |

```bash
sudo tcpdump -i eth0 -w capture.pcap port 80
```
