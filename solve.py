
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
  while (checkSolve(cube)):
    for cubie in cube.pieces:
      if cube.isCorrectOrientation(cubie) or cubie.type == "CENTER":
        continue

      # TODO: Implement the solving algorithm
      elif (cubie.type == "CORNER"):
        moves.append(solveCorner(cubie))
      elif (cubie.type == "EDGE"):
        moves.append(solveEdge(cubie))



      # Simplify the moves
      if moves[-1].name == moves[-2].name:
        moves[-2].direction += moves[-1].direction
        moves.pop()

  return moves

def checkSolved(cube):
  for cubie in cube.pieces:
    if not cube.isCorrectOrientation(cubie):
      return False
  return True

def solveCorner(cubie):
  
  pass

def solveEdge(cubie):
  
  pass