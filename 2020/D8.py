import string
import copy
#1139043-20201203-f3167993


inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D8_input.txt"
#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D8_sample.txt"
inFile = open(inputFile, 'r')

print("- D7 -----------------------------------------------------------------------------------")
print(inputFile)

# ------------------------------------------------------------------------------------------------
def read_code( file ):
    program = []
    inFile        = open(inputFile, 'r')
    id=1
    for line in inFile:
        program.append( (id, line.rstrip("\n").split(' ') + [False] ))
        id+=1
    inFile.close()

    return dict(program)

def run_code( idx, code, accumulator):
    if code[idx][2]: #Command already launched
        #print( "PROGRAM LOOP" , idx, accumulator )
        True
    else:
        code[idx][2] = True
        accumulator += int(code[idx][1]) if code[idx][0] == "acc" else 0
        idx         += int(code[idx][1]) if code[idx][0] == "jmp" else 1

        if idx == len( code ) + 1:
            print( "PROGRAM TERMINATED SUCCESSFULL" , idx, accumulator )
        else:
            ( idx, code, accumulator) = run_code( idx, code, accumulator)
    return (idx,accumulator,False)

code = read_code(inputFile)
for code_line in read_code(inputFile):
    if code[code_line][0] == "jmp":
        code_updated = copy.deepcopy(code)
        code_updated[code_line] = ["nop" , code_updated[code_line][1] , code_updated[code_line][2] ]
        run_code(1, code_updated, 0)

print('END')
inFile.close()
