import json

with open("talabalar.json", "r", encoding="utf-8") as fayl:
    malumotlar = json.load(fayl)

eng_katta_talaba = max(malumotlar, key=lambda t: t["yosh"])
print(f"{eng_katta_talaba['ism']} - {eng_katta_talaba['yosh']} yosh")
