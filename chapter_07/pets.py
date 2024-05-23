pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:  # removes one instance of cat until there are no more
    pets.remove('cat')
# when there are no more instances of 'cat' inside, the loop exits
print(pets)
