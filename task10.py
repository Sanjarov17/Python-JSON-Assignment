import json

with open("talabalar.json", "r", encoding="utf-8") as fayl:
    malumotlar = json.load(fayl)

tartiblangan_talabalar = sorted(malumotlar, key=lambda t: t["yosh"])

for t in tartiblangan_talabalar:
    print(f"{t['ism']} - {t['yosh']} yosh")
