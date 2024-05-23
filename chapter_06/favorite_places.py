favorite_places = {
    'hector': ['boston', 'japan', 'finland'],
    'ricky': ['santo domingo'],
    'nicole': ['medellin', 'santo domingo'],
}

for person, locations in favorite_places.items():
    if len(locations) == 1:
        print(f"\n{person.title()}'s favorite place is:")
    else:
        print(f"\n{person.title()}'s favorite places are:")
    for location in locations:
        print(f"\t{location.title()}")
