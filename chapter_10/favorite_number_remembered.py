# Hector Delgado 5/14/24

from pathlib import Path
import json

path = Path('favorite_number.json')

if path.exists():
    fav_num = json.loads((path).read_text())
    print(f"I know your favorite number! It's {fav_num}.")
else:
    fav_num = input("What is your favorite number? ")
    Path('favorite_number.json').write_text(json.dumps(fav_num))
