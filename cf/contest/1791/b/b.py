import math 
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations

def parse_input(data):
    return data

# ---------------------------------------------------------

def solve(inp):
    directions = {
        'U': (0,1),
        'D': (0,-1),
        'L': (-1,0),
        'R': (1,0)
    }
    posx, posy = 0,0
    for dir_ in inp:
        dx, dy = directions[dir_]
        posx += dx
        posy += dy
        if (posx, posy) == (1,1):
            return "YES"
    return "NO"

# ---------------------------------------------------------

input_type = 'ntest_size_data'
if input_type == 'ntest_size_data':
    n_tests = int(input())
    for _ in range(n_tests):
        n = int(input())
        data = input()  
        parsed_data = parse_input(data)
        res = solve(parsed_data)
        print(res)

