import json
import os

if not os.path.exists("talabalar.json"):
    with open("talabalar.json", "w", encoding="utf-8") as fayl:
        json.dump([], fayl, indent=4, ensure_ascii=False)
else:
    print("Fayl allaqachon mavjud.")
