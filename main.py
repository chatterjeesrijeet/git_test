def add(x,y):
    return (x+y)

def sub(x,y):
    return (x-y) 

def mult(x,y):
    return (x*y)  

def div(x,y):
    return (x//y)


def square(x):
    return x*x

def factorial(x):
    if x <= 1:
        return 1
    return x*factorial(x-1)