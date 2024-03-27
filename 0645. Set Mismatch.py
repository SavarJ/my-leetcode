class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup=0
        for num in nums:
            if nums[abs(num)-1] < 0: dup=abs(num)
            else: nums[abs(num)-1]*=-1
        return [dup, next(num for num in range(1,len(nums)+1) if nums[num-1] > 0)]
