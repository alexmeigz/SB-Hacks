
from webcam import takePic
from crop import *


def main():
  # Takes the raw images from the webcam
  takePic()


  webcamImgs = ["capture1.jpg", "capture2.jpg", "capture3.jpg", "capture4.jpg", "capture5.jpg", "capture6.jpg"]
  cropToSize(webcamImgs)        # crop to correct size
  cutToTiles(webcamImgs, 3)     # make the 9 different tiles

if __name__ == "__main__":
  main()