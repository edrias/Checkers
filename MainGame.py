#'main' where the game will be played
from GameBoard import GameBoard

game = GameBoard()
print(" Welcome to Checkeres")
print("======================")
game.initialize_emptySpaces()
game.set_gamePieces()
game.printBoard()

while(True):
    x = int(input("Enter x coordinate"))
    y = int(input("Enter y coordinate"))
    game.move(x,y)
    game.printBoard()

