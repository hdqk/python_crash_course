# make list and fill it with various sandwiches
sandwich_orders = ['italian', 'pastrami', 'cheese steak', 'pastrami',
                   'hoagie', 'pastrami']
# make empty list called finished_sandwiches
finished_sandwiches = []

print("The deli has run out of pastrami!")

# remove any instances of 'pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# loop through the list of sandwich orders and print a message for each order
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

# print a message listing all the sandwiches that have been made
print("\nThese are the sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")
