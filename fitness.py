
from rubix import *
from cube import *

def calcFitness(cube):

  count = 0
  for cubie in cube.allPieces:
    if cube.isCorrectOrientation(cubie):
      count += 1;
  return count/20 # closer to 1 means better