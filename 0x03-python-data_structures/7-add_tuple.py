#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
        tuple_c = (0, 0)
        tuple_d = (0, 0)
        tuple_aa = tuple_a + tuple_c
        tuple_bb = tuple_b + tuple_d
        return tuple_aa[0] + tuple_bb[0], tuple_aa[1] + tuple_bb[1]
