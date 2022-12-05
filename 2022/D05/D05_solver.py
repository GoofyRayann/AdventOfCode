from copy import copy

import myLib
import re

DAY = "D05"
inputTestFile = DAY + "_puzzle_test.txt"
inputFile = DAY + "_puzzle.txt"

# --------------------------------------------------------------------------------------------------
class ComputeFile:
    def getStacksFromFile(inputFile):
        lines = open(inputFile).read().rstrip("\n").split("\n\n")
        return lines[0].split("\n")

    def getMovesFromFile(inputFile):
        lines = open(inputFile).read().rstrip("\n").split("\n\n")
        return lines[1].split("\n")

class Move:
    def __init__(self, moveFromFile):
        moveRead = re.match(r'move (\d+) from (\d+) to (\d+)', moveFromFile).groups()
        self.numCrates, self.fromStack, self.toStack = int(moveRead[0]), int(moveRead[1]) - 1, int(moveRead[2]) - 1

class Crane:
    def __init__(self, craneModel):
        self.craneModel = craneModel

    def MoveCrates(self, stacks, move):
        partToMove = stacks.stacks[move.fromStack][-move.numCrates:]
        if self.craneModel == "CrateMover 9000":
            partToMove = partToMove[::-1]
        stacks.stacks[move.toStack]  += partToMove
        stacks.stacks[move.fromStack] = stacks.stacks[move.fromStack][:len(stacks.stacks[move.fromStack]) - move.numCrates]
        return

class Stacks:
    def __init__(self, stacksFromFile):
        self.stacks = self.InitStacksfromStacksFromFile(stacksFromFile )

    def InitStacksfromStacksFromFile(self, stacksFromFile):
        stacksNumber = len(re.findall(r'\d+', stacksFromFile[-1]))
        stacks       = [''] * stacksNumber
        stacksFromFile.pop() #- Remove line with stack ids
        for line in list(reversed(stacksFromFile)):
            for x in range(0, len(line) // 4 + 1):
                if line[1 + x * 4] != ' ':
                    stacks[x] += line[1 + x * 4]
        return stacks

    def getTopOfStacks(self):
        return ''.join([stack[-1] for stack in self.stacks])

# --------------------------------------------------------------------------------------------------
def Puzzle(inputFile, craneModel):
    crane  = Crane(craneModel)
    stacks = Stacks(ComputeFile.getStacksFromFile(inputFile))
    for move in ComputeFile.getMovesFromFile(inputFile):
        crane.MoveCrates(stacks, Move( move))
    return stacks.getTopOfStacks()

def Puzzle_1(inputFile):
    return Puzzle( inputFile,  "CrateMover 9000" )

def Puzzle_2(inputFile):
    return Puzzle( inputFile,  "CrateMover 9001" )

# --------------------------------------------------------------------------------------------------
myLib.display_header(DAY, inputFile)

myLib.display_result("1", str(Puzzle_1(inputFile)))
myLib.display_result("2", str(Puzzle_2(inputFile)))

myLib.display_footer()
