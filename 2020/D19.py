import string
import nltk
from nltk import CFG

#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D19_input.txt"
inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D19_input_2.txt"
#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D19_sample.txt"

print("= TEST NLTK ===================================================================================================")

grammar = CFG.fromstring(""" 
0 -> 4 1 5 
1 -> 2 3 | 3 2 
2 -> 4 4 | 5 5 
3 -> 4 5 | 5 4 
4 -> 'a' 
5 -> 'b' 
""")
messages = ["ababbb","bababa","abbbab","aaabbb","aaaabbb"]
#parser = nltk.ChartParser(grammar)
#for message in messages:
#    print(message)
#    for t in parser.parse(message):
#        print(t.pretty_print())

print("====================================================================================================")

print("- D19 ---------------------------------------------------------------------------------")
print(inputFile)

def read_puzzle( file ):
    with open(file) as f:
        lines = [ line.rstrip("\n") for line in f.readlines()]
    lines.sort() #!!!!! Grammar must start by top level
    syntax = ""
    messages = []
    for line in lines:
        str=line.replace('"', "'").replace(':', " ->")
        if '->' in str: syntax+= str + "\n"
        else          : messages.append(line)
    print(syntax)
    grammar = CFG.fromstring(syntax)
    return grammar,messages

def Puzzle_1(grammar,messages):
    count=0
    parser = nltk.ChartParser(grammar)
    for message in messages:
        for tree in parser.parse(message):
            count+=1
            #print(tree.pretty_print())
        print(count,message)
    return count

def Puzzle_2(grammar,messages):


    return 0

print("------------------------------------------------------------------------------------------")

grammar,messages    = read_puzzle(inputFile)
print("grammar",grammar)
print("messages",messages)

value =  Puzzle_1( grammar,messages )
print( "       PUZZLE_1 : " + str(value) + " " )

val2 = Puzzle_2( grammar,messages )
print( "       PUZZLE_2 : " + str(val2) + " " )

print("------------------------------------------------------------------------------------------")
print('END')

