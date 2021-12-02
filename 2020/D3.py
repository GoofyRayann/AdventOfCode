import math
#1139043-20201203-f3167993

inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D3_input.txt"
inFile = open(inputFile, 'r')

print(inputFile)

print("- D3.1 -----------------------------------------------------------------------------------")
nblines = 0
lines=[]
for line in inFile:
    lines.append(line.rstrip())
    nblines         = nblines + 1

#- CREATE FULL AREA

width         = len(lines[0] )
height        = nblines
slopes        = [ (1,1) , (3,1), (5,1), (7,1), (1,2)]
area          = []
trees         = 1
for slope in slopes:
    area.clear()
    left, down    = slope
    nb_duplicates = round( height / (width/left) ) + 1

    for line in lines:
        area.append(line * nb_duplicates)

    print( 'Left:' + str(left) + ' - Down:' + str( down) + ' - Width:' + str( width) + ' - Height:' + str( height) + ' - NbDuplicates:' + str(nb_duplicates))

    posx=0
    posy=0
    nbtrees = 0

    while posy < height-down:
        posx       = posx + left
        posy       = posy + down

        if( area[posy][posx] == "#" ):
            nbtrees = nbtrees + 1

        area[posy] = area[posy][:posx]  + "X" + area[posy][posx+1:]

    trees = trees * nbtrees
    print( "NB TREES : " + str(nbtrees) )

print( "TOTAL TREES  " + str(trees) )
print('END')
inFile.close()
