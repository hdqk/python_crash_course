cities = {
    'paris': {
        'country': 'france',
        'population': '2.16 million',
        'fact': "has the world's biggest art museum",
    },
    'boston': {
        'country': 'the united states',
        'population': '650,000',
        'fact': "built America's first subway in 1897",
    },
    'dubai': {
        'country': 'united arab emirates',
        'population': '3.33 million',
        'fact': "has the world's tallest building",
    },
}

for city, info in cities.items():
    print(f"{city.title()} is located in {info['country'].title()} and has a \
population of approximately {info['population']}. It {info['fact']}.\n")
