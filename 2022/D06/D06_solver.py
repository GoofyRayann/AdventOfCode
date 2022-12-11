import myLib

DAY           = "D06"
inputTestFile = DAY + "_puzzle_test.txt"
inputFile     = DAY + "_puzzle.txt"

# --------------------------------------------------------------------------------------------------
def DetectDistinctMarkerPosition(message, markerLength):
    pos    = markerLength
    while( len(set(list(message[pos-markerLength:pos]))) != markerLength ):
        pos+=1
    return pos

def Puzzle_1(inputFile):
    return DetectDistinctMarkerPosition( message=myLib.input_as_string(inputFile), markerLength=4 )

def Puzzle_2(inputFile):
    return DetectDistinctMarkerPosition( message=myLib.input_as_string(inputFile), markerLength=14)

# --------------------------------------------------------------------------------------------------
myLib.display_header(DAY, inputFile)

myLib.display_result("1", str(Puzzle_1(inputFile)))
myLib.display_result("2", str(Puzzle_2(inputFile)))

myLib.display_footer()
