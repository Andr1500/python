oldlist = [45, 23, 12, 56, 46, -34, 2, 78]

def bubble_sort(mylist):
    last_item = len(mylist) - 1
    for z in range(0, last_item):
        for x in range(0, last_item-z):
            print(mylist)
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]

    return mylist

print("old list: ", oldlist)
newlist = bubble_sort(oldlist).copy()
print("new list: ", newlist)