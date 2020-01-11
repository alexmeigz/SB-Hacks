#ALL ORIENTATIONS ARE WITH RESPECT TO THE FRONT FACING SIDE

class Cube:
    frontFace = None
    leftFace = None
    backFace = None
    rightFace = None
    topFace = None
    bottomFace = None

    def __init__(self, front, left, back, right, top, bottom):
        self.frontFace = front
        self.leftFace = left
        self.backFace = back
        self.rightFace = right
        self.topFace = top
        self.bottomFace = bottom

    def rotateUp(self):
        '''rotates cube upward'''
        temp = self.bottomFace
        self.topFace = self.frontFace
        self.backFace = self.topFace
        self.bottomFace = self.backFace
        self.frontFace = temp

    def rotateDown(self):
        '''rotates cube downward'''
        temp = self.topFace
        self.bottomFace = self.frontFace
        self.backFace = self.bottomFace
        self.topFace = self.backFace
        self.frontFace = temp

    def rotateLeft(self):
        '''rotates cube leftward'''
        temp = self.rightFace
        self.leftFace = self.frontFace
        self.backFace = self.leftFace
        self.rightFace = self.backFace
        self.frontFace = temp

    def rotateRight(self):
        '''rotates cube rightward'''
        temp = self.leftFace
        self.rightFace = self.frontFace
        self.backFace = self.rightFace
        self.leftFace = self.backFace
        self.frontFace = temp

    def __str__(self):
        return ("Front Face: " + str(self.frontFace) +
                "\nLeft Face: " + str(self.leftFace) +
                "\nBack Face: " + str(self.backFace) +
                "\nRight Face: " + str(self.rightFace) +
                "\nTop Face: " + str(self.topFace) +
                "\nBottom Face: " + str(self.bottomFace))
        
