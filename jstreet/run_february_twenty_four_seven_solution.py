#!/Users/darchitect/miniconda3/bin/python3
import numpy as np
from sudoku import Sudoku
from z3.z3 import *

board = np.array([
	[None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, 1, None, None, None, None, None, 6, 5, None],
	[None, None, None, None, None, 3, None, None, None, None, 6, None],
	[None, 4, None, None, None, None, None, None, 7, None, None, None],
	[None, None, None, None, 2, None, None, None, None, None, None, 7],
	[None, None, 6, None, None, None, None, None, 3, 7, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, 7, None, 5, None, None, None, None, None, None],
	[None, 5, None, None, None, 7, None, None, None, None, None, None],
	[None, 6, 7, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, 6, None, None, None, None, None, None, None]
])
blue_nums_col = { # col -> (top, bottom)
	0: (6, 6),
	1: (36, None),
	2: (30, None),
	3: (34, 4),
	4: (27, None),
	5: (3, None),
	6: (40, None),
	7: (27, None),
	8: (None, None),
	9: (None, None),
	10: (7, None),
	11: (None, None)
}
blue_num_rows = { # row -> (left, right)
	0: (5, 4),
	1: (7, None),
	2: (7, None),
	3: (33, 1),
	4: (29, None),
	5: (2, None),
	6: (40, None),
	7: (28, None),
	8: (None, None),
	9: (None, None),
	10: (36, None),
	11: (None, 7)
}

def check_7x7_sequence_rule():
	global board
	return True

def check_4num_sum20_rule():
	global board
	return True

def check_2x2_at_least_one_empty_rule():
	global board
	return True

def check_numbers_form_connected_sequence_rule():
	global board
	return True

def is_valid():
	global board
	return (
		check_7x7_sequence_rule()
		and check_4num_sum20_rule()
		and check_2x2_at_least_one_empty_rule()
		and check_numbers_form_connected_sequence_rule()
	)

def solve():
	pass

if __name__ == '__main__':
	pass
