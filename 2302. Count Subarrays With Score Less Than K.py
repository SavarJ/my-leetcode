class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = l = summ = size = 0
        for r in range(len(nums)):
            summ, size = summ+nums[r], size+1
            while l <= r and summ*size >= k: summ, size, l = summ-nums[l], size-1, l+1
            res += r-l+1
        return res
