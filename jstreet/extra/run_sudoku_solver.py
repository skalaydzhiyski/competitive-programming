import numpy as np
from sudoku import Sudoku

def can_put_number_at(x, y, n):
    global board
    row = board[x]
    col = board[:, y]

def solve():
    global board, rows, cols
    for x in range(rows):
        for y in range(cols):
            for n in range(1,10):
                if can_put_number_at(x, y, n):
                    board[x][y] = n
                    solve()
                    board[x][y] = 0
            return
    return board

board = np.array(Sudoku(3).difficulty(.5).board)
board[board == None] = 0
rows, cols = board.shape
print(f'Board:\n{board}')
res = solve()
print(f'Solution:\n{res}')
