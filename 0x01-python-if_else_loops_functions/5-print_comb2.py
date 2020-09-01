#!/usr/bin/python3
str = ", "
for i in range(0, 100):
    if i == 99:
        str = "\n"
    print("{:02d}".format(i), end=str)
