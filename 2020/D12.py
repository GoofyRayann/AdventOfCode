import string
import copy

inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D12_input.txt"
#inputFile = "D:\Z_DEVELOPPEMENT\Divers\\adventofcode.com\D1\D12_sample.txt"

print("- D12 ---------------------------------------------------------------------------------")
print(inputFile)

directions = [ ('N',0,-1),('E',1,0),('S',0,1),('W',-1,0)]
boussole   = { "N":0, "E":1, "S":2, "W":3}
turn       = { 90:1, 180:2, 270:3}

def read_instrs( file ):
    with open(file) as f:
        instrs = [ (line[0] , int(line[1:].rstrip("\n"))) for line in f.readlines()]
    return instrs

class Bateau_1:
    def __init__(self, direction, x,y):
        self.direction = direction #0,1,2,3
        self.x         = x
        self.y         = y
        print( "INIT", self.direction, directions[self.direction][0], self.x, self.y)

    def Move(self, instr,value):
        if( instr == "F"):
            self.x += directions[ self.direction ][1] * value
            self.y += directions[ self.direction ][2] * value
        if (instr == "L"):
            self.direction = ( self.direction -  turn[ value] )  % 4
        if (instr == "R"):
            self.direction = (self.direction + turn[value]) % 4
        if( instr in ["N","E","S","W"] ):
            self.x += directions[ boussole[instr] ][1] * value
            self.y += directions[ boussole[instr] ][2] * value
        print( instr, value, "=>", self.direction, directions[self.direction][0], self.x, self.y)

class Bateau_2:
    def __init__(self,  x,y, wpx, wpy):
        self.x         = x
        self.y         = y
        self.wpx       = wpx
        self.wpy       = wpy
        print( "INIT", self.x, self.y, " - WP:", self.wpx, self.wpy)

    def Move(self, instr,value):
        if  instr == "F":
            self.x += self.wpx * value
            self.y += self.wpy * value
        if instr in ["L","R"]:
            if value == 180:
                self.wpx, self.wpy = -self.wpx, -self.wpy
            if (value == 90 and instr == "R") or (value == 270 and instr == "L") :
                self.wpx , self.wpy = -self.wpy , self.wpx
            if (value == 270 and instr == "R") or (value == 90 and instr == "L") :
                self.wpx, self.wpy = self.wpy, - self.wpx
        if instr in ["N","E","S","W"] :
            self.wpx += directions[ boussole[instr] ][1] * value
            self.wpy += directions[ boussole[instr] ][2] * value
        print( instr, value, "=>",  self.x, self.y, " - WP:", self.wpx, self.wpy)


def Puzzle_1( initdirection, initx,inity, moves):
    bateau=Bateau_1( boussole[initdirection], initx,inity )
    for (instr, value) in  moves:
        bateau.Move(instr, value)
    return abs(bateau.x) + abs(bateau.y)


def Puzzle_2(initx, inity,  initwpx, initwpy,moves):
    bateau = Bateau_2( initx, inity,  initwpx, initwpy)
    for (instr, value) in moves:
        bateau.Move(instr, value)
    return abs(bateau.x) + abs(bateau.y)


print("------------------------------------------------------------------------------------------")

moves    = read_instrs(inputFile)
print(moves)

value =  Puzzle_1( "E",0,0, moves )

print( "       PUZZLE_1 : " + str(value) + " " )
value = Puzzle_2( 0,0,10,-1 , moves )

print( "       PUZZLE_2 : " + str(value) + " " )

print("------------------------------------------------------------------------------------------")
print('END')

