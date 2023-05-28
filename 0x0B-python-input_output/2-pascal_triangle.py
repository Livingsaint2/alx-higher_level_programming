#!/usr/bin/python3
"""
Pascal triangle implementation
"""


def pascal_triangle(n):
    """pascal triangle interview answer"""
    if (n <= 0):
        return []
    init = [[1]]
    for i in range(1, n):
        if (i == 1):
            init.append([1, 1])
        else:
            init.append([0] * (i + 1))
            init_point = 0
            for num in range(i + 1):
                if (num == 0):
                    init[i][num] = 1
                    continue
                elif (num == i):
                    init[i][num] = 1
                    continue
                if (init_point != i - 1):
                    val = init[i - 1][init_point] + init[i - 1][init_point + 1]
                    init[i][num] = val
                    init_point += 1
    return(init)
