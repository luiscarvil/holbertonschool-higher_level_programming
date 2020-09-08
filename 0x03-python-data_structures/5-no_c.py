#!/usr/bin/python3
def no_c(my_string):
    my_new = ""
    for i in my_string:
        if i not in ['c', 'C']:
            my_new = my_new + i
    return(my_new)
