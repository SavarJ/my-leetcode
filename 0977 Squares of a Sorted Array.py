class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        l, r = 0, len(nums)-1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[r-l] = nums[l]**2
                l += 1
            else:
                res[r-l] = nums[r]**2
                r -= 1
        return res
