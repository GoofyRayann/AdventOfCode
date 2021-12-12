import myLib
import re
from generativepy.nparray import save_nparray_image
import numpy as np

DAY       = "D11"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# ==================================================================================================

def makeFlash( ax, ay, energy ,octopusMap, flashed ):
    adjacents           = [ (-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1) ]
    octopusMap[ay][ax] += energy

    if octopusMap[ay][ax] == 10 or (octopusMap[ay][ax] - energy) == 10:
        octopusMap[ay][ax] += 100 #- DUMMY VALUE IN ORDER TO NOT RETREAT THIS OCTOPUS
        flashed[ (ax,ay) ] = True

        for (dx,dy) in adjacents:
            if (ax+dx) >= 0 and (ax+dx) < len(octopusMap[0]) and (ay+dy) >= 0 and (ay+dy) < len(octopusMap):
                makeFlash(ax+dx, ay+dy, 1, octopusMap, flashed)
    return

# --------------------------------------------------------------------------------------------------
def Puzzle_1( inputFile ):

    octopusMap  = myLib.input_as_list_of_list_of_ints((inputFile))
    flashed     = {}
    nbFlashed   = 0
    nbOctopuses = len(octopusMap) * len( octopusMap[0])
    noStep      = 0
    resPuzzle1 = 0
    resPuzzle2 = 0


    while len(flashed) != nbOctopuses :
        noStep += 1
        flashed.clear()

        #- INCREMENT +1
        for y in range( 0,len(octopusMap)):
            for x in range( 0, len( octopusMap[0]) ):
                octopusMap[y][x] += 1

        #- TREAT OTCOPUSES THAT SHOULD FLASH
        for y in range(0, len(octopusMap) ):
            for x in range(0, len(octopusMap[0]) ):
                makeFlash( x , y , 0 , octopusMap, flashed)

        #- ENERGY OF ALL OCTOPUS THAT FLASHED GOES DOWN TO ZERO
        for (x,y) in flashed:
            octopusMap[y][x] = 0

        nbFlashed += len(flashed) #- Count number of octopuses that flashed

        if noStep ==100:
            resPuzzle1 = nbFlashed #- result at Step 100

        print("==> ", noStep)
        for line in octopusMap:
            print(line)

        if len(flashed) == nbOctopuses: #- stop when all octopuses flashed during the step
            break

    resPuzzle2 = noStep

    print("resPuzzle1", resPuzzle1)
    print("resPuzzle1", resPuzzle2)

    return 0

# --------------------------------------------------------------------------------------------------
def Puzzle_2(inputFile):
    return 0

# ==================================================================================================

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile )))
myLib.display_result("2",str(Puzzle_2( inputFile )))

myLib.display_footer()



