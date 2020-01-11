#Abbreviations of Cubes:
#Given'XYZ'
#X is Top (T), Center (C), or Bottom (B)
#Y is Left (L), Center (C), or Right (R)
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
    pass
