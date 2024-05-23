# Hector Delgado 5/13/24

from pathlib import Path

try:
    cats = Path('cats.txt').read_text().splitlines()
    dogs = Path('dogs.txt').read_text().splitlines()
except FileNotFoundError:
    print("At least one of the files was not found.")
else:
    for cat in cats:
        print(f"\n{cat}")
    for dog in dogs:
        print(f"\n{dog}")
