#Emmanuil Simkhayev
    #White game piece

class White:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.look = "w "
        self.allMoves = [(x, y) for x in range(25) for y in range(25)]

    def __str__(self):
        return self.look

    def setX(self, xPos):
        self.xPos = xPos

    def getX(self):
        return self.xPos

    def setY(self, yPos):
        self.yPos = yPos

    def getY(self):
        return self.yPos

    def get_valid_moves(self, board):
        self.allMoves.clear()
        self.tempX = self.xPos
        self.tempY = self.yPos
        self.validMove = False

        if (self.empty_space(self.xPos - 1, self.yPos + 1, board)):
            self.validMove = True
            # add coordinates to list
            self.allMoves.append((self.xPos - 1, self.yPos + 1))
        if (self.empty_space(self.xPos - 1, self.yPos - 1, board)):
            self.validMove = True
            self.allMoves.append((self.xPos - 1, self.yPos - 1))

    def empty_space(self, xPos, yPos, board):
        if yPos < 0 or yPos > 7 or xPos < 0 or xPos > 7:
            return False
        if board[xPos][yPos] == ". ":
            return True

        return False

    def print_valid_moves(self):
        count = 0
        for elem in self.allMoves:
            print("{0}. {1}".format(count, elem))
            count += 1

    def move_piece(self, board, choice):
        if (self.validMove == False):
            print('Black piece {0} , {1} has no moves'.format(self.getX(), self.getY()))
            return board
        else:
            coordinates = self.allMoves[choice]
            index = abs(self.yPos - coordinates[1])

            for i in range(index):
                board[self.xPos][self.yPos] = ". "
                if coordinates[1] > self.yPos:
                    self.setX(self.xPos - 1)
                    self.setY(self.yPos + 1)
                else:
                    self.setX(self.xPos - 1)
                    self.setX(self.yPos - 1)

                self.setX(coordinates[0])
                self.setY(coordinates[1])
                board[self.getX()][self.getY()] = self
                self.allMoves.clear()

        return board

