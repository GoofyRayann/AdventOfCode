import myLib
import re

DAY       = "D6"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# ==================================================================================================
def countFishes( fishes: list[int], nbDays: int):
    nbFishesReachZero = [0] * (nbDays+10)
    nbFishes          = [0] * (nbDays+10)
    nbFishes[0]       = len(fishes)

    for fish in fishes:
        nbFishesReachZero[fish] += 1

    for day in range(1, nbDays+1):
        nbFishesReachZero[day + 7] += nbFishesReachZero[day] #- when cycle will expire for existing fishes
        nbFishesReachZero[day + 9] += nbFishesReachZero[day] #- when cycle will expire for new fishes
        nbFishes[day]               = nbFishes[day - 1] + nbFishesReachZero[day - 1]

    return nbFishes[nbDays]


# --------------------------------------------------------------------------------------------------
def Puzzle_1( inputFile ):
    return countFishes(  myLib.input_as_list_of_ints(inputFile)[0] , 80 )

# --------------------------------------------------------------------------------------------------
def Puzzle_2(inputFile):
    return countFishes(  myLib.input_as_list_of_ints(inputFile)[0] , 256 )

# ==================================================================================================

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile)))
myLib.display_result("2",str(Puzzle_2( inputFile)))

myLib.display_footer()



