import numpy as np


def decimal_to_quaternary(num, n):
    list = np.zeros(n)
    for x in range(n):
        list[x] = num//4**(n-x-1)
        num = num%4**(n-x-1)
    return(list)

CArule = [decimal_to_quaternary(i,9) for i in range(4**8)]
print(CArule)
