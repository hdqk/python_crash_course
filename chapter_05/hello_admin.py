usernames = ['qan', 'scruffington', 'shea', 'deathcubek', 'ushiki', 'admin']

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username.title()}, would you like to see a status report?")
        else:
            print(f"Greetings {username.title()}, welcome back!")
else:
    print("We need to find some users!")
