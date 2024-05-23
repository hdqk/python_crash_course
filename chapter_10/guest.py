# Hector Delgado 5/20/2024

from pathlib import Path

name = input("Please enter your name: ")

Path('guest.txt').write_text(f"{name}")
