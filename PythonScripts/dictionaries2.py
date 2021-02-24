enemy = {
    'loc_x':     30,
    'loc_y':     40,
    'color':     'green',
    'health':    200,
    'name':      'Vasia',
    'image':     ['1.jpg', '2.jpg', '3.jpg']
}

#create dictionaries with array

all_enemies = []  #array

for x in range(0, 5):
    all_enemies.append(enemy) #copy from the same dictonary, copy

for y in all_enemies: #print result in different lines
    print(y)
print('-----------------')
#create dictionaries with array

all_enemies = []  #array

for x in range(0, 5):
    all_enemies.append(enemy.copy()) #copy from the next dictonary, copy

all_enemies[3] ['health'] = 50
all_enemies[1] ['loc_y'] += 10 #the same value +10
for y in all_enemies: #print result in different lines
    print(y)