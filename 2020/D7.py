import string
#1139043-20201203-f3167993

inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D7_input.txt"
#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D7_sample.txt"
inFile = open(inputFile, 'r')

print("- D7 -----------------------------------------------------------------------------------")
print(inputFile)

# ------------------------------------------------------------------------------------------------
# INPUT:  vibrant purple bags contain 3 shiny lavender bags, 1 mirrored gray bag, 4 muted bronze bags.
# OUTPUT: [('vibrant purple', [('shiny lavender', '3'), ('mirrored gray', '1'), ('muted bronze', '4')])
#        , ('posh crimson'  , [('drab plum', '4'), ('dotted purple', '5'), ('vibrant lavender', '3'), ('striped plum', '2')]),...
def read_rules( file ):
    containers = []
    inFile        = open(inputFile, 'r')

    for line in inFile:
        container = line.split(' bags contain ')[0].rstrip().lstrip()
        contains  = extract_bags_from_what_contains( line.split(' bags contain ')[1].rstrip("\n") )
        containers.append( (container,contains) )
    return containers

# ------------------------------------------------------------------------------------------------
# INPUT:  3 shiny lavender bags, 1 mirrored gray bag, 4 muted bronze bags.
# OUTPUT: [('shiny lavender', '3'), ('mirrored gray', '1'), ('muted bronze', '4')]
# ------------------------------------------------------------------------------------------------
def extract_bags_from_what_contains(rule):
    bags=[]
    for rule_bag in rule.replace('bags,','|').replace('bag,','|').replace('bags.','|').replace('bag.','|').split('|'):
        try:
            number =  rule_bag.rstrip().lstrip().split(' ')[0]
            if number != 'no':
                color = rule_bag.rstrip().lstrip().split(' ',1)[1]
                bags.append(( color, number) )
        except IndexError:
            True
    return bags

# ------------------------------------------------------------------------------------------------
print("- D7.1 -----------------------------------------------------------------------------------")
# ------------------------------------------------------------------------------------------------

def wich_contains_bags( search_bag, containers , result ):

    for container in containers:
        bag, contains = container
        dict_contains = dict(contains)
        try:
            dict_contains[ search_bag ]
            print(" FOUND " + search_bag + " IN " + bag + " : " + str(container))
            wich_contains_bags(bag, containers, result)
            result.append( bag )
        except KeyError:
            True
    return result

res=[]
wich_contains_bags ( "shiny gold", read_rules( inputFile ), res )

print( len( list(set(res)) ) )

# ------------------------------------------------------------------------------------------------
print("- D7.2 -----------------------------------------------------------------------------------")
# ------------------------------------------------------------------------------------------------

def how_many_bags_of( search_bag, containers ):

    print( " -> " + search_bag)
    nb_bags         = 1
    dict_containers = dict( containers )
    try:
        bags            = dict_containers[search_bag]
        for bag, number in bags:
            nb_bags = nb_bags + int(number) *  how_many_bags_of( bag, containers )
            print( "      -" + bag + " - " + number + " - " + str(nb_bags))
    except KeyError:
        True

    return nb_bags

print( how_many_bags_of( "shiny gold", read_rules( inputFile )) -1 )


print('END')
inFile.close()
