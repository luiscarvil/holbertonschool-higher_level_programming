#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sys import argv
    suma = 0
    for i in range(1, len(argv)):
        suma += int(argv[i])
    print(suma)
