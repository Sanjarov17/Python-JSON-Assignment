import json

with open("talabalar.json", "r", encoding="utf-8") as fayl:
    malumotlar = json.load(fayl)

katta_talabalar = [t for t in malumotlar if t["yosh"] > 20]

for t in katta_talabalar:
    print(f"{t['ism']} - {t['yosh']} yosh")
