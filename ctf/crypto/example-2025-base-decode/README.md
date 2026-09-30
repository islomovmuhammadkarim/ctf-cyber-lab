# Base Decode (namuna)

<!-- To‘ldirilgan NAMUNA. Real flag yo‘q — hammasi placeholder. -->

| Maydon         | Qiymat                          |
| -------------- | ------------------------------- |
| **Challenge**  | Base Decode                     |
| **Category**   | Crypto                          |
| **Platform**   | Example CTF                     |
| **Difficulty** | Easy                            |
| **Objective**  | Berilgan kodlangan matndan flag'ni chiqarish |
| **Tags**       | encoding, base64, base32        |

## TL;DR

Berilgan matn bir necha marta Base64 va Base32 bilan kodlangan edi. Qatlamma-qatlam
dekod qilib flag olindi.

## 1. Berilgan ma'lumot

`cipher.txt` faylida uzun, faqat `A-Z2-7=` belgilaridan iborat matn (Base32 belgisi).

## 2. Analysis

- Faqat katta harf va `2-7` raqamlar + `=` → bu **Base32**.
- Dekod qilingach, `A-Za-z0-9+/=` chiqdi → keyingi qatlam **Base64**.

## 3. Solution

```bash
# Bir qatlam Base32, keyin Base64
base32 -d cipher.txt | base64 -d
```

Yoki Python bilan (yechim skripti: `solve.py`):

```bash
python3 solve.py
```

## 4. Flag

```text
flag{REDACTED}
```

## 5. Lessons Learned

- Belgilar to‘plamiga qarab encoding turini aniqlash mumkin:
  - `A-Z2-7=` → Base32
  - `A-Za-z0-9+/=` → Base64
  - `0-9a-f` → hex
- [CyberChef](https://gchq.github.io/CyberChef/) ning "Magic" funksiyasi encoding'ni avtomatik taxmin qiladi.
