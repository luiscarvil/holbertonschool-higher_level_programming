#!/usr/bin/python3
import sys
from sys import argv
if len(argv) - 1 == 0:
    print("0 arguments.")
else:
    aux = len(argv) - 1
    if aux == 1:
        print("{} argument:".format(aux))
        print("{}: {}".format(aux, sys.argv[aux]))
    else:
        print("{} arguments:".format(aux))
        for i in range(1, aux + 1):
            print("{}: {}".format(i, sys.argv[i]))
