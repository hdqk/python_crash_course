favorite_fruits = ['strawberry', 'mango', 'banana']
all_fruits = favorite_fruits[:]
all_fruits.append('grape')
all_fruits.append('apple')

if 'strawberry' in favorite_fruits:
    print(f"You really like strawberries!")
if 'apple' in favorite_fruits:
    print(f"You really like apples!")
if 'mango' in favorite_fruits:
    print(f"You really like mangos!")
if 'grape' in favorite_fruits:
    print(f"You really like grapes!")
if 'banana' in favorite_fruits:
    print(f"You really like bananas!")

for fruit in all_fruits:
    if fruit in favorite_fruits:
        print(f"You really like {fruit}!")
    else:
        print(f"{fruit.title()} is not one of your favorite fruits.")