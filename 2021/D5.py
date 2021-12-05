import myLib
import re
import matplotlib.pyplot as plt

DAY       = "D5"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# ==================================================================================================

def computeMap( inputFile, diagonals:bool , graph):
    coords=[]
    for coord in myLib.input_as_lines(inputFile):
        coords.append( tuple( [int(val) for val in re.findall(r'\d+',coord)]))

    #-> Init a map
    maxX = max( [ max( [x1,x2]) for (x1, y1 ,x2,y2) in coords] )
    maxY = max( [ max( [y1,y2]) for (x1, y1 ,x2,y2) in coords] )
    map  = [[0] * (maxX+1) for i in range(maxY+1)]

    # -> Draw the map
    for (x1, y1, x2, y2) in coords:
        if diagonals or not diagonals and ( x1==x2 or y1==y2):
            dx      = (x2 > x1) - ( x2 < x1)
            dy      = (y2 > y1) - ( y2 < y1)
            nbIters = max([abs(y2 - y1) + 1, abs(x2 - x1) + 1])

            for iter in range(nbIters):
                map[x1 + iter * dx][y1 + iter * dy] += 1

            graph.plot([x1,x2] , [-y1,-y2],linewidth=0.2,color=(0,0,0) )

    #-> Compute sum ( cross points)
    res = sum([sum(val >= 2 for val in row) for row in map])
    return res

# --------------------------------------------------------------------------------------------------
def Puzzle_1( inputFile , graph):
    return computeMap(inputFile, False, graph)

# --------------------------------------------------------------------------------------------------
def Puzzle_2(inputFile, graph):
    return computeMap(inputFile, True, graph)

# ==================================================================================================

figure,graph = myLib.init_matlibgraph(DAY)

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile, graph[0] )))
myLib.display_result("2",str(Puzzle_2( inputFile, graph[1] )))

myLib.save_matlibgraph(figure, DAY)

myLib.display_footer()



