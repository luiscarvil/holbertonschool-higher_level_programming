#!/usr/bin/python3
"""pascal tringle in python
"""


def pascal_triangle(n):
    """
    implementation
    """
    new_l = []
    if n <= 0:
        return new_l
    for i in range(n):
        if i == 0:
            new_l.append([1])
        elif i == 1:
            new_l.append([1, 1])
        else:
            new_l2 = []
            for j in range(i + 1):
                new_l2.append(j)
            for j in range(i):
                new_l2[0], new_l2[i] = 1, 1
                new_l2[j] = new_l[i - 1][j] + new_l[i - 1][j - 1]
            new_l.append(new_l2)
    return new_l
