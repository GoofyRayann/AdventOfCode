import myLib

DAY           = "D01"
inputTestFile = DAY+"_puzzle_test.txt"
inputFile     = DAY+"_puzzle.txt"

# --------------------------------------------------------------------------------------------------
def GetTotalCaloriesPerElfSortedByCalory(inputFile):
    caloriesList    = myLib.input_as_list_of_vertical_list_of_ints(inputFile)
    caloriesPerElve = list(map(sum, caloriesList))
    caloriesPerElve.sort()
    return caloriesPerElve

def Puzzle_1( inputFile ):
    return GetTotalCaloriesPerElfSortedByCalory(inputFile)[-1]

def Puzzle_2(inputFile):
    return sum(GetTotalCaloriesPerElfSortedByCalory(inputFile)[-3:])

# --------------------------------------------------------------------------------------------------

myLib.display_header(DAY, inputFile )

myLib.display_result("1", str(Puzzle_1( inputFile )))
myLib.display_result("2", str(Puzzle_2( inputFile )))

myLib.display_footer()


