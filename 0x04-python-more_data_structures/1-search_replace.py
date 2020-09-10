#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list2 = my_list.copy()
    for n, i in enumerate(my_list):
        if i == search:
            my_list2[n] = replace
    return(my_list2)
