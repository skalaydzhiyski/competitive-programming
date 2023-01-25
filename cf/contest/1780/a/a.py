import math 
from collections import defaultdict, deque
from itertools import permutations, combinations


def parse_input(data):
    return list(map(int, data.split()))


def solve(inputs):
    n = len(inputs)
    m = {}
    evens = [i for i,n in enumerate(inputs) if n % 2 == 0]
    odds = [i for i, n in enumerate(inputs) if n % 2 != 0]
    if len(odds) >= 3:
        return ("YES", odds[:3])
    if len(evens) >= 2:
        if len(odds):
            return ("YES", evens[:2] + odds[:1])
    return "NO"


input_type = 'ntest_size_data'
if input_type == 'ntest_size_data':
    n_tests = int(input())
    for _ in range(n_tests):
        n = int(input())
        data = input()  
        parsed_data = parse_input(data)
        res = solve(parsed_data)
        if type(res) == str:
            print(res)
        else:
            print(res[0])
            print(' '.join([str(x+1) for x in res[1]]))
