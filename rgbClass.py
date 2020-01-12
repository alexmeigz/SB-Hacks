class RGB:
    red = 0
    green = 0
    blue = 0
    
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b
        
    def __str__(self):
        return "rgb({}, {}, {})".format(self.red, self.green, self.blue)

baseColors = {"YELLOW": RGB(235,228,27), "GREEN": RGB(50,205,50),
          "BLUE": RGB(4,61,159),  
          "WHITE": RGB(255, 255, 255), "RED": RGB(209, 35, 35),
          "ORANGE": RGB(219, 77, 6)}

def classify(color):
    classified = None
    minError = 200000
    for c in list(baseColors.values()):
        if ste(c, color) < minError:
            classified = c
            minError = ste(c, color)
    return classified
                
def ste(expC, actC):
        return (error_square(expC.red, actC.red) +
                error_square(expC.green, actC.green) +
                error_square(expC.blue, actC.blue) )**(0.5)

def error_square(exp, act):
        return (exp - act)**2
