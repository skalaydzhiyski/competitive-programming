import math

def solve(n):
    k = 10**9 + 7
    p = []
    current = 1
    while current <= n:
        p.append(current)
        current += 1
    b = sum(p[:-1])*2
    res = (math.factorial(n) * b) % k
    return res
    number = int(number)

ntest = int(input())
for _ in range(ntest):
    n = int(input())
    res = solve(n)
    print(res)