#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        value = my_list[0]
        for i in my_list:
            if value < i:
                value = i
        return(value)
    else:
        return None
