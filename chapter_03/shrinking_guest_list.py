guests = ['jesus', 'oppenheimer', 'john f. kennedy', 'elon musk', 'bill gates', 'warren buffet']

print(f"{guests[0].title()}, please join me for dinner tonight, details to follow.")
print(f"{guests[1].title()}, please join me for dinner tonight, details to follow.")
print(f"{guests[2].title()}, please join me for dinner tonight, details to follow.")
print(f"{guests[3].title()}, please join me for dinner tonight, details to follow.")
print(f"{guests[4].title()}, please join me for dinner tonight, details to follow.")
print(f"{guests[5].title()}, please join me for dinner tonight, details to follow.")

print(f"\nWe regret to inform you all that we will only have room for two guests tonight, sorry for any inconvenience.")

uninvited_guest = guests.pop(1)
print(f"\n{uninvited_guest.title()}, we regret to inform you that we do not have room for you at tonight's dinner.")
uninvited_guest = guests.pop(1)
print(f"{uninvited_guest.title()}, we regret to inform you that we do not have room for you at tonight's dinner.")
uninvited_guest = guests.pop(2)
print(f"{uninvited_guest.title()}, we regret to inform you that we do not have room for you at tonight's dinner.")
uninvited_guest = guests.pop(2)
print(f"{uninvited_guest.title()}, we regret to inform you that we do not have room for you at tonight's dinner.")

print(f"\n{guests[0].title()}, you are one of two people still invited to tonight's dinner.")
print(f"{guests[1].title()}, you are one of two people still invited to tonight's dinner.")

del guests[0]
del guests[0]

print(guests)