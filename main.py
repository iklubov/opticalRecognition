import os

from constants import path, SYMBOL
from invariants import getVerticalInvariants


def transfromString(f):
    lines = f.readlines()
    vistart, vistop = 0, 0
    histart, histop = len(lines), 0
    currentState = 0

    for i, l in enumerate(lines):
        mi, ma = l.find(SYMBOL), l.rfind(SYMBOL)
        if mi != -1 and currentState == 0:
            currentState = 1
            vistart = i
        if (mi == -1 or i == len(lines) - 1) and currentState == 1:
            currentState = 0
            vistop = i+1 if mi>-1 else i
        if mi != -1:
            histart = min(histart, mi)
            histop = max(histop, ma + 1)

    res = [l[histart:histop].replace('\n', ' ') for l in lines[vistart:vistop]]
    maxLen = max(len(line) for line in res )
    for rindex, line in enumerate(res):
        if maxLen == len(line):
            continue
        line += ' '
        res[rindex] = line
    return res

counter = 0
for filename in os.listdir(path):
    f = open(path + '/' + filename, 'r')
    matrix = transfromString(f)
    print('MATRIX', matrix)
    verticalBublz = getVerticalInvariants(matrix)
    print('VERTICAL BUBLZ', verticalBublz)
