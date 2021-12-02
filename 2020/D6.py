import string
#1139043-20201203-f3167993

inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D6_input.txt"
inFile = open(inputFile, 'r')

print("- D6 -----------------------------------------------------------------------------------")
print(inputFile)

# ------------------------------------------------------------------------------------------------
# INPUT:
# OUTPUT:
# ------------------------------------------------------------------------------------------------
def read_raw_answers( file ):
    all_answers   = []
    group_answer = []
    inFile        = open(inputFile, 'r')

    for line in inFile:
        if not (line in ['\n', '\r\n']):
            group_answer.append( line.rstrip("\n") )
        else:
            all_answers.append(group_answer)
            group_answer = []
            group_answer.clear()
    all_answers.append(group_answer)
    print(all_answers)
    inFile.close()
    return all_answers

# ------------------------------------------------------------------------------------------------
# INPUT:
# OUTPUT:
# ------------------------------------------------------------------------------------------------
def count_all_yes_answers( group_answers ):
    questions     = string.ascii_lowercase[:26]
    count_all_yes = 0
    count_people  = len(group_answers)

    for letter in questions:
        count_yes_answer=0
        for answer in group_answers:
            if  answer.find( letter ) != -1 :
                count_yes_answer = count_yes_answer + 1

        if count_yes_answer == count_people: count_all_yes = count_all_yes+1
    return count_all_yes


# ------------------------------------------------------------------------------------------------
print("- D6.1 -----------------------------------------------------------------------------------")
# ------------------------------------------------------------------------------------------------

count_1=0
for group_answers in read_raw_answers( inputFile ):
    group_letters=[]
    for answer in group_answers:
        for letter in answer:
            group_letters.append( letter)
    distinct_letters = list( set( group_letters ) )
    count_1 = count_1 + len(distinct_letters)

print( count_1)

# ------------------------------------------------------------------------------------------------
print("- D6.2 -----------------------------------------------------------------------------------")
# ------------------------------------------------------------------------------------------------

count_2=0
for group_answers in read_raw_answers( inputFile ):
    count_2 = count_2 + count_all_yes_answers(group_answers)

print( count_2)

print('END')
inFile.close()




