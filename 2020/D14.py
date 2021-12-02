import string
import copy
import math
import re

inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D14_input.txt"
#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D14_sample.txt"

print("- D12 ---------------------------------------------------------------------------------")
print(inputFile)

def read_instr( file ):
    with open(file) as f:
        lines = [ line.rstrip("\n") for line in f.readlines()]
    instr=[]
    for line in lines:
        mask = re.findall(r"mask = (.*)" , line)
        mem  = re.findall(r"mem\[(.*)\] = (.*)" , line)
        if len(mask) == 1: instr.append( ("mask", mask[0]) )
        if len(mem ) == 1: instr.append( ("mem" , (int(mem[0][0]),int(mem[0][1])) ))
    return instr


def Puzzle_1(instr):

    mask = "X"*36
    memory={}
    for instr, value in instr:
        if instr == "mask":
            mask = value
        else:
            offset, store = value
            adr           = [0]
            binoffset     = list( bin(offset)[2:].zfill(36) )

            for idx, bit in enumerate( list(mask )) :
                if bit == "1" or bit == "0" and binoffset[idx] == "1":
                    adr = [ val + pow(2,35-idx) for val in adr]
                if bit == "X":
                    for val in copy.deepcopy(adr):
                        adr.append( val +  pow(2,35-idx))

            for a in adr:
                memory[a] = store

    return sum(memory.values())

def Puzzle_2(instr):

    return 2


print("------------------------------------------------------------------------------------------")

instr    = read_instr(inputFile)
print(instr)

value =  Puzzle_1( instr )
print( "       PUZZLE_1 : " + str(value) + " " )

value = Puzzle_2( instr )
print( "       PUZZLE_2 : " + str(value) + " " )

print("------------------------------------------------------------------------------------------")
print('END')

