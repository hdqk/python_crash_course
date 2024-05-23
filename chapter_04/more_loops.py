my_foods = ['pizza', 'tacos', 'burgers']
friend_foods = my_foods[:]

my_foods.append('banana bread')
friend_foods.append('dulce de leche')

print(f"My favorite foods are:")
for food in my_foods:
    print(food)

print(f"\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)