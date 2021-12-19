import myLib
import math

DAY       = "D16"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"


workflow=[ "version" , "typeId", "valueType4", "operator"]
pos = 0

sumVersion = 0

def computePacket( bits, mainPacket, indent):
    global pos
    global sumVersion
    indent+='   '
    result  = 0

    VERSION = int(bits[pos:pos + 3], 2)
    sumVersion += VERSION
    pos += 3

    TYPEID = int(bits[pos:pos + 3], 2)
    pos += 3

    if TYPEID == 4:
        readValue = ''
        while bits[pos] == '1':
            readValue += bits[pos + 1:pos + 5]
            pos += 5
        readValue += bits[pos + 1:pos + 5]
        pos += 5
        LITERALVALUE = int(readValue, 2)
        result       = LITERALVALUE
        print(indent, 'PACKET ',VERSION,'-',TYPEID,': LITERAL VALUE = ', LITERALVALUE)

    if TYPEID != 4:

        literalValues=[]

        if bits[pos] == '1':
            pos += 1
            nbSubPackets = int(bits[pos:pos + 11], 2)
            pos += 11
            print(indent, 'PACKET ', VERSION, '-', TYPEID, ': OPERATOR (', nbSubPackets, ' packets)')

            for i in range(0, nbSubPackets):
                literalValues += [ computePacket( bits,  False, indent) ]

        else :
            pos += 1
            nbBitsSubPackets = int(bits[pos:pos + 15], 2)
            pos += 15
            print(indent,'PACKET ', VERSION, '-', TYPEID, ': OPERATOR (', nbBitsSubPackets, ')')

            destPos = pos + nbBitsSubPackets
            while pos < destPos:
                literalValues += [ computePacket(bits, False, indent) ]

        if TYPEID == 0:  result = sum( literalValues )
        if TYPEID == 1:  result = math.prod( literalValues)
        if TYPEID == 2:  result = min( literalValues )
        if TYPEID == 3:  result = max( literalValues )
        if TYPEID == 5:  result = 1 if literalValues[0] > literalValues[1] else 0
        if TYPEID == 6:  result = 1 if literalValues[0] < literalValues[1] else 0
        if TYPEID == 7:  result = 1 if literalValues[0] == literalValues[1] else 0

        print(indent, 'PACKET ', VERSION, '-', TYPEID, ': RESULT = ', result )

    if mainPacket and pos % 8 != 0: pos += 8 - (pos % 8)  # to take care extras dus to hex representation

    return result



# --------------------------------------------------------------------------------------------------
def Puzzle_1( inputFile ):

    transmissions = myLib.input_as_lines((inputFile))
    print( transmissions)
    bits = bin( int('1'+transmissions[0], 16) )[3::]
    print( bits )

    while pos < len(bits):
        print( 'RES PUZZLE 2 = ' , computePacket(bits, True, '') )

    print ( 'RES PUZZLE 1 = ' , sumVersion )

    return 0

# --------------------------------------------------------------------------------------------------
def Puzzle_2(inputFile):

    return 0

# ==================================================================================================

myLib.display_header(DAY, inputFile )

myLib.display_result("1",str(Puzzle_1( inputFile )))
myLib.display_result("2",str(Puzzle_2( inputFile )))

myLib.display_footer()



