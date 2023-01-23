
def solve(numbers):
    res = 0
    for left, right in zip(numbers, numbers[1:]):
        same_parity = left % 2 == right % 2 == 0 or left % 2 == right % 2 == 1
        if same_parity:
            res += 1
    return res


n = int(input())
for _ in range(n):
    k = int(input())
    lst = list(map(int, input().split()))
    res = solve(lst)
    print(res)