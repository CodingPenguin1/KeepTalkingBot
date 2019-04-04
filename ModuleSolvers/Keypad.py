# ============================================================
# Title: Keep Talking and Nobody Explodes Solver: Keypad
# Author: Ryan J. Slater
# Date: 4/3/2019
# ============================================================


def solveKeypad(keypadSymbols):  # Symbols on the player's keypad
    # List of the 6 columns of symbols
    sourceSymbols = [['spoon', 'at', 'lambda', 'resistor', 'cat', 'h', 'backwardsc'],
                     ['backwardse', 'spoon', 'backwardsc', 'cl', 'hollowstar', 'h', 'upsidedownquestionmark'],
                     ['copyright', 'ballsack', 'cl', 'doublek', 'trailer', 'lambda', 'hollowstar'],
                     ['six', 'paragraph', 'b', 'cat', 'doublek', 'upsidedownquestionmark', 'smileyface'],
                     ['trident', 'smileyface', 'b', 'forwardsc', 'paragraph', 'snake', 'filledstar'],
                     ['six', 'backwardse', 'railroad', 'ae', 'trident', 'backwardsn', 'omega']]

    # Figure out which column is the correct one
    correctColumnNumber = -1
    for i in range(len(sourceSymbols)):
        # Assume true until proven otherwise
        correctColumn = True
        for symbol in keypadSymbols:
            # Here's the proof otherwise
            if sourceSymbols[i].count(symbol) == 0:
                correctColumn = False
                break
        # Break if found the correct column
        if correctColumn:
            correctColumnNumber = i
            break

    # Determine the correct order to press
    column = sourceSymbols[correctColumnNumber]
    orderToPress = []
    for symbol in column:
        if symbol in keypadSymbols:
            orderToPress.append(symbol)
    return ', '.join(orderToPress)


# Testing
if __name__ == '__main__':
    keypadSymbols = ['backwardsc', 'lambda', 'resistor', 'spoon']
    print(solveKeypad(keypadSymbols))