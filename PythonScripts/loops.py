#print x loopimg from 0 to 100

for x in range(0, 100):
    print(x)

#print x loopimg from 0 to 100 with step = 5

for x in range (10, 100, 5):
    print(x)

#print x looping in string type
for x in range (-110, 10, 5):
    print("number x =", str(x))

#print x looping in string type with break condition
for x in range (110, 10, -5):
    print("x =", str(x))
    if x == 50:
        break

#print x looping forever, with break condition (without end condition looping)

x = 0

while True:
    x = x + 1
    print(x)

    if x == 50:
        break

