import math


def add(*args):
    """ This function is for adding numbers, you can pass 'n' number of parameters """

    return sum(args)

print(f"The addition is {add(1,2,3)}")


def mux(*args):
    """ This function is for multiplying numbers, you can pass 'n' number of parameters """

    num = 1

    for i in args:
        num *= i

    return num
print(f"The multiplication is: {mux(1,2,3,4)} ")


def sqr(x):
    """ This function is to find the square of a given number"""
    return x ** 2


def sqrt(x):
    """ This function is to find the square root of a given number"""
    return math.sqrt(x)


def power(x, y):
    """ This function is to find the power of a given number"""
    return math.pow(x, y)

answer = power(2,3)
print(answer)



