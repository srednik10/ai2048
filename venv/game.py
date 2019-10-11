import sys
from random import randint

# import keyboard
import pynput
import numpy as np
import pygame
from msvcrt import getch
import time

# from pynput import keyboard
from pynput import keyboard

from venv.board import Board


def run():

    board = Board()

    # def on_press(key):
    #     return
    #
    # def on_release(key):
    #     if(board.isAnyIndexAllowed()):
    #         if key.name == 'up':
    #             board.upArrowClick()
    #         if key.name == 'left':
    #             board.leftArrowClick()
    #         if key.name == 'down':
    #             board.downArrowClick()
    #         if key.name == 'right':
    #             board.rightArrowClick()
    #         board.fillRandomIndex()
    #         board.printBoard()


    # Collect events until released
    # with keyboard.Listener(
    #         on_press=on_press,
    #         on_release=on_release) as listener:
    #     listener.join()

    while board.isAnyIndexAllowed():
        # time.sleep(1)
        randomInt = randint(0, 3)
        if randomInt == 0:
            board.upArrowClick()
        if randomInt == 1:
            board.leftArrowClick()
        if randomInt == 2:
            board.downArrowClick()
        if randomInt == 3:
            board.rightArrowClick()
        board.fillRandomIndex()
        print(board.moves)
        board.printBoard()

run()