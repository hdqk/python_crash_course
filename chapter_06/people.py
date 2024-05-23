people = {
    'nfont': {
        'first': 'nicole',
        'last': 'font',
        'age': 25,
        'location': 'santo domingo',
    },
    'lfont': {
        'first': 'lisa',
        'last': 'font',
        'age': 24,
        'location': 'santo domingo',
    },
    'mteixeira': {
        'first': 'monica',
        'last': 'texeira',
        'age': 26,
        'location': 'boston',
    },
}

for person, info in people.items():
    print(f"{info['first'].title()} {info['last'].title()} is \
{info['age']} years old and lives in {info['location'].title()}.\n")
