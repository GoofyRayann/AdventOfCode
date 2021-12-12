import myLib
import re
from generativepy.nparray import save_nparray_image
import numpy as np

DAY       = "D7"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# ==================================================================================================

# --------------------------------------------------------------------------------------------------
def Puzzle_1( inputFile ):

    crabPositions = myLib.input_as_list_of_ints((inputFile))[0]
    computeFuel   = dict( [ (  destposition
                           , sum( [ abs(crabPosition-destposition) for crabPosition in crabPositions])
                           )
                          for destposition in range( min(crabPositions), max( crabPositions))
                          ] )

    return computeFuel[min(computeFuel, key=computeFuel.get)]

# --------------------------------------------------------------------------------------------------
def Puzzle_2(inputFile):

    def sumVal(x): return x * (x + 1) // 2

    crabPositions = myLib.input_as_list_of_ints((inputFile))[0]
    crabPositions.sort()
    print(crabPositions)

    image = np.full(( len(crabPositions) + 1, max(crabPositions)+30, 1), 0, dtype=np.uint)

    computeFuel   = dict( [ (  destposition
                           , sum( [  sumVal( abs(crabPosition-destposition) ) for crabPosition in crabPositions])
                           )
                          for destposition in range( min(crabPositions), max( crabPositions))
                          ] )

    for x in range( len(crabPositions) ):
        image[x,crabPositions[x] ]= 100 + crabPositions[x]

    maxFuel = computeFuel[max(computeFuel, key=computeFuel.get)]
    for y in  range( min(crabPositions), max( crabPositions)):
        image[  len(crabPositions) * int(computeFuel[y]/maxFuel)  , y ] = 500

    save_nparray_image('D7_puzzle2.png', myLib.generativePy_colorizeImage(image))

    return computeFuel[min(computeFuel, key=computeFuel.get)]

# ==================================================================================================

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile )))
myLib.display_result("2",str(Puzzle_2( inputFile )))

myLib.display_footer()



