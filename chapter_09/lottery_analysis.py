# Hector Delgado 5/9/2024

import random

my_ticket = ['a', '2', 'c', '4']
lottery = ('a', 'b', 'c', 'd', 'e',
           '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
result = random.choices(lottery, k=len(my_ticket))
tries = 1

while result != my_ticket:
    result = random.choices(lottery, k=len(my_ticket))
    tries += 1

if tries == 1:
    print(f"It only took you {tries} try to win the lottery!")
else:
    print(f"It took you {tries} tries to win the lottery!")


# another version that uses range() to generate a list of numbers
# import random

# my_ticket = [1, 2, 3, 4, 5, 6]
# lottery = list(range(0, 32))
# result = random.choices(lottery, k=len(my_ticket))
# tries = 1

# while result != my_ticket:
    # result = random.choices(lottery, k=len(my_ticket))
#     tries += 1

# if tries == 1:
#     print(f"It only took you {tries} try to win the lottery!")
# else:
#     print(f"It took you {tries} tries to win the lottery!")
