import string
import copy
import math

inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D13_input.txt"
#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D13_sample.txt"

print("- D12 ---------------------------------------------------------------------------------")
print(inputFile)

def read_notes( file ):
    with open(file) as f:
        notes = [ line.rstrip("\n") for line in f.readlines()]
    return notes


def Puzzle_1(notes):
    mindepart   = int(notes[0])
    buses       = list(set(notes[1].split(',')))
    buses       = filter(lambda a: a != 'x', buses)
    buses       = [int(item) for item in buses]

    firstDeparts= {}
    for bus in buses:
        firstDeparts[bus] = math.ceil(mindepart / bus) * bus - mindepart
    firstBus = min(firstDeparts, key=firstDeparts.get)
    return ( firstBus * firstDeparts[firstBus] )

def Puzzle_2(notes):
    all_buses = []
    for index, bus in ((index, bus) for index, bus in  enumerate( notes[1].split(',') ) if bus != 'x'):
        all_buses.append((index, int(bus)))
    print( all_buses )

    t=all_buses[0][1]
    delta=all_buses[0][1]
    for i in range(1, len(all_buses)):
        while (t+all_buses[i][0])%all_buses[i][1] != 0:
            t+=delta
        delta *= all_buses[i][1]
    return t


print("------------------------------------------------------------------------------------------")

notes    = read_notes(inputFile)
print(notes)

value =  Puzzle_1( notes )
print( "       PUZZLE_1 : " + str(value) + " " )

value = Puzzle_2( notes )
print( "       PUZZLE_2 : " + str(value) + " " )

print("------------------------------------------------------------------------------------------")
print('END')

