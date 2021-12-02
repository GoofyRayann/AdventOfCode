import string
import copy

inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D11_input.txt"
#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D11_sample.txt"

print("- D11 -----------------------------------------------------------------------------------")
print(inputFile)

def print_seats(seats):
    print('-----------')
    for i in seats: print( ''.join(i))

def read_seats( file ):
    with open(file) as f:
        seats = [list(line.rstrip("\n")) for line in f.readlines()]
    return seats

def nboccupied(x,y,seats,iter):
    nbOccupied = 0
    directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    for (dx, dy) in directions:
        for i in range(1, iter + 1):
            if (y + dy*i < 0) or (x + dx*i < 0) or (y + dy*i >= len(seats)) or (x + dx*i >= len(seats[0])) or (seats[y + dy*i][x + dx*i] == 'L'):
                break
            if seats[y+dy*i][x+dx*i] == '#':
                nbOccupied+=1
                break
    return nbOccupied

def process_round( seats,iter,minoccupied):
    round = copy.deepcopy(seats)

    for x,y in ( (x,y) for x in range(0, len(seats[0])) for y in range(0, len(seats)) ) :
        nb = nboccupied(x, y, seats, iter)
        if seats[y][x] == "#" and nb >= minoccupied: round[y][x] = "L"
        if seats[y][x] == "L" and nb == 0          : round[y][x] = "#"
    return round, True if str(seats) == str(round) else False

def Puzzle( seats,iter,minoccupied):
    round    = seats
    iso      = False
    while not iso:
        (round, iso) = process_round(round, iter, minoccupied)
    return str(round).count('#')

def Puzzle_1( seats):
    return Puzzle(seats,1,4)

def Puzzle_2(seats):
    return Puzzle(seats, max(len(seats), len(seats[0]))+1, 5)

print("------------------------------------------------------------------------------------------")

seats    = read_seats(inputFile)
print(seats)

print("- D11.1 -----------------------------------------------------------------------------------")
value =  Puzzle_1( seats )
print( "       PUZZLE_1 : " + str(value) + " occupied seats" )

print("- D11.2 -----------------------------------------------------------------------------------")

result   = Puzzle_2( seats )
print( "       PUZZLE_2 : " + str(result) + " occupied seats" )

print("------------------------------------------------------------------------------------------")
print('END')

