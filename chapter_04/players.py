players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print(players[0:3]) #from 1st to 3rd
# print(players[1:4]) #from 2nd to 4th
# print(players[:4]) #from 1st to 3rd
# print(players[2:]) #from #3 to the end
# print(players[-3:]) #last 3

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())