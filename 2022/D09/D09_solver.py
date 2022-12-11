import re
import myLib

DAY           = "D09"
inputTestFile = DAY + "_puzzle_test.txt"
inputFile     = DAY + "_puzzle.txt"

moves   = { (0,2) :(0,1) ,(1,2)  :(1,1) ,(2,2):(1,1)     ,(2,1):(1,1),
            (2,0) :(1,0) ,(2,-1) :(1,-1) ,(2,-2):(1,-1)  ,(1,-2):(1,-1),
            (0,-2):(0,-1),(-1,-2):(-1,-1),(-2,-2):(-1,-1),(-2,-1):(-1,-1),
            (-2,0):(-1,0),(-2,1) :(-1,1) ,(-2,2):(-1,1)  ,(-1,2):(-1,1)}

rules   = { "U": (0,1), "D": (0,-1), "L": (-1,0), "R": (1,0) }

# --------------------------------------------------------------------------------------------------
class Knot:
    def __init__(self, x,y ):
        self.x = x
        self.y = y

    def move(self , dx,dy):
        self.x += dx
        self.y += dy

    def follow(self , head ):
        dx = head.x - self.x
        dy = head.y - self.y
        mx,my=0,0
        if  (dx,dy) in moves:
            (mx,my) = moves[(dx,dy)]
        self.move(mx,my)
        return ( self.x, self.y)

class Rope:
    def __init__(self,numKnots):
        self.knots = [Knot(0,0) for i in range ( numKnots)]
        self.visited = {}

    def moveKnots(self, dx,dy ):
        self.knots[0].move(dx,dy)
        for knotId in range( 1, len(self.knots)):
            self.knots[knotId].follow( self.knots[knotId-1])
        self.traceVisited( self.knots[len(self.knots)-1])
        return

    def traceVisited(self, knot ):
        self.visited[ (knot.x,knot.y)] = True
        return

    def computeMoves(self, inputFile):
        for move in myLib.input_as_lines(inputFile):
            direction = move.split(' ')[0]
            loop      = int( move.split(' ')[1] )
            for i in range( 0,loop):
                (dx,dy) = rules[direction]
                self.moveKnots( dx,dy )
        return

# --------------------------------------------------------------------------------------------------
def Puzzle_1(inputFile):
    rope = Rope(2)
    rope.computeMoves(inputFile)
    return  len( rope.visited )

def Puzzle_2(inputFile):
    rope = Rope(10)
    rope.computeMoves(inputFile)
    return  len( rope.visited )

# --------------------------------------------------------------------------------------------------
myLib.display_header(DAY, inputFile)

myLib.display_result("1", str(Puzzle_1(inputFile)))
myLib.display_result("2", str(Puzzle_2(inputFile)))

myLib.display_footer()
