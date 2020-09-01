#!/usr/bin/python3
str = ", "
for i in range(1, 100):
        if(int(i % 10 >= i % 100 / 10)):
            if i == 89:
                str = "\n"
            print("{:02d}".format(i), end=str)
