class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        leftCum, rightCum = 1, 1
        for i in range(len(nums)):
            res[i] *= leftCum
            res[~i] *= rightCum
            leftCum *= nums[i]
            rightCum *= nums[]
        return res
