import myLib
import re

DAY       = "D5"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# --------------------------------------------------------------------------------------------------
def computeMap( inputFile, diagonals:bool ):
    coords=[]
    for coord in myLib.input_as_lines(inputFile):
        c=re.findall(r'[0-9]+', coord )
        coords.append( (int(c[0]),int(c[1]), int(c[2]),int(c[3]) ) )

    #-> Init a map
    maxX = max( [ max( [x1,x2]) for (x1, y1 ,x2,y2) in coords] )
    maxY = max( [ max( [y1,y2]) for (x1, y1 ,x2,y2) in coords] )
    map  = [[0] * (maxX+1) for i in range(maxY+1)]

    # -> Draw the map
    for (x1, y1, x2, y2) in coords:
        if diagonals or not diagonals and ( x1==x2 or y1==y2):
            dx      = 1 if x2 > x1 else -1 if x2 < x1 else 0
            dy      = 1 if y2 > y1 else -1 if y2 < y1 else 0
            nbIters = max([abs(y2 - y1) + 1, abs(x2 - x1) + 1])

            for iter in range(nbIters):
                map[x1 + iter * dx][y1 + iter * dy] += 1

    #-> Compute sum ( cross points)
    res = sum([sum(val >= 2 for val in row) for row in map])

    return res

# --------------------------------------------------------------------------------------------------
def Puzzle_1( inputFile ):
    return computeMap(inputFile, False)

# --------------------------------------------------------------------------------------------------
def Puzzle_2(inputFile):
    return computeMap(inputFile, True)

# --------------------------------------------------------------------------------------------------

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile )))
myLib.display_result("2",str(Puzzle_2( inputFile )))

myLib.display_footer()


