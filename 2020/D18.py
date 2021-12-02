import string
import copy
import math
import copy

from collections import defaultdict
import re
import ast

inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D18_input.txt"
#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D18_sample.txt"

print("====================================================================================================")

print("- D17 ---------------------------------------------------------------------------------")
print(inputFile)

def read_puzzle( file ):
    with open(file) as f:
        puzzle = [ line.rstrip("\n") for line in f.readlines()]
    return puzzle

def compute_1(operation): #A op B op C op D ...
    line  = operation.split(' ',1)
    value = int(line[0])
    while len(line)>1:
        line = line[1].split(' ', 1)
        op   = line[0][0]
        line = line[1].split(' ', 1)
        valB = int(line[0])
        if op == '+': value+=valB
        if op == '*': value*= valB
    return value

def Puzzle_1(puzzle):
    tot=0
    for operation in puzzle:
        line = operation
        while '(' in line:
            findgroup = re.findall(r".*(\([0-9 +*]*\)).*", line)
            for group in findgroup:
                val   = compute_1( group[1:len(group)-1])
                line  = line.replace(group, str(val))
        tot+= compute_1(line)
    return tot

def compute_2(operation): #A op B op C op D ...
    line =' ' + operation + ' '
    while '+' in line:
        findplus = re.findall(r".* ([0-9]+) \+ ([0-9]+).*", line)
        val      = int(findplus[0][0]) + int(findplus[0][1])
        line     = line.replace(' ' + findplus[0][0] + ' + ' + findplus[0][1] + ' ', ' ' + str(val) + ' ')
    while '*' in line:
        findm    = re.findall(r".* ([0-9]+) \* ([0-9]+).*", line)
        val      = int(findm[0][0]) * int(findm[0][1])
        line     = line.replace( ' ' + findm[0][0] + ' * ' + findm[0][1]  + ' ', ' ' + str(val)+ ' ')
    return int(line)

def Puzzle_2(puzzle):

    tot=0
    for operation in puzzle:
        line = operation
        while '(' in line:
            findgroup = re.findall(r".*(\([0-9 +*]*\)).*", line)
            for group in findgroup:
                val   = compute_2( group[1:len(group)-1])
                line  = line.replace(group, str(val))
        tot+= compute_2(line)

    return tot

print("------------------------------------------------------------------------------------------")

puzzle    = read_puzzle(inputFile)
print(puzzle)

value =  Puzzle_1( puzzle )
print( "       PUZZLE_1 : " + str(value) + " " )

puzzle    = read_puzzle(inputFile)
val2 = Puzzle_2( puzzle )
print( "       PUZZLE_2 : " + str(val2) + " " )

print("------------------------------------------------------------------------------------------")
print('END')

