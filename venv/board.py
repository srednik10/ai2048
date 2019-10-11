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

    def fromBoardtoBitsArray(self):
        resultBitArray = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                binaryFormArray = self.intTo4Bits(self.board[i][j])
                for k in range(4):
                    resultBitArray.append(binaryFormArray[k])
        return resultBitArray

    def fromBitsArrayToBoard(self, bitsArray):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                self.board[i][j] = self.bitsToInt(bitsArray[16*i+4*j:16*i+4*j+4])
        return self.board



    def intTo4Bits(self,number):
        bitsArray = []
        for i in range(4):
            if(number%2 == 1):
                bitsArray.append(1)
                number = number/2 - 1
            else:
                bitsArray.append(0)
                number = number/2
        return list(reversed(bitsArray))

    def bitsToInt(self, bitsArray):
        intValue = 0
        multipler = 8
        for i in range(len(bitsArray)):
            intValue = intValue + multipler*bitsArray[i]
            multipler = multipler/2
        return intValue









