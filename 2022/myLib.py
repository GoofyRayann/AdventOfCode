from typing import List
from collections import deque
import numpy as np

import matplotlib.pyplot as plt

#from generativepy.nparray import  make_npcolormap, apply_npcolormap
#from generativepy.color import Color

#- ------------------------------------------------------------------------------------------------------------------

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
    """Return a list where each line in the input file is converted into a list of integers separated by ,"""
    lines = input_as_lines(filename)
    return [ [ int(value) for value in line.rstrip('\n').split(',')] for line in lines]

def input_as_list_of_horizontal_list_of_ints(filename:str) -> List[ List[int]]:
    """Return a list where each line in the input file is a list of integers"""
    lines = input_as_lines(filename)
    line_as_listofInts = lambda l: [int(char) for char in list(l.rstrip('\n'))]
    return list(map(line_as_listofInts, lines))

def input_as_list_of_vertical_list_of_ints(filename: str) -> List[List[int]]:
    """Return a list where each  group of lines separated by single carriage in the input file is a list of integers"""
    lines = input_as_string(filename)
    verticalListofInts = lambda l: [ int( value) for value in l.split("\n")]
    return  list(map( verticalListofInts, list(lines.split("\n\n")) ))

def rotate_list( vList:List, vValue:int) -> List:
    """Return a list shifted by N positions"""
    items = deque(vList)
    items.rotate(vValue)
    return list(items)

#- ------------------------------------------------------------------------------------------------------------------

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

#- ------------------------------------------------------------------------------------------------------------------

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

#- ------------------------------------------------------------------------------------------------------------------

# def generativePy_colorizeImage( image):
#     image        = np.reshape(image, (image.shape[0], image.shape[1]))
#     power_counts = np.power(image, 1.2)
#     maxcount     = np.max(power_counts)
#
#     normalised_counts = (power_counts * 1023 / max(maxcount, 1)).astype(np.uint32)
#
#     colormap = make_npcolormap(1024, [Color('black'), Color('red'), Color('orange'), Color('yellow'), Color('white')])
#     outarray = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
#     apply_npcolormap(outarray, normalised_counts, colormap)
#
#     return outarray