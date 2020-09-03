#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sys import argv
    aux = len(argv) - 1
    if len(argv) - 1 == 0:
        print("0 arguments.")
    elif aux == 1:
            print("1 argument:\n{}: {}".format(aux, sys.argv[aux]))
    else:
        print("{} arguments:".format(aux))
        for i in range(1, aux + 1):
            print("{}: {}".format(i, sys.argv[i]))
