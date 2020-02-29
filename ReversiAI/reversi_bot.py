import numpy as np
import random as rand
import reversi
import copy
import sys
import time

class ReversiBot:
    def __init__(self, move_num):
        self.move_num = move_num
        self.robotNum = 0
        self.humanNum = 0
        self.maxDepth = 5
        self.movesLeft = 34
        self.theBeginning = time.time()
        self.remainingTime = (int(sys.argv[3]) * 60)
        self.timePerMove = (self.remainingTime / self.movesLeft)
        print("Time per move: ", self.timePerMove)
        self.rewardMatrix = np.array([[120, -20, 20, 5, 5, 20, -20, 120],
        [-20, -40, -5, -5, -5, -5, -40, -20],
        [20, -5, 15, 3, 3, 15, -5, 20],
        [5, -5, 3, 3, 3, 3, -5, 5],
        [5, -5, 3, 3, 3, 3, -5, 5],
        [20, -5, 15, 3, 3, 15, -5, 20],
        [-20, -40, -5, -5, -5, -5, -40, -20],
        [120, -20, 20, 5, 5, 20, -20, 120]])

    def make_move(self, state):

        #Set AI and opponent player numbers
        self.robotNum = state.turn
        if(self.robotNum == 1):
            self.humanNum = 2
        else:
            self.humanNum = 1

        dahBestMax = 0
        dahBestMove = (0,0)
        self.maxDepth = 3
        self.startTime = time.time()
        while(True):
            depth = 0
            alpha = -10000
            beta = 10000
            dahBestMax, dahBestMove = self.max(state,depth,alpha,beta)
            currTime = time.time() - self.startTime
            self.maxDepth += 1
            if self.maxDepth > 20:
                break
            if(currTime > (self.timePerMove/2)):
                break
        self.updateCorners(dahBestMove)
        if(self.movesLeft > 0):
            self.updateTimePerMove(currTime)
        self.movesLeft -= 1
        print("Ellapsed time: ", currTime)
        print("Searched to depth: ", self.maxDepth)
        print("My best max is: ",dahBestMax)
        return dahBestMove

    def updateTimePerMove(self, currTime):
        self.remainingTime -= currTime
        print("     Remaining time: ", self.remainingTime)
        self.timePerMove = (self.remainingTime / self.movesLeft)
        print("     Time left per move: ", self.timePerMove)

    def updateCorners(self,move):
        if(move == (0,0)):
            self.rewardMatrix[0,1] = 150
            self.rewardMatrix[1,1] = 150
            self.rewardMatrix[1,0] = 150
        elif(move == (7,7)):
            self.rewardMatrix[6,7] = 150
            self.rewardMatrix[7,6] = 150
            self.rewardMatrix[6,6] = 150
        elif(move == (0,7)):
            self.rewardMatrix[0,6] = 150
            self.rewardMatrix[1,6] = 150
            self.rewardMatrix[1,7] = 150
        elif(move == (7,0)):
            self.rewardMatrix[6,0] = 150
            self.rewardMatrix[6,1] = 150
            self.rewardMatrix[7,1] = 150

    def undoCorners(self,move):
        if(move == (0,0)):
            self.rewardMatrix[0,1] = -20
            self.rewardMatrix[1,1] = -40
            self.rewardMatrix[1,0] = -20
        elif(move == (7,7)):
            self.rewardMatrix[6,7] = -20
            self.rewardMatrix[7,6] = -20
            self.rewardMatrix[6,6] = -40
        elif(move == (0,7)):
            self.rewardMatrix[0,6] = -20
            self.rewardMatrix[1,6] = -40
            self.rewardMatrix[1,7] = -20
        elif(move == (7,0)):
            self.rewardMatrix[6,0] = -20
            self.rewardMatrix[6,1] = -40
            self.rewardMatrix[7,1] = -20

    def max(self,currState,depth,alpha,beta):
        currState.turn = self.robotNum
        bestMax = -10000
        bestMaxMove = None
        currValidMoves = currState.get_valid_moves()
        baseBoard = copy.deepcopy(currState.board)

        if(depth >= self.maxDepth):
            #Place heuristic for evaluating winning here
            if(0 in currState.board):
                robotReward = self.totalReward(currState.board,self.robotNum)
                opponentReward = self.totalReward(currState.board,self.humanNum)
                return (robotReward - opponentReward), (0,0)
            else:
                numRobotStones = self.countNumStones(self.robotNum,currState.board)
                numOppononentStones = self.countNumStones(self.humanNum,currState.board)
                return (numRobotStones - numOppononentStones), (0,0)

        if(len(currValidMoves) < 1):
            bestMax, possibleMove = self.min(currState,depth+1,alpha,beta)

        for nextMove in currValidMoves:
            #Change the corner reards if moving in a corner
            self.updateCorners(nextMove)
            #Make the move
            currState.board[nextMove] = self.robotNum
            currState.board = self.flipStones(nextMove,self.robotNum,currState.board)
            #Update the reward
            #tempReward = reward + self.rewardMatrix[nextMove]
            possibleMax, possibleMove = self.min(currState,depth+1,alpha,beta)
            #Change the reward matrix back to it's current state
            self.undoCorners(nextMove)

            #Check to see if we have a better max value aka a better move to make
            if(possibleMax > bestMax):
                bestMax = possibleMax
                bestMaxMove = nextMove
            #Reset the board
            currState.board = copy.deepcopy(baseBoard)

            #Alpha-beta pruning part
            if bestMax >= beta:
                return bestMax, bestMaxMove
            if bestMax > alpha:
                alpha = bestMax

        return bestMax, bestMaxMove

    def min(self,currState,depth,alpha,beta):

        currState.turn = self.humanNum
        bestMin = 10000
        bestMinMove = None
        currValidMoves = currState.get_valid_moves()
        baseBoard = copy.deepcopy(currState.board)

        if(depth >= self.maxDepth):
            #Guess heuristic for non-terminal game states
            if(0 in currState.board):
                robotReward = self.totalReward(currState.board,self.robotNum)
                opponentReward = self.totalReward(currState.board,self.humanNum)
                return (robotReward - opponentReward), (0,0)
            #Accurate heuristic for the end of the game
            else:
                numRobotStones = self.countNumStones(self.robotNum,currState.board)
                numOppononentStones = self.countNumStones(self.humanNum,currState.board)
                return (numRobotStones - numOppononentStones), (0,0)

        if(len(currValidMoves) < 1):
            bestMin, possibleMove = self.max(currState,depth+1,alpha,beta)

        for nextMove in currValidMoves:
            currState.board[nextMove] = self.humanNum
            currState.board = self.flipStones(nextMove,self.humanNum,currState.board)
            possibleMin, possibleMove = self.max(currState,depth+1,alpha,beta)

            #Check to see if we have a better min value aka a better move to make
            if(possibleMin < bestMin):
                bestMin = possibleMin
                bestMinMove = nextMove

            #Reset the board
            currState.board = copy.deepcopy(baseBoard)

            #Alpha-beta pruning part
            if bestMin <= alpha:
                return bestMin, bestMinMove
            if bestMin < beta:
                beta = bestMin

        return bestMin, bestMinMove

    def flipStones(self,stoneCoords,playerNum,currBoard):

        row = stoneCoords[0]
        column = stoneCoords[1]
        currBoard = self.flipDemStones(row,column,0,1,playerNum,currBoard)
        currBoard = self.flipDemStones(row,column,1,1,playerNum,currBoard)
        currBoard = self.flipDemStones(row,column,1,0,playerNum,currBoard)
        currBoard = self.flipDemStones(row,column,1,-1,playerNum,currBoard)
        currBoard = self.flipDemStones(row,column,0,-1,playerNum,currBoard)
        currBoard = self.flipDemStones(row,column,-1,-1,playerNum,currBoard)
        currBoard = self.flipDemStones(row,column,-1,0,playerNum,currBoard)
        currBoard = self.flipDemStones(row,column,-1,1,playerNum,currBoard)
        return currBoard

    def flipDemStones(self,row,column,rowDirection,columnDirection,playerNum,currBoard):
        stonesToFlip = []
        row+=rowDirection
        column+=columnDirection
        while(not self.outOfBounds(row,column) and currBoard[row,column] != playerNum and currBoard[row,column] != 0):
            stonesToFlip.append((row,column))
            row+=rowDirection
            column+=columnDirection
        if(not self.outOfBounds(row,column) and currBoard[row,column] == playerNum):
            for stone in stonesToFlip:
                currBoard[stone] = playerNum
        return currBoard

    def totalReward(self,currBoard, playerNum):
        reward = 0
        for i in range(0,8):
            for j in range(0,8):
                if (currBoard[i][j] == playerNum):
                    reward = reward + self.rewardMatrix[i,j]
        return reward

    def outOfBounds(self,row,column):
        if(row < 0 or row >=8):
            return True
        elif(column < 0 or column >=8):
            return True
        else:
            return False

    def countNumStones(self,playerNum,currBoard):
        count = 0
        for i in range(0,8):
            for j in range(0,8):
                if (currBoard[i][j] == playerNum):
                    count += 1
        return count
