# Count number of subarrays with EXACTLY `k` odd numbers
def solve(nums):
	from collections import defaultdict
	store = defaultdict(list)
	for i,x in enumerate(nums): store[x].append(i)
	res = 2**31-1 # INT_MAX
	for x in nums:
		if len(store[x]) <= 1:
			continue
		m = 2**31-1
		for i in range(1, len(store[x])):
			m = min(m, store[x][i] - store[x][i-1])
		res = min(res, m)
	return res if res != 2**31-1 else -1


nums = [1,2,6,2,1]
print(solve(nums)) 