import myLib
import re

DAY       = "D4"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# --------------------------------------------------------------------------------------------------

def readBingos(inputFile):
    with open(inputFile) as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    #-> GET DRAWN NUMBERS

    drawnNumbers  = [ int(n) for n in lines[0].split(',')]

    #-> GET ALL BOARDS IN BOARDS [noBoard] [noLine] [noColumn] = value

    boards         = []
    numberOfBoards = int((len(lines)-1)/6)

    for noBoard in range(0, numberOfBoards):
        boards.append( [
            [int(n) for n in re.findall(r'[0-9]+', lines[noBoard * 6 + 2])],
            [int(n) for n in re.findall(r'[0-9]+', lines[noBoard * 6 + 3])],
            [int(n) for n in re.findall(r'[0-9]+', lines[noBoard * 6 + 4])],
            [int(n) for n in re.findall(r'[0-9]+', lines[noBoard * 6 + 5])],
            [int(n) for n in re.findall(r'[0-9]+', lines[noBoard * 6 + 6])]
        ]  )

    #-> COMPUTE POSITION OF DRAWN NUMBERS IN ALL BOARDS AS A DICTIONNARY drawnNumber : [ (noboard, noline, nocolumn),...]

    valuePositions={}
    for drawnNumber in drawnNumbers: valuePositions[drawnNumber]=[]

    for noBoard in range( 0, len(boards) ):
        for noLine in range (5):
            for noColumn in range(5):
                value          = boards[noBoard][noLine][noColumn]
                valuePositions[value].append( ( noBoard,noLine,noColumn ))

    return ( drawnNumbers, boards,valuePositions )

# --------------------------------------------------------------------------------------------------
def Puzzle_1( inputFile ):
    drawnNumbers, boards, valuePositions = readBingos(inputFile)

    #-> init for each board number of marked value in line or column
    resultLines   = [[0] * 5 for i in range(len(boards))]
    resultColumns = [[0] * 5 for i in range(len(boards))]

    res = 0
    for drawnNumber in drawnNumbers:
        for noBoard, noLine, noColumn in valuePositions[drawnNumber]:

            #-> Increment line or column in board where drawn number is found + unmark value in board
            resultLines  [noBoard][noLine]           += 1
            resultColumns[noBoard][noColumn]         += 1
            boards       [noBoard][noLine][noColumn]  = 0

            #-> when a line or column in a board is complete, it is won
            if resultLines[noBoard][noLine] == 5 or resultColumns[noBoard][noColumn] == 5:
                print( "Winner Board : ", noBoard )
                res = sum( [sum(line) for line in boards[noBoard]] ) * drawnNumber
                return res

    return res

# --------------------------------------------------------------------------------------------------
def Puzzle_2(inputFile):
    drawnNumbers, boards, valuePositions = readBingos(inputFile)

    # -> init for each board number of marked value in line or column
    resultLines   = [[0] * 5 for i in range(len(boards))]
    resultColumns = [[0] * 5 for i in range(len(boards))]
    winnerBoard   = [0]  * len(boards)

    res = 0
    for drawnNumber in drawnNumbers:
        for noBoard, noLine, noColumn in valuePositions[drawnNumber]:

            # -> Increment line or column in board where drawn number is found + unmark value in board
            resultLines   [noBoard][noLine]          += 1
            resultColumns [noBoard][noColumn]        += 1
            boards        [noBoard][noLine][noColumn] = 0

            # -> when a line or column is complete, a board is won, so mark the board as Won
            if resultLines[noBoard][noLine] == 5 or resultColumns[noBoard][noColumn] == 5:
                winnerBoard[noBoard] = 1

                # -> if all oards are won, give rhe last won board values
                if sum( winnerBoard) == len(boards):
                    print('The last won board is ' ,noBoard , 'with drawn ' ,drawnNumber )
                    res = sum([sum(line) for line in boards[noBoard]]) * drawnNumber
                    return res
    return res

# --------------------------------------------------------------------------------------------------

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile )))

myLib.display_result("2",str(Puzzle_2( inputFile )))

myLib.display_footer()


