import sys

from random import randint
from keras.utils import to_categorical
# import keyboard
import pynput
import numpy as np
import pygame
from msvcrt import getch
import time

# from pynput import keyboard
from pynput import keyboard

from venv.board import Board
from venv.network import Network


def cubeRoot(x):
    if x > 0:
        return x ** (1. / 3.)
    else:
        return -((-x) ** (1. / 3.))


def run():


    network = Network()

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

    gamesCount = 0
    movesCountPerGameMemory = []
    movesMemory = []
    statesMemory = []

    while True:
        board = Board()
        learned = 0
        while board.isGameEnded is False and board.isAnyIndexAllowed():
            board.fillRandomIndex()
            # board.printBoard()
            statesMemory.append(np.asarray([board.fromBoardtoBitsArray()]))
            moveIndex = randint(0, 3)
            if network.model.predict(np.asarray([board.fromBoardtoBitsArray()])).max() > 0.3:
                moveIndex = np.argmax(network.model.predict(np.asarray([board.fromBoardtoBitsArray()])))
                learned = learned + 1
            # time.sleep(0.5)
            # targetIndex = randint(0, 3)
            if moveIndex == 0:
                # print('up')
                board.upArrowClick()
            if moveIndex == 1:
                # print('left')
                board.leftArrowClick()
            if moveIndex == 2:
                # print('down')
                board.downArrowClick()
            if moveIndex == 3:
                # print('right')
                board.rightArrowClick()
            movesMemory.append(moveIndex)
        gamesCount = gamesCount + 1
        print(board.printBoard())
        print('played game number ' + gamesCount.__str__() + ', moves made: ' + board.moves.__str__())
        print('learned ' + learned.__str__())

        movesCountPerGameMemory.append(board.moves)
        movesCountPerGameMemory = movesCountPerGameMemory[len(movesCountPerGameMemory) - 100:len(movesCountPerGameMemory)]

        reward = sum(movesCountPerGameMemory)/len(movesCountPerGameMemory) - board.moves
        reward = cubeRoot(reward)
        # reward = np.sign(reward)
        for i in range(len(movesMemory)):
            target_f = network.model.predict(statesMemory[i])
            # target_f[0][np.argmax(to_categorical(movesMemory[i], num_classes=4))] = target_f[0][np.argmax(to_categorical(movesMemory[i], num_classes=4))] + reward
            target_f[0][np.argmax(to_categorical(movesMemory[i], num_classes=4))] = reward
            network.model.fit(statesMemory[i], target_f, epochs=1, verbose=0)
        movesMemory = []
        statesMemory = []
        learned = 0











run()