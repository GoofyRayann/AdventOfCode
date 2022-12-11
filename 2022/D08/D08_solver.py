import re
import myLib

DAY           = "D08"
inputTestFile = DAY + "_puzzle_test.txt"
inputFile     = DAY + "_puzzle_test.txt"

# --------------------------------------------------------------------------------------------------
class Patch:
    def __init__(self, inputFile):
        self.patch   = myLib.input_as_list_of_horizontal_list_of_ints(inputFile)
        self.width   = len(self.patch[0])
        self.height  = len(self.patch)
        self.lines   = [ [-1] + line + [-1] for line in self.patch]
        self.columns = [ [-1] + [line[col]  for line in self.patch] + [-1] for col in range(0, self.height) ]

    def isTreeVisible( self, x, y ):
        tree = self.patch[y][x]
        if any(t >= tree for t in self.lines[y][0: x + 1]) \
            and any(t >= tree for t in self.lines[y][x + 2:]) \
            and any(t >= tree for t in self.columns[x][0: y + 1]) \
            and any(t >= tree for t in self.columns[x][y + 2:]):
            return False
        return True

    def getNumberOfTreesViewd(self , x,y, trees):
        tree = self.patch[y][x]
        viewedTrees=0
        for t in trees:
            if t == -1  :  return viewedTrees
            viewedTrees += 1
            if t >= tree:  return viewedTrees
        return viewedTrees

    def getLeftTreesViewed(self, x,y):
        return  self.getNumberOfTreesViewd( x,y, self.lines[y][0: x + 1][::-1])

    def getRightTreesViewed(self, x,y):
       return  self.getNumberOfTreesViewd( x,y, self.lines[y][x + 2:])

    def getTopTreesViewed(self, x,y):
        return  self.getNumberOfTreesViewd( x,y, self.columns[x][0: y + 1][::-1])

    def getBottomTreesViewed(self, x,y):
        return  self.getNumberOfTreesViewd( x,y, self.columns[x][y + 2:])

# --------------------------------------------------------------------------------------------------
def Puzzle_1(inputFile):
    patch = Patch( inputFile )
    count = 0
    for x in range(0,patch.width):
        for y in range(0,patch.height):
            count += 1 if patch.isTreeVisible( x,y) else 0
    return count

def Puzzle_2(inputFile):
    patch = Patch(inputFile)
    scores=[]
    for x in range(0,patch.width):
        for y in range(0,patch.height):
            scores.append( patch.getLeftTreesViewed(x, y) *
                  patch.getRightTreesViewed(x, y) *
                  patch.getTopTreesViewed(x, y) *
                  patch.getBottomTreesViewed(x, y))
    return max(scores)

# --------------------------------------------------------------------------------------------------
myLib.display_header(DAY, inputFile)

myLib.display_result("1", str(Puzzle_1(inputFile)))
myLib.display_result("2", str(Puzzle_2(inputFile)))

myLib.display_footer()
