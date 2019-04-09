# ============================================================
# Title: Keep Talking and Nobody Explodes Solver: Full Bot
# Author: Ryan J. Slater
# Date: 4/4/2019
# Description: This is the bot that does it all. It needs a
# 1920x1080 screen to work and nothing else. Upon starting,
# it will alt+tab, then look for a start button, then solve the bomb.
# ============================================================

import pyautogui as p
from time import sleep
from os import system as bash
import numpy as np
import cv2
from matplotlib import pyplot as plt


def center(boundingBox):
    # Returns center of bounding box as tuple in form (left, top, width, height)
    x = boundingBox[0] + (boundingBox[2] // 2)
    y = boundingBox[1] + (boundingBox[3] // 2)
    return x, y


def grabScreen(grayscale=True):
    # Turn screencap into openCV image
    screenCap = p.screenshot()
    screenCap = screenCap.convert('RGB')
    screenCap = np.array(screenCap)
    if grayscale:
        screenCap = cv2.cvtColor(screenCap, cv2.COLOR_RGB2GRAY)
    return screenCap


def findImageOnScreen(referenceImage):
    # Finds referenceImage on screen, returns (left, top, width, height)

    # Convert reference to be opencv-readable
    referenceImage = cv2.imread(referenceImage, 0)
    w, h = referenceImage.shape[::-1]

    # Grab screen
    screenCap = grabScreen()

    # Match reference
    res = cv2.matchTemplate(referenceImage, screenCap, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    return max_loc[0], max_loc[1], w, h


if __name__ == '__main__':
    bombSpecs = {'serialNumberLastDigit': 0,
                 'serialNumberVowel': False,
                 'numBatteries': 0,
                 'indicatorLit_FRK': False}

    # Wait for user to say the game has started
    p.alert(title='Waiting for the game to start', text='Press OK when the lights turn on!', button='OK')

    # Find game window
    gameBox = findImageOnScreen('ReferenceScreenshots/lightsUp.png')

    # Click the bomb
    p.moveTo(center(gameBox)[0], center(gameBox)[1])
    p.moveRel(0, 50, 0.1)
    p.click()
    p.moveRel(0, -50)
    sleep(0.5)

    # Flip bomb to bottom
    p.drag(0, -250, 1, button='right')

    print(findImageOnScreen('ReferenceScreenshots/dBatteryHolder.png'))