guests = ['jesus', 'oppenheimer', 'john f. kennedy']
print(f"I'd be honored if you'd join me for dinner tonight {guests[0].title()}.")
print(f"Mr. {guests[1].title()}, please be my guest of honor for dinner tonight.")
print(f"It would delight me if you, {guests[2].title()}, would join me for dinner tonight.")

print(f"\nEsteemed guests, we were able to secure a larger table for tonight's dinner. More guests will be joining us.\n")

guests.insert(0, 'elon musk')
guests.insert(2, 'bill gates')
guests.append('warren buffet')

print(f"{guests[0].title()}, please join me for dinner tonight, details to follow.")
print(f"{guests[1].title()}, please join me for dinner tonight, details to follow.")
print(f"{guests[2].title()}, please join me for dinner tonight, details to follow.")
print(f"{guests[3].title()}, please join me for dinner tonight, details to follow.")
print(f"{guests[4].title()}, please join me for dinner tonight, details to follow.")
print(f"{guests[5].title()}, please join me for dinner tonight, details to follow.")