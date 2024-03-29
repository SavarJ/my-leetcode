class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = count = l = 0
        m = max(nums)
        for r in range(len(nums)):
            count += nums[r]==m
            while l <= r and count == k:
                res += len(nums)-r
                count -= nums[l]==m
                l += 1
        return res
