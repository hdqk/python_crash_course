# Hector Delgado 5/13/24

from pathlib import Path

books = ['frankenstein.txt', 'pride_and_prejudice.txt', 'romeo_and_juliet.txt']

for book in books:
    words = Path(book).read_text(encoding='utf-8').lower().count('the')
    print(f"{book} has {words} occurences of 'the'")
