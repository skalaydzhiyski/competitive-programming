class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        N = len(nums) // 2
        left, right = 0, N
        res = []
        for i in range(N):
            res.append(nums[left+i])
            res.append(nums[right+i])
        return res