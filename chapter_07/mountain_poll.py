responses = {}  # create an empty dictionary

# set flag to indicate that polling is active
polling_active = True

while polling_active:  # while polling_active remains True
    # prompt for the person's name nad response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # store the response in the empty dictionary we created
    # format is dictionary[key] = value
    responses[name] = response

    # find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no' or repeat == 'n':
        polling_active = False

# polling is complete, show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
