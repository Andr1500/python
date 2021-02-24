cities = ['Gdansk', 'Wroclaw', 'berlin', 'Lviv', 'Odessa']
print(cities)

# len  - function returns the number of characters in the string.
print(len(cities))

#print the value from the string (first number from the begin)
print(cities[0])

#print the value from the string (first number from the end)
print(cities[-1])

#print the value from the string with title and upper parameters.
print(cities[2].title())
print(cities[2].upper())

#change the value in the string
cities[2] = 'Stavropol'
print(cities)


#add new value in the end of the string
cities.append('Zalcburg')
print(cities)

#insert new value in the direct plase of the string
cities.insert(1, 'Grodno')
print(cities)

#delete the value from the string
del cities[-1]
print(cities)

#remove the value from the string (if we don't know the number of the value)
cities.remove('Grodno')
print(cities)

#pop - removes and returns last value from the list or the given index value
delcity = cities.pop()
print("deleted city:" + delcity)
print(cities)

#sort data in the list by alphabet
cities.sort()
print(cities)

#sort data in the list by alphabet, from the end to the begin
cities.sort(reverse=True)
print(cities)

#reverse data from the list
cities.reverse()
print(cities)