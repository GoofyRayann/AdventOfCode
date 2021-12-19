import myLib
import re
from collections import defaultdict
from generativepy.nparray import save_nparray_image
import numpy as np
import os
from copy import copy
import numpy

DAY       = "D15"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# ==================================================================================================

def ComputeMap( caveMap ):

    caveMapXWidth  = len(caveMap[0])
    caveMapYheight = len(caveMap)

    #- GET ALL NEIGHBOURS - neighbours[ (x,y) ] = [ ( x+1,y,value), (x-1,y,value),...]
    neighbours = defaultdict(list)
    for x in range(0, caveMapXWidth ):
        for y in range(0, caveMapYheight):
            for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < caveMapXWidth and 0 <= y + dy < caveMapYheight:
                    neighbours[(x, y)] += [((x + dx, y + dy), caveMap[y + dy][x + dx])]

    print("STEP ", 0)

    #- IMPLEMENT DIJKSTRA ALGO
    #- LIKE THAT: https://www.maths-cours.fr/methode/algorithme-de-dijkstra-etape-par-etape)

    steps                = defaultdict(lambda: None)
    steps[(0, 0)]        = 0
    start                = ( (0, 0), 0)
    dest                 = (caveMapXWidth - 1, caveMapYheight - 1)
    t                    = 0
    links                = {}

    while start[0] != dest:
        t                 += 1
        if t % caveMapXWidth == 0: print(".",end='')

        newSteps           = copy(steps)
        cost               = newSteps[start[0]]
        newSteps[start[0]] = -1  # TO FORGOT IT

        for ((x, y), value) in neighbours[start[0]]:
            if newSteps[(x, y)] == -1  : continue #- don't treat an already computed position
            if newSteps[(x, y)] is None or newSteps[(x, y)] is not None and newSteps[(x, y)] > cost + value:
                newSteps[(x, y)] = cost + value
                links[(x,y)] = start[0]

        steps    = newSteps
        newStart = min( dict(filter(lambda elem: elem[1] != -1, newSteps.items())), key=lambda v: v[1])
        start    = (newStart, newSteps[newStart] )

    #- TRACE PATH AND COMPUTE RESULT

    print("MAP:")

    (x,y) = ( caveMapXWidth-1,  caveMapYheight -1 )
    res   = 0
    while (x,y) != (0,0):
        res          += caveMap[y][x]
        caveMap[y][x] ="X"
        (x,y)         = links[ (x,y) ]

    for line in caveMap:
        print(''.join([str(x) for x in line]) )
    print(res)
    return res

# --------------------------------------------------------------------------------------------------
def Puzzle_1( inputFile ):

    #- GET TEMPLATE
    lines     = myLib.input_as_list_of_list_of_ints(inputFile)

    return ComputeMap(lines)

# --------------------------------------------------------------------------------------------------
def Puzzle_2(inputFile):
    #- GET TEMPLATE
    lines     = myLib.input_as_list_of_list_of_ints(inputFile)

    #- MULTIPLY MAPS x5 WITH INCREMENTA LAMBDA
    incrAllValues = lambda t: ((t + 1) < 10) * t + 1
    x1 = np.array(lines)
    x2 = incrAllValues(x1)
    x3 = incrAllValues(x2)
    x4 = incrAllValues(x3)
    x5 = incrAllValues(x4)
    l1 = np.concatenate((x1,x2,x3,x4,x5), axis=1)
    l2 = incrAllValues(l1)
    l3 = incrAllValues(l2)
    l4 = incrAllValues(l3)
    l5 = incrAllValues(l4)
    mapX5 = np.concatenate((l1,l2,l3,l4,l5), axis=0)

    res = ComputeMap( mapX5.tolist() )

    return res

# ==================================================================================================

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile )))
myLib.display_result("2",str(Puzzle_2( inputFile )))

myLib.display_footer()



