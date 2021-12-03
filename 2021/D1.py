import myLib

DAY       = "D1"
inputFile = "D:\Dev_Perso\\AdventOfCode\\2021\\"+DAY+".txt"

# --------------------------------------------------------------------------------------------------

def resolve( measures: list):
    res=0
    for (a,b) in zip( measures[1:], measures):
        if (a>b): res+=1
    return res


def Puzzle_1( inputFile ):
    return  resolve( myLib.input_as_ints(inputFile) )

def Puzzle_2(inputFile):
    measures         = myLib.input_as_ints(inputFile)
    measuresAgg_way2 = list(map(lambda x: sum(list(x)), list(zip(measures, measures[1:], measures[2:]))))

    return resolve( measuresAgg_way2 )

# --------------------------------------------------------------------------------------------------

myLib.display_header(DAY, inputFile )

myLib.display_result("1", str(Puzzle_1( inputFile )))
myLib.display_result("2", str(Puzzle_2( inputFile )))

myLib.display_footer()


