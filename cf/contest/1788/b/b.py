import math 
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations

def parse_input(data):
    return int(data)

# ---------------------------------------------------------

def dsum(x):
    res = 0
    while x:
        res += x % 10
        x //= 10
    return res

def solve(n):
    if n % 2 == 0:
        return n//2, n//2
    else:
        if n % 10 != 9:
            return (n+1)//2, (n-1)//2
        else:
            n /= 10
            x, y = solve(n)
            if dsum(x) > dsum(y):
                return (x*10 + 4), (y*10 + 5)
            else:
                return (x*10+5), (y*10+4)

# ---------------------------------------------------------

input_type = 'ntest_size_data'
if input_type == 'ntest_size_data':
    n_tests = int(input())
    for _ in range(n_tests):
        data = input()  
        parsed_data = parse_input(data)
        res = solve(parsed_data)
        print(" ".join([str(int(x)) for x in res]))

