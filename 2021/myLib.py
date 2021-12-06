from typing import List
from collections import deque
import matplotlib.pyplot as plt

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

def input_as_list_of_ints(filename:str) -> List[int]:
    """Return a list where each line in the input file is converted into a list onf integers """
    lines = input_as_lines(filename)
    return [ [ int(value) for value in line.rstrip('\n').split(',')] for line in lines]

def input_as_separatedBits(filename:str) -> List[ List[int]]:
    """Return a list where each line in the input file is an element of the list, converted into a list of bits as integer"""
    lines = input_as_lines(filename)
    line_as_listofBits = lambda l: [int(char) for char in list(l.rstrip('\n'))]
    return list(map(line_as_listofBits, lines))

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

def init_matlibgraph(day:str):
    figure, graph = plt.subplots(1, 2)
    graph[0].title.set_text(day + " puzzle 1")
    graph[0].axis('off')
    graph[1].title.set_text(day + " puzzle 2")
    graph[1].axis('off')
    return(figure, graph)

def save_matlibgraph(figure, day:str):
    figure.tight_layout()
    figure.savefig(day + '.png',dpi=300)

