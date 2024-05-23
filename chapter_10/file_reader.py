# Hector Delgado 5/10/2024

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

# print(Path('pi_digits.txt').read_text())
# #another way to do the same operation

lines = contents.splitlines()
for line in lines:
    print(line)
