#create the dictionary (like object)

#         item
#     key        value
enemy = {
    'loc_x':     30,
    'loc_y':     40,
    'color':     'green',
    'health':    200,
    'name':      'Vasia',
}
#print necessary informations from the dictionary
print('location x: ' + str(enemy['loc_x']))
print('location y: ' + str(enemy['loc_y']))
print('Name is: ' + enemy['name'])

#add new parameters into the dictionary and delete it
enemy['level'] = 'General'

del enemy['level']

#change parameters int the dictionary

enemy['loc_x'] = enemy['loc_x'] + 35
enemy['health'] = enemy['health'] - 55
if enemy['health'] < 150:
    enemy['color'] = 'yellow'

print(enemy)

#print keys and values in different rows
print(enemy.keys())
print(enemy.values())
