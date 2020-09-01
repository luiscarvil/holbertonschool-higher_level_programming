#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number % 10 == 0:
    print("Last digit of", end=" ")
    print("{:d} is {:d} and is 0".format(number, number % 10))
elif number > 0:
    print("Last digit of", end=" ")
    if number % 10 > 5:
        print("{:d} is {:d}greater than 5".format(number, number % 10))
    elif number % 10 < 6:
        print("{:d} is {:d}".format(number, number % 10), end=" ")
        print("and is less than 6 and not 0")
else:
    print("Last digit of", end=" ")
    print("{:d} is {:d}".format(number, number % -10), end=" ")
    print("and is less than 6 and not 0")
