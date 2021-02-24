#creating functions, def - defined
name = "Vova"

def hello():
    """print hello"""
    print("congratulations " + name + "!")
    #print("welcome to our site")


def aaa():
    print("AAA access")


print("--------------------")
hello()

#function with numbers

def summa (x, y):
    print(x + y)

summa(10, 20)

#calculation in function

def summa(x, y):
    return x+y

x = summa(12, 40)
print(x)

#function with factorial

def factorial(x):
    """calc factorial"""
    result = 1
    for z in range(1, x+1):
       result = result * z
    return result

print(factorial(2))
print(factorial(5))

#factorial in range

for i in range(1, 15):
    print(str(i) + "!\t = " + str(factorial(i)))
