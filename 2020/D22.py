import string
import copy
import math
import copy

from collections import defaultdict
import re
import ast
import sys

sys.setrecursionlimit(2000000)

DAY="22"
inputFile = "D:\Dev_Perso\\adventofcode.com\D1\D"+DAY+"_input.txt"
#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D"+DAY+"_sample.txt"

print("====================================================================================================")

print("- D"+DAY+" ---------------------------------------------------------------------------------")
print(inputFile)

def read_puzzle( file ):
    with open(file) as f:
        puzzle = [ line.rstrip("\n") for line in f.readlines()]
    print( puzzle)
    decks  = {}
    for line in puzzle:
        if line == ''          : continue
        elif "Player " in line : player = int(line.lstrip("Player ").rstrip(":"))-1 ; decks[ player ] = []
        else                   : decks[player].append( int(line))
    print( decks)
    return decks

def recurseGame(game, round, decks):

    history = [[],[]]
    while all( len(decks[p]) > 0  for p in [0,1]):

#        print("-- Round", game, '.', round, " ---------")
#        for p in [0,1] : print("    Player",p,"'s deck:", decks[p])

#        for p in [0,1]: print ("history ", p, " - ", history[p])
#        for p in [0, 1]: print("desc    ", p, " - ", decks[p])

        #CHECK IF DECK EXISTS IN PREVIOUS ROUND
        if any( decks[p] in history[p] for p in [0,1]):
            print("    The winner of game", game, "is 0 because deck reappeared")
            return 0

        for p in [0, 1]: history[p].append(copy.deepcopy(decks[p]))

        #PLAY CARDS
        played_cards = [ decks[0][0], decks[1][0] ]
        for p in [0, 1]:
            decks[p].pop(0)
#        print("    Player",p,"plays :", played_cards[p])

        #CHECK IF NEW GAME NEEDED
        if all( played_cards[p] <= len( decks[p]) for p in [0,1] ) :
#            print("    Playing a sub-game to determine the winner...")
#            print("== GAME",game+1, "==")
            newdeck    = copy.deepcopy(decks)
            for p in [0, 1]: newdeck[p]=newdeck[p][:played_cards[p]]
            winner     = recurseGame(game+1, 1, newdeck )

        #ELSE DEFINE WINNER OF THE TURN
        else: winner = 0 if played_cards[0] > played_cards[1] else 1

        #ADD PLAYED CARDS IN THE ROUND, TO WINNER DECK
#        print("    => Player", winner, "wins the round")
        for p in [0, 1]: decks[winner].append(played_cards[ (winner+p) %2])

        round+=1


    winner = 0 if len(decks[0]) > len(decks[1]) else 1
    print("    The winner of game", game, "is", winner )
    return winner

def Puzzle_1(decks):

    winner = recurseGame( 1,1,decks)

    print( "==================================")
    for p in [0, 1]: print("Player",p,"'s deck:", decks[p])
    print("WINNER IS : ", winner )
    print( "==================================")

    res=0
    for idx, card in enumerate(decks[winner]):
        res+= (len(decks[winner])-idx) * card
    return res


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

