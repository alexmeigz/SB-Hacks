import pandas as pd

from cube import *
from rubix import *
from rgbClass import *
from colorDetection import *

def readImages():
    colNames = ["Image", "Red", "Green", "Blue"]
    df = pd.DataFrame(columns = colNames)

    for i in range(6):
        for j in range(3):
            for k in range(3):
                img = "CroppedPhotos/capture{}-{},{}.jpg".format(i+1, j, k)
                rgb = detect_properties(img)
                df.loc[i*9+j*3+k] = [img, rgb.red, rgb.green, rgb.blue]
    df.to_csv('dataframe.csv', index=True, header=True)

def readColors():
    df = pd.read_csv("colors.csv", index_col=0)
    colorCol = df['Predicted']
    #print(list(colorCol))
    lyst = []
    for i in range(6):
        face = []
        for j in range(3):
            row = []
            for k in range(3):
                row.append(colorCol[i*9+j*3+k])
            face.append(row)
        lyst.append(face)
    return lyst

def convert(lyst):
    '''lyst is a list of faces (3x3 matrices of colors(str)), where lyst[0] has the blue center,
    lyst[1] has the white center, lyst[2] has the green center, lyst[3] has the
    yellow center, lyst[4] has the red center, and lyst[5] has the orange center'''

    #front top row
    tlf = Cube(lyst[1][0][0], lyst[0][0][2], None, None, lyst[4][2][0], None)
    tcf = Cube(lyst[1][0][1], None, None, None, lyst[4][2][1], None)
    trf = Cube(lyst[1][0][2], None, None, lyst[2][0][0], lyst[4][2][2], None)

    #front center row
    clf = Cube(lyst[1][1][0], lyst[0][1][2], None, None, None, None)
    ccf = Cube(lyst[1][1][1], None, None, None, None, None)
    crf = Cube(lyst[1][1][2], None, None, lyst[2][1][0], None, None)

    #front bottom row
    blf = Cube(lyst[1][2][0], lyst[0][2][2], None, None, None, lyst[5][0][0])
    bcf = Cube(lyst[1][2][1], None, None, None, None, lyst[5][0][1])
    brf = Cube(lyst[1][2][2], None, None, lyst[2][2][0], None, lyst[5][0][2])

    #center top row
    tlc = Cube(None, lyst[0][0][1], None, None, lyst[4][1][0], None)
    tcc = Cube(None, None, None, None, lyst[4][1][1], None)
    trc = Cube(None, None, None, lyst[2][0][1], lyst[4][1][2], None)

    #center center row
    clc = Cube(None, lyst[0][1][1], None, None, None, None)
    ccc = Cube(None, None, None, None, None, None)
    crc = Cube(None, None, None, lyst[2][1][1], None, None)

    #center bottom row
    blc = Cube(None, lyst[0][2][1], None, None, None, lyst[5][1][0])
    bcc = Cube(None, None, None, None, None, lyst[5][1][1])
    brc = Cube(None, None, None, lyst[2][2][1], None, lyst[5][1][2])

    #back top row
    tlb = Cube(None, lyst[0][0][0], lyst[3][0][2], None, lyst[4][0][0], None)
    tcb = Cube(None, None, lyst[3][0][1], None, lyst[4][0][1], None)
    trb = Cube(None, None, lyst[3][0][0], lyst[2][0][2], lyst[4][0][2], None)

    #back center row
    clb = Cube(None, lyst[0][1][0], lyst[3][1][2], None, None, None)
    ccb = Cube(None, None, lyst[3][1][1], None, None, None)
    crb = Cube(None, None, lyst[3][1][0], lyst[2][1][2], None, None)

    #back bottom row
    blb = Cube(None, lyst[0][2][0], lyst[3][2][2], None, None, lyst[5][2][0])
    bcb = Cube(None, None, lyst[3][2][1], None, None, lyst[5][2][1])
    brb = Cube(None, None, lyst[3][2][0], lyst[2][2][2], None, lyst[5][2][2])

    return Rubix(tlf, tcf, trf, clf, ccf, crf, blf, bcf, brf,
                 tlc, tcc, trc, clc, ccc, crc, blc, bcc, brc,
                 tlb, tcb, trb, clb, ccb, crb, blb, bcb, brb)

#lyst = readColors()
#rubixCube = convert(lyst)
