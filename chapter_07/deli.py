# make list and fill it with various sandwiches
sandwich_orders = ['italian', 'cheese steak', 'hoagie', 'pastrami']
# make empty list called finished_sandwiches
finished_sandwiches = []

# loop through the list of sandwich orders and print a message for each order
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nThese are the sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")
