import json
import csv

with open("talabalar.json", "r", encoding="utf-8") as fayl:
    malumotlar = json.load(fayl)

with open("talabalar.csv", "w", newline="", encoding="utf-8") as csv_fayl:
    yozuvchi = csv.DictWriter(csv_fayl, fieldnames=["ism", "familiya", "yosh"])
    yozuvchi.writeheader()
    yozuvchi.writerows(malumotlar)
