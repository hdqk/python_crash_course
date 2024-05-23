rivers = {
    'nile': 'egypt',
    'euphrates': 'turkey',
    'mississippi': 'the united states',
}

for key,value in rivers.items():
    print(f"The {key.title()} river runs through {value.title()}.")

for key in rivers.keys():
    print({key})

for value in rivers.values():
    print({value})
    