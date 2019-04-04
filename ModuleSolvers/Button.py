# ============================================================
# Title: Keep Talking and Nobody Explodes Solver: Button
# Author: Ryan J. Slater
# Date: 4/3/2019
# ============================================================


def solveButton(indicatorColor,  # None/String: The color of the indicator. None type if the indicator color is unknown (the button isn't being held down)
                buttonColor,     # String: The color of the button
                buttonText,      # String: The text on the button
                bombSpecs):      # Dictionary of bomb specs such as serial number last digit, parallel port, battery count, etc
    if indicatorColor is None:
        if bombSpecs['numBatteries'] > 1 and buttonText == 'detonate':
            return 'Press and immediately release the button'
        elif bombSpecs['numBatteries'] > 2 and bombSpecs['indicatorLit_FRK'] is True:
            return 'Press and immediately release the button'
        elif buttonColor == 'red' and buttonText == 'hold':
            return 'Press and immediately release the button'
        else:
            return 'Hold down the button. What color is the indicator?'
    else:
        if indicatorColor == 'blue':
            return 'Release when the countdown timer has a 4 in any position'
        elif indicatorColor == 'white':
            return 'Release when the countdown timer has a 1 in any position'
        elif indicatorColor == 'yellow':
            return 'Release when the countdown timer has a 5 in any position'
        else:
            return 'Release when the countdown timer has a 1 in any position'
