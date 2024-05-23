pizzas = ['deep dish', 'brooklyn', 'thin crust', 'stuffed crust']
friend_pizzas = pizzas[:]

pizzas.append('detroit')
friend_pizzas.append('sicilian')

print(f"My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print(f"My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
