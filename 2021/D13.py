import myLib
import re
from collections import defaultdict
from generativepy.nparray import save_nparray_image
import numpy as np

DAY       = "D13"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# ==================================================================================================


# --------------------------------------------------------------------------------------------------
def Puzzle_1( inputFile ):

    papers       = []
    instructions = []

    #-> GET POINTS AND INSTRUCTIONS FROM FILE

    points       = defaultdict( bool )
    for line in myLib.input_as_lines(inputFile):

        #-> Get Points
        coords=line.split(',')
        if len(coords) == 2:
            points[ ( int(coords[0]) , int(coords[1]) ) ] = True

        # -> Get Instructions
        instr=line.split(' ')
        if len(instr) == 3:
            instructions.append( ( (instr[2].split('='))[0], int( (instr[2].split('='))[1] ) ) )

    #-> Get Paper Size
    maxX = max( [ x for (x,y) in points ])
    maxY = max( [ y for (x,y) in points ])

    #-> Keep paper states
    papers.append(( maxX, maxY, points) )


    #-> COMPUTE ALL FOLDS
    step = 0
    for (instruction, value) in instructions:
        step                     += 1
        (maxX, maxY, paperPoints) = papers[step - 1]

        newPoints = defaultdict( bool )
        for (x,y) in paperPoints:

            if instruction == "y" and y != value:
                delta                   = max( 0, maxY - 2 * value )
                newX                    = x
                newY                    = y if y < value else 2 * value - y + delta
                newPoints[(newX, newY)] = True

            if instruction == "x" and x != value:
                delta                   = max( 0, maxX - 2 * value )
                newY                    = y
                newX                    = x if x < value else 2 * value - x + delta
                newPoints[(newX, newY)] = True

        maxX = max([x for (x, y) in newPoints])
        maxY = max([y for (x, y) in newPoints])
        papers.append((maxX, maxY, newPoints))


    print( "RES PUZZEL_1 :" ,  len(papers[1][2]) )

    RESULT = [ ['.'] * (papers[step][0]+1) for i in range(0, papers[step][1] +1) ]
    for (x,y) in   papers[step][2]:
        RESULT[y][x] = 'X'

    print("RES PUZZEL_2 :" ) #ABKJFBGC
    for line in RESULT:
        print( ''.join( line))

    return 0

# --------------------------------------------------------------------------------------------------
def Puzzle_2(inputFile):
    return 0

# ==================================================================================================

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile )))
myLib.display_result("2",str(Puzzle_2( inputFile )))

myLib.display_footer()



