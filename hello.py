#print("Hello! Python")
#SHEETAL KUMAR

import numpy as np


def AND(x1, x2):
    x = np.array([1, x1, x2])
    w = np.array([-1.5, 1, 1])
    y = np.sum(w*x)
    if y <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([1, x1, x2])
    w = np.array([-0.5, 1, 1])
    y = np.sum(w*x)
    if y <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([1, x1, x2])
    w = np.array([1.5, -1, -1])
    y = np.sum(w*x)
    if y <= 0:
        return 0
    else:
        return 1

def NOT(x1):
    x = np.array([1,x1])
    w = np.array([0.5,-1])
    y = np.sum(w*x)
    if y <= 0:
        return 0
    else:
        return 1

'''def NOR(x1,x2):
    x = np.array([1,x1,x2])
    w = np.array([-1, 1, 1])
    y = np.sum(w*x)
    if y <= 0:
        return 0
    else:
        return 1'''


if __name__ == '__main__':
    input = [(0, 0), (1, 0), (0, 1), (1, 1)]
    input_not = [0,1]

    print("\nAND")
    for x in input:
        y = AND(x[0], x[1])
        print(str(x) + " -  " + str(y))

    print("\nOR")
    for x in input:
        y = OR(x[0], x[1])
        print(str(x) + " - " + str(y))

    print("\nNAND")
    for x in input:
        y = NAND(x[0], x[1])
        print(str(x) + " - " + str(y))

    print("\nNOT")
    for x in input_not:
        y = NOT(x)
        print(str(x) + " - " + str(y))

    '''print("NOR")
    for x in input:
        y = NOR(x[0], x[1])
        print(str(x) + " -> " + str(y)) '''



   