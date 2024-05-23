# Hector Delgado 5/10/2024

from pathlib import Path

print(f"{Path('learning_python.txt').read_text()}\n")

lines = Path('learning_python.txt').read_text().splitlines()
for line in lines:
    print(line)
