class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = count = 1
        for curr, nxt in pairwise(nums):
            count = count+1 if curr < nxt else 1
            res = max(res, count)
        
        return res
