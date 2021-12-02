from typing import List
from collections import deque

def input_as_string(filename:str) -> str:
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")

def input_as_lines(filename:str) -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")

def input_as_ints(filename:str) -> List[int]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)
    line_as_int = lambda l: int(l.rstrip('\n'))
    return list(map(line_as_int, lines))

def rotate_list( vList:List, vValue:int) -> List:
    """Return a list shifted by N positions"""
    items = deque(vList)
    items.rotate(vValue)
    return list(items)

def display_header(day:str, filename:str):
    print("====================================================================================================")
    print("- " + day + " -> " + filename)
    print("------------------------------------------------------------------------------------------")
    return

def display_result(id:str, res:str):
    print( "       PUZZLE "+id+": " + res + " " )
    return

def display_footer():
    print("------------------------------------------------------------------------------------------")
    return



