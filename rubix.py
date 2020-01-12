#Abbreviations of Cubes:
#Given'YXZ'
#Y is Top (T), Center (C), or Bottom (B)
#X is Left (L), Center (C), or Right (R)
#Z is Front (F), Center (C), or Back (B)

class Rubix:
    def __init__(self, tlf, tcf, trf, clf, ccf, crf, blf, bcf, brf,
                       tlc, tcc, trc, clc, ccc, crc, blc, bcc, brc,
                       tlb, tcb, trb, clb, ccb, crb, blb, bcb, brb, ):
        self.frontColor = ccf
        self.backColor = ccb
        self.rightColor = crc
        self.leftColor = clc
        self.bottomColor = bcc
        self.topColor = tcc

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

        self.pieces = [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]

        self.updatePiecesPosition()
        self.allPieces = []

        for i in range(len(self.pieces)):
            for j in range(3):
                for k in range(3):
                    self.allPieces.append(self.pieces[i][j][k])

    def getPiece(t, r, f):
        return self.pieces[-t + 1][-r + 1][-f + 1]

    def updatePiecesPosition(self):
        self.pieces[0][2][0] = self.tlfFace
        self.pieces[0][1][0] = self.tcfFace
        self.pieces[0][0][0] = self.trfFace
        self.pieces[1][2][0] = self.clfFace
        self.pieces[1][1][0] = self.ccfFace
        self.pieces[1][0][0] = self.crfFace
        self.pieces[2][2][0] = self.blfFace
        self.pieces[2][1][0] = self.bcfFace
        self.pieces[2][0][0] = self.brfFace

        self.pieces[0][2][1] = self.tlcFace
        self.pieces[0][1][1] = self.tccFace
        self.pieces[0][0][1] = self.trcFace
        self.pieces[1][2][1] = self.clcFace
        self.pieces[1][1][1] = self.cccFace
        self.pieces[1][0][1] = self.crcFace
        self.pieces[2][2][1] = self.blcFace
        self.pieces[2][1][1] = self.bccFace
        self.pieces[2][0][1] = self.brcFace

        self.pieces[0][2][2] = self.tlbFace
        self.pieces[0][1][2] = self.tcbFace
        self.pieces[0][0][2] = self.trbFace
        self.pieces[1][2][2] = self.clbFace
        self.pieces[1][1][2] = self.ccbFace
        self.pieces[1][0][2] = self.crbFace
        self.pieces[2][2][2] = self.blbFace
        self.pieces[2][1][2] = self.bcbFace
        self.pieces[2][0][2] = self.brbFace


    def isCorrectOrientation(self, cubie):
        correctOrientation = True
        if cubie.frontFace is not None:
            correctOrientation = cubie.frontFace == self.frontColor
        if cubie.backFace is not None:
            correctOrientation = cubie.backFace == self.backColor
        if cubie.rightFace is not None:
            correctOrientation = cubie.rightFace == self.rightColor
        if cubie.leftFace is not None:
            correctOrientation = cubie.leftFace == self.leftColor
        if cubie.topFace is not None:
            correctOrientation = cubie.topFace == self.topColor
        if cubie.bottomFace is not None:
            correctOrientation = cubie.bottomFace == self.bottomColor
        return correctOrientation

    def rotateF(self, clockwise):
        '''
        Takes boolean - true is clockwise rotation, false is counterclockwise
        '''
        if clockwise:
            temp = self.tlfFace
            self.tlfFace = self.blfFace
            self.blfFace = self.brfFace
            self.brfFace = self.trfFace
            self.trfFace = temp

            self.tlfFace.rotateClockwise()
            self.blfFace.rotateClockwise()
            self.brfFace.rotateClockwise()
            self.trfFace.rotateClockwise()

            temp = self.tcfFace
            self.tcfFace = self.clfFace
            self.clfFace = self.bcfFace
            self.bcfFace = self.crfFace
            self.crfFace = temp

            self.tcfFace.rotateClockwise()
            self.clfFace.rotateClockwise()
            self.bcfFace.rotateClockwise()
            self.crfFace.rotateClockwise()

        else:
            temp = self.tlfFace
            self.tlfFace = self.trfFace
            self.trfFace = self.brfFace
            self.brfFace = self.blfFace
            self.blfFace = temp

            self.tlfFace.rotateCounterClockwise()
            self.trfFace.rotateCounterClockwise()
            self.brfFace.rotateCounterClockwise()
            self.blfFace.rotateCounterClockwise()

            temp = self.tcfFace
            self.tcfFace = self.crfFace
            self.crfFace = self.bcfFace
            self.bcfFace = self.clfFace
            self.clfFace = temp

            self.tcfFace.rotateCounterClockwise()
            self.crfFace.rotateCounterClockwise()
            self.bcfFace.rotateCounterClockwise()
            self.clfFace.rotateCounterClockwise()
        self.updatePiecesPosition()

    def rotateB(self, clockwise):
        if clockwise: #cube notation for B, L, and D are opposite of F, R, U faces
            temp = self.tlbFace
            self.tlbFace = self.trbFace
            self.trbFace = self.brbFace
            self.brbFace = self.blbFace
            self.blbFace = temp

            self.tlbFace.rotateCounterClockwise()
            self.trbFace.rotateCounterClockwise()
            self.brbFace.rotateCounterClockwise()
            self.blbFace.rotateCounterClockwise()

            temp = self.tcbFace
            self.tcbFace = self.crbFace
            self.crbFace = self.bcbFace
            self.bcbFace = self.clbFace
            self.clbFace = temp

            self.tcbFace.rotateCounterClockwise()
            self.crbFace.rotateCounterClockwise()
            self.bcbFace.rotateCounterClockwise()
            self.clbFace.rotateCounterClockwise()

        else:
            temp = self.tlbFace
            self.tlbFace = self.blbFace
            self.blbFace = self.brbFace
            self.brbFace = self.trbFace
            self.trbFace = temp

            self.tlbFace.rotateClockwise()
            self.blbFace.rotateClockwise()
            self.brbFace.rotateClockwise()
            self.trbFace.rotateClockwise()

            temp = self.tcbFace
            self.tcbFace = self.clbFace
            self.clbFace = self.bcbFace
            self.bcbFace = self.crbFace
            self.crbFace = temp

            self.tcbFace.rotateClockwise()
            self.clbFace.rotateClockwise()
            self.bcbFace.rotateClockwise()
            self.crbFace.rotateClockwise()
        self.updatePiecesPosition()

    def rotateR(self, clockwise):
        if clockwise:
            temp = self.trfFace
            self.trfFace = self.brfFace
            self.brfFace = self.brbFace
            self.brbFace = self.trbFace
            self.trbFace = temp

            self.trfFace.rotateUp()
            self.brfFace.rotateUp()
            self.brbFace.rotateUp()
            self.trbFace.rotateUp()

            temp = self.trcFace
            self.trcFace = self.crfFace
            self.crfFace = self.brcFace
            self.brcFace = self.crbFace
            self.crbFace = temp

            self.trcFace.rotateUp()
            self.crfFace.rotateUp()
            self.brcFace.rotateUp()
            self.crbFace.rotateUp()

        else:
            temp = self.trfFace
            self.trfFace = self.trbFace
            self.trbFace = self.brbFace
            self.brbFace = self.brfFace
            self.brfFace = temp

            temp = self.trcFace
            self.trcFace = self.crbFace
            self.crbFace = self.brcFace
            self.brcFace = self.crfFace
            self.crfFace = temp

            self.trfFace.rotateDown()
            self.trbFace.rotateDown()
            self.brbFace.rotateDown()
            self.brfFace.rotateDown()

            self.trcFace.rotateDown()
            self.crbFace.rotateDown()
            self.brcFace.rotateDown()
            self.crfFace.rotateDown()

        self.updatePiecesPosition()

    def rotateL(self, clockwise):
        if not clockwise:
            temp = self.tlfFace
            self.tlfFace = self.blfFace
            self.blfFace = self.blbFace
            self.blbFace = self.tlbFace
            self.tlbFace = temp

            self.tlfFace.rotateUp()
            self.blfFace.rotateUp()
            self.blbFace.rotateUp()
            self.tlbFace.rotateUp()

            temp = self.tlcFace
            self.tlcFace = self.clfFace
            self.clfFace = self.blcFace
            self.blcFace = self.clbFace
            self.clbFace = temp

            self.tlcFace.rotateUp()
            self.clfFace.rotateUp()
            self.blcFace.rotateUp()
            self.clbFace.rotateUp()

        else:
            temp = self.tlfFace
            self.tlfFace = self.tlbFace
            self.tlbFace = self.blbFace
            self.blbFace = self.blfFace
            self.blfFace = temp

            self.tlfFace.rotateDown()
            self.tlbFace.rotateDown()
            self.blbFace.rotateDown()
            self.blfFace.rotateDown()

            temp = self.tlcFace
            self.tlcFace = self.clbFace
            self.clbFace = self.blcFace
            self.blcFace = self.clfFace
            self.clfFace = temp

            self.tlcFace.rotateDown()
            self.clbFace.rotateDown()
            self.blcFace.rotateDown()
            self.clfFace.rotateDown()
        self.updatePiecesPosition()


    def rotateU(self, clockwise):
        if clockwise:
            temp = self.tlfFace
            self.tlfFace = self.trfFace
            self.trfFace = self.trbFace
            self.trbFace = self.tlbFace
            self.tlbFace = temp

            self.tlfFace.rotateLeft()
            self.trfFace.rotateLeft()
            self.trbFace.rotateLeft()
            self.tlbFace.rotateLeft()

            temp = self.tcfFace
            self.tcfFace = self.trcFace
            self.trcFace = self.tcbFace
            self.tcbFace = self.tlcFace
            self.tlcFace = temp

            self.tcfFace.rotateLeft()
            self.trcFace.rotateLeft()
            self.tcbFace.rotateLeft()
            self.tlcFace.rotateLeft()
        else:
            temp = self.tlfFace
            self.tlfFace = self.tlbFace
            self.tlbFace = self.trbFace
            self.trbFace = self.trfFace
            self.trfFace = temp

            self.tlfFace.rotateRight()
            self.tlbFace.rotateRight()
            self.trbFace.rotateRight()
            self.trfFace.rotateRight()

            temp = self.tcfFace
            self.tcfFace = self.tlcFace
            self.tlcFace = self.tcbFace
            self.tcbFace = self.tlcFace
            self.tlcFace = temp

            self.tcfFace.rotateRight()
            self.tlcFace.rotateRight()
            self.tcbFace.rotateRight()
            self.tlcFace.rotateRight()

        self.updatePiecesPosition()

    def rotateD(self, clockwise):
        if not clockwise:
            temp = self.blfFace
            self.blfFace = self.brfFace
            self.brfFace = self.brbFace
            self.brbFace = self.blbFace
            self.blbFace = temp

            self.blfFace.rotateLeft()
            self.brfFace.rotateLeft()
            self.brbFace.rotateLeft()
            self.blbFace.rotateLeft()

            temp = self.bcfFace
            self.bcfFace = self.brcFace
            self.brcFace = self.bcbFace
            self.bcbFace = self.blcFace
            self.blcFace = temp

            self.bcfFace.rotateLeft()
            self.brcFace.rotateLeft()
            self.bcbFace.rotateLeft()
            self.blcFace.rotateLeft()
        else:
            temp = self.blfFace
            self.blfFace = self.blbFace
            self.blbFace = self.brbFace
            self.brbFace = self.brfFace
            self.brfFace = temp

            self.blfFace.rotateRight()
            self.blbFace.rotateRight()
            self.brbFace.rotateRight()
            self.brfFace.rotateRight()

            self.bcfFace.rotateRight()
            self.blcFace.rotateRight()
            self.bcbFace.rotateRight()
            self.blcFace.rotateRight()

        self.updatePiecesPosition()
