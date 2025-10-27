import json

with open("talabalar.json", "r", encoding="-8") as fayl:
    malumotlar = json.load(fayl)

for talaba in malumotlar:
    print(f"{talaba['ism']} - {talaba['yosh']} yosh")
