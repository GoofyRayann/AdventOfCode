import re
import myLib

DAY           = "D10"
inputTestFile = DAY + "_puzzle_test.txt"
inputFile     = DAY + "_puzzle.txt"

# --------------------------------------------------------------------------------------------------
def Puzzle_1(inputFile):

    def checkCycle(cycle, X, strength):
        if (cycle-20)% 40 == 0:
            return (cycle+1,  strength + X * cycle)
        return (cycle+1, strength)

    instrs   = myLib.input_as_lines(inputFile)
    X        = 1
    cycle    = 1
    strength = 0
    for fullInstr in instrs:
        instr = fullInstr.split(' ')[0]
        match instr:
            case "addx":
                (cycle, strength) = checkCycle( cycle, X, strength)
                (cycle, strength) = checkCycle( cycle, X, strength)
                X                += int( fullInstr.split(' ')[1])
            case "noop":
                (cycle, strength) = checkCycle( cycle, X, strength)
    return strength

def Puzzle_2(inputFile):
    def processRay(cycle, X, crt):
        pixel = '█' if cycle in [X, X + 1, X + 2] else ' '
        return ( (cycle +1 ) % 40, crt + pixel )

    instrs   = myLib.input_as_lines(inputFile)
    X        = 0
    cycle    = 0
    crt      = ''

    for fullInstr in instrs:
        instr = fullInstr.split(' ')[0]
        match instr:
            case "addx":
                (cycle,crt) = processRay(cycle, X, crt)
                (cycle,crt) = processRay(cycle, X, crt)
                X          += int(fullInstr.split(' ')[1])
            case "noop":
                (cycle,crt) = processRay(cycle, X, crt)

    for displayLine in [crt[i:i+40] for i in range(0, len(crt), 40)]:
        print( displayLine)

    #+> RLEZFLGE

    return 'RLEZFLGE'

# --------------------------------------------------------------------------------------------------
myLib.display_header(DAY, inputFile)

myLib.display_result("1", str(Puzzle_1(inputFile)))
myLib.display_result("2", str(Puzzle_2(inputFile)))

myLib.display_footer()
