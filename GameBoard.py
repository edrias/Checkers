#Emmanuil Simkhayev
#Gameboard where we call both black and white
from White import White
from Black import Black

class GameBoard:
    def __init__(self):
        self.w, self.h = 8,8


        self.board = [[0 for x in range(self.w)] for y in range(self.h)]


    def initialize_emptySpaces(self):
        for i in range(self.w):
            for j in range(self.h):
                self.board[i][j] = ". "


    def set_gamePieces(self):
        #initialize the black and white game peices to their respective locations
        count = 0
        for i in range(self.w):
            for j in range(self.w):
                if (i+j)%2 != 0 and count<24:
                    self.board[i][j] = Black(i,j)
                    count +=1
                elif (i+j)%2 != 0 and count > 39:
                    self.board[i][j] = White(i,j)
                    count+=1
                else:
                    count+=1

    def move(self, xPos, yPos):
        #inst = [Black for Black in self.board if Black.getX() == xPos and Black.getY() == yPos]
        if self.board[xPos][yPos] == Black:
           print("piece is black")
           inst = self.board[xPos][yPos]
           inst.get_valid_moves(self.board)
           self.board = inst.move_piece(self.board)
        else:
            print("not black")
            print(self.board[xPos][yPos])

    def printBoard(self):
        for i in range(self.w):
            #index= elem
            for j in range(self.h):
                print(self.board[i][j], end = " ")
            print(end="\n")











