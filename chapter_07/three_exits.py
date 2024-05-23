# prompt = "Please enter a pizza topping:"
# prompt += "\n(When finished, enter 'exit'.) "

# active = True

# while active == True:
#     topping = input(prompt)
#     if topping == 'exit':
#         active = False
#     if topping != 'exit':
#         print(f"\nAdding {topping} to your pizza.")

prompt = "Please enter your age:"
prompt += "\n(When finished, enter 'exit'.) "
age = 0
while age != 'exit':
    age = input(prompt)
    if age == 'exit':
        continue
    if int(age) < 3:
        print("\nYour ticket is free!")
    elif int(age) >= 3 and int(age) <= 12:
        print("\nYour ticket is $10.")
    elif int(age) > 12:
        print("\nYour ticket is $15.")
