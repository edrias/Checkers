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
#for debugging#player1_moves = [(5,0),(5,2),(6,1),(7,0),(5,6)]
#for debugging#player2_moves = [(2,1),(2,3),(3,0),(5,2),(7,0)]
white_valid_moves = []
black_valid_moves = []
count = 0





while(True):
    game.printBoard()
    didMove = False
    white_valid_moves.clear()
    game.location_of_white()

    for i in range(len(game.list_of_white)):
        coordinates = game.list_of_white[i]
        #print("Coordinates {0}".format(coordinates))
        if game.check_valid_move( coordinates[0],coordinates[1], White, Black,):
            white_valid_moves.append(coordinates)


    if len(white_valid_moves) == 0:
        print("Player 2 Wins!")
        break# game over

    while(didMove == False):
        print("Player ones turn")
        print("Here are your valid moves")
        print(white_valid_moves)

        choice = int(input("Enter a choice corresponding to the index of the list"))


        move = white_valid_moves[0]
        coordinates = game.list_of_white[choice]
        print("Move {0}".format(move))

        didMove = game.move(coordinates[0],coordinates[1], White, Black)
        game.printBoard()


    didMove = False
    game.location_of_black()
    black_valid_moves.clear()
    for i in range(len(game.list_of_black)):
        coordinates = game.list_of_black[i]
        #print("Coordinates {0}".format(coordinates))
        if game.check_valid_move(coordinates[0],coordinates[1], Black, White):
            black_valid_moves.append(coordinates)
    if len(black_valid_moves) == 0:
        print("Player 1 Wins!")
        break


    while(didMove == False):
        print("Player twos turn")
        print("Here are your valid moves")
        print(black_valid_moves)

        choice = int(input("Enter a choice corresponding to the index of the list"))

        move = black_valid_moves[choice]
        print("Move {0}".format(move))


        didMove = game.move(coordinates[0],coordinates[1], Black, White)

        #game.printBoard()

    #count+=1
