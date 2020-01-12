import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("/Applications/everything/SBHacks/SB-Hacks-VI/dataframe.csv")
# Preview the first 5 lines of the loaded data
# data.head()


df = pd.DataFrame(data)
red = df['Red']
green = df['Green']
blue = df['Blue']
print (df)

df = pd.DataFrame({
    'x': red,
    'y': green,
    'z': blue
})
np.random.seed(200)
k = 3
# centroids[i] = [x, y]
centroids = {
    i + 1: [np.random.randint(0, 80), np.random.randint(0, 80)]
    for i in range(k)
}

