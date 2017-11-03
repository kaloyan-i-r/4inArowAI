from log import *
from evaluate_position import cost
import numpy
from numpy import array
from board import *



examples = [
                         #0|0  1  2  3  4  5  6
[ [0,1],          array([[  0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,]])],
[ [1],            array([[  0, 1, 0, 0, 0, 0, 0, 
                            0, 0, 0, 0, 0, 0, 0, 
                            0, 0, 0, 0, 0, 0, 0, 
                            0, 0, 0, 0, 0, 0, 0, 
                            0, 0, 0, 0, 0, 0, 0, 
                            0, 0, 0, 0, 0, 0, 0,]])],
[ [1],            array([[  0, 1, 0, 0, 0, 0, 0, 
                            0, 1, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,]])],
[ 
  [0,1,2,3,4,5],  array([[ -1, 1,-1, 0, 0, 0, 0,
                            1, 1,-1, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,]])],
]

emtpy_board = numpy.empty( (1,4,))
emtpy_board[:] = 0
info(f'emtpy_board : {emtpy_board}' )

for example in examples:
    for move in example[0]:
        board = example[1]
        printBoard(board)
        print(f'move:{move} cost:{cost(board,move)}')
    pass

