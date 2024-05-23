# Hector Delgado 5/13/24

print("Provide 2 numbers and I'll add them up: ")
num1 = input("First number: ")
num2 = input("Second number: ")

try:
    print(int(num1) + int(num2))
except ValueError:
    print("At least one of the values you entered was not a number.")
