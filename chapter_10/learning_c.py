# Hector Delgado 5/10/2024

from pathlib import Path

lines = Path('learning_python.txt').read_text().splitlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line)
