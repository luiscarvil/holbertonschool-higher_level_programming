#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
aux = number % 10
if number < 0:
    aux = (number % -10) 
if aux > 5:
    print("Last digit of", number, "is", aux, "greater than 5")
if aux == 0:
    print("Last digit of", number, "is", aux, "and is 0")
elif aux < 6 and aux != 0:
    print("Last digit of", number, "is", aux, "and is less than 6 and not 0")
