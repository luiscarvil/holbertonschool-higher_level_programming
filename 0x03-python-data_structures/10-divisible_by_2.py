#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tot = []
    for i in my_list:
        tot.append(i % 2 == 0)
    return tot
