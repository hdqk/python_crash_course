favorite_places = {
    'hector': ['boston', 'japan', 'finland'],
    'ricky': ['santo domingo'],
    'nicole': ['medellin', 'santo domingo'],
}

favorites = []

for person, locations in favorite_places.items():
    if len(locations) == 1:
        print(f"\n{person.title()}'s favorite place is:")
    else:
        print(f"\n{person.title()}'s favorite places are:")
    for location in locations:
        favorites.append(location)
        print(f"\t{location.title()}")

print(f"\nThese are all of the favorite places listed:")
unique_favorites = set(favorites)
for item in unique_favorites:
    print(f"\t{item.title()}")
