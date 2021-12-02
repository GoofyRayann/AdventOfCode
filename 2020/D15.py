import string
import copy
import math
import re
from time import time


print("- D15 ---------------------------------------------------------------------------------")

def Puzzle_1(puzzle):
    suite = [int(x)  for x in puzzle.split(',')]
    suite.append(0)
    turn=len(suite)
    while turn <2020:
        prev=suite[turn-1]
        if  suite.count(prev) == 1:
            suite.append(0)
        else:
            id=turn-2
            while suite[id] != prev: id-=1
            suite.append( turn-1 - id)
        turn +=1
    return suite[turn-1]

def Puzzle_2(puzzle):
    suite = { int(val) : (id,-1)  for id, val in enumerate( puzzle.split(',')) }
    prev  = list(suite)[-1]
    turn  = len(suite)
    while turn < 30000000:
        idx, idxprev = suite[prev]
        value= 0 if idxprev == -1 else idx - idxprev
        suite[value]= (turn,  -1 if suite.get(value) == None else suite[value][0])
        prev = value
        turn += 1
    return prev


print("------------------------------------------------------------------------------------------")

puzzle="1,20,11,6,12,0"
#puzzle="1,3,2"

t_start = time()
value =  Puzzle_1( puzzle )
print( "       PUZZLE_1 : " + str(value) + " " )

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
t_start = time()

value = Puzzle_2( puzzle )
print( "       PUZZLE_2 : " + str(value) + " " )

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)

print("------------------------------------------------------------------------------------------")
print('END')

