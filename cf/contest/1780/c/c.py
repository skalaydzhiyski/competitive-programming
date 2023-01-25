import math 
from collectinos import defaultdict, deque
from itertools import permutations, combinations


def parse_input(data):
  return list(map(int, data.split()))


def solve(inputs):
    # TODO: solution here.
    pass


input_type = 'ntest_size_data'
if input_type == 'ntest_size_data':
    n_tests = int(input())
    for _ in range(n_tests):
        n = int(input())
        data = input()  
        parsed_data = parse(data)
        res = solve(data)
        print(res)
