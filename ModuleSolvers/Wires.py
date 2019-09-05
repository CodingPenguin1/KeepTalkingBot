# ============================================================
# Title: Wires Solver
# Author: Ryan J. Slater
# Date: 4/3/2019
# ============================================================


def solveWires(wireList,    # List of strings stating wire colors (ex. ['red', 'blue', 'black'])
               bombSpecs):  # Dictionary of bomb specs such as serial number last digit, parallel port, battery count, etc
    if len(wireList) == 3:
        if wireList.count('red') == 0:
            return 'Cut the second wire'
        elif wireList[-1] == 'white':
            return 'Cut the last wire'
        elif wireList.count('blue') > 1:
            return 'Cut the last blue wire'
        else:
            return 'Cut the last wire'
    elif len(wireList) == 4:
        if wireList.count('red') > 1 and bombSpecs['serialNumberLastDigit'] % 2 == 1:
            return 'Cut the fourth wire'
        elif wireList.count('red') == 1 and wireList.count('yellow') > 1:
            return 'Cut the first wire'
        elif wireList.count('black') == 0:
            return 'Cut the second wire'
        else:
            return 'Cut the first wire'
    elif len(wireList) == 5:
        if wireList[-1] == 'black' and bombSpecs['serialNumberLastDigit'] % 2 == 1:
            return 'Cut the fourth wire'
        elif wireList.count('red') == 1 and wireList.count('yellow') > 1:
            return 'Cut the first wire'
        elif wireList.count('black') == 0:
            return 'Cut the second wire'
        else:
            return 'Cut the first wire'
    elif len(wireList) == 6:
        if wireList.count('yellow') == 0 and bombSpecs['serialNumberLastDigit'] % 2 == 1:
            return 'Cut the third wire'
        elif wireList.count('yellow') == 1 and wireList.count('white') > 1:
            return 'Cut the fourth wire'
        elif wireList.count('red') == 0:
            return 'Cut the last wire'
        else:
            return 'Cut the fourth wire'
    else:
        return 'Failed to solve simple wires: {}'.format(wireList)
