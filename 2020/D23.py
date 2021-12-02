import string
import copy
import math
import copy

from collections import defaultdict
import re
import ast
DAY="23"

print("====================================================================================================")
print("- D"+DAY+" ---------------------------------------------------------------------------------")

def Puzzle_1():
    print(" --- PUZZLE_1 ---")
    cups       = [4,6,9,2,1,7,5,3,8]
    #cups       = [3,8,9,1,2,5,4,6,7]
    maxmoves   = 100
    move =0
    while move < maxmoves:
        move += 1
        #print("-- move",move,"--")
        #print( "cups: ",cups )

        currentcup = cups[0]
        pickup     = cups[1:4]

        for _ in range(0,3):del cups[1]
        destcup    = currentcup-1
        while destcup > 0 and destcup not in cups: destcup-=1
        if destcup == 0: destcup = max( cups)
        while cups[0] != destcup : cups.append(cups.pop(0))
        for idx in range(0,3): cups.insert( 1+idx,pickup[idx])

        while cups[0] != currentcup: cups.append(cups.pop(0))
        cups.append(cups.pop(0))

        #print("pickup : ", pickup)
        #print("destination:", destcup)

    while cups[0] != 1: cups.append(cups.pop(0))
    cups.append(cups.pop(0))
    print( 'FINAL STATE : ', cups[0:10])
    return

Puzzle_1()

def Puzzle_2():
    print(" --- PUZZLE_2 ---")
    moves    = 10000000
    maxvalue = 1000000

    cups = [4, 6, 9, 2, 1, 7, 5, 3, 8]
    #cups       = [3,8,9,1,2,5,4,6,7]
    cups      += list( range( 10, 1000001) )
    chain      = dict( zip( cups, cups[1:]+cups[:1]))
    currentcup = cups[0]

    move = 0
    while move < moves:
        move+=1
        #print("move",move)
        pickup = [ chain[currentcup], chain[chain[currentcup]], chain[chain[chain[currentcup] ]]]
        #print( list( chain.items())[0:15])
        chain[currentcup] = chain[pickup[2]]
        destcup =  currentcup-1
        while destcup in pickup and destcup > 0: destcup-=1
        if destcup == 0: destcup =maxvalue
        while destcup in pickup: destcup -= 1
        chain[pickup[2]] = chain[destcup]
        chain[destcup]=pickup[0]
        #print(list(chain.items())[0:15])
        currentcup= chain[currentcup]

    print(chain[1])
    print(chain[chain[1]])

    print(chain[1] * chain[chain[1]])

Puzzle_2()
