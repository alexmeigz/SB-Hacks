from webcam import takePic
from crop import *
from conversions import *
import pandas as pd
from sklearn.cluster import KMeans

#kmeans predictions
kmeans = KMeans(n_clusters=6)
df = pd.read_csv("training.csv", index_col=0)
kmeans.fit(df[['Red','Green','Blue']])
df["Fitted"] = kmeans.labels_
colors = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'WHITE']
d = {}
for color in colors:
    d[df[df['Actual'] == color]["Fitted"].mode()[0]] = color

def predictColors(filename):
    df2 = pd.read_csv(filename, index_col=0)
    df2["Predicted"] = kmeans.predict(df2[['Red', 'Green', 'Blue']])
    df2["Predicted"] = df2["Predicted"].apply(lambda x: d.get(x))
    df2.to_csv('colors.csv', index=True, header=True)
    
def main():
  # Takes the raw images from the webcam
  takePic()

  webcamImgs = ["capture1.jpg", "capture2.jpg", "capture3.jpg", "capture4.jpg", "capture5.jpg", "capture6.jpg"]
  cropToSize(webcamImgs)         # crop to correct size
  cutToTiles(webcamImgs, 3)      # make the 9 different tiles
  readImages()                   # reads cropped images, converts into dataframe.csv
  predictColors("dataframe.csv") # predicts colors of tiles into color.csv
  colorLyst = readColors()       # reads colors and arranges into appropriate faces (lyst)
  rubixCube = convert(colorLyst) # coverts colorLyst into rubixCube
  

if __name__ == "__main__":
  main()
