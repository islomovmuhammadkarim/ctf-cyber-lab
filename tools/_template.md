# <Tool nomi>

<!--
  Shablondan foydalanish:
  1. Papka yarating: tools/<kategoriya>/<tool-nomi>/
  2. Bu faylni o‘sha papkaga README.md sifatida nusxalang va to‘ldiring.
  3. Python bo‘lsa, requirements.txt ga faqat haqiqatan kerakli paketlarni yozing (versiya bilan).
  4. API key / token kodga yozilmaydi — environment variable yoki .env orqali o‘qiladi.
-->

> <Bir gapda: tool nima qiladi.>

## Maqsadi

<Qanday muammoni hal qiladi, qachon ishlatiladi.>

## O‘rnatish

```bash
cd tools/<kategoriya>/<tool-nomi>
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Foydalanish

```bash
python3 <tool-nomi>.py --help
```

| Argument        | Tavsif         | Default |
| --------------- | -------------- | ------- |
| `-t, --target`  | <tavsif>       | —       |

## Example

```bash
python3 <tool-nomi>.py -t 10.10.x.x
```

```text
<namunaviy output — real target ma'lumotlarisiz>
```

## Limitations

- <Nimani qila olmaydi, ma'lum muammolar.>

## Security notes

- Faqat ruxsat berilgan target'larda ishlating.
- <Tool qanday maxfiy ma'lumotlar bilan ishlaydi va ular qayerda saqlanadi.>
