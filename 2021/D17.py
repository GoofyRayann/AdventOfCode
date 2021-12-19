import myLib

DAY       = "D17"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# ==================================================================================================
# I DID IT IN VERY DIRTY BULKED MODE. DON'T KNOW OF TO DO IT IN A NICER WAY...
# THE HIGHEST IS (vx,vy,HIGHEST) (HIGHEST=answer of Puzzle 1) :  (19, 108, 5886)
# THERE ARE  1806  DISTINCT VELOCITIES THAT REACH THE TARGET (=answer of PUZZLE 3)
# ==================================================================================================

def sumVal(x): return x * (x + 1) // 2
def positionX( xVelocity, noStep):
    res = 0
    for i in range( 1, noStep+1):
        res+=xVelocity
        xVelocity+= -1 if xVelocity > 0 else 0
    return res

def positionY( yVelocity, noStep): return yVelocity * noStep - sumVal( noStep-1)
def velocity( position, noStep): return ( position + sumVal( noStep-1) ) / noStep

# --------------------------------------------------------------------------------------------------
def Puzzle_1( inputFile ):

    #- test
    ( xTargetMin, xTargetMax ) = ( 20, 30 )
    ( yTargetMin, yTargetMax ) = (-10, -5 )

    #- PUZZLE
    (xTargetMin, xTargetMax) = (179, 201)
    (yTargetMin, yTargetMax) = (-109, - 63)

    yIterations = 1000 #- Truc bien bourrin!

    print("FIND ALL REACHED")
    reached=[]
    for vx in range( 1,xTargetMax+1):
        for vy in range ( yTargetMin ,yIterations):
            (x,y)      = (0,0)
            (dvx, dvy) = (vx, vy )
            while y >= yTargetMin:
                (x, y) = (x + dvx, y+dvy)
                dvy   += -1
                if dvx >0: dvx+=-1
                if yTargetMin <= y <= yTargetMax and xTargetMin <= x <= xTargetMax:
                    reached.append( (vx,vy) )
                    print( "Reached (vx,vy):", vx,vy)

    print( "NOW, FIND HIGHEST POINT FOR EACH REACHED")

    highests=[]
    for ( vx, vy ) in reached:
        (x, y)     = (0, 0)
        (dvx, dvy) = (vx, vy)
        highest    = 0
        while y >= yTargetMin:
            (x, y) = (x + dvx, y+dvy)
            dvy   += -1
            if dvx >0: dvx+=-1
            if y > highest:
                highest = y
                print( "Highest point is: ", highest, "for velocity x,y:", vx,vy)
                highests.append( (vx,vy,highest))

    print("-------------------------------------------------------------")
    print(" THE HIGHEST IS (vx,vy,HIGHEST) (HIGHEST=answer of Puzzle 1) : ", max( highests, key= lambda x:x[2]))
    print( "THERE ARE ",  len( list(set(reached))) , " DISTINCT VELOCITIES THAT REACH THE TARGET (=answer of PUZZLE 3)" )

    return 0

# --------------------------------------------------------------------------------------------------
def Puzzle_2(inputFile):

    return 0

# ==================================================================================================

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile )))
myLib.display_result("2",str(Puzzle_2( inputFile )))

myLib.display_footer()



