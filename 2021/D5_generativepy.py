import myLib
import re
from generativepy.nparray import save_nparray_image
import numpy as np

DAY       = "D5"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# ==================================================================================================

def computeMap( inputFile, diagonals:bool):
    coords=[]
    for coord in myLib.input_as_lines(inputFile):
        coords.append( tuple( [int(val) for val in re.findall(r'\d+',coord)]))

    #-> Init a map
    maxX = max( [ max( [x1,x2]) for (x1, y1 ,x2,y2) in coords] )
    maxY = max( [ max( [y1,y2]) for (x1, y1 ,x2,y2) in coords] )
    map  = [[0] * (maxX+1) for i in range(maxY+1)]

    image=np.full((maxX+1, maxY+1, 1), 0, dtype=np.uint)

    # -> Draw the map
    for (x1, y1, x2, y2) in coords:
        if diagonals or not diagonals and ( x1==x2 or y1==y2):
            dx      = (x2 > x1) - ( x2 < x1)
            dy      = (y2 > y1) - ( y2 < y1)
            nbIters = max([abs(y2 - y1) + 1, abs(x2 - x1) + 1])

            for iter in range(nbIters):
                map[x1 + iter * dx][y1 + iter * dy] += 1
                image[x1 + iter * dx][y1 + iter * dy] += 1

    #-> Compute sum ( cross points)
    res = sum([sum(val >= 2 for val in row) for row in map])
    return (res,image)

# --------------------------------------------------------------------------------------------------
def Puzzle_1( inputFile ):

    res,image = computeMap(inputFile, False)
    save_nparray_image('D5_puzzle1.png', myLib.generativePy_colorizeImage(image))

    return res

# --------------------------------------------------------------------------------------------------
def Puzzle_2(inputFile):

    res, image = computeMap(inputFile, True)
    save_nparray_image('D5_puzzle2.png', myLib.generativePy_colorizeImage(image))

    return res

# ==================================================================================================

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile )))
myLib.display_result("2",str(Puzzle_2( inputFile )))

myLib.display_footer()



