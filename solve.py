
from rubix import *

class Move:
  def __init__(self, n, d):
    '''
    name: R = Right side
    direction: 1 =  90 clockwise, 2 = 180 clockwise, -1 = 90 counterclockwise
    '''
    self.name = n
    self.direction = d



def solveCube(cube):
  moves = []
  for cubie in cube.pieces:
    if cube.isCorrectOrientation(cubie) or cubie.type == "CENTER":
      continue
    elif (cubie.type == "CORNER"):
      moves.append(solveCorner(cubie))
    elif (cubie.type == "EDGE"):
      moves.append(solveEdge(cubie))
  return moves

def solveCorner(cubie):
  # just return the moves using old pochman
  pass

def solveEdge(cubie):
  # just return the moves using old pochman
  pass