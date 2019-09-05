#!/home/rjslater/anaconda3/bin/python
# ============================================================
# Title: Command Line Bot
# Author: Ryan J. Slater
# Date: 9/4/2019
# Description: Run this on the side of the game and input
# commands to recieve a solution for a module
# ============================================================

from ModuleSolvers.Wires import solveWires


def askForInt(message):
    while True:
        response = input(message + ': ').strip()
        try:
            return int(float(response))
        except ValueError:
            pass


def askForBool(message):
    while True:
        response = input(message + ': ').strip()
        if 'n' in response or '0' in response or 'f' in response:
            return False
        elif 'y' in response or '1' in response or 't' in response:
            return True


if __name__ == '__main__':
    # Initializing need-to-know bomb specs
    bombSpecs = {'serialNumberLastDigit': 0,
                 'serialNumberVowel': False,
                 'numBatteries': 0,
                 'indicatorLit_FRK': False}

    # Asking for the serial number last digit
    bombSpecs['serialNumberLastDigit'] = askForInt('Serial number last digit')

    # Asking for if there is a vowel in the serial number
    bombSpecs['serialNumberVowel'] = askForBool('Vowel in serial number')

    # Asking for number of batteries
    bombSpecs['numBatteries'] = askForInt('Number of batteries')

    # Asking for number of batteries
    bombSpecs['indicatorLit_FRK'] = askForBool('Lit indicator FRK')

    print(bombSpecs)

    while True:
        command = input('> ').lower().split(' ')

        if command[0] == 'simpwire':
            print(solveWires(command[1:], bombSpecs))
