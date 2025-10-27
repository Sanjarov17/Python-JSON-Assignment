import json

with open("talabalar.json", "r", encoding="utf-8") as fayl:
    malumotlar = json.load(fayl)

ortalacha_yosh = sum(t["yosh"] for t in malumotlar) / len(malumotlar)
print(ortalacha_yosh)
