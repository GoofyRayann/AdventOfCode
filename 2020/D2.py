# --- Day 2: Password Philosophy ---
# Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.
# The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.
# Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.
# To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.
# For example, suppose you have the following list:
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
# In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.
# How many passwords are valid according to their policies?
# Your puzzle answer was 445.
# --- Part Two ---
# While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.
# The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.
# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
# Given the same example list from above:
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?
# Your puzzle answer was 491.
# Both parts of this puzzle are complete! They provide two gold stars: **
# At this point, you should return to your Advent calendar and try another puzzle.
# If you still want to see it, you can get your puzzle input.
# You can also [Share] this puzzle.

inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D2_input.txt"
inFile = open(inputFile, 'r')

print(inputFile)

print("- D2.1 -----------------------------------------------------------------------------------")
pwd_ok = 0
nblines = 0
for line in inFile:
    nblines         = nblines + 1
    values          = line.split()
    value_min       = int(values[0].split("-")[0])
    value_max       = int(values[0].split("-")[1])
    value_letter    = values[1].split(":")[0]
    value_password  = values[2]

    nb_letter_in_pwd = value_password.count( value_letter)

    if ( nb_letter_in_pwd >= value_min) and (nb_letter_in_pwd <= value_max ):
        print(str(value_min) + "-" + str(value_max) + "-" + value_letter + "-" + value_password)
        print("   => OK")
        pwd_ok = pwd_ok + 1

print( "nb lines : " + str(nblines))
print( "pwd ok   : " + str(pwd_ok))

print("- D2.2 -----------------------------------------------------------------------------------")

inFile.close()
inFile = open(inputFile, 'r')

pwd_ok = 0
nblines = 0
for line in inFile:
    nblines         = nblines + 1
    values          = line.split()
    value_pos1      = int(values[0].split("-")[0])
    value_pos2      = int(values[0].split("-")[1])
    value_letter    = values[1].split(":")[0]
    value_password  = values[2]

    print(str(value_pos1) + "-" + str(value_pos2) + "-" + value_letter + "-" + value_password)

    try:
        letter1 = value_password[value_pos1 - 1 ]
        letter2 = value_password[value_pos2 - 1]

        if ( ( letter1 ==  value_letter ) and ( letter2 !=  value_letter )) \
                or ( ( letter1 !=  value_letter ) and ( letter2 ==  value_letter )) :
            print(str(value_pos1) + "-" + str(value_pos2) + "-" + value_letter + "-" + value_password)
            print("   => OK")
            pwd_ok = pwd_ok + 1
    except IndexError:
        True


print( "nb lines : " + str(nblines))
print( "pwd ok   : " + str(pwd_ok))
print("------------------------------------------------------------------------------------------")

print('END')
inFile.close()
