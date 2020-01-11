#Abbreviations of Cubes:
#Given'YXZ'
#Y is Top (T), Center (C), or Bottom (B)
#X is Left (L), Center (C), or Right (R)
#Z is Front (F), Center (C), or Back (B)

class miniRubix:
    def __init__(self, tlf, blf, trf, brf, tlb, blb, trb, brb):
        self.tlfFace = tlf
        self.blfFace = blf
        self.trfFace = trf
        self.brfFace = brf
        self.tlbFace = tlb
        self.blbFace = blb
        self.trbFace = trb
        self.brbFace = brb

    def rotateUp(col):
        '''rotate 1 col up'''
        if col == "left":
            temp = self.tlbFace
            self.tlbFace = self.tlfFace.rotateUp()
            self.tlfFace = self.blfFace.rotateUp()
            self.blfFace = self.blbFace.rotateUp()
            self.blbFace = temp.rotateUp()
        elif col == "right":
            temp = self.trbFace
            self.trbFace = self.trfFace.rotateUp()
            self.trfFace = self.brfFace.rotateUp()
            self.brfFace = self.brbFace.rotateUp()
            self.brbFace = temp.rotateUp()
        else:
            print("Invalid Column")

    def rotateDown(col):
        pass

class Rubix3:
    def __init__(self, tlf, tcf, trf, clf, ccf, crf, blf, bcf, brf,
                       tlc, tcc, trc, clc, ccc, crc, blc, bcc, brc,
                       tlb, tcb, trb, clb, ccb, crb, blb, bcb, brb, ):
        self.frontColor = "WHITE"
        self.backColor = "YELLOW"
        self.rightColor = "GREEN"
        self.leftColor = "BLUE"
        self.bottomColor = "ORANGE"
        self.topColor = "RED"

        self.tlfFace = tlf
        self.tcfFace = tcf
        self.trfFace = trf
        self.clfFace = clf
        self.ccfFace = ccf
        self.crfFace = crf
        self.blfFace = blf
        self.bcfFace = bcf
        self.brfFace = brf

        self.tlcFace = tlc
        self.tccFace = tcc
        self.trcFace = trc
        self.clcFace = clc
        self.cccFace = ccc
        self.crcFace = crc
        self.blcFace = blc
        self.bccFace = bcc
        self.brcFace = brc

        self.tlbFace = tlb
        self.tcbFace = tcb
        self.trbFace = trb
        self.clbFace = clb
        self.ccbFace = ccb
        self.crbFace = crb
        self.blbFace = blb
        self.bcbFace = bcb
        self.brbFace = brb

        self.pieces = [
            self.tlfFace,
            self.tcfFace,
            self.trfFace,
            self.clfFace,
            self.ccfFace ,
            self.crfFace ,
            self.blfFace ,
            self.bcfFace ,
            self.brfFace ,

            self.tlcFace ,
            self.tccFace,
            self.trcFace,
            self.clcFace,
            self.cccFace,
            self.crcFace ,
            self.blcFace ,
            self.bccFace,
            self.brcFace,

            self.tlbFace ,
            self.tcbFace ,
            self.trbFace,
            self.clbFace ,
            self.ccbFace ,
            self.crbFace ,
            self.blbFace ,
            self.bcbFace,
            self.brbFace

        ]


    def isCorrectOrientation(cubie):
        correctOrientation = True
        if cubie.frontFace != None:
            correctOrientation = cubie.frontFace == self.frontFace
        if cubie.backFace != None:
            correctOrientation = cubie.backFace == self.backFace
        if cubie.rightFace != None:
            correctOrientation = cubie.rightFace == self.rightFace
        if cubie.leftFace != None:
            correctOrientation = cubie.leftFace == self.leftFace
        if cubie.topFace != None:
            correctOrientation = cubie.topFace == self.topFace
        if cubie.bottomFace != None:
            correctOrientation = cubie.bottomFace == self.bottomFace
        return correctOrientation

    def rotateF(clockwise):
        '''
        Takes boolean - true is clockwise rotation, false is counterclockwise
        '''
        if clockwise:
            temp = self.tlfFace
            self.tlfFace = self.blfFace.rotateClockwise()
            self.blfFace = self.brfFace.rotateClockwise()
            self.brfFace = self.trfFace.rotateClockwise()
            self.trfFace = temp.rotateClockwise()

            temp = self.tcfFace
            self.tcfFace = self.clfFace.rotateClockwise()
            self.clfFace = self.bcfFace.rotateClockwise()
            self.bcfFace = self.crfFace.rotateClockwise()
            self.crfFace = temp.rotateClockwise()
        else:
            temp = self.tlfFace
            self.tlfFace = self.trfFace.rotateCounterClockwise()
            self.trfFace = self.brfFace.rotateCounterClockwise()
            self.brfFace = self.blfFace.rotateCounterClockwise()
            self.blfFace = temp.rotateCounterClockwise()

            temp = self.tcfFace
            self.tcfFace = self.crfFace.rotateCounterClockwise()
            self.crfFace = self.bcfFace.rotateCounterClockwise()
            self.bcfFace = self.clfFace.rotateCounterClockwise()
            self.clfFace = temp.rotateCounterClockwise()

    def rotateB(clockwise):
        if clockwise: #cube notation for B, L, and D are opposite of F, R, U faces
            temp = self.tlbFace
            self.tlbFace = self.trbFace.rotateCounterClockwise()
            self.trbFace = self.brbFace.rotateCounterClockwise()
            self.brbFace = self.blbFace.rotateCounterClockwise()
            self.blbFace = temp.rotateCounterClockwise()

            temp = self.tcbFace
            self.tcbFace = self.crbFace.rotateCounterClockwise()
            self.crbFace = self.bcbFace.rotateCounterClockwise()
            self.bcbFace = self.clbFace.rotateCounterClockwise()
            self.clbFace = temp.rotateCounterClockwise()
        else:
            temp = self.tlbFace
            self.tlbFace = self.blbFace.rotateClockwise()
            self.blbFace = self.brbFace.rotateClockwise()
            self.brbFace = self.trbFace.rotateClockwise()
            self.trbFace = temp.rotateClockwise()

            temp = self.tcbFace
            self.tcbFace = self.clbFace.rotateClockwise()
            self.clbFace = self.bcbFace.rotateClockwise()
            self.bcbFace = self.crbFace.rotateClockwise()
            self.crbFace = temp.rotateClockwise()

    def rotateR(clockwise):
        if clockwise:
            temp = self.trfFace
            self.trfFace = self.brfFace.rotateUp()
            self.brfFace = self.brbFace.rotataUp()
            self.brbFace = self.trbFace.rotateUp()
            self.trbFace = temp.rotateUp()

            temp = self.trcFace.rotateUp()
            self.trcFace = self.crfFace.rotateUp()
            self.crfFace = self.brcFace.rotateUp()
            self.brcFace = self.crbFace.rotateUp()
            self.crbFace = temp.rotateUp()
        else:
            temp = self.trfFace
            self.trfFace = self.trbFace.rotateDown()
            self.trbFace = self.brbFace.rotateDown()
            self.brbFace = self.brfFace.rotateDown()
            self.brfFace = temp.rotateDown()

            temp = self.trcFace
            self.trcFace = self.crbFace.rotateDown()
            self.crbFace = self.brcFace.rototeDown()
            self.brcFace = self.crfFace.rotateDown()
            self.crfFace = temp.rotateDown()

    def rotateL(clockwise):
         if not clockwise:
            temp = self.tlfFace
            self.tlfFace = self.blfFace.rotateUp()
            self.blfFace = self.blbFace.rotataUp()
            self.blbFace = self.tlbFace.rotateUp()
            self.tlbFace = temp.rotateUp()

            temp = self.tlcFace.rotateUp()
            self.tlcFace = self.clfFace.rotateUp()
            self.clfFace = self.blcFace.rotateUp()
            self.blcFace = self.clbFace.rotateUp()
            self.clbFace = temp.rotateUp()
        else:
            temp = self.tlfFace
            self.tlfFace = self.tlbFace.rotateDown()
            self.tlbFace = self.blbFace.rotateDown()
            self.blbFace = self.blfFace.rotateDown()
            self.blfFace = temp.rotateDown()

            temp = self.tlcFace
            self.tlcFace = self.clbFace.rotateDown()
            self.clbFace = self.blcFace.rototeDown()
            self.blcFace = self.clfFace.rotateDown()
            self.clfFace = temp.rotateDown()


    def rotateU(clockwise):
        if clockwise:
            temp = self.tlfFace
            self.tlfFace = self.trfFace.rotateLeft()
            self.trfFace = self.trbFace.rotateLeft()
            self.trbFace = self.tlbFace.rotateLeft()
            self.tlbFace = temp.rotateLeft()

            temp = self.tcfFace
            self.tcfFace = self.trcFace.rotateLeft()
            self.trcFace = self.tcbFace.rotateLeft()
            self.tcbFace = self.tlcFace.rotateLeft()
            self.tlcFace = temp.rotateLeft()
        else:
            temp = self.tlfFace
            self.tlfFace = self.tlbFace.rotateRight()
            self.tlbFace = self.trbFace.rotateRight()
            self.trbFace = self.trfFace.rotateRight()
            self.trfFace = temp.rotateRight()

            temp = self.tcfFace
            self.tcfFace = self.tlcFace.rotateRight()
            self.tlcFace = self.tcbFace.rotateRight()
            self.tcbFace = self.tlcFace.rotateRight()
            self.tlcFace = temp.rotateRight()

    def rotateD(clockwise):
        if not clockwise:
            temp = self.blfFace
            self.blfFace = self.brfFace.rotateLeft()
            self.brfFace = self.brbFace.rotateLeft()
            self.brbFace = self.blbFace.rotateLeft()
            self.blbFace = temp.rotateLeft()

            temp = self.bcfFace
            self.bcfFace = self.brcFace.rotateLeft()
            self.brcFace = self.bcbFace.rotateLeft()
            self.bcbFace = self.blcFace.rotateLeft()
            self.blcFace = temp.rotateLeft()
        else:
            temp = self.blfFace
            self.blfFace = self.blbFace.rotateRight()
            self.blbFace = self.brbFace.rotateRight()
            self.brbFace = self.brfFace.rotateRight()
            self.brfFace = temp.rotateRight()

            temp = self.bcfFace
            self.bcfFace = self.blcFace.rotateRight()
            self.blcFace = self.bcbFace.rotateRight()
            self.bcbFace = self.blcFace.rotateRight()
            self.blcFace = temp.rotateRight()








