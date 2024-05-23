favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

new_people = ['mike', 'sarah', 'erin', 'jen']

for name in new_people:
    if name in favorite_languages.keys():
        print(f"Thank you for for responding to the poll, {name.title()}.")
    else:
        print(f"Please click the link below to take the poll {name.title()}.")

