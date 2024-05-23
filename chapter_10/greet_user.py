# Hector Delgado 5/14/24

from pathlib import Path
import json

path = Path('username.json')
contents = path.read_text()
username = json.loads(contents)

# username = json.loads(Path('username.json').read_text())
# Another way to write the code above

print(f"Welcome back, {username.title()}!")
