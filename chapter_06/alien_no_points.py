alien_0  ={'color': 'green', 'sped': 'slow'}

# print(alien_0['points']) #produces a KeyError because 'points' doesn't exist
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)