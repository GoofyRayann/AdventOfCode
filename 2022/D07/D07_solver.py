import re
import myLib

DAY           = "D07"
inputTestFile = DAY + "_puzzle_test.txt"
inputFile     = DAY + "_puzzle.txt"

# --------------------------------------------------------------------------------------------------
class Device:
    def __init__(self, deviceSpace, upgradeNeededSpace, console):
        self.deviceSpace = deviceSpace
        self.upgradeNeededSpace = upgradeNeededSpace
        self.directories = Directories( console)

    def getDirSizeToFreeForUpgrade( self):
        unusedSpace = self.deviceSpace - self.directories.dirFullSizes["root"]
        spaceToFree = self.upgradeNeededSpace - unusedSpace
        selectedDir = "root"
        for dir in self.directories.dirFullSizes:
            if self.directories.dirFullSizes[dir] >= spaceToFree and self.directories.dirFullSizes[dir] < self.directories.dirFullSizes[selectedDir]:
                selectedDir = dir
        return self.directories.dirFullSizes[selectedDir]

# --------------------------------------------------------------------------------------------------
class Directories:
    def __init__(self, console):
        self.dirSizes = self.getDirSizes(console)
        self.dirFullSizes = self.getDirFullSizes(self.dirSizes)

    def getDirSizes(self, console):
        currentDir = []
        currentDirStr = ''
        dirSize = {}
        for line in console:
            match line.split(' '):
                case ['$', 'cd', *dirs]:
                    match dirs:
                        case ['/']  : currentDir = ['root']
                        case ['..'] : currentDir.pop()
                        case _      : currentDir.append(dirs[0])
                case ['$', 'ls']:
                    currentDirStr = '/'.join(currentDir)
                    dirSize[currentDirStr] = 0
                case _:
                    content = line.split(' ')
                    if content[0] != 'dir': dirSize[currentDirStr] += int(content[0])
        return dirSize

    def getDirFullSizes( self, dirSizes ):
        dirTotalSize = {}
        for dir in dirSizes:
            dirTotalSize[dir] = sum([dirSizes[subdir] if subdir.startswith(dir) else 0 for subdir in dirSizes])
        return dirTotalSize

    def getSumSizeOfDirLessThan(self,  limitSize: int):
        return  sum( [self.dirFullSizes[dir] if self.dirFullSizes[dir] < limitSize else 0 for dir in self.dirFullSizes ])

# --------------------------------------------------------------------------------------------------
def Puzzle_1(inputFile):
    device = Device( deviceSpace= 70000000, upgradeNeededSpace = 30000000, console=myLib.input_as_lines(inputFile))
    return  device.directories.getSumSizeOfDirLessThan( limitSize=100000)

def Puzzle_2(inputFile):
    device = Device( deviceSpace= 70000000, upgradeNeededSpace = 30000000, console=myLib.input_as_lines(inputFile))
    return device.getDirSizeToFreeForUpgrade()

# --------------------------------------------------------------------------------------------------
myLib.display_header(DAY, inputFile)

myLib.display_result("1", str(Puzzle_1(inputFile)))
myLib.display_result("2", str(Puzzle_2(inputFile)))

myLib.display_footer()
