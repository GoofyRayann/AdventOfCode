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

    crabPositions = myLib.input_as_list_of_ints((inputFile))[0]

    #-> Compute 1+2+3... for each potentiel move of crabs
    sumVal        = dict( set( [ (val, sum( range(val+1)) ) for val in range( max( crabPositions)+1)  ] ) )

    computeFuel   = dict( [ (  destposition
                           , sum( [  sumVal[abs(crabPosition-destposition)] for crabPosition in crabPositions])
                           )
                          for destposition in range( min(crabPositions), max( crabPositions))
                          ] )

    return computeFuel[min(computeFuel, key=computeFuel.get)]

# ==================================================================================================

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile )))
myLib.display_result("2",str(Puzzle_2( inputFile )))

myLib.display_footer()



