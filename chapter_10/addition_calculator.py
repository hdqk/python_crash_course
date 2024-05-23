# Hector Delgado 5/13/24

print("To quit, enter 'q'.")

while True:
    print("\nProvide 2 numbers and I'll add them up: ")
    num1 = input("First number: ")
    if num1 == 'q':
        break
    num2 = input("Second number: ")
    if num2 == 'q':
        break
    try:
        print(int(num1) + int(num2))
    except ValueError:
        print("At least one of the values you entered was not a number.")
