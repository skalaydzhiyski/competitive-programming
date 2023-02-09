import math 
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations

def parse_input(data):
    return data

# ---------------------------------------------------------

def solve(input_string):
    seen = set()
    rep = {}
    count = 0
    res = 0
    for idx, c in enumerate(input_string):
        if c in seen:
            current = count + len(set(input_string[idx:]))
            if current > res:
                res = current
            count = 0
        count += 1
        seen.add(c)
    return res




    # distinct = set(input_string)
    # n = len(input_string)
    # count_seen = 0
    # seen = set()
    # res = 1
    # for idx in range(n):
    #     if input_string[idx] in distinct:
    #         distinct.remove(input_string[idx])

    #     if input_string[idx] not in seen:
    #         count_seen += 1
    #         seen.add(input_string[idx])

    #     right = input_string[idx+1:]
    #     current = count_seen + len(set(right))
    #     if current > res:
    #         res = current

    #     if not len(distinct):
    #         break
    # return res
    

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

