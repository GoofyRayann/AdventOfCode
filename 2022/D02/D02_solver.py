import myLib

DAY = "D02"
inputTestFile = DAY + "_puzzle_test.txt"
inputFile = DAY + "_puzzle.txt"

# --------------------------------------------------------------------------------------------------
shapeRules = {("Rock", "Scissors"): "Win", ("Scissors", "Paper"): "Win", ("Paper", "Rock"): "Win",
              ("Rock", "Rock"): "Draw", ("Scissors", "Scissors"): "Draw", ("Paper", "Paper"): "Draw",
              ("Rock", "Paper"): "Loss", ("Scissors", "Rock"): "Loss", ("Paper", "Scissors"): "Loss"}
shapeValues = {"Rock": 1, "Scissors": 3, "Paper": 2}
turnPoints = {"Win": 6, "Loss": 0, "Draw": 3}

def Puzzle_1(inputFile):
    guide = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "Rock", "Y": "Paper", "Z": "Scissors"}
    turns = myLib.input_as_lines(inputFile)
    score = 0
    for line in turns:
        turn = line.split(" ")
        oppHand, myHand = guide[turn[0]], guide[turn[1]]
        score    += shapeValues[myHand] + turnPoints[shapeRules[(myHand, oppHand)]]
    return score


def Puzzle_2(inputFile):
    guide = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "Loss", "Y": "Draw", "Z": "Win"}
    turns = myLib.input_as_lines(inputFile)
    score = 0

    handForIssue = {(b, shapeRules[(a, b)]): a for (a, b) in shapeRules}

    for line in turns:
        turn = line.split(" ")
        oppHand, turnIssue = guide[turn[0]], guide[turn[1]]
        myHand    = handForIssue[(oppHand, turnIssue)]
        score    += shapeValues[myHand] + turnPoints[shapeRules[(myHand, oppHand)]]
    return score

# --------------------------------------------------------------------------------------------------

myLib.display_header(DAY, inputFile)

myLib.display_result("1", str(Puzzle_1(inputFile)))
myLib.display_result("2", str(Puzzle_2(inputFile)))

myLib.display_footer()
