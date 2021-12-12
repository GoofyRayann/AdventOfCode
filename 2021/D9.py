import myLib
import re
from generativepy.nparray import save_nparray_image
import numpy as np

DAY       = "D9"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# ==================================================================================================

def loadHeightMap( inputFile):
    # - Get heightmap and add 0s arround
    heightmap = myLib.input_as_list_of_list_of_ints((inputFile))
    heightmap = [[9] * len(heightmap[0])] + heightmap + [[9] * len(heightmap[0])]
    heightmap = [[9] + line + [9] for line in heightmap]
    return heightmap

def getLowPoints(heightmap):
    # - Identify low pointsin a height map
    lowPoints = []
    for x in range(1, len(heightmap[0]) - 1):
        for y in range(1, len(heightmap) - 1):
            heightPoint = heightmap[y][x]
            if         (heightPoint < heightmap[y + 1][x]
                    and heightPoint < heightmap[y - 1][x]
                    and heightPoint < heightmap[y][ x + 1]
                    and heightPoint < heightmap[y][x - 1]):
                lowPoints.append((x, y))
    return lowPoints

def getPointsInBassin(heightmapBassin, pointsInBassin, point  ):
    deltas                = [ (0,1), (0,-1), (1,0), (-1,0) ]
    (x, y)                = point
    heightmapBassin[y][x] = 9
    pointsInBassin.append(point)

    for (dx,dy) in deltas:
        if heightmapBassin[y + dy][x + dx] < 9:
            (heightmapBassin, pointsInBassin) = getPointsInBassin(heightmapBassin, pointsInBassin, (x + dx, y + dy ))

    return (heightmapBassin, pointsInBassin)

# --------------------------------------------------------------------------------------------------
def Puzzle_1( inputFile ):

    heightmap = loadHeightMap(inputFile)
    lowPoints = getLowPoints(heightmap)
    res       = sum( [  heightmap[y][x] + 1 for (x,y) in lowPoints ] )

    return res

# --------------------------------------------------------------------------------------------------
def Puzzle_2(inputFile):
    #-> identify all points in bassins from all lowpoints
    heightmap = loadHeightMap(inputFile)
    lowPoints = getLowPoints(heightmap)
    bassins   = []

    for lowPoint in lowPoints:
        pointsInBassin  = []
        getPointsInBassin( heightmap, pointsInBassin,lowPoint)
        bassins.append(pointsInBassin)

    #-> Create an image of the matrix
    image = np.full((len(heightmap[0]) + 1, len(heightmap) + 1, 1), 0, dtype=np.uint)
    for y in range(0, len(heightmap) ):
        for x in range( 0, len(heightmap[0]) ):
            image[x][y] = heightmap[y][x]+100
    save_nparray_image('D9_puzzle.png', myLib.generativePy_colorizeImage(image))

    #-> Get the 3 greatests bassins
    sizeofBassins = [ len(bassin) for bassin in bassins]
    sizeofBassins.sort()
    sizeofBassins.reverse()

    return sizeofBassins[0] * sizeofBassins[1] * sizeofBassins[2]

# ==================================================================================================

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile )))
myLib.display_result("2",str(Puzzle_2( inputFile )))

myLib.display_footer()



