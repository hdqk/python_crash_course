# alien_0 = {'color': 'green', 'points': 5}
# # print(alien_0['color']) #retrieves value of given key
# # print(alien_0['points'])

# # print(f"You just earned {alien_0['points']} points!")

# print(alien_0)
# alien_0['x_pos'] = 0 #adds new key:pair values to dictionary
# alien_0['y-pos'] = 25
# print(alien_0)

# alien_0 = {}
# alien_0['color'] = 'green' #adding key:value pairs to an empty dictionary
# alien_0['points'] = 5
# print(alien_0)

# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")
# alien_0 = {'color': 'yellow'} #changing the value of a key:value pair
# print(f"The alien is {alien_0['color']}.")

# alien_0 = {'x-pos': 0, 'y-pos': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x-pos']}, {alien_0['y-pos']}.")
# #Move the alien to the right.
# #Determine how far to move the alien based on its current speed.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment= 2
# else:
#     x_increment = 3
# #The new position is the old position plus the increment.
# alien_0['x-pos'] = alien_0['x-pos'] + x_increment
# print(f"New position: {alien_0['x-pos']}, {alien_0['y-pos']}.")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points'] #removes a key:value pair
print(alien_0)