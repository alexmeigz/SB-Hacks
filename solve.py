
from rubix import *
from cube import *

class Move:
  def __init__(self, n, d = 1):
    '''
    name: R = Right side
    direction: 1 =  90 clockwise, 2 = 180 clockwise, -1 = 90 counterclockwise
    '''
    self.name = n
    self.direction = d




def solveCube(cube):
  moves = []
  while (checkSolve(cube)):

    #for cubie in cube.pieces:
      if cube.isCorrectOrientation(cubie) or cubie.type == "CENTER":
        continue

      # TODO: Implement the solving algorithm
      elif (cubie.type == "CORNER"):
        r = solveCorner(cube)
        if r is not None:
          moves.append(r)
      elif (cubie.type == "EDGE"):
        r = solveEdge(cube)
        if r is not None:
          moves.append(r)



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

def getSwapCornerMoves(buffer, target):
  '''
  returns the sequence of moves to swap two pieces
  '''

  # TODO: Find setup moves, then alg, then undo setup moves

  pass

def getSwapEdgeMoves(buffer, target):
  pass

  

def cornersLeft(cube):
  for i in range(len(cube.allPieces)):
    if cube.allPieces[i].type == "CORNER" and not cube.allPieces[i].targetOrientation == cube.allPieces[i].currentOrientation:
      return cube.allPieces[i]
  return None

def edgesLeft(cube):
  for i in range(len(cube.allPieces)):
    if cube.allPieces[i].type == "EDGE" and not cube.allPieces[i].targetOrientation == cube.allPieces[i].currentOrientation:
      return cube.allPieces[i]
  return None


def solveCorner(cube):
  while (cornersLeft(cube) is not None):
    cubie = cube.getPiece(1, -1, -1)
    # cubieTarget = cubie.targetOrientation
    # cubieCurrent = cubie.currentOrientation
    # diff = [cubieTarget[0] - cubieCurrent[0], cubieTarget[1] - cubieCurrent[1], cubieTarget[2] - cubieCurrent[2]]
    
    return getSwapCornerMoves(cubie, cornersLeft(cube))

  return None


def solveEdge(cube):
  while (edgesLeft(cube) is not None):
    cubie = cube.getPiece(1, 1, 0)
   
    return getSwapEdgeMoves(cubie, edgesLeft(cube))

  return None
    