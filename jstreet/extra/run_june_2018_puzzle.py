#!/Users/darchitect/miniconda3/bin/python3
from time import time
import numpy as np

grid = np.array([
	[0,4,0,0,0,0,0],
	[0,0,6,3,0,0,6],
	[0,0,0,0,0,5,5],
	[0,0,0,4,0,0,0],
	[4,7,0,0,0,0,0],
	[2,0,0,7,4,0,0],
	[0,0,0,0,0,1,0]
])

# NOTE: Think about the search space and how best to encode it.
# 		Keep in mind that every row or col at any given point in time will have
# 		only SOME numbers that can go into it so we need to generate this list of numbers
# 		everytime we attempt to put a number.
