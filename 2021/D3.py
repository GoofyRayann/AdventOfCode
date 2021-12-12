import myLib

DAY       = "D3"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# --------------------------------------------------------------------------------------------------

def Puzzle_1( inputFile ):
    values    = myLib.input_as_list_of_list_of_ints(inputFile)
    nbBits    = len(values[0])
    nbValues  = len(values)
    gammaRate , epsilonRate = '', ''

    for i in range(0,nbBits):
        sumBit       = sum([bits[i] for bits in values])
        gammaRate   += '1' if sumBit > nbValues/2 else '0'
        epsilonRate += '0' if sumBit > nbValues/2 else '1'

    return int(gammaRate,2) * int(epsilonRate,2)

def Puzzle_2_computeBitCritera( values:list[list[int]] , bitCriteria : int):
    nbBits = len(values[0])

    for i in range(0, nbBits):
        nbValues   = len(values)
        sumBit     = sum([bits[i] for bits in values])
        choosenBit = bitCriteria if sumBit >= nbValues / 2 else (bitCriteria+1)%2
        filterList = [bits for bits in values if bits[i] == choosenBit]

        values     = filterList
        if len(values) <= 1: break

    return ''.join(str(bit) for bit in values[0]) #- String '01011' from List [0,1,0,1,1]


def Puzzle_2(inputFile):
    values     = myLib.input_as_list_of_list_of_ints(inputFile)
    oxygenRate = Puzzle_2_computeBitCritera(values, 1 )
    co2Rate    = Puzzle_2_computeBitCritera(values, 0 )

    return int(oxygenRate,2) * int(co2Rate,2)


# --------------------------------------------------------------------------------------------------

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile )))

myLib.display_result("2",str(Puzzle_2( inputFile )))

myLib.display_footer()


