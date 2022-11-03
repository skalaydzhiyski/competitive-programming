# Count number of subarrays with sum EXACTLY equal to `k`
def solve(nums, k):
	prefix = {0}
	current = res = 0
	for x in nums:
		current += x
		if current - k in prefix: res += 1
		prefix.add(current)
	return res

nums = [1,2,1,2,1]
k = 3
print(solve(nums, k)) 