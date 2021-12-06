import myLib
import matplotlib.pyplot as plt

DAY       = "D2"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# --------------------------------------------------------------------------------------------------

def Puzzle_1a( inputFile , graph ):
    graph.axis('on')
    posHorizontal = 0
    posDepth      = 0
    rules         = { "forward" : (1,0), "up" : (0,-1), "down" : (0,1)}  #-> action : ( affectH, affectD )

    for line in myLib.input_as_lines(inputFile):
        x, y           = posHorizontal, posDepth
        command        = line.split(' ')
        rule           = rules[command[0]]
        posHorizontal += rule[0] * int(command[1])
        posDepth      += rule[1] * int(command[1])

        graph.plot([x, posHorizontal], [-y, -posDepth], linewidth=0.5, color=(0, 0, 0))

    return  posHorizontal * posDepth

def Puzzle_1b( inputFile ):

    values     = [ ( line.split(" ")[0] , int(line.split(" ")[1]) )  for line in myLib.input_as_lines(inputFile) ]
    sumForward = sum(v if a == "forward" else 0 for a, v in values)
    sumUp      = sum(v if a == "up"      else 0 for a, v in values)
    sumDown    = sum(v if a == "down"    else 0 for a, v in values)

    return sumForward * ( sumDown - sumUp )

def Puzzle_2(inputFile, graph):
    graph.axis('on')
    posAim        = 0
    posHorizontal = 0
    posDepth      = 0
    rules         = {"forward": (1, 0, 1), "up": (0, -1, 0), "down": (0, 1, 0)} # -> action : ( affectH, affectA, affectD )

    for line in myLib.input_as_lines(inputFile):
        x,y            = posHorizontal, posDepth
        command,value  = line.split(' ')
        rule           = rules[command]
        posAim        += rule[1] * int(value)
        posHorizontal += rule[0] * int(value)
        posDepth      += rule[2] * int(value) * posAim

        graph.plot([x,posHorizontal], [-y,-posDepth], linewidth=0.5, color=(0, 0, 0))

    return posHorizontal * posDepth

# --------------------------------------------------------------------------------------------------

figure,graph = myLib.init_matlibgraph(DAY)

myLib.display_header(DAY, inputFile )

myLib.display_result("1a",str(Puzzle_1a( inputFile , graph[0])))
myLib.display_result("1b",str(Puzzle_1b( inputFile )))
myLib.display_result("2 ",str(Puzzle_2( inputFile, graph[1] )))

myLib.display_footer()

myLib.save_matlibgraph(figure, DAY)

