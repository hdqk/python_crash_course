# Hector Delgado 5/20/2024

from pathlib import Path

names = ''

name = input("Please enter your name: ")
print("If you are the last user, enter 'exit' to terminate the program.")

while name != 'exit':
    name = input("Please enter your name: ")
    names += f"{name}\n"

Path('guest_book.txt').write_text(f"{names}")
