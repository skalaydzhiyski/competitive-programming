import math 
from collections import defaultdict, deque
from itertools import permutations, combinations

def parse_input(data):
    return list(map(int, data.split()))

# ---------------------------------------------------------

def solve(inputs):
    n, s, r = inputs
    max_ = s - r
    res = [max_]
    rem = [1 for _ in range(n-1)]
    idx = 0
    current = sum(rem)
    while current < r:
        if rem[idx] == max_:
            idx += 1
        rem[idx] += 1
        current = sum(rem)
    res += rem
    return ' '.join(map(str, res))

# ---------------------------------------------------------

input_type = 'ntest_size_data'
if input_type == 'ntest_size_data':
    n_tests = int(input())
    for _ in range(n_tests):
        data = input()  
        parsed_data = parse_input(data)
        res = solve(parsed_data)
        print(res)

