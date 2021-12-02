import string
import copy
import math
import re

inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D16_input.txt"
#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D16_sample.txt"

print("- D16 ---------------------------------------------------------------------------------")
print(inputFile)

def read_rules( file ):
    with open(file) as f:
        lines = [ line.rstrip("\n") for line in f.readlines()]
    tickets=[]
    fields =[]

    for line in lines:
        if bool( re.match("^.*:.*-.* or .*-.*", line) ):
            mask = re.findall(r"(.*): (.*)-(.*) or (.*)-(.*)", line)
            fields.append(mask)
        if bool(re.match("^.*,.*", line)):
            tickets.append(line)
    fields   = [ ( x[0], int(x[1]), int(x[2]), int(x[3]),int(x[4]) )  for x in  sum( fields,[])]
    myticket = tickets[0]
    tickets  = tickets[1:]

    return (myticket, fields,tickets)

def Puzzle_1(fields, tickets):
    badvalues=[]
    from_to = sum( [ [(x[1],x[2]), (x[3],x[4]) ] for x in  fields] , [])
    for ticket in tickets:
        for value in [int(val) for val in ticket.split(',')]:
            if not any( rfrom <= value <= rto for (rfrom, rto) in from_to):
                badvalues.append(value)
    return sum(badvalues)

def Puzzle_2(fields, tickets, myticket):

    #- IDENTIFY GOOD TICKETS
    from_to = sum( [ [(x[1],x[2]), (x[3],x[4]) ] for x in  fields] , [])
    goodtickets = []
    for ticket in tickets:
        test=True
        for value in [int(val) for val in ticket.split(',')]:
            if not any( rfrom <= value <= rto for (rfrom, rto) in from_to):
                test=False
                break
        if test: goodtickets.append(ticket)

    goodtickets.append( myticket )

    #- TRANSFORM COLUMN FIELD VALUES TO LINE
    colvalues= [[] for i in range(0,len(  goodtickets[0].split(','))) ]
    for ticket in goodtickets:
        for id, val in [ ( id, int(val) ) for id, val in enumerate( ticket.split(',')) ] :
            colvalues[id]+=[val]

    #- CREATE LIST FIELD =>  COLUMNS MATCHING
    matches={}
    for field in fields:
        matches[field[0]]= []
        from_to          = [(field[1], field[2]), (field[3], field[4])]
        for col, values in enumerate( colvalues ) :
            if all( from_to[0][0] <= value <= from_to[0][1] or from_to[1][0] <= value <= from_to[1][1] for value in values):
                matches[field[0]].append( col )

    #- IDENTIFY WHAT UNIQ COLUMN MATCH A FIELD
    results = {}
    while matches != {}:
        for field in matches:
            if len( matches[field] ) == 1:
                results[field] = matches[field][0]
                matches.pop(field)
                for f in matches:
                    l = matches[f]
                    l.remove(results[field])
                    matches[f] = l
                break
    print(results)

    #COMPUTE RESULT
    result=1
    for bob in results:
        if bob.startswith("departure"):
            result*=int(myticket.split(',')[results[bob]])

    return result


print("------------------------------------------------------------------------------------------")

myticket, fields,tickets    = read_rules(inputFile)
print(fields, myticket, tickets)

value =  Puzzle_1( fields, tickets )
print( "       PUZZLE_1 : " + str(value) + " " )

value = Puzzle_2( fields, tickets, myticket )
print( "       PUZZLE_2 : " + str(value) + " " )

print("------------------------------------------------------------------------------------------")
print('END')

