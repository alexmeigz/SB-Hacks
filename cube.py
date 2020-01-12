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


        self.targetOrientation = [0,0,0]
        # {top, right, front}
        colorDict = {"RED": [1,0,0], "GREEN": [0,2,0], "WHITE": [0,0,3], 
                        "ORANGE": [-1,0,0], "BLUE": [0,-2,0], "YELLOW": [0,0,-3]}

        for i in [front, left, back, right, top, bottom]:
            if i is not None:
                r = colorDict[i]
                self.targetOrientation[0] += r[0]
                self.targetOrientation[1] += r[1]
                self.targetOrientation[2] += r[2]

        orientationDict = {"RED": 1, "GREEN": 2, "WHITE": 3, "ORANGE": -1, "BLUE": -2, "YELLOW": -3}

        self.currentOrientation = [0,0,0]
        if front is not None:
            self.currentOrientation[2] = orientationDict[front]
        elif back is not None:
            self.currentOrientation[2] = orientationDict[back]

        if right is not None:
            self.currentOrientation[1] = orientationDict[right]
        elif left is not None:
            self.currentOrientation[1] = orientationDict[left]

        if top is not None:
            self.currentOrientation[0] = orientationDict[top]
        elif bottom is not None:
            self.currentOrientation[0] = orientationDict[bottom]






    def rotateUp(self):
        '''rotates cube upward'''
        temp = self.bottomFace
        self.bottomFace = self.backFace
        self.backFace = self.topFace
        self.topFace = self.frontFace
        self.frontFace = temp

        temp = self.currentOrientation[2]
        self.currentOrientation[2] = -self.currentOrientation[0]
        self.currentOrientation[0] = temp


    def rotateDown(self):
        '''rotates cube downward'''
        temp = self.topFace
        self.topFace = self.backFace
        self.backFace = self.bottomFace
        self.bottomFace = self.frontFace
        self.frontFace = temp

        temp = self.currentOrientation[0]
        self.currentOrientation[0] = -self.currentOrientation[2]
        self.currentOrientation[2] = temp

    def rotateLeft(self):
        '''rotates cube leftward'''
        temp = self.rightFace
        self.rightFace = self.backFace
        self.backFace = self.leftFace
        self.leftFace = self.frontFace
        self.frontFace = temp

        temp = self.currentOrientation[2]
        self.currentOrientation[2] = self.currentOrientation[1]
        self.currentOrientation[1] = -temp

    def rotateRight(self):
        '''rotates cube rightward'''
        temp = self.leftFace
        self.leftFace = self.backFace
        self.backFace = self.rightFace
        self.rightFace = self.frontFace
        self.frontFace = temp

        temp = self.currentOrientation[1]
        self.currentOrientation[1] = self.currentOrientation[2]
        self.currentOrientation[2] = -temp

    def rotateClockwise(self):
        temp = self.topFace
        self.topFace = self.leftFace
        self.leftFace = self.bottomFace
        self.bottomFace = self.rightFace
        self.rightFace = temp

        temp = self.currentOrientation[0]
        self.currentOrientation[0] = -self.currentOrientation[1]
        self.currentOrientation[1] = temp

    def rotateCounterClockwise(self):
        temp = self.topFace
        self.topFace = self.rightFace
        self.rightFace = self.bottomFace
        self.bottomFace = self.leftFace
        self.leftFace = temp

        temp = self.currentOrientation[1]
        self.currentOrientation[1] = -self.currentOrientation[0]
        self.currentOrientation[0] = temp

    def __str__(self):
        return ("Front Face: " + str(self.frontFace) +
                "\nLeft Face: " + str(self.leftFace) +
                "\nBack Face: " + str(self.backFace) +
                "\nRight Face: " + str(self.rightFace) +
                "\nTop Face: " + str(self.topFace) +
                "\nBottom Face: " + str(self.bottomFace))
        
