from enum import Enum
from dataclasses import dataclass
import myLib

DAY = "D02"
inputTestFile = DAY + "_puzzle_test.txt"
inputFile = DAY + "_puzzle.txt"

# --------------------------------------------------------------------------------------------------

class Rules(Enum):
    Rock = 1
    Scissors = 3
    Paper = 2
    Win = 6
    Loss = 0
    Draw = 3

    guide_1 = {"A": Rock, "B": Paper, "C": Scissors, "X": Rock, "Y": Paper, "Z": Scissors}
    guide_2 = {"A": Rock, "B": Paper, "C": Scissors, "X": Loss, "Y": Draw , "Z": Win}

    handRules = {(Rock, Scissors): Win, (Scissors, Paper): Win, (Paper, Rock): Win,
                 (Rock, Rock): Draw, (Scissors, Scissors): Draw, (Paper, Paper): Draw,
                 (Rock, Paper): Loss, (Scissors, Rock): Loss, (Paper, Scissors): Loss}

@dataclass(frozen=True)
class Hand:
    myHand : str
    oppHand: str
    result : str

    @classmethod
    def GiveHand(cls, myHand, oppHand, result) :
        #- Don't know where to put that, to not make it process for each hand :(
        handForResult = {(b, Rules.handRules.value[(a, b)]): a for (a, b) in Rules.handRules.value}
        if result == "":
            result = Rules.handRules.value[(myHand, oppHand)]
        if myHand == "":
            myHand = handForResult[(oppHand, result)]
        return cls(myHand, oppHand, result)

@dataclass(frozen=True)
class Game:
    hands: list

    @classmethod
    def LoadGame(cls, inputFile , ruleId):
        turns         = myLib.input_as_lines(inputFile)
        hands         = list()
        for line in turns:
            turn = line.split(" ")
            match ruleId:
                case 1:
                    oppHand = Rules.guide_1.value[turn[0]]
                    myHand  = Rules.guide_1.value[turn[1]]
                    result  = ""
                case 2:
                    oppHand = Rules.guide_1.value[turn[0]]
                    myHand  = ""
                    result  = Rules.guide_2.value[turn[1]]
            hands.append( Hand.GiveHand( myHand, oppHand, result ) )
        return cls(hands)

    def Score(self):
        score = 0
        for hand in self.hands:
            score += hand.myHand + hand.result
        return score

def Puzzle_1(inputFile):
    game = Game.LoadGame(inputFile, ruleId=1)
    return game.Score()

def Puzzle_2(inputFile):
    game = Game.LoadGame(inputFile, ruleId=2)
    return game.Score()

# --------------------------------------------------------------------------------------------------

myLib.display_header(DAY, inputFile)

myLib.display_result("1", str(Puzzle_1(inputFile)))
myLib.display_result("2", str(Puzzle_2(inputFile)))

myLib.display_footer()
