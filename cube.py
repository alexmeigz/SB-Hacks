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

        # determine what type of cubie it is
        self.type = "CENTER"
        counter = 0
        for i in [front, left, back, right, top, bottom]:
            if i is not None:
                counter += 1
        if counter == 3:
            self.type = "CORNER"
        elif counter == 2:
            self.type = "EDGE"



    def rotateUp(self):
        '''rotates cube upward'''
        temp = self.bottomFace
        self.bottomFace = self.backFace
        self.backFace = self.topFace
        self.topFace = self.frontFace
        self.frontFace = temp


    def rotateDown(self):
        '''rotates cube downward'''
        temp = self.topFace
        self.topFace = self.backFace
        self.backFace = self.bottomFace
        self.bottomFace = self.frontFace
        self.frontFace = temp

    def rotateLeft(self):
        '''rotates cube leftward'''
        temp = self.rightFace
        self.rightFace = self.backFace
        self.backFace = self.leftFace
        self.leftFace = self.frontFace
        self.frontFace = temp

    def rotateRight(self):
        '''rotates cube rightward'''
        temp = self.leftFace
        self.leftFace = self.backFace
        self.backFace = self.rightFace
        self.rightFace = self.frontFace
        self.frontFace = temp

    def rotateClockwise(self):
        temp = self.topFace
        self.topFace = self.leftFace
        self.leftFace = self.bottomFace
        self.bottomFace = self.rightFace
        self.rightFace = temp

    def rotateCounterClockwise(self):
        temp = self.topFace
        self.topFace = self.rightFace
        self.rightFace = self.bottomFace
        self.bottomFace = self.leftFace
        self.leftFace = temp

    def __str__(self):
        return ("Front Face: " + str(self.frontFace) +
                "\nLeft Face: " + str(self.leftFace) +
                "\nBack Face: " + str(self.backFace) +
                "\nRight Face: " + str(self.rightFace) +
                "\nTop Face: " + str(self.topFace) +
                "\nBottom Face: " + str(self.bottomFace))
        
