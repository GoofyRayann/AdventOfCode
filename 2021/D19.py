import myLib
import re
from collections import defaultdict
from generativepy.nparray import save_nparray_image
import numpy as np
import math

DAY       = "D19"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# ==================================================================================================

#nbRotations : 0 = 0°   , 1 = 90°  , 2 = 180°, 3=270° counterwise
def rotateAxis(scanner, axis="x", nbRotations=1):
    if nbRotations == 0: return scanner.copy()

    whatRotate= { "z": (0,1), "x": (2,1), "y": (2, 0) }
    (h,v)     = whatRotate[axis]

    rotatedScanner=[]
    for point in scanner:
        newPoint = point.copy()
        (x,y)    = whatRotate[axis]

        if nbRotations == 1:  #  90°: (x,y) => (-y,x)
            newPoint[ x ] = -point[y]
            newPoint[ y] = point[x]

        if nbRotations == 2:  # 180°: (x,y) => (-x,-y)
            newPoint[ x ] = -point[x]
            newPoint[ y ] = -point[y]

        if nbRotations == 3:  # 270°: (x,y) => (y,-x)
            newPoint[ x ] = point[y]
            newPoint[ y ]  = -point[x]

        rotatedScanner.append(newPoint)
    return rotatedScanner

#Returns 24 Variations of a scanner arround the 3 axis
def getVariations( scanner ):
    variations = []

    variations.append( scanner.copy() ) #id 0
    for rotates in range(1,4):
        variations.append(rotateAxis(scanner, axis="x", nbRotations= rotates))

    variations.append(rotateAxis(scanner, axis="y", nbRotations= 1)) #id=4
    for rotates in range(1, 4):
        variations.append(rotateAxis(variations[4], axis="z", nbRotations=rotates))

    variations.append(rotateAxis(scanner, axis="y", nbRotations=2)) #id=8
    for rotates in range(1, 4):
        variations.append(rotateAxis(variations[8], axis="x", nbRotations=rotates))

    variations.append(rotateAxis(scanner, axis="y", nbRotations=3)) #id=12
    for rotates in range(1, 4):
        variations.append(rotateAxis(variations[12], axis="z", nbRotations=rotates))

    variations.append(rotateAxis(scanner, axis="z", nbRotations=1)) #id=16
    for rotates in range(1, 4):
        variations.append(rotateAxis(variations[16], axis="y", nbRotations=rotates))

    variations.append(rotateAxis(scanner, axis="z", nbRotations=3)) #id=20
    for rotates in range(1, 4):
        variations.append(rotateAxis(variations[20], axis="y", nbRotations=rotates))

    return variations

#RETURNS THE NUMBER OF MATCHING POINTS + MOVING VECTOR TO MATCH, BETWEEN 2 SCANNERS
def getNumberMatchingPoints( scanner1, scanner2):

    vectors=[]
    for idPoint1 in range( 0, len(scanner1)):
        for idPoint2 in range( 0, len(scanner2) ):
            (x1, y1, z1) = (scanner1[idPoint1][0],scanner1[idPoint1][1],scanner1[idPoint1][2])
            (x2, y2, z2) = (scanner2[idPoint2][0], scanner2[idPoint2][1], scanner2[idPoint2][2])
            vector      = (x1-x2, y1-y2, z1-z2)
            vectors.append( vector)

    mostCommonVector =  max(set(vectors), key = vectors.count)
    nbMatchingpoints = vectors.count( mostCommonVector)

    return (nbMatchingpoints, mostCommonVector)


# --------------------------------------------------------------------------------------------------
def Puzzle_1( inputFile ):

    #- READ INPUT
    scanners = []
    for rawScanner in open(inputFile).read().split("\n\n"):
         scanners.append( [list( map( int,rawValues.split(',') )) for rawValues in rawScanner.split("\n")[1:] ] )

    #- IDENTIFY 24 VARIATIONS FOR ALL SCANNERS
    scannersVariations = []
    for scanner in scanners:
        scannersVariations.append( getVariations(scanner) )

    #- IDENTIFY SCANNERS THAT HAVE 12 COMMON POINTS

    scannerPositions      = defaultdict()
    scannerPositionned    = defaultdict()
    scannerPositionned[0] = scanners[0]
    scannerPositions[0]   = (0,0,0)
    alreadyScanned        = defaultdict(bool)

    #Recursive find matchings
    def findMatchings(scanner, idScanner ):
        print( "=> Compute ", idScanner)
        for idScanner2 in range(0, len(scannersVariations)):

            if idScanner2 != idScanner \
                    and ( not alreadyScanned[(idScanner, idScanner2)] or not alreadyScanned[(idScanner2, idScanner)] ) :
                alreadyScanned[(idScanner, idScanner2)] = True
                alreadyScanned[(idScanner2, idScanner)] = True

                print("=> Compute scanner ", idScanner, " versus scanner ", idScanner2)

                for idVariation in range(0, len(scannersVariations[idScanner2])):

                    alreadyScanned[(idScanner, idScanner2)] = True
                    alreadyScanned[(idScanner2, idScanner)] = True

                    (matchings, vector) = getNumberMatchingPoints(scanner, scannersVariations[idScanner2][idVariation])

                    if matchings == 12:
                        print("=> Compute scanner ", idScanner, " scanner ", idScanner2, " variation" , idVariation , " MATCHED")
                        repositionnedBeacons = [ [ point[0]+vector[0],point[1]+vector[1],point[2]+vector[2]]
                                                 for point in scannersVariations[idScanner2][idVariation] ]

                        scannerPositions[idScanner2] = ( vector[0], vector[1], vector[2] )
                        scannerPositionned[idScanner2] = repositionnedBeacons

                        findMatchings( repositionnedBeacons,idScanner2 )
        return

    for computeScanner in range( 0, len( scanners) ):
        if scannerPositionned.get( computeScanner ) != None:
            print("GO", computeScanner)
            findMatchings( scannerPositionned[computeScanner], computeScanner )

    #- NOW, scannerPositionned CONTAINS REAL POSITION OF ALL BEACON

    allBeaconsScanned = [ tuple(coord)  for scanner in list( scannerPositionned.values())  for coord in scanner     ]
    resultPuzzle1     = len( set( allBeaconsScanned))

    print( "RESULT PUZZLE 1 = " , resultPuzzle1 )

    #NOW, LETS COMPUTE THE MAX MANHATTAN DISTANCE
    print( scannerPositions)

    maxD=0
    maxPoints= (0,0)
    for ip1 in range( 0, len(scannerPositions)-1):
        for ip2 in range( ip1+1, len(scannerPositions)):
            d = abs( scannerPositions[ip1][0] - scannerPositions[ip2][0]) + \
              abs (scannerPositions[ip1][1] - scannerPositions[ip2][1])  + \
              abs (scannerPositions[ip1][2] - scannerPositions[ip2][2])
            if d> maxD:
                maxD = d
                maxPoints = (ip1,ip2)
    print( maxPoints )
    print( maxD)








    return 0

# --------------------------------------------------------------------------------------------------
def Puzzle_2(inputFile):


    return 0

# ==================================================================================================

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile )))
myLib.display_result("2",str(Puzzle_2( inputFile )))

myLib.display_footer()



