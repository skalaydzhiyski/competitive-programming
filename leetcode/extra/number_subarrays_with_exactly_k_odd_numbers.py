# Count number of subarrays with EXACTLY `k` odd numbers
def solve(nums, k):
	from collections import defaultdict
	counts = defaultdict(int)
	current = res = 0
	for x in nums:
		current += x % 2
		res += counts[current - k]
		counts[current] += 1
	return res

nums = [1,1,2,1,1]
k = 3
print(solve(nums, k)) 