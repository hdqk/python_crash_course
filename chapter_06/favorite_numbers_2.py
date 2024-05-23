favorite_numbers = {
    'nicole': [7, 11],
    'hector': [3, 6, 12, 24],
    'lisa': [3],
    'monica': [20, 42],
    'duper': [31],
}

for person, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"\n{person.title()}'s favorite number is:")
    else:
        print(f"\n{person.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
