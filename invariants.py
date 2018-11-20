# utils
from constants import SYMBOL


def getBubbleNum(array):
    result = -1
    flag = 0
    for word in array:
        if (word != SYMBOL and flag == 0) or (word == SYMBOL and flag == 1):
            continue
        if word == SYMBOL and flag == 0:
            flag = 1
            result += 1
        if word != SYMBOL and flag == 1:
            flag = 0
    return result

def getVerticalInvariants(matrix):
    print("Matrix", matrix, [len(l) for l in matrix])
    result = [[] for i in range(len(matrix[0]))]
    for l in matrix:
        for index, s in enumerate(l):
            result[index].append(s)
    #print(result)
    print('BUBLZ', [getBubbleNum(r) for r in result])


