from rubix import *
from cube import *

def cubeToData(c):
    data = []
    for cubie in c.allPieces:
        if c.isCorrectOrientation(cubie):
            data.append(1)
        else:
            data.append(0)
    return data

