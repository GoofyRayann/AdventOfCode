import string
import copy
import math
import copy

from collections import defaultdict
import re
import ast
import sys

sys.setrecursionlimit(2000000)

DAY="24"
#inputFile = "D:\Dev_Perso\\adventofcode.com\D1\D"+DAY+"_input.txt"
inputFile = "D:\Dev_Perso\\adventofcode.com\D1\D"+DAY+"_sample.txt"


print("====================================================================================================")

print("- D"+DAY+" ---------------------------------------------------------------------------------")
print(inputFile)

grid={}




def read_puzzle( file ):
    with open(file) as f:
        puzzle = [ line.rstrip("\n") for line in f.readlines()]
    print( puzzle)
    return puzzle


def Puzzle_1(puzzle):

    direction={'e':(1,0),'se':(1,-1),'sw':(0,-1),'w':(-1,0),'nw':(0,1),'ne':(1,1)}
    grid=[]

    for line in puzzle:
        print("===> line : ", line)
        x,y = 0,0
        while len(line) > 0:
            dir  = line[0]
            line = line[1:]
            if dir not in direction: dir += line[0]; line = line[1:]
            dx,dy = direction[dir]
            x, y = x+dx, y+dy
        if ( x,y ) in grid:
            grid.remove( (x,y) )
            print( " (",x,",",y,") goes WHITE")
        else              :
            grid.append( (x,y) )
            print(" (", x, ",", y, ") goes BLACK")

    print( grid)
    return 0


def Puzzle_2(puzzle):
    res=0
    return res

print("------------------------------------------------------------------------------------------")

puzzle    = read_puzzle(inputFile)
value =  Puzzle_1( puzzle )
print( "       PUZZLE_1 : " + str(value) + " " )

puzzle    = read_puzzle(inputFile)
val2 = Puzzle_2( puzzle )
print( "       PUZZLE_2 : " + str(val2) + " " )

print("------------------------------------------------------------------------------------------")
print('END')

