import math 
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations

def parse_input(data):
    return data

# ---------------------------------------------------------

def solve(inputs):
    return "YES" if inputs in 'codeforces' else "NO"

# ---------------------------------------------------------

input_type = 'ntest_size_data'
if input_type == 'ntest_size_data':
    n_tests = int(input())
    for _ in range(n_tests):
        data = input()  
        parsed_data = parse_input(data)
        res = solve(parsed_data)
        print(res)

