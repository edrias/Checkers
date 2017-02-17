#'main' where the game will be played
from GameBoard import GameBoard
from White import White
from Black import Black

game = GameBoard()
print(" Welcome to Checkeres")
print("======================")
game.initialize_emptySpaces()
game.set_gamePieces()
game.printBoard()
player1_moves = [(5,0),(5,2),(6,1),(7,0),(5,6)]
player2_moves = [(2,1),(2,3),(3,0),(5,2),(7,0)]
count = 0





while(True):
    game.printBoard()
    didMove = False
    game.location_of_white()
    while(didMove == False):
        print("Player ones turn")
        #x = int(input("Enter x coordinate"))
        #y = int(input("Enter y coordinate"))
        #index = randint(0,len(game.list_of_white)-1)
        #game.move_white(x,y)
        move = player1_moves[count]
        #coordinates = game.list_of_white[index]

        didMove = game.move(move[0],move[1], White, Black)
        game.printBoard()


    didMove = False
    game.location_of_black()

    while(didMove == False):
        print("Player twos turn")
        #print(game.list_of_black)
        #index = randint(0,len(game.list_of_black))
        #print(index)

        #coordinates = game.list_of_black[index]
        #x = int(input("Enter x coordinate"))
        #y = int(input("Enter y coordinate"))
        move = player2_moves[count]

        didMove = game.move(move[0],move[1], Black, White)
        #didMove = game.move_black(x,y)

        #game.printBoard()

    count+=1


#NEXT IS KING PIECES!

