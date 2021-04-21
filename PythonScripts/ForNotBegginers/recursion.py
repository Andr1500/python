def hello(x):  #the function for printing "hello"recursively N times
    if x == 0:
        return
    else:
        print("hello")
        hello(x-1)

hello(2)

def sum(q):  #the function for calculating digits in recursion
    if q == 0:
        return 0
    elif q == 1:
        return 1
    else:
        return q + sum(q-1)

z = sum(12)
print(z)

def factorial(a):  #the function for searching factorial in recursion
    if a == 0:
        return 1
    else:
        return a * factorial(a-1)

print("factorial: " + str(factorial(6)))

def fido(w):  #the function for searching Fibonacci digits in  recursion
    if w == 0:
        return 0
    if w == 1:
        return 1
    else:
        return fido(w-1) + fido(w-2)

print("Fibonacci digit:" + str(fido(12)))
