import string
import copy
import math

DAY="20"
inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D"+DAY+"_input.txt"
#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D"+DAY+"_sample.txt"

print("====================================================================================================")

print("- D"+DAY+" ---------------------------------------------------------------------------------")
print(inputFile)

#================================================================================================================
def rotate( HDBG ): # (H,D,B,G) = 1111110010, 0010100000, 1000110100, 0100001000
    return (  HDBG[3][::-1], HDBG[0] , HDBG[1][::-1] , HDBG[2])

def flipH( HDBG ): #1111110010 0010100000 1000110100 0100001000
    return (HDBG[0][::-1], HDBG[3], HDBG[2][::-1],HDBG[1])

def convInt( HDBG): #1111110010 0010100000 1000110100 0100001000
    return ( int(HDBG[0],2) , int(HDBG[1],2) , int(HDBG[2],2) , int(HDBG[3],2) )

def linesMatch( tiles, lineup,linedown):
    for idxTile in range(0,len(lineup)):
        if  tiles[lineup[idxTile]][1][2] != tiles[linedown[idxTile]][1][0]:
            return False
    return True

def flipMatrice(matrice):
    return [ str[::-1] for str in matrice ]

def rotateMatrice(matrice):
    mat=[]
    for x in range( 0, len(matrice[0]) ):
        str=''
        for y in range(len(matrice)-1 , -1, -1): str+=matrice[y][x]
        mat.append(str)
    return mat

def removeBorderMatrice(matrice):
    mat=[]
    for y in range( 1, len(matrice)-1 ):
        mat.append( matrice[y][1: len(matrice[y])-1])
    return mat


#================================================================================================================
def read_puzzle( file ):
    raw_tiles = {}
    with open(file) as f:
        for line in f.readlines():
            line=line.rstrip("\n")
            if line == '': continue
            if 'Tile' in line:
                tileId= int(line.split(' ')[1].split(':')[0])
                raw_tiles[tileId]=[]
            else:
                raw_tiles[tileId].append(line)

    tiles    =[]
    for tile in raw_tiles:
        H = raw_tiles[tile][0]                              .replace('.','0').replace('#','1')
        D = ''.join([x[len(x)-1] for x in raw_tiles[tile]]) .replace('.','0').replace('#','1')
        B = raw_tiles[tile][len(raw_tiles[tile][0])-1]      .replace('.','0').replace('#','1')
        G = ''.join([x[0] for x in raw_tiles[tile] ])       .replace('.','0').replace('#','1')

        tiles.append( (tile, convInt( (H,D,B,G) )                                 , "R0F0" ) )
        tiles.append( (tile, convInt( rotate( (H, D, B, G) ))                     , "R1F0" ) )
        tiles.append( (tile, convInt( rotate( rotate( (H, D, B, G) )))            , "R2F0" ) )
        tiles.append( (tile, convInt( rotate( rotate( rotate( (H, D, B, G)))))    , "R3F0" ) )

        tiles.append( (tile, convInt(flipH((H, D, B, G)))                         , "R0F1" ) )
        tiles.append( (tile, convInt(rotate(flipH((H, D, B, G))))                 , "R1F1" ) )
        tiles.append( (tile, convInt(rotate(rotate(flipH((H, D, B, G)))))         , "R2F1" ) )
        tiles.append( (tile, convInt(rotate(rotate(rotate(flipH((H, D, B, G)))))) , "R3F1" ) )

    return raw_tiles, tiles

#================================================================================================================
#---- COMPUTE ALL POSSIBLE LINE COMBINATIONS
def IdentifyUniqLines(raw_tiles,  tiles):
    print("- IDENTIFY ALL LINES COMINAISONS ======================================", end='')
    nbgrid=int(math.sqrt( len(raw_tiles)))
    combis_lines=[]
    combis_lines.append([ [idx] for idx in range(0, len( tiles)) ])
    for iteration in range(0,nbgrid-1):
        combisIter=[]
        for combi in combis_lines[iteration]:
            leftValInCombi  = tiles[combi[0]]           [1][3]
            rightValInCombi = tiles[combi[len(combi)-1]][1][1]
            idTilesInCombi  = [ tiles[k][0] for k in combi]
            for noTile, tile in enumerate(tiles):
                idTile       = tile[0]
                leftvalTile  = tile[1][3]
                rightvalTile = tile[1][1]
                if idTile not in idTilesInCombi:
                    if rightvalTile == leftValInCombi  : combisIter.append( [noTile] + combi    )
                    if leftvalTile  == rightValInCombi : combisIter.append( combi    + [noTile] )
        combis_lines.append( [list(x) for x in set(tuple(x) for x in combisIter)] )
        print("." , end='')
    print('')
    lines=combis_lines[ len(combis_lines)-1]
    return lines

#================================================================================================================
#---- COMPUTE ALL LINE BETWEEN THEMSELVES
def IdentifyImages(raw_tiles, tiles, lines):
    print("- IDENTIFY ALL LINES MATCHINGS ========================================", end='')
    nbgrid=int(math.sqrt( len(raw_tiles)))
    combis = []
    combis.append([[idx] for idx in range(0, len(lines))])
    for iteration in range(0, nbgrid - 1):
        combisIter = []
        for combi in combis[iteration]:
            for idxline, line in enumerate(lines):
                if idxline in combi: continue
                ATileAlreadyExists = False
                for noTileLine in line:
                    idTileLine= tiles[noTileLine][0]
                    for noLineInCombi in combi:
                        for noTileInLineCombi in lines[noLineInCombi]:
                            if tiles[noTileInLineCombi][0] == idTileLine:
                                ATileAlreadyExists = True
                if  ATileAlreadyExists: continue
                if linesMatch( tiles, line                        , lines[combi[0]]) : combisIter.append( [idxline] + combi )
                if linesMatch( tiles, lines[combi[ len(combi)-1]] , line           ) : combisIter.append( combi  + [idxline])
        combis.append( [list(x) for x in set(tuple(x) for x in combisIter)] )
        print("." , end='')
    print('')
    return combis[nbgrid-1]

#================================================================================================================
#---- CREATE FINAL IMAGE
def CreateFinalImage(raw_tiles, tiles, lines, images):
    print("- CREATE FINAL IMAGE ========================================")
    result=[]
    for line in images[0]:
        LINE=['']*100
        for noTile in lines[line]:
            idxTile = tiles[noTile][0]
            transfo = tiles[noTile][2] #RnFn
            tile    = raw_tiles[idxTile]
            if transfo[3]=="1":
                tile = flipMatrice( tile)
            for _ in range( 0, int(transfo[1])) :
                tile =rotateMatrice(tile)
            tile=removeBorderMatrice(tile)
            for idx, str in enumerate(tile):
                LINE[idx]+=str
            LINE=LINE[:len(tile)]
        for str in LINE:
            result.append(str)
    return result

#================================================================================================================
def Puzzle_1(raw_tiles,  tiles):
    nbgrid = int(math.sqrt(len(raw_tiles)))
    lines  = IdentifyUniqLines(raw_tiles,  tiles)
    images = IdentifyImages(raw_tiles, tiles, lines) #[[noline, noline, noline] , ..., [noline, noline, noline] ]

    print( "images :",images )
    print( "angle 1 :",tiles[ lines[ images[0][0] ][0]][0]
           ,"angle 2 :",tiles[ lines[ images[0][0]][nbgrid-1]][0]
           ,"angle 3 :",tiles[ lines[images[0][nbgrid-1]][0]][0]
           ,"angle 4 :",tiles[ lines[images[0][nbgrid-1]][nbgrid-1]][0])

    return tiles[ lines[ images[0][0] ][0]][0] \
           * tiles[ lines[ images[0][0]][nbgrid-1]][0]\
           * tiles[ lines[images[0][nbgrid-1]][0]][0]\
           * tiles[ lines[images[0][nbgrid-1]][nbgrid-1]][0]

def Puzzle_2(raw_tiles, tiles):
    lines      = IdentifyUniqLines(raw_tiles, tiles)
    images     = IdentifyImages(raw_tiles, tiles, lines)  # [[noline, noline, noline] , ..., [noline, noline, noline] ]
    finalImage = CreateFinalImage(raw_tiles, tiles, lines, images)
    monster    = ['                  # ' , '#    ##    ##    ###' , ' #  #  #  #  #  #   ']
    monsterXY  = []

    for dx, dy in ((dx, dy) for dx in range(0, len(monster[0])) for dy in range(0, len(monster))):
        if monster[dy][dx] == "#":
            monsterXY.append( (dx,dy) )

    finalImages=[]
    finalImages.append(finalImage)
    finalImages.append(rotateMatrice(finalImage))
    finalImages.append(rotateMatrice(rotateMatrice(finalImage)))
    finalImages.append(rotateMatrice(rotateMatrice(rotateMatrice(finalImage))))
    finalImages.append(flipMatrice(finalImage))
    finalImages.append(rotateMatrice(flipMatrice(finalImage)))
    finalImages.append(rotateMatrice(rotateMatrice(flipMatrice(finalImage))))
    finalImages.append(rotateMatrice(rotateMatrice(rotateMatrice(flipMatrice(finalImage)))))

    imageWithMonsters = []
    monsterCoords     = []
    for image in (finalImages):
        for x in range( 0, len(image[0]) - len(monster[0]) +1 ):
            for y in range(0, len(image) - len(monster) +1 ):
                monsterFound=True
                for dx,dy in monsterXY:
                    if image[y+dy][x+dx] != "#":
                        monsterFound=False
                        break
                if monsterFound:
                    imageWithMonsters = image
                    monsterCoords.append((x,y))

    for x,y in monsterCoords:
        for dx,dy in monsterXY:
            imageWithMonsters[y+dy] = imageWithMonsters[y+dy][0:x+dx] + 'O' +  imageWithMonsters[y+dy][x+dx+1:]

    for line in imageWithMonsters: print(line)
    tot=0
    for line in imageWithMonsters: tot+= line.count('#')
    return tot

print("------------------------------------------------------------------------------------------")

raw_tiles, tiles    = read_puzzle(inputFile)
print("raw_tiles : ",raw_tiles)
print("tiles     : ",tiles)

value =  Puzzle_1( raw_tiles, tiles )
print( "       PUZZLE_1 : " + str(value) + " " )

puzzle    = read_puzzle(inputFile)
val2 = Puzzle_2( raw_tiles, tiles )
print( "       PUZZLE_2 : " + str(val2) + " " )

print("------------------------------------------------------------------------------------------")
print('END')

