import numpy as np
from random import randint


class Board:

    moves = 0

    board = np.zeros((4, 4))

    def printBoard(self):
        print(self.board)


    def isAnyIndexAllowed(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                if self.board[i][j] == 0 or self.board[i][j] == 1:
                    return True
        return False


    def fillRandomIndex(self):
        self.moves = self.moves + 1

        allowedIndexes = []
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                if self.board[i][j] == 0 or self.board[i][j] == 1:
                    allowedIndexes.append([i, j])

        randomCoordinates = allowedIndexes[randint(0, len(allowedIndexes))-1]
        xIndex = randomCoordinates[0]
        yIndex = randomCoordinates[1]

        if self.board[xIndex][yIndex] == 0:
            self.board[xIndex][yIndex] = 1
        else:
            self.board[xIndex][yIndex] = 2


    def leftArrowClick(self):
        for i in range(len(self.board)):
            self.board[i] = self.moveEmptyAtTheEndLeftDirection(self.board[i])
            self.board[i] = self.mergeNumbersLeftDirection(self.board[i])
            self.board[i] = self.moveEmptyAtTheEndLeftDirection(self.board[i])

    def upArrowClick(self):
        self.board = np.transpose(self.board)
        for i in range(len(self.board)):
            self.board[i] = self.moveEmptyAtTheEndLeftDirection(self.board[i])
            self.board[i] = self.mergeNumbersLeftDirection(self.board[i])
            self.board[i] = self.moveEmptyAtTheEndLeftDirection(self.board[i])
        self.board = np.transpose(self.board)

    def downArrowClick(self):
        self.board = np.transpose(self.board)
        for i in range(len(self.board)):
            self.board[i] = self.moveEmptyAtTheEndRightDirection(self.board[i])
            self.board[i] = self.mergeNumbersRightDirection(self.board[i])
            self.board[i] = self.moveEmptyAtTheEndRightDirection(self.board[i])
        self.board = np.transpose(self.board)


    def rightArrowClick(self):
        for i in range(len(self.board)):
            self.board[i] = self.moveEmptyAtTheEndRightDirection(self.board[i])
            self.board[i] = self.mergeNumbersRightDirection(self.board[i])
            self.board[i] = self.moveEmptyAtTheEndRightDirection(self.board[i])


    def mergeNumbersRightDirection(self, array):
        i = 3
        while i > 0:
            if array[i] == array[i-1] and array[i] != 0:
                array[i] = array[i] + 1
                array[i-1] = 0
                i = i - 2
            i = i - 1
        return array


    def mergeNumbersLeftDirection(self, array):
        i = 0
        while i < 3:
            if array[i] == array[i+1] and array[i] != 0:
                array[i] = array[i] + 1
                array[i+1] = 0
                i = i + 2
            i = i + 1
        return array

    def moveEmptyAtTheEndLeftDirection(self,array):
        resultArray = []
        numbersArray = []
        emptyArray = []

        for i in range(len(array)):
            if array[i] == 0:
                emptyArray.append(array[i])
            else:
                numbersArray.append(array[i])

        for i in range(len(numbersArray)):
            resultArray.append(numbersArray[i])

        for i in range(len(emptyArray)):
            resultArray.append(emptyArray[i])

        return resultArray


    def moveEmptyAtTheEndRightDirection(self,array):
        resultArray = []
        numbersArray = []
        emptyArray = []

        for i in range(len(array)):
            if array[i] == 0:
                emptyArray.append(array[i])
            else:
                numbersArray.append(array[i])

        for i in range(len(emptyArray)):
            resultArray.append(emptyArray[i])

        for i in range(len(numbersArray)):
            resultArray.append(numbersArray[i])

        return resultArray




