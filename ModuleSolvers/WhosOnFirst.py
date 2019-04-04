# ============================================================
# Title: Keep Talking and Nobody Explodes Solver: Who's on First?
# Author: Ryan J. Slater
# Date: 4/4/2019
# ============================================================


def solveSimonSays(textList,    # List of strings [displayText, topLeft, topRight, middleLeft, middleRight, bottomLeft, bottomRight]
                   bombSpecs):  # Dictionary of bomb specs such as serial number last digit, parallel port, battery count, etc
    # Top Left
    if textList[0] in ['ur']:
        return getResponsesFromWord(textList[1])
    # Top Right
    elif textList[0] in ['first', 'okay', 'c']:
        return getResponsesFromWord(textList[2])
    # Middle Left
    elif textList[0] in ['yes', 'nothing', 'led', 'they are']:
        return getResponsesFromWord(textList[3])
    # Middle Right
    elif textList[0] in ['blank', 'read', 'red', 'you', 'you\'re', 'their']:
        return getResponsesFromWord(textList[4])
    # Bottom Left
    elif textList[0] in ['', 'reed', 'leed', 'they\'re]:
        return getResponsesFromWord(textList[5])
    # Bottom Right
    elif textList[0] in ['display', 'says', 'no', 'lead', 'hold on', 'you are', 'there', 'see', 'cee']:
        return getResponsesFromWord(textList[6])


def getResponsesFromWord(word):  # Word to be used as the key for step 2
    # Returns a csv string in the order of words to try
    if word == 'ready':
        return 'YES, OKAY, WHAT, MIDDLE, LEFT, PRESS, RIGHT, BLANK, READY, NO, FIRST, UHHH, NOTHING, WAIT'.lower()
    elif word == 'first':
        return 'LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, BLANK, WHAT, PRESS, FIRST'.lower()
    elif word == 'no':
        return 'BLANK, UHHH, WAIT, FIRST, WHAT, READY, RIGHT, YES, NOTHING, LEFT, PRESS, OKAY, NO, MIDDLE'.lower()
    elif word == 'blank':
        return 'WAIT, RIGHT, OKAY, MIDDLE, BLANK, PRESS, READY, NOTHING, NO, WHAT, LEFT, UHHH, YES, FIRST'.lower()
    elif word == 'nothing':
        return 'UHHH, RIGHT, OKAY, MIDDLE, YES, BLANK, NO, PRESS, LEFT, WHAT, WAIT, FIRST, NOTHING, READY'.lower()
    elif word == 'yes':
        return 'OKAY, RIGHT, UHHH, MIDDLE, FIRST, WHAT, PRESS, READY, NOTHING, YES, LEFT, BLANK, NO, WAIT'.lower()
    elif word == 'what':
        return 'UHHH, WHAT, LEFT, NOTHING, READY, BLANK, MIDDLE, NO, OKAY, FIRST, WAIT, YES, PRESS, RIGHT'.lower()
    elif word == 'uhhh':
        return 'READY, NOTHING, LEFT, WHAT, OKAY, YES, RIGHT, NO, PRESS, BLANK, UHHH, MIDDLE, WAIT, FIRST'.lower()
    elif word == 'left:
        return 'RIGHT, LEFT, FIRST, NO, MIDDLE, YES, BLANK, WHAT, UHHH, WAIT, PRESS, READY, OKAY, NOTHING'.lower()
    elif word == 'right':
        return 'YES, NOTHING, READY, PRESS, NO, WAIT, WHAT, RIGHT, MIDDLE, LEFT, UHHH, BLANK, OKAY, FIRST'.lower()
    elif word == 'middle':
        return 'BLANK, READY, OKAY, WHAT, NOTHING, PRESS, NO, WAIT, LEFT, MIDDLE, RIGHT, FIRST, UHHH, YES'.lower()
    elif word == 'okay':
        return 'MIDDLE, NO, FIRST, YES, UHHH, NOTHING, WAIT, OKAY, LEFT, READY, BLANK, PRESS, WHAT, RIGHT'.lower()
    elif word == 'wait':
        return 'UHHH, NO, BLANK, OKAY, YES, LEFT, FIRST, PRESS, WHAT, WAIT, NOTHING, READY, RIGHT, MIDDLE'.lower()
    elif word == 'press':
        return 'RIGHT, MIDDLE, YES, READY, PRESS, OKAY, NOTHING, UHHH, BLANK, LEFT, FIRST, WHAT, NO, WAIT'.lower()
    elif word == 'you':
        return 'SURE, YOU ARE, YOUR, YOU\'RE, NEXT, UH HUH, UR, HOLD, WHAT?, YOU, UH UH, LIKE, DONE, U'.lower()
    elif word == 'you are':
        return 'YOUR, NEXT, LIKE, UH HUH, WHAT?, DONE, UH UH, HOLD, YOU, U, YOU\'RE, SURE, UR, YOU ARE'.lower()
    elif word == 'your':
        return 'UH UH, YOU ARE, UH HUH, YOUR, NEXT, UR, SURE, U, YOU\'RE, YOU, WHAT?, HOLD, LIKE, DONE'.lower()
    elif word == 'you\'re':
        return 'YOU, YOU\'RE, UR, NEXT, UH UH, YOU ARE, U, YOUR, WHAT?, UH HUH, SURE, DONE, LIKE, HOLD'.lower()
    elif word == 'ur':
        return 'DONE, U, UR, UH HUH, WHAT?, SURE, YOUR, HOLD, YOU\'RE, LIKE, NEXT, UH UH, YOU ARE, YOU'.lower()
    elif word == 'u':
        return 'UH HUH, SURE, NEXT, WHAT?, YOU\'RE, UR, UH UH, DONE, U, YOU, LIKE, HOLD, YOU ARE, YOUR'.lower()
    elif word == 'uh huh':
        return 'UH HUH, YOUR, YOU ARE, YOU, DONE, HOLD, UH UH, NEXT, SURE, LIKE, YOU\'RE, UR, U, WHAT?'.lower()
    elif word == 'uh uh':
        return 'UR, U, YOU ARE, YOU\'RE, NEXT, UH UH, DONE, YOU, UH HUH, LIKE, YOUR, SURE, HOLD, WHAT?'.lower()
    elif word == 'what?':
        return 'YOU, HOLD, YOU\'RE, YOUR, U, DONE, UH UH, LIKE, YOU ARE, UH HUH, UR, NEXT, WHAT?, SURE'.lower()
    elif word == 'done':
        return 'SURE, UH HUH, NEXT, WHAT?, YOUR, UR, YOU\'RE, HOLD, LIKE, YOU, U, YOU ARE, UH UH, DONE'.lower()
    elif word == 'next':
        return 'WHAT?, UH HUH, UH UH, YOUR, HOLD, SURE, NEXT, LIKE, DONE, YOU ARE, UR, YOU\'RE, U, YOU'.lower()
    elif word == 'hold':
        return 'YOU ARE, U, DONE, UH UH, YOU, UR, SURE, WHAT?, YOU\'RE, NEXT, HOLD, UH HUH, YOUR, LIKE'.lower()
    elif word == 'sure':
        return 'YOU ARE, DONE, LIKE, YOU\'RE, YOU, HOLD, UH HUH, UR, SURE, U, WHAT?, NEXT, YOUR, UH UH'.lower()
    elif word == 'like':
        return 'YOU\'RE, NEXT, U, UR, HOLD, DONE, UH UH, WHAT?, UH HUH, YOU, LIKE, SURE, YOU ARE, YOUR'.lower()
