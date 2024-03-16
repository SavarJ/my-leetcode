class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res, runningSum, psum = 0, 0, {0:0}
        for i, num in enumerate(nums):
            runningSum += (-1 if num == 0 else 1)
            if runningSum in psum:
                res = max(res, i+1-psum[runningSum])
            else:
                psum[runningSum] = i+1
        
        return res
