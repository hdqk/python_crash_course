# Hector Delgado 5/14/24

from pathlib import Path
import json


fav_num = json.loads(Path('favorite_number.json').read_text())
print(f"I know your favorite number! It's {fav_num}.")
