#using list

mylist = []

msg = ""

while msg != 'stop':
    msg = input('enter new item, and put stop for finish')
    mylist.append(msg)

print(mylist)

#imput name (strings)

name = input("please, imput your name: ")
print(name)

#imput numbers(we need to convert it into integer)

num1 = input("x: ")

num2 = input("y: ")

summa = int(num2) + int(num1)
print(summa)

#reading input data from the user

message = ""
while True:
    message = input("enter password: ")
    if message == "secret":
        break
    print('password is incorrect')



