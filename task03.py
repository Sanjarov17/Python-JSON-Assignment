import json

yangi_talaba = {"ism": "Shahzoda", "familiya": "Nazarova", "yosh": 22}

with open("talabalar.json", "r", encoding="utf-8") as fayl:
    malumotlar = json.load(fayl)

malumotlar.append(yangi_talaba)

with open("talabalar.json", "w", encoding="utf-8") as fayl:
    json.dump(malumotlar, fayl, indent=4, ensure_ascii=False)

print("✅ Yangi talaba qo‘shildi.")
