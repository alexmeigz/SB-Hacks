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

def cutToTiles(images, dimension):
  for imgName in images:
    tiles = [[],[],[]]
    image = Image.open(imgName)
    w, h = image.size

    for i in range(dimension):
      for j in range(dimension):
        tiles[i].append(image.crop(((i * w/3), (j * h/3), ((i + 1) * w/3), ((j + 1) * h/3))))

        #ToDo: pass into face object for storage
        
        #tiles[i][j].save(imgName[:-4] + "-" + str(i) + "," + str(j) + ".jpg")
  

'''
  # Shows the image in image viewer 
  #imageCube.show()

  # Cuts the pictures into 9 different color tiles
  colorTileImage = [[], [], []]

  w, h = cubeSide.size

  for i in range(3):
    for j in range(3):
      colorTileImage[i].append(cubeSide.crop(((i * w/3), (j * h/3), ((i + 1) * w/3), ((j + 1) * h/3))))
      # colorTileImage[i][j].save("colorTile-" + str(i) + "-" +str(j) + ".jpg")
  
  # Converts the color images to 
'''