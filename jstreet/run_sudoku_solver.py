#!/Users/darchitect/miniconda3/bin/python3
import numpy as np
from sudoku import Sudoku
from z3.z3 import *

# TODO: continue here when you're coming back to the JS puzzle.
#       start with a new notebook and first solution attempt with a SAT solver.
# NOTE -> handle the overlap by just having 4 sets of interleaved constraints for
#         for the 4 overlapping squares and just 1 solver.
# good luck !

def solve(board):
  pass

board = np.array(Sudoku(3).difficulty(.5).board)
board[board == None] = 0

print(f'Board:\n{board}')
res = solve()
