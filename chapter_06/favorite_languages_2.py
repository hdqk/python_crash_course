favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# friends = ['phil', 'sarah']
# for name, language in favorite_languages.items():
#     print(f"Hi {name.title()}.")
#     if name in friends:
#         print(f"\t{name.title()}, I see you love {language.title()}!")
# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# for name in sorted(favorite_languages.keys()): #will sort the dictionary alphabetically before looping
#     print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): #set() removes duplicates and a set must contain only unique items
    print({language.title()})