import myLib
import re

DAY = "D04"
inputTestFile = DAY + "_puzzle_test.txt"
inputFile = DAY + "_puzzle.txt"

def parseFile(inputFile):
    def convertTupleValuesToIntPairs(a: tuple):
        return (int(a[0]), int(a[1])), (int(a[2]), int(a[3]))
    return [convertTupleValuesToIntPairs(re.match(r'(\d+)-(\d+),(\d+)-(\d+)', pairs).groups())
            for pairs in myLib.input_as_lines(inputFile)]

def pairIsContained(p1: tuple, p2: tuple):
    (p1a, p1b), (p2a, p2b) = p1, p2
    return (p1a <= p2a <= p2b <= p1b) or (p2a <= p1a <= p1b <= p2b)

def pairIsOverlapped(p1: tuple, p2: tuple):
    (p1a, p1b), (p2a, p2b) = p1, p2
    #return (p1a <= p2a <= p1b) or (p1a <= p2b <= p1b) or (p2a <= p1a <= p1b <= p2b) #-> my classic way
    return len( range( max(p1a, p2a), min( p1b, p2b) +1 ) ) > 0 #-> the way of Guillaume did, I prefer it

def Puzzle_1(inputFile):
    return sum([pairIsContained(p1, p2) for (p1, p2) in parseFile(inputFile)])

def Puzzle_2(inputFile):
    return sum([pairIsOverlapped(p1, p2) for (p1, p2) in parseFile(inputFile)])

myLib.display_header(DAY, inputFile)

myLib.display_result("1", str(Puzzle_1(inputFile)))
myLib.display_result("2", str(Puzzle_2(inputFile)))

myLib.display_footer()
