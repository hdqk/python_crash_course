# Hector Delgado 5/13/24

from pathlib import Path


def count_words(path):
    """Count the approcimate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"Sorry, the file {path} does not exist.")
        pass
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = ['alice.txt', 'moby_dick.txt',
             'siddhartha.txt', 'little_women.txt']
for filename in filenames:
    count_words(Path(filename))
