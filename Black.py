#Emmanuil Simkhayev
#Checkers
    #Instance of black game piece
from math import*
#from White import White


class Black:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.look = "b "
        self.validMove = False
        self.allMoves = [(x,y) for x in range(25) for y in range(25)]

    #returns a string that represents the object as a string
    def __str__(self):
        return self.look

    def __eq__(self, other):
        return self.look == other




    def setX(self, xPos):
        self.xPos = xPos
    #get x coordinate
    def getX(self):
        return self.xPos

    def setY(self, yPos):
        self.yPos = yPos

    def getY(self):
        return self.yPos

    def get_valid_moves(self,board):
        self.allMoves.clear()
        self.tempX = self.xPos
        self.tempY = self.yPos
        self.validMove = False
        self.canJump = False


        if(self.empty_space(self.xPos +1, self.yPos +1, board)):
            self.validMove = True
            #add coordinates to list
            self.allMoves.append( (self.xPos +1, self.yPos +1) )
        if(self.empty_space(self.xPos +1, self.yPos -1, board)):
            self.validMove = True
            self.allMoves.append( (self.xPos+1,self.yPos -1) )


    def can_jump_moves(self,board,enemy):
        self.canJump = False
        if self.is_enemy(self.tempX +1, self.tempY -1,board,enemy):
            if self.empty_space(self.tempX +2, self.tempY -2, board):
                self.allMoves.append((self.tempX +2,self.tempY -2))
                self.validMove = True
                self.canJump = True
                self.tempX +=2
                self.tempY -=2
                print("move1")
                self.can_jump_moves(board,enemy)


        if self.is_enemy(self.tempX+1, self.tempY +1, board,enemy):
            if self.empty_space(self.tempX +2, self.tempY +2, board):
                self.allMoves.append((self.tempX +2, self.tempY +2))
                self.validMove = True
                self.canJump = True
                self.tempX +=2
                self.tempY +=2
                print("move2")
                self.can_jump_moves(board,enemy)

        self.tempX = self.xPos
        self.tempY = self.yPos



    def is_enemy(self, xPos, yPos, board,enemy):
        if self.yPos < 0 or self.yPos >7 or self.xPos <0 or self.xPos >7:
            return False
        if isinstance(board[xPos][yPos],enemy):
            return True
        return False

    def empty_space(self,xPos, yPos, board):
        if yPos <0 or yPos >7 or xPos <0 or xPos >7:
            return False
        if board[xPos][yPos] == ". ":
            return True

        return False

    def print_valid_moves(self):
        count = 0
        for elem in self.allMoves:
            print("{0}. {1}".format(count, elem))
            count+=1


    def move_piece(self, board, choice):
        if(self.validMove == False):
            print('Black piece {0} , {1} has no moves'.format(self.getX(),self.getY()))
            return board
        else:
            coordinates = self.allMoves[choice]
            print('new coordiantes = {0}, {1}'.format(coordinates[0],coordinates[1]))
            print ('current position = {0}, {1}'.format(self.getX(),self.getY()))

            index = abs(self.yPos - coordinates[1])
            print(index)
            for i in range(index):
                if coordinates[1] > self.yPos:
                    board[self.xPos][self.yPos] =". "
                    self.setX(self.xPos + 1)
                    self.setY(self.yPos + 1)
                    print('{0}, {1}'.format(self.getX(), self.getY()))
                else:
                    board[self.xPos][self.yPos] = ". "
                    self.setX(self.xPos + 1 )
                    self.setY(self.yPos - 1 )
                    print('{0}, {1}'.format(self.getX(), self.getY()))
                #print('{0}, {1}'.format(self.getX(), self.getY()))


            self.setX(coordinates[0])
            self.setY(coordinates[1])
            board[self.getX()][self.getY()] = self
            self.allMoves.clear()

        return board








