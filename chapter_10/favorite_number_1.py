# Hector Delgado 5/14/24

from pathlib import Path
import json


fav_num = input("What is your favorite number? ")
Path('favorite_number.json').write_text(json.dumps(fav_num))
