# Hector Delgado 5/14/24

from pathlib import Path
import json

path = Path('user_info.json')
user_info = {}

if path.exists():
    user_info = json.loads((path).read_text())
    print(f"Here's what I know about you:\n {user_info}.")
else:
    fav_num = input("What is your favorite number? ")
    user_info['fav_num'] = fav_num
    name = input("What is your name? ")
    user_info['name'] = name
    age = input("How old are you? ")
    user_info['age'] = age
    Path('user_info.json').write_text(json.dumps(user_info))
