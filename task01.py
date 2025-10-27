import json

talabalar = [
    {"ism": "Ali", "familiya": "Valiyev", "yosh": 20},
    {"ism": "Laylo", "familiya": "Karimova", "yosh": 21},
    {"ism": "Bekzod", "familiya": "Xolmatov", "yosh": 19}
]

with open("talabalar.json", "w", encoding="utf-8") as fayl:
    json.dump(talabalar, fayl, indent=4, ensure_ascii=False)

print("✅ talabalar.json fayliga yozildi.")
