# Hector Delgado 5/13/24

from pathlib import Path

try:
    cats = Path('cats.txt').read_text().splitlines()
    dogs = Path('dogs.txt').read_text().splitlines()
except FileNotFoundError:
    pass
else:
    for cat in cats:
        print(f"\n{cat}")
    for dog in dogs:
        print(f"\n{dog}")
