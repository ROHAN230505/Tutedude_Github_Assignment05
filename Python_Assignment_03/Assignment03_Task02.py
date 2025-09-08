# Import the functions from the math module
from math import *


def calculate(num):
    if num > 0:
        square_root = sqrt(num)
        logarithm = log(num)
        sine = sin(num)

        print('Square Root: ', square_root)
        print('Logarithm: ', logarithm)
        print('Sine: ', sine)
    else:
        print('Please enter valid number')


# Take the input from the user
n = int(input("Enter a number: "))
res = calculate(n)
