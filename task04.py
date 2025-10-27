import json
import os

if not os.path.exists("talabalar.json"):
    with open("talabalar.json", "w", encoding="utf-8") as fayl:
        json.dump([], fayl)

ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")
yosh = int(input("Yoshingizni kiriting: "))

with open("talabalar.json", "r", encoding="utf-8") as fayl:
    malumotlar = json.load(fayl)

malumotlar.append({"ism": ism, "familiya": familiya, "yosh": yosh})

with open("talabalar.json", "w", encoding="utf-8") as fayl:
    json.dump(malumotlar, fayl, indent=4, ensure_ascii=False)

print("Malumot faylga qoshildi.")
