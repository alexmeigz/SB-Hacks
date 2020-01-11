# Improting Image class from PIL module 
from PIL import Image 
import cv2
  
webcamImgs = ["capture1.jpg", "capture2.jpg", "capture3.jpg", "capture4.jpg", "capture5.jpg", "capture6.jpg"]

for imgName in webcamImgs:
  # Opens a image in RGB mode 
  im = Image.open(imgName) 
    
  # Size of the image in pixels (size of orginal image) 
  # (This is not mandatory) 
  width, height = im.size 

    
  # Setting the points for cropped image 
  left = height/8
  top = height/8
  right = 7 * height / 8
  bottom =  7* height / 8
    
  # Cropped image of above dimension 
  # (It will not change orginal image) 
  cubeSide = im.crop((left, top, right, bottom)) 

  cubeSide.save("imageSide.jpg") # saves portion of the cube face only

  # Shows the image in image viewer 
  #imageCube.show()

  # Cuts the pictures into 9 different color tiles
  colorTileImage = [[], [], []]

  w, h = cubeSide.size

  for i in range(3):
    for j in range(3):
      colorTileImage[i].append(cubeSide.crop(((i * w/3), (j * h/3), ((i + 1) * w/3), ((j + 1) * h/3))))
      colorTileImage[i][j].save("colorTile-" + str(i) + "-" +str(j) + ".jpg")


