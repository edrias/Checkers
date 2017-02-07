#Emmanuil Simkhayev
    #White game piece

class White:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.look = "w "

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



white =White(0,0)
white.setX(12)
white.setY(10)
#print('{0} {1} {2}'.format("coordinates:", white.getX(),white.getY()))