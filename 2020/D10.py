from functools import reduce
import string
import copy
#1139043-20201203-f3167993

inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D10_input.txt"
#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D10_sample.txt"

print("- D10 -----------------------------------------------------------------------------------")
print(inputFile)

def read_adapters( file ):
    with open(file) as f:
        adapters = [int(line) for line in f.readlines()]
        adapters.sort()
    return adapters

def Puzzle_1( outlet, adapters):
    diffs=[0,0,0]
    print( adapters)
    for idx in range(0, len(adapters) ):
        if adapters[idx] <= outlet +3:
            diffs[adapters[idx] - outlet-1] += 1
            outlet = adapters[idx]
    print(diffs)
    return diffs

def Puzzle_2( outlet, adapters):
    adapters=[0]+adapters
    res     =[1]*(len(adapters))
    print( adapters)

    for idx in range(len(adapters) - 1, -1, -1):

        try:
            res[idx] = res[idx + 1]

            if adapters[idx + 2] - adapters[idx] <= 3:
                res[idx] += res[idx + 2]
        except IndexError:
            True

        try:
            if adapters[idx + 3] - adapters[idx] <= 3:
                res[idx] += res[idx + 3]
        except IndexError:
            True

        try:
            True
        except IndexError:
            True

    return res[0]


print("------------------------------------------------------------------------------------------")

adapters    = read_adapters(inputFile)
adapters.append( adapters[len(adapters)-1] + 3)
outlet = 0

print("- D10.1 -----------------------------------------------------------------------------------")

result = Puzzle_1( outlet, adapters)
print( "PUZZLE_1 : " + str(result[0]*result[2]) )

print("- D10.2 -----------------------------------------------------------------------------------")

result = Puzzle_2( 6, adapters)
print( "PUZZLE_2 : " + str(result) )


print("------------------------------------------------------------------------------------------")
print('END')

