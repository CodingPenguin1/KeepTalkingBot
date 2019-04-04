# ============================================================
# Title: Keep Talking and Nobody Explodes Solver: Simon Says
# Author: Ryan J. Slater
# Date: 4/4/2019
# ============================================================


def solveButton(numStrikes,
                flashSequence,  # List of strings: colors flashed
                bombSpecs):     # Dictionary of bomb specs such as serial number last digit, parallel port, battery count, etc
    if bombSpecs['serialNumberVowel'] is True:
        if numStrikes == 0:
            for i in range(len(flashSequence)):
                if flashSequence[i] == 'red':
                    flashSequence[i] = 'blue'
                elif flashSequence[i] = 'blue':
                    flashSequence[i] = 'red'
                elif flashSequence[i] = 'green':
                    flashSequence[i] = 'yelllow'
                else:
                    flashSequence[i] = 'green'
        elif numStrikes == 1:
            for i in range(len(flashSequence)):
                if flashSequence[i] == 'red':
                    flashSequence[i] = 'yellow'
                elif flashSequence[i] = 'blue':
                    flashSequence[i] = 'green'
                elif flashSequence[i] = 'green':
                    flashSequence[i] = 'blue'
                else:
                    flashSequence[i] = 'red'
        else:
            for i in range(len(flashSequence)):
                if flashSequence[i] == 'red':
                    flashSequence[i] = 'green'
                elif flashSequence[i] = 'blue':
                    flashSequence[i] = 'red'
                elif flashSequence[i] = 'green':
                    flashSequence[i] = 'yelllow'
                else:
                    flashSequence[i] = 'blue'
    else:
        if numStrikes == 0:
            for i in range(len(flashSequence)):
                if flashSequence[i] == 'red':
                    flashSequence[i] = 'blue'
                elif flashSequence[i] = 'blue':
                    flashSequence[i] = 'yellow'
                elif flashSequence[i] = 'green':
                    flashSequence[i] = 'green'
                else:
                    flashSequence[i] = 'red'
        elif numStrikes == 1:
            for i in range(len(flashSequence)):
                if flashSequence[i] == 'red':
                    flashSequence[i] = 'red'
                elif flashSequence[i] = 'blue':
                    flashSequence[i] = 'blue'
                elif flashSequence[i] = 'green':
                    flashSequence[i] = 'yelllow'
                else:
                    flashSequence[i] = 'green'
        else:
            for i in range(len(flashSequence)):
                if flashSequence[i] == 'red':
                    flashSequence[i] = 'yellow'
                elif flashSequence[i] = 'blue':
                    flashSequence[i] = 'green'
                elif flashSequence[i] = 'green':
                    flashSequence[i] = 'blue'
                else:
                    flashSequence[i] = 'red'
    return ', '.join(flashSequence)