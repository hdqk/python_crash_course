# age = input("How old are you? ")
# print(age)
# print(age >= 18) #will produce a typeerror because the user input is a str

age = input("How old are you? ")
age = int(age)
print(age >= 18)  # will produce a typeerror because the user input is a str
