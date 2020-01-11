import pandas as pd
from rgb import *
from colorDectection import *

def readImages():
    colNames = ["Image", "Red", "Green", "Blue"]
    df = pd.DataFrame(columns = colNames)
    
    for i in range(6):
        for j in range(3):
            for k in range(3):
                img = "set3/capture{}-{},{}.jpg".format(i+1, j, k)
                rgb = detect_properties(img)
                df.loc[i*9+j*3+k] = [img, rgb.red, rgb.green, rgb.blue]
    df.to_csv('dataframe.csv', index=True, header=True)

                
                
