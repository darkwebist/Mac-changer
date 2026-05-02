# MAC Changer

Ushbu Python skripti Linux tizimlarida tarmoq interfeysi (Wi-Fi yoki Ethernet) MAC manzilini vaqtincha o‘zgartirish imkonini beradi.

## O‘rnatish

Skriptni o‘rnatish va ishlatish uchun quyidagi amallarni bajaring:

1. **Repositoriyani klon qiling:**
   ```bash
   git clone https://github.com/darkwebist/Mac-changer.git
   ```

1. Loyiha papkasiga o‘ting:
   ```bash
   cd Mac-changer
   ```
2. Skriptni bajariladigan qilib belgilang:
   ```bash
   chmod +x mac_changer.py
   ```

## Ishlatish

MAC manzilni o‘zgartirish uchun skriptni sudo huquqi bilan ishga tushiring va interfeys hamda yangi MAC manzilni ko‘rsating.

```bash
sudo python3 mac_changer.py -i <interfeys> -m <yangi_mac>
```

Misol:

```bash
sudo python3 mac_changer.py -i eth0 -m 02:11:22:33:44:55
```

Majburiy argumentlar:

 · -i yoki --interface: Tarmoq interfeysi nomi (masalan, eth0, wlan0)
 · -m yoki --mac: Yangi MAC manzil (format: XX:XX:XX:XX:XX:XX)

## Talablar

 · Linux operatsion tizimi
 · Python 3.6 yoki undan yangisi
 · ip buyrug‘i (odatda iproute2 paketi tarkibida)
 · sudo huquqi (MAC manzilni o‘zgartirish uchun zarur)

## Muhim eslatmalar

 · Skript faqat sudo bilan ishga tushirilishi kerak.
 · MAC manzil o‘zgarishi vaqtinchalik – tizim qayta yuklanganda zavod manzili qaytadi.
 · Yaroqsiz MAC manzillarni (masalan 00:00:00:00:00:00) ishlatmang. Xavfsiz misol: 02:11:22:33:44:55.

## Muallif

@DarkWebist
