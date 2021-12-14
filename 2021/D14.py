import myLib
import re
from collections import defaultdict
from generativepy.nparray import save_nparray_image
import numpy as np

DAY       = "D14"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# ==================================================================================================


# --------------------------------------------------------------------------------------------------
def Puzzle_1( inputFile ):

    #- GET TEMPLATE + PAIRS
    lines     = open(inputFile).read().rstrip("\n").split("\n")
    templates = []
    pairs     = {}

    templates.append( list( lines[0]) )

    for line in lines[2:]:
        pairs[ ( line[0], line[1] ) ] = line[ 6 ]

    #- COMPUTE STEPS BY STEP EACH TEMPLATE FROM PREVIOUS ONE

    for step in range (1,11):
        newTemplate = []
        for indexElement in range ( 1, len( templates[step-1] ) ):
            element1 = templates[step - 1][indexElement - 1]
            element2 = templates[step - 1][indexElement ]

            newTemplate.append( element1 )
            newTemplate.append( pairs[ (element1 , element2 ) ] )
        newTemplate.append(templates[step - 1][-1])
        templates.append( newTemplate )
        print( "Step ", step, "-", ''.join(newTemplate))

    #- RESULT A STEP 10
    print ( "STEP 10: " , [[x, templates[10].count(x)] for x in set(templates[10])] )

    #- NEED TO COMPUTE THE RESULT, I DID IT MANUALY :)

    return 0

# --------------------------------------------------------------------------------------------------
def Puzzle_2(inputFile):
    lines = open(inputFile).read().rstrip("\n").split("\n")

    templates = []
    pairs     = {}

    template  = defaultdict(int)

    #- templates[ step ] = { (elem,elem) : nb , (elem,elem) : nb , ...}
    for i in range(0, len(lines[0])-1):
        template[ (lines[0][i],lines[0][i+1])] += 1
    templates.append(template)

    #- pairs = { (elem, elem) : elem, (elem, elem) : elem, ... }
    for line in lines[2:]:
        pairs[(line[0], line[1])] = ( line[6], ( line[0],line[6]), ( line[6],line[1]) )

    #- Count for each step the numbers of pairs in the template, from the prevoius template
    for step in range(1, 41):
        newTemplate = defaultdict(int)
        templates.append(newTemplate)
        for element in templates[step-1]:
            templates[step][ pairs[element][1] ] += templates[step-1][element]
            templates[step][ pairs[element][2] ] += templates[step-1][element]

    #- Count the numbers of pairs for each letters
    for step in range(0, 41):
        print( "TOTAUX STEP " , step)
        cntElements = defaultdict(int)
        for (element1, element2) in templates[step]:
            cntElements[ element1] += templates[step][(element1, element2)]
        cntElements[lines[0][-1]] += 1

        print("  Min = ", min(cntElements, key=cntElements.get), cntElements[min(cntElements, key=cntElements.get)])
        print("  Max = ", max(cntElements, key=cntElements.get), cntElements[max(cntElements, key=cntElements.get)])
        print("  Res = ", cntElements[max(cntElements, key=cntElements.get)] - cntElements[ min(cntElements, key=cntElements.get) ])

    return 0


# ==================================================================================================

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile )))
myLib.display_result("2",str(Puzzle_2( inputFile )))

myLib.display_footer()



