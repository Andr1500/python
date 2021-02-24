cars = ['bmw', 'mercedes', 'seat', 'ziguli', 'skoda']

# print from the list with loops
for car in cars:
    print(car.upper())

my_list = list(range(0, 10))
print(my_list)
print("___________")

for x in my_list:
    x = x * 2
    print(x)

#sorting array from the end to the begin
my_list.sort(reverse=True)
print(my_list)

#max , min , sum from the array
print("max number is " + str(max(my_list)))

print("min number is " + str(min(my_list)))

print("sum from my list is " + str(sum(my_list)))

print("---------------")
#cat the piece of the array
# pos.    0        1          2        3        4
cars = ['bmw', 'mercedes', 'seat', 'ziguli', 'skoda']

mycars = cars[1:3] #including 1st and 2nd , not 3rd
print(mycars)

# pos.    -5       -4         -3       -2       -1
cars = ['bmw', 'mercedes', 'seat', 'ziguli', 'skoda']
mycars = cars[-5:-3] #including -5 and -4, but not -3
print(mycars)

print("---------------")
# to coppy array without changing in copy
# pos.    0        1          2        3        4
cars = ['bmw', 'mercedes', 'seat', 'ziguli', 'skoda']

mycars = cars[:]
cars = ['bmw', 'mercedes', 'seat', 'ziguli', 'suzuki']
print(cars)
print(mycars)