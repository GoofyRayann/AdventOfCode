import myLib

DAY = "D03"
inputTestFile = DAY + "_puzzle_test.txt"
inputFile = DAY + "_puzzle.txt"

# --------------------------------------------------------------------------------------------------
def CommonItem(compartmentA: str, compartmentB: str):
    keysA = dict.fromkeys( compartmentA)
    keysB = dict.fromkeys( compartmentB)
    return ''.join( list( keysA.keys() & keysB.keys() ) )

def ItemPriority( item : bytes):
    itemValue    =  ord(item)
    itemPriority = 27+itemValue-65 if itemValue < 97 else 1+itemValue-97
    return itemPriority

def Puzzle_1(inputFile):
    rucksacks  = myLib.input_as_lines(inputFile)
    priorities = 0
    for rucksack in rucksacks:
        commonItem  = CommonItem( rucksack[len(rucksack) // 2:], rucksack[:len(rucksack) // 2])
        priorities += ItemPriority(commonItem[0])
    return priorities

def Puzzle_2(inputFile):
    rucksacks = myLib.input_as_lines(inputFile)
    priorities = 0
    for idx in range( 0, len(rucksacks) //3 ):
        commonItem  = CommonItem( CommonItem(rucksacks[idx*3],rucksacks[idx*3+1])  , rucksacks[idx*3+2])
        priorities += ItemPriority(commonItem[0])
    return priorities

# --------------------------------------------------------------------------------------------------

myLib.display_header(DAY, inputFile)

myLib.display_result("1", str(Puzzle_1(inputFile)))
myLib.display_result("2", str(Puzzle_2(inputFile)))

myLib.display_footer()
