import math 
from collections import defaultdict, deque
from itertools import permutations, combinations

def parse_input(data):
    return data

# ---------------------------------------------------------

def solve(inputs):
    pi = '''
    31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
    '''.strip()
    res = 0
    for i in range(len(inputs)):
        if pi[i] != inputs[i]:
            break
        res += 1
    return res

# ---------------------------------------------------------

input_type = 'ntest_size_data'
if input_type == 'ntest_size_data':
    n_tests = int(input())
    for _ in range(n_tests):
        data = input()  
        parsed_data = parse_input(data)
        res = solve(parsed_data)
        print(res)

