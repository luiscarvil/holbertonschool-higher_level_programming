#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
aux = number % 10
if number < 0:
    aux = (number % -10)
if aux > 5:
    print("Last digit of {:d} is {:d} greater\
 than 5".format(number, aux))
if aux == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, aux))
elif aux < 6 and aux != 0:
    print("Last digit of {:d} is {:d} and is less\
 than 6 and not 0".format(number, aux))
