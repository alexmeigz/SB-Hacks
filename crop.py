# Improting Image class from PIL module 
from PIL import Image 
import cv2



  
#webcamImgs = ["capture1.jpg", "capture2.jpg", "capture3.jpg", "capture4.jpg", "capture5.jpg", "capture6.jpg"]


def cropToSize(images):

  for imgName in images:
    # Opens a image in RGB mode 
    im = Image.open(imgName) 
      
    # Size of the image in pixels (size of orginal image) 
    # (This is not mandatory) 
    width, height = im.size 

    border = height/8
    size = height - 2 * border
    # Setting the points for cropped image 
    left = (width- size)/2
    top = border
    right = width - (width - size)/2
    bottom =  height - border
      
    # Cropped image of above dimension 
    # (It will not change orginal image) 
    cubeSide = im.crop((left, top, right, bottom)) 
    print (cubeSide.size[0], cubeSide.size[1])
    cubeSide.save(imgName) # saves portion of the cube face only

def cutToTiles(images, n):
  '''Takes list of images, cuts each to n times n pieces, 
      and return cubeface objects according to color of center piece'''
  cubeFaces = {}
  for imgName in images:
    tiles = [[],[],[]]
    image = Image.open(imgName)
    w, h = image.size

    for i in range(n):
      for j in range(n):
        tiles[i].append(image.crop(((i * w/3), (j * h/3), ((i + 1) * w/3), ((j + 1) * h/3))))

        #ToDo: pass into face object for storage and add it to dictionary cubeFace

        #tiles[i][j].save(imgName[:-4] + "-" + str(i) + "," + str(j) + ".jpg")
  return cubeFaces
  

