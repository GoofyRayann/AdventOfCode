import re
#1139043-20201203-f3167993

inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D5_input.txt"
#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D5_sample.txt"
inFile = open(inputFile, 'r')

print(inputFile)

print("- D5 -----------------------------------------------------------------------------------")
# ------------------------------------------------------------------------------------------------
# INPUT: FBFBBFBRRL
# OUTPUT: ["FBFBBFBRRL","..."]
# ------------------------------------------------------------------------------------------------
def read_seats( file ):
    raw_seats = []
    inFile    = open(inputFile, 'r')
    for raw_seat in inFile:
        raw_seats.append(raw_seat.rstrip("\n"))
    inFile.close()
    return raw_seats

# ------------------------------------------------------------------------------------------------
# INPUT:
def parse_seat( seat ):
    seatid = 0
    rowSeat  = seat[0:7]
    lineSeat = seat[7:]
    rowCode  = 0
    lineCode = 0

    #- ROW 1 2 3 4 5 6 7 (B or F) B=1 F=0
    for position in list(range( 7 )):
        if rowSeat[position] == "B" :
            rowCode = rowCode + int( pow( 2, 7-position ) / 2 )

    #- SEAT 8 9 10 (R or L) R=1 L=0
    for position in list(range( 3 )):
        if lineSeat[position] == "R" :
            lineCode = lineCode + int( pow( 2, 3-position ) / 2 )


    return ( rowCode *8 + lineCode, seat )

allSeats=[]
for seat in read_seats( inputFile ):
    allSeats.append(parse_seat(seat))

seats = dict( allSeats )
for id in range( 1, 1024 ):
    try:
        freeSeat = seats[id]
        print("seat " + str(id) + " exists, KO")
    except KeyError:
        print("seat " + str(id) + " doesn't exists, could be mine" )
        try:
            seatplus = seats[id+1]
            try:
                seatplus = seats[id - 1]
                print("seat " + str(id) + " +1 and -1 exist, so it could be mine!!!!!!!!")
            except KeyError:
                print("seat " + str(id) + " the -1 doesn't exists, so KO")
        except KeyError:
            print("seat " + str(id) + " the +1 doesn't exists, so KO")

print('END')
inFile.close()




