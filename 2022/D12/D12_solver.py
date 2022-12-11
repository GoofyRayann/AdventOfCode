import re
import math
from functools import reduce
from typing import Dict, List

import myLib

DAY           = "D11"
inputTestFile = DAY + "_puzzle_test.txt"
inputFile     = DAY + "_puzzle.txt"

# --------------------------------------------------------------------------------------------------
class Monkey:
    def __init__(self, settings):
        configs=settings.split("\n")
        self.id            = int( re.match(r'Monkey (\d+):', configs[0]).groups()[0] )
        self.items         = [ int(item) for item in re.match(r'  Starting items: (.+)', configs[1]).groups()[0].split(', ') ]
        self.operation     = re.match(r'  Operation: new = (.+)', configs[2]).groups()[0]
        self.testDivision  = int( re.match(r'  Test: divisible by (\d+)', configs[3]).groups()[0] )
        self.goToIfTrue    = int( re.match(r'    If true: throw to monkey (\d+)', configs[4]).groups()[0] )
        self.goToIfFalse   = int( re.match(r'    If false: throw to monkey (\d+)', configs[5]).groups()[0] )
        self.inspectedItem = 0

    def addItem(self, item):
        self.items.append(item)

    def inspectItem(self, item):
        self.inspectedItem += 1
        return eval( self.operation.replace( "old", str(item)))

    def boredItem(self, item):
        return item//3

    def getMonkeyToThrow(self , item):
        if (item % self.testDivision) == 0:
            return self.goToIfTrue
        return self.goToIfFalse

class Monkeys:
    def __init__(self, inputFile):
        self.monkeys:  List[Monkey]=[]
        self.round = 0
        for monkeySettings in myLib.input_as_string(inputFile).split("\n\n"):
            self.monkeys.append( Monkey(monkeySettings) )

    def computeRound(self, isWorried:bool):
        for monkey in self.monkeys:
            for item in monkey.items:
                item=monkey.inspectItem(item)
                if isWorried: item=monkey.boredItem(item)
                destMonkey = monkey.getMonkeyToThrow(item)
                self.monkeys[destMonkey].addItem(item)
            monkey.items.clear()
        self.round+=1
        self.moduloItems()

    def displayBags(self):
        print( "ROUND " , self.round)
        for monkey in self.monkeys:
            print( "   Monkey" , monkey.id, monkey.items , " has inspected:", monkey.inspectedItem)

    def moduloItems(self):
        #-After a round, all item should be moduloted by a common "test" diviser to avoir so large item 8( if not used
        moduloTestDivisions =  reduce(lambda itemA, itemB: itemA * itemB, [monkey.testDivision for monkey in self.monkeys])
        for monkey in self.monkeys:
           monkey.items = [item % moduloTestDivisions for item in monkey.items]
        return

# --------------------------------------------------------------------------------------------------
def Puzzle_1(inputFile):
    monkeys=Monkeys(inputFile)
    monkeys.displayBags()
    for round in range(0,20):
        monkeys.computeRound(True)
    monkeys.displayBags()

    most2actives = sorted( [ monkey.inspectedItem for monkey in monkeys.monkeys],key=int,reverse=True)
    return most2actives[0] * most2actives[1]

def Puzzle_2(inputFile):
    monkeys=Monkeys(inputFile)
    for round in range(0,10000):
        if round%1000 == 0 : print( "Round", round)
        monkeys.computeRound(False)
    monkeys.displayBags()

    most2actives = sorted( [ monkey.inspectedItem for monkey in monkeys.monkeys],key=int,reverse=True)
    return most2actives[0] * most2actives[1]

# --------------------------------------------------------------------------------------------------
myLib.display_header(DAY, inputFile)

myLib.display_result("1", str(Puzzle_1(inputFile)))
myLib.display_result("2", str(Puzzle_2(inputFile)))

myLib.display_footer()
