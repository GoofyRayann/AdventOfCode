import re
#1139043-20201203-f3167993

inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D4_input.txt"
#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D4_sample.txt"
inFile = open(inputFile, 'r')

print(inputFile)

print("- D4.1 -----------------------------------------------------------------------------------")

rules = [ ("byr", ("mandatory" , "^(2000|2001|2002|19[2-9][0-9])$") ), #1920-2002
          ("iyr", ("mandatory" , "^(201[0-9]|2020)$") ), #2010-2020
          ("eyr", ("mandatory" , "^(202[0-9]|2030)$") ), #2020-2030
          ("hgt", ("mandatory" , "^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$") ), #150-193cm ou 59-76in
          ("hcl", ("mandatory" , "^#[a-f0-9]{6}$") ),
          ("ecl", ("mandatory" , "^(amb|blu|brn|gry|grn|hzl|oth)$") ),
          ("pid", ("mandatory" , "^[0-9]{9}$") ),
          ("cid", ("optional"  , "^\*?") )]

# ------------------------------------------------------------------------------------------------
# INPUT:
# eyr:2021 hcl:#6b5442 byr:1994 hgt:170cm ecl:amb pid:348959147 iyr:2013
# byr:1957 ecl:hzl hgt:156cm pid:890752588 eyr:2025 hcl:e7c520 cid:199 iyr:2017
# OUTPUT: ["eyr:2021...","..."]
# ------------------------------------------------------------------------------------------------
def read_raw_passports( file ):
    passports = []
    passport  = " "
    inFile    = open(inputFile, 'r')
    for line in inFile:
        if not (line in ['\n', '\r\n']):
            passport = passport + " " + line.rstrip("\n")
        else:
            passports.append(passport)
            passport = " "
    passports.append(passport)
    print(passports)
    inFile.close()
    return passports

# ------------------------------------------------------------------------------------------------
# INPUT:
# "byr:1957 ecl:hzl hgt:156cm pid:890752588 eyr:2025 hcl:e7c520 cid:199 iyr:2017"
# OUTPUT: [(byr,1957),(ecl,hzl),(hgt,156cm)...]
# ------------------------------------------------------------------------------------------------
def parse_raw_passport( raw_passport ):
    passport=[]
    for tuple in raw_passport.split(" "):
        if ( tuple != '' ):
            values = tuple.split(":")
            key    = values[0]
            value  = values[1]
            passport.append( (key, value) )
    return passport


# ------------------------------------------------------------------------------------------------
# INPUT:
# "byr:1957 ecl:hzl hgt:156cm pid:890752588 eyr:2025 hcl:e7c520 cid:199 iyr:2017"
#  [ ("byr","mandatory"), ("iyr","mandatory"),("eyr","mandatory"), ("hgt","mandatory"), ("cid","optional") ]
# OUTPUT: true/false
# ------------------------------------------------------------------------------------------------

def check_passport( passport, rules):
    passport_values = dict( passport )
    passportIsValid=True
    for rule in rules:
        key   = rule[0]
        attribut, pattern = ( rule[1][0], rule[1][1])
        try:
            checkAttribute = passport_values[key]

            if key == "pid" and bool(re.match(pattern, passport_values[key])):
                print(key + "-" + passport_values[key] + "-" + pattern)

            if not bool(re.match(pattern, passport_values[key])):
                passportIsValid=False

        except KeyError:
            if attribut != "optional":
                passportIsValid = False

    return  passportIsValid

# ------------------------------------------------------------------------------------------------
# CHECK PASSPORT VALIDATION
# ------------------------------------------------------------------------------------------------

nbValidPassports=0
for raw_passport in read_raw_passports( inputFile ):
    if check_passport( parse_raw_passport( raw_passport ) , rules ):
        nbValidPassports = nbValidPassports + 1

print( nbValidPassports )

print('END')
inFile.close()




