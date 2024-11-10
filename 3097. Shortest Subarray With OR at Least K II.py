class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        res = inf
        bits = [0]*32

        def update_bits(num, diff):
            res = 0
            for i in range(32):
                if num & (1<<i):
                    bits[i] += diff
                if bits[i]:
                    res += (1<<i)

            return res

        for r in range(len(nums)):
            curr = update_bits(nums[r], 1)    
            while curr >= k:
                res = min(res, r-l+1)
                if res == 1: return res
                curr = update_bits(nums[l], -1)
                l += 1

        return -1 if res == inf else res
