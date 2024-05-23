car = 'toyota'
print("Is car == 'toyota'? I predict True.")
print(car == 'toyota')
print("\nIs car == 'subaru'? I predict False.")
print(car == 'subaru')
print("\nIs car != 'bmw'? I predict True.")
print(car != 'bmw')

toppings = ['pineapple', 'bacon', 'onions']
print("\nIs pepperoni one of the toppings? I predict False.")
print('pepperoni' in toppings)
print("\nIs pineapple one of the toppings? I predict True.")
print('pineapple' in toppings)
print("\nIs bacon not one of the toppings? I predict False.")
print('bacon' not in toppings)

age1, age2 = 18, 22
print("\nAre both people at least 21 years old? I predict False.")
print(age1 >= 21 and age2 >= 21)
print("\nIs either one over the age of 21? I predict True.")
print(age1 >= 21 or age2 >= 21)
print("\nAre they both over 18? I predict True.")
print(age1 >= 18 and age2 >= 18)

name = 'mike'
print("\nIs name == 'mike'? I predict True.")
print(name == 'mike')
print("\nIs name == 'Mike'? I predict False.")
print(name == 'Mike')
print("\nIs name == 'mike' in titlecase? I predict True.")
print(name.title() == 'Mike')