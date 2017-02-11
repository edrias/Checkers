#'main' where the game will be played
from GameBoard import GameBoard

game = GameBoard()
print(" Welcome to Checkeres")
print("======================")
game.initialize_emptySpaces()
game.set_gamePieces()
game.printBoard()

while(True):
    didMove = False
    while(didMove == False):
        print("Player ones turn")
        x = int(input("Enter x coordinate"))
        y = int(input("Enter y coordinate"))
        #game.move_white(x,y)
        didMove = game.move_white(x,y)
        game.printBoard()


    didMove = False
    while(didMove == False):
        print("Player twos turn")
        x = int(input("Enter x coordinate"))
        y = int(input("Enter y coordinate"))
        didMove = game.move_black(x,y)
        game.printBoard()



