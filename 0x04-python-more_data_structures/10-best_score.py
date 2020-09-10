#!/usr/bin/python3
def best_score(a_dictionary):
    a_dic_max = None
    if a_dictionary:
        a_dic_max = max(a_dictionary, key=a_dictionary.get)
    return a_dic_max
