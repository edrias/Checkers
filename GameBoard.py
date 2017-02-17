#Emmanuil Simkhayev
#Gameboard where we call both black and white
from White import White
from Black import Black

class GameBoard:
    def __init__(self):
        self.w, self.h = 8,8 # height and width of board
        self.list_of_black = [] #empty list for location of black pieces
        self.list_of_white = [] #empty list for location of black pieces
        #initializing the game board with zeros.
        self.board = [[0 for x in range(self.w)] for y in range(self.h)]

    #method sets all positions on board with ". " or empty space
    def initialize_emptySpaces(self):
        for i in range(self.w):
            for j in range(self.h):
                self.board[i][j] = ". "

    #initializes the game pieces
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

    def move(self, xPos, yPos, piece, enemy ):
        # make sure coordinates chosen are indeed black
        if isinstance(self.board[xPos][yPos], piece):
            print("piece is {0}".format(piece))
            inst = self.board[xPos][yPos]  # assign this black piece to value inst
            inst.get_valid_moves(self.board)
            inst.can_jump_moves(self.board, enemy )  # moves where piece can jump enemy
            inst.print_valid_moves()
            if len(inst.allMoves) == 0:  # if there are no moves then return false
                return False
            else:  # if there are moves, they will be displayed and user enters a number corresponding to the move
                choice = int(input("Enter a choice for your move"))
                self.board = inst.move_piece(self.board, choice)  # update the board
                inst.checkKing()  # check if piece is a king after moving.
            return True

        else:  #this else is here in case user did not enter the correct coordinates.
            inst = self.board[xPos][yPos]
            print(inst)
            print("not {0}".format(piece))
            return False

    def printBoard(self):
        print("Printing board")
        for i in range(self.w):
            #index= elem
            for j in range(self.h):
                print(self.board[i][j] , end= " ")
            print(end="\n")

    def location_of_black(self):
        self.list_of_black.clear()
        for i in range(self.w):
            for j in range(self.h):
                if isinstance(self.board[i][j],Black):
                    self.list_of_black.append((i,j))


    def location_of_white(self):
        self.list_of_white.clear()
        for i in range(self.w):
            for j in range(self.h):
                if isinstance(self.board[i][j],White):
                    self.list_of_white.append((i,j))

