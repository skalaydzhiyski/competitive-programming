import math 
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations

def parse_input(data):
    return list(map(int, data.split()))

# ---------------------------------------------------------

def solve(inputs):
    total = 1
    for x in inputs:
        total *= x
    current = 1
    for idx, x in enumerate(inputs):
        current *= x
        total /= x
        if current == total:
            return idx + 1
        if current > total:
            return -1
    return -1

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

