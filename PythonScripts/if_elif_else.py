#if else operators

x = 15

if x == 15:
    print("correct")
else:
    print("not correct")

#if elif(else if)

age = 500

if (age > 0) and (age <= 4):
    print("baby")
elif (age > 4) and (age <= 10):
    print("child")
elif (age > 10) and (age <= 20):
    print("teenager")
elif (age >20) and (age < 100):
    print("adult")
else:
    print("incorrect number")

#searching and comparison between 2 arrays

cars = ['bmw', 'mercedes', 'seat', 'ziguli', 'suzuki', 'skoda']
german_cars = ['bmw', 'mercedes']

for x in cars:
    if x in german_cars:
        print(x + " is german car")
    else:
        print(x + " is NOT german car")