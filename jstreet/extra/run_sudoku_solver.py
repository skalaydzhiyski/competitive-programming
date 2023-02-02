import numpy as np
from sudoku import Sudoku

def solve():
  pass

board = np.matrix(Sudoku(3).difficulty(.5).board)
board[board == None] = 0
print(board)
