motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati' #replaces 'honda' with 'ducati'
# print(motorcycles)

# motorcycles.append('ducati') #appends 'ducati' to the end of the list
# print(motorcycles)

# motorcycles = [] #starts with an empty list
# motorcycles.append('honda') #adds items to the list
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

# motorcycles.insert(0, 'ducati') #inserts an item at the desired index
# print(motorcycles)

# del motorcycles[0] #deletes the item at the given index
# del motorcycles[1] #deletes the item at the given index
# print(motorcycles)

# popped_motorcycle = motorcycles.pop() #removes the last item in the list and assigns it to a new variable
# print(motorcycles)
# print(popped_motorcycle)

# last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}.")

# first_owned = motorcycles.pop(0) #pops an item from the list at given index
# print(f"The first motorcycle I owned was a {first_owned.title()}.")

# motorcycles.append('ducati')
# print(motorcycles)
# motorcycles.remove('ducati') #removes an item based on it's value
# print(motorcycles)


motorcycles.append('ducati')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")