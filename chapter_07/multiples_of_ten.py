number = int(
    input("Choose a number and I will tell you if it's a multiple of 10: "))

if number % 10 == 0:
    print(f"\n{number} is a multiple of 10.")
else:
    print(f"\n{number} is not a multiple of 10.")
