import math 
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations

def parse_input(data):
    return list(map(int, data.split()))

# ---------------------------------------------------------

def solve(inputs):
    res = 0
    m = dict(Counter(inputs))
    start = next(iter(m))
    while m:
        if start not in m:
            start = next(iter(m))

        current = start
        while current in m:
            m[current] -= 1
            if not m[current]:
                m.pop(current)
            current += 1

        current = start-1
        while current in m:
            m[current] -= 1
            if not m[current]:
                m.pop(current)
            current -= 1

        res += 1
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


'''
1
8
4 2 2 4 3 3 4 3 5

res = 3
'''