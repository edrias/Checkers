#Emmanuil Simkhayev
#Checkers
    #Instance of black game piece




class Black:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.look = "b "
        self.validMove = False
        self.allMoves = []
    #returns a string that represents the object as a string
    def __str__(self):
        return self.look

    #def __eq__(self, other):



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
        self.allMoves = [0]
        self.tempX = self.xPos
        self.tempY = self.yPos
        self.validMove = False

        if(self.empty_space(self.xPos +1, self.yPos +1, board)):
            self.validMove = True
            self.allMoves.append(self.xPos+1, self.yPos +1)
        if(self.empty_space(self.xPos -1, self.yPos +1, board)):
            self.validMove = True
            self.allMoves.append(self.xPos+1,self.yPos +1)


    def empty_space(self,xPos, yPos, board):
        if yPos <0 or yPos >7 or xPos <0 or xPos >7:
            return False
        if board[xPos][yPos] == ". ":
            return True

        return False



    def move_piece(self, board, choice):
        if(self.validMove == False):
            print('Black piece {0} , {1} has no moves'.format(self.getX(),self.getY()))
            return board







