import string
import copy
import math
import copy

from collections import defaultdict

inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D17_input.txt"
#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D17_sample.txt"

print("- D17 ---------------------------------------------------------------------------------")
print(inputFile)

neighbours=[(w, x, y,z) for w in range(-1,2) for x in range(-1,2) for y in range(-1,2) for z in range(-1,2) ]
neighbours.remove( (0,0,0,0) )

def read_puzzle( file ):
    with open(file) as f:
        lines = [ line.rstrip("\n") for line in f.readlines()]
    space=[]
    for y,line in enumerate(lines):
        for x,state in enumerate( line):
            if state == "#": space.append( (x,y,0,0) )
    return space

def Puzzle_1(original_space):
    active = copy.deepcopy(original_space)
    for cycle in range(1,7):
        newspace = []
        GridCoords = [(x, y,z,w) for x in range(-cycle,8+cycle) for y in range(-cycle,8+cycle) for z in range(-cycle,1+cycle)  for w in range(-cycle,1+cycle) ]
        for (x,y,z,w) in GridCoords:
            nbActivates = sum( 1 if (x+dx,y+dy,z+dz,w+dw) in active else 0 for dx, dy, dz, dw in neighbours)
            if ( x,y,z,w) in active and nbActivates in (2,3) or ( x,y,z) not in active and nbActivates == 3:
                newspace.append( ( x,y,z,w) )
        active = copy.deepcopy(newspace)
    return len(active)

def Puzzle_2(space):

    return 0


print("------------------------------------------------------------------------------------------")

space    = read_puzzle(inputFile)
print(space)


value =  Puzzle_1( space )
print( "       PUZZLE_1 : " + str(value) + " " )

value = Puzzle_2( space )
print( "       PUZZLE_2 : " + str(value) + " " )

print("------------------------------------------------------------------------------------------")
print('END')

