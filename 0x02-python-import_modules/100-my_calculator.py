#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        """print("here {}".format(argv[1]))
        """
        a = int(argv[1])
        """print("here {}".format(argv[3]))
        """
        b = int(argv[3])
        if argv[2] == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        if argv[2] == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        if argv[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        if argv[2] == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
    """print(len(argv))
    """
