

def binarysearch(mylist, search, start, stop):
    if start > stop:
        return False
    else:
        middle = (start + stop) // 2
        if search == mylist[middle]:
            return middle
        elif search < mylist[middle]:
            return binarysearch(mylist, search, start, middle - 1)
        else:
            return binarysearch(mylist, search, middle + 1, stop)
mylist = [5, 12, 16, 19, 23, 25, 27, 29, 33, 67]
search = 33

x = binarysearch(mylist, search, 0, len(mylist))

if x == False:
    print("the number ", search, " is not found!")
else:
    print("the number ", search, " is found at index: ", x)