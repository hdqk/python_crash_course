prompt = "Please enter your age:"
prompt += "\n(When finished, enter 'exit'.) "

while True:
    age = input(prompt)
    if age == 'exit':
        break
    elif int(age) < 3:
        print("\nYour ticket is free!")
    elif int(age) >= 3 and int(age) <= 12:
        print("\nYour ticket is $10.")
    elif int(age) > 12:
        print("\nYour ticket is $15.")
