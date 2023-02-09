import math 
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations

def parse_input(data):
    return data

# ---------------------------------------------------------

def solve(input_string):
    n = len(input_string)
    left, right = 0, n - 1
    res = n
    while left <= right:
        if input_string[left] != input_string[right]:
            res -= 2
        else:
            break
        left += 1
        right -= 1
    return res

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

