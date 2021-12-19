import myLib
import re
import matplotlib.pyplot as plt

DAY       = "D8_test"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# ==================================================================================================

# --------------------------------------------------------------------------------------------------
def Puzzle_1( inputFile , graph):
    linkDigit_NumberSegments= { 0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

    numberOfDigits = [0]*10
    for line in myLib.input_as_lines(inputFile):
        for digit in re.findall(r'\w+', line.split('|')[1]):
            numberOfDigits[ len(digit) ] += 1

    res = sum( [ numberOfDigits[linkDigit_NumberSegments[value]] for value in [1,4,7,8] ] )
    return res

# --------------------------------------------------------------------------------------------------
def Puzzle_2(inputFile, graph):

    def allLettersAreInWord(word: str, letters: str):
        return all(letter in word for letter in letters)

    for line in myLib.input_as_lines(inputFile):
        encodedDigits  = sorted( [ ''.join(sorted(code)) for code in re.findall(r'\w+', line.split('|')[0]) ], key=len)
        digitsToDecode = [ ''.join(sorted(code)) for code in re.findall(r'\w+', line.split('|')[1]) ]
        decodedDigits  = [0] * 10

        print( encodedDigits, digitsToDecode)

        decodedDigits[1] = encodedDigits[0] # mot len(2)
        decodedDigits[4] = encodedDigits[2] # mot len(4)
        decodedDigits[7] = encodedDigits[1] # mot len(3)
        decodedDigits[8] = encodedDigits[9] # mot len(7)

        #- mot len(5) avec toutes lettres digits(1)
        for encodedDigit in [encodedDigits[3],encodedDigits[4],encodedDigits[5] ]:
            if allLettersAreInWord( encodedDigit, decodedDigits[1]):
                decodedDigits[8] = encodedDigit

#				DIGIT	SEGMENTS							NB DIGITS
# 	a
# b		c
# 	d				a	b	c	d	e	f	g
# e		f		1			x			x		2	mot len(2)
# 	g			4		x	x	x		x		4	mot len(4)
# 				7	x		x			x		3	mot len(3)
# 				8	x	x	x	x	x	x	x	7	mot len(7)
# 				3	x		x	x		x	x	5	mot len(5) avec toutes lettres digits(1)
# 				5	x	x		x		x	x	5	mot len(5) avec toutes lettres( lettres digit 4 - lettres digit 1 )
# 				2	x		x	x	x		x	5	mot len(5), le restant
# 				9	x	x	x	x		x	x	6	mot len(6) avec toutes lettres ( lettres digit 3)
# 				6	x	x		x	x	x	x	6	mot len(6) avec toutes lettres( lettres digit 2 - lettres digit 7 )
# 				0	x	x	x		x	x	x	6	mot len(6), le restant



    return 0

# ==================================================================================================

#figure,graph = myLib.init_matlibgraph(DAY)

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile, None )))
myLib.display_result("2",str(Puzzle_2( inputFile, None )))

#myLib.save_matlibgraph(figure, DAY)

myLib.display_footer()



