# utils
from constants import SYMBOL, MAX_STACKED


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
    result = [[] for i in range(len(matrix[0]))]
    for l in matrix:
        for index, s in enumerate(l):
            result[index].append(s)
    rawBublz = [getBubbleNum(r) for r in result]
    stacked = [x for i, x in enumerate(rawBublz) if i == 0 or x != rawBublz[i-1]]
    stacked.extend([0]*(MAX_STACKED - len(stacked)))
    return stacked

def getHorizontalInvariants(matrix):
    rawBublz = [getBubbleNum(l) for l in matrix]
    stacked = [x for i, x in enumerate(rawBublz) if i == 0 or x != rawBublz[i-1]]
    stacked.extend([0]*(MAX_STACKED - len(stacked)))
    return stacked



