#Emmanuil Simkhayev
    #White game piece
#from Black import Black

class White:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.look = "w "
        self.allMoves = [(x, y) for x in range(25) for y in range(25)]
        self.isKing = False

        #booleans for jumping
        self.down_right = True
        self.down_left = True
        self.up_right = True
        self.up_left = True

        #boolean for moving up or down.
        self.moveUp = False;
        self.moveDown = False;


    def __str__(self):
        return self.look

    def __eq__(self, other):
        return self.look == other

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
        self.down_right = True
        self.down_left = True
        self.up_right = True
        self.up_left = True

        if (self.empty_space(self.xPos - 1, self.yPos + 1, board)):
            self.validMove = True
            # add coordinates to list
            self.allMoves.append((self.xPos - 1, self.yPos + 1))
        if (self.empty_space(self.xPos - 1, self.yPos - 1, board)):
            self.validMove = True
            self.allMoves.append((self.xPos - 1, self.yPos - 1))

        if self.isKing == True:#if piece is king then we perform the check for black pieces also
            if (self.empty_space(self.xPos + 1, self.yPos + 1, board)):
                self.validMove = True
                # add coordinates to list
                self.allMoves.append((self.xPos + 1, self.yPos + 1))
            if (self.empty_space(self.xPos + 1, self.yPos - 1, board)):
                self.validMove = True
                self.allMoves.append((self.xPos + 1, self.yPos - 1))


    def can_jump_moves(self,board,enemy):
        self.canJump = False
        #print("TOP - down_right {}, down_left {}, up_right {}, up_left {}".format(self.down_right, self.down_left,self.up_right,self.up_left))
        if self.up_left == True and self.is_enemy(self.tempX -1, self.tempY -1,board,enemy):# up and left
            if self.empty_space(self.tempX -2, self.tempY -2, board):
                self.allMoves.append((self.tempX -2,self.tempY -2))
                self.validMove = True
                self.canJump = True
                self.tempX -=2
                self.tempY -=2
                #print("up left")

                self.down_right = False
                self.down_left = True
                self.up_right = True
                self.up_left = True
                #print("down_right {}, down_left {}, up_right {}, up_left {}".format(self.down_right, self.down_left,
                     #                                                               self.up_right, self.up_left))
                self.can_jump_moves(board,enemy)



        if self.up_right == True and self.is_enemy(self.tempX-1, self.tempY +1, board,enemy):# up and right
            if self.empty_space(self.tempX -2, self.tempY +2, board):
                self.allMoves.append((self.tempX -2, self.tempY +2))
                self.validMove = True
                self.canJump = True
                self.tempX -=2
                self.tempY +=2
                #print("up right")
                self.down_left = False
                self.down_right = True
                self.up_right = True
                self.up_left = True
                #print("down_right {}, down_left {}, up_right {}, up_left {}".format(self.down_right, self.down_left,
                 #                                                                   self.up_right, self.up_left))
                self.can_jump_moves(board,enemy)


        if self.down_left == True and self.isKing == True:#if isKing is true then white performs same checks as black
            if self.is_enemy(self.tempX + 1, self.tempY - 1, board, enemy):#down and left
                if self.empty_space(self.tempX + 2, self.tempY - 2, board):
                    self.allMoves.append((self.tempX + 2, self.tempY - 2))
                    self.validMove = True
                    self.canJump = True
                    self.tempX += 2
                    self.tempY -= 2
                    #print("King down left")
                    self.up_right = False
                    self.down_right = True
                    self.down_left = True
                    self.up_left = True
                    #print("down_right {}, down_left {}, up_right {}, up_left {}".format(self.down_right, self.down_left,
                     #                                                                   self.up_right, self.up_left))
                    self.can_jump_moves(board, enemy)


            if self.down_right == True and self.is_enemy(self.tempX + 1, self.tempY + 1, board, enemy):
                if self.empty_space(self.tempX + 2, self.tempY + 2, board):#down and right
                    self.allMoves.append((self.tempX + 2, self.tempY + 2))
                    self.validMove = True
                    self.canJump = True
                    self.tempX += 2
                    self.tempY += 2
                    #print("King down right")

                    self.up_left = False
                    self.down_right = True
                    self.down_left = True
                    self.up_left = True
                    #print("down_right {}, down_left {}, up_right {}, up_left {}".format(self.down_right, self.down_left,
                     #                                                                   self.up_right, self.up_left))
                    self.can_jump_moves(board, enemy)

        #self.tempX = self.xPos
        #self.tempY = self.yPos

    def is_enemy(self, xPos, yPos, board,enemy):
        if yPos < 0 or yPos >7 or xPos <0 or xPos >7:
            return False
        if isinstance(board[xPos][yPos],enemy):
            return True
        return False

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

    def checkKing(self):
        #print("White In checkKing method")
        if self.xPos == 0:
            self.isKing = True
            self.look = "wK "

    def move_piece(self, board, choice):
        if (self.validMove == False):
            print('White piece {0} , {1} has no moves'.format(self.getX(), self.getY()))
            return board
        else:
            coordinates = self.allMoves[choice]#the new coordinates
            index = abs(self.xPos - coordinates[0])# distance from current point to new point
            if (self.xPos > coordinates[0]): #piece is moving up
                self.moveUp = True
            if(self.xPos < coordinates[0]): #piece is moving down
                self.moveDown = True


            for i in range(index):
                board[self.xPos][self.yPos] = ". "
                print("*ycoord = {0} currcoords = {1}".format(coordinates[1], self.yPos))

                if self.moveUp == True:
                    if coordinates[1] > self.yPos:
                        print("ycoord = {0} currcoords = {1}".format(coordinates[1],self.yPos))
                        print("moving left and up")
                        self.setX(self.xPos - 1)
                        self.setY(self.yPos + 1)

                    else:
                        print("ycoord = {0} currcoords = {1}".format(coordinates[1], self.yPos))
                        print("moving right and up")
                        self.setX(self.xPos - 1)
                        self.setY(self.yPos - 1)

                if self.moveDown == True:
                    for i in range(index):
                        if coordinates[1] > self.yPos:
                            board[self.xPos][self.yPos] = ". "
                            self.setX(self.xPos + 1)
                            self.setY(self.yPos + 1)
                            print('{0}, {1}'.format(self.getX(), self.getY()))
                        else:
                            board[self.xPos][self.yPos] = ". "
                            self.setX(self.xPos + 1)
                            self.setY(self.yPos - 1)
                            print('{0}, {1}'.format(self.getX(), self.getY()))


                #list.append((self.getX(), self.getY()))
            print('{0}, {1}'.format(self.getX(), self.getY()))
                #print('{0}, {1}'.format(self.getX(), self.getY()))
        print(list)
        self.setX(coordinates[0])
        self.setY(coordinates[1])
        board[self.getX()][self.getY()] = self
        self.allMoves.clear()

        return board


