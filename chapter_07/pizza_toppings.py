prompt = "Please enter a pizza topping:"
prompt += "\n(When finished, enter 'exit'.) "

while True:
    topping = input(prompt)
    if topping == 'exit':
        break
    print(f"\nAdding {topping} to your pizza.")
