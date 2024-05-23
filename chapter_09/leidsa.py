# Hector Delgado 5/10/2024
# A simulation of the LEIDSA (Lotería Electrónica Internacional Dominicana S.A.)

import random

my_ticket = [1, 2, 3, 4, 5, 6, 7, 8]
lottery = list(range(1, 9))  # true value is 1-40
super = list(range(1, 9))  # true value is 1-12
result = random.sample(lottery, 6) + random.sample(super, 2)
tries = 1

while result != my_ticket:
    result = random.sample(lottery, 6) + random.sample(super, 2)
    tries += 1

if tries == 1:
    print(f"It only took you {tries} try to win the lottery!")
else:
    print(f"It took you {tries} tries to win the lottery!")
