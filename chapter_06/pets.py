meiko = {
    'species': 'cat',
    'owner': 'hector',
}
lacey = {
    'species': 'dog',
    'owner': 'ricky',
}
tony = {
    'species': 'turtle',
    'owner': 'junior',
}

pets = [meiko, lacey, tony]

for pet in pets[:]:
    print(f"{pet['owner'].title()} has a {pet['species']}!\n")
