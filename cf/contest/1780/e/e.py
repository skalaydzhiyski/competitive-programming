import math 
from collections import defaultdict, deque
from itertools import permutations, combinations
from pprint import pprint

def parse_input(data):
    return list(map(int, data.split()))

# ---------------------------------------------------------

def solve(inputs):
    left, right = inputs
    if left == right:
        return 0
    res = set([1])
    q = deque([1, left])
    while q:
        print(q, res)
        current = q.popleft()
        print('current', current)
        print(q)
        print()
        prev = current
        while left <= current * 2 <= right:
            res.add(current)
            current *= 2
            q.append(current)
        prev += 1
        if prev < right:
            q.append(prev)
    return res

def solve_old(inputs):
    left, right = inputs
    if left == right:
        return 0
    pairs = list(combinations([x for x in range(left, right+1)], 2))
    m = {p: math.gcd(*p) for p in pairs}
    #pprint(m)
    return set(m.values())

# ---------------------------------------------------------

input_type = 'ntest_size_data'
if input_type == 'ntest_size_data':
    n_tests = int(input())
    for _ in range(n_tests):
        #n = int(input())
        data = input()  
        parsed_data = parse_input(data)
        res = solve(parsed_data)
        actual = solve_old(parsed_data)
        print('-'*50)
        print('actual', res, len(res))
        print('expected', actual, len(actual))
