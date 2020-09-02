#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
        else:
            i = chr(ord(i))
        print("{}".format(i), end="")
    print("")
