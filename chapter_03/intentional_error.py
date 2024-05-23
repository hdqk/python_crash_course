languages = ['finnish', 'swahili', 'russian']
languages.append('english')
languages.insert(0, 'spanish')
languages.sort()
print(languages)
print(len(languages))
# print(languages[5]) #will cause an indexerror due to no 6th item
print(languages[-1])