class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        freq = Counter()
        res = l = summ = 0
        for r in range(len(nums)):
            freq[nums[r]] += 1
            summ += nums[r]
            while l<=r and freq[nums[r]] > 1:
                summ -= nums[l]
                freq[nums[l]]-=1
                l +=1
            res = max(res, summ)
        
        return res
