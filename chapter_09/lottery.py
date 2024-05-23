# Hector Delgado 5/9/2024

from random import choices

lottery = ('a', 'b', 'c', 'd', 'e',
           '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

print(f"Any ticket matching these 4 numbers or letters wins a prize!"
      f"\n{choices(lottery, k=4)}")
