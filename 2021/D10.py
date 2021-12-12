import myLib
import re
import matplotlib.pyplot as plt

DAY       = "D10_test"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# ==================================================================================================

def ComputeCode ( inputFile , graph):
    closingSyntax         = {'{': '}', '[': ']', '(': ')', '<': '>'}
    scoreIllegalChar      = {')': 3, ']': 57, '}': 1197, '>': 25137}
    scoreClosingChar      = {')': 1, ']': 2, '}': 3, '>': 4}
    scoresFixedLine       = []
    totalScoreIllegalChar = 0

    for line in myLib.input_as_lines(inputFile):
        nbChanges = 1

        # ->Remove all good chunks until no closed chunk
        #- input  : {([(<{}[<>[]}>{[]{[(<()>
        #- transfo: {([(<[}>{{[(
        while nbChanges > 0:
            (line, nbChanges) = re.subn(r'(\(\))', '',
                                re.sub(r'(\[\])', '()', re.sub(r'(\{\})', '[]', re.sub(r'(\<\>)', '{}', line))))

        # -> A remaining closing chars in the line means an issue in the line
        search = re.search(r'[\>\]\}\)]', line, re.I)

        # -> Compute wrong line for Puzzle 1
        if search is not None:
            (s, e) = search.span()
            totalScoreIllegalChar += scoreIllegalChar[line[s]]

        # -> Compute good line for Puzzle 2
        else:
            scoreLine = 0
            for char in line[::-1]:
                scoreLine = scoreLine * 5 + scoreClosingChar[closingSyntax[char]]
            scoresFixedLine.append(scoreLine)

    scoresFixedLine.sort()
    totalScoreFixedChar = scoresFixedLine[int(len(scoresFixedLine) / 2)]

    return( totalScoreIllegalChar, totalScoreFixedChar)

# ==================================================================================================

myLib.display_header(DAY, inputFile )

resPuzzle1, resPuzzle2 = ComputeCode( inputFile , None)

myLib.display_result("1",str(resPuzzle1))
myLib.display_result("2",str(resPuzzle2))

myLib.display_footer()



