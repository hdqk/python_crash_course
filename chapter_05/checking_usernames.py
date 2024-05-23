current_users = ['qan', 'scruffington', 'shea', 'deathcubek', 'Ushiki']
new_users = ['Scruffington', 'bees', 'big opa', 'ushiki', 'ages']
current_users = [user.lower() for user in current_users] #converts list to lower

for user in new_users:
    if user.lower() in current_users: #checks if the lowercase version of the username in new_users exists in current users
        print(f"{user} is taken. Please enter a different username.")
    else:
        print(f"{user} is available. Would you like to use {user}?")