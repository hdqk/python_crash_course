# Hector Delgado 5/10/2024

from pathlib import Path

for line in Path('learning_python.txt').read_text().splitlines():
    line = line.replace('Python', 'C')
    print(line)
