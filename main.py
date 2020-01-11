
from webcam import takePic
from crop import *


def main():
  
  #takePic()
  webcamImgs = ["capture1.jpg", "capture2.jpg", "capture3.jpg", "capture4.jpg", "capture5.jpg", "capture6.jpg"]
  #cropToSize(webcamImgs)
  
  cutToTiles(webcamImgs, 3)

if __name__ == "__main__":
  main()