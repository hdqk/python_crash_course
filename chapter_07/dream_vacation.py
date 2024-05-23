locations = []

vacation_prompt = "If you could visit one place in the world, "
vacation_prompt += "where would you go? "

polling_active = True

while polling_active:
    vacation = input(vacation_prompt)
    locations.append(vacation)
    end_polling = input("Would anyone else like to answer? (y/n)")
    if end_polling == 'n' or end_polling == 'no':
        polling_active = False

print("These are the dream vacation spots submitted: ")
for location in locations:
    print(f"\t{location.title()}")
