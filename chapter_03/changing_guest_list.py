guests = ['jesus', 'oppenheimer', 'jfk']
print(f"I'd be honored if you'd join me for dinner tonight {guests[0].title()}.")
print(f"Mr. {guests[1].title()}, please be my guest of honor for dinner tonight.")
print(f"It would delight me if you, {guests[2].upper()}, would join me for dinner tonight.")

print(f"\n{guests[2].upper()} has declined the dinner invitation.\n")
guests[2] = 'elon musk'

print(f"I'd be honored if you'd join me for dinner tonight {guests[0].title()}.")
print(f"Mr. {guests[1].title()}, please be my guest of honor for dinner tonight.")
print(f"It would delight me if you, {guests[2].title()}, would join me for dinner tonight.")