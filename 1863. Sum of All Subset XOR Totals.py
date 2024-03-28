class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def bt(i, x): return x if i >= len(nums) else bt(i+1, x ^ nums[i]) + bt(i+1, x)
        return bt(0, 0)
