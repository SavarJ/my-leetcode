class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = Counter()
        summ = 0
        res = 0
        for i, num in enumerate(nums):
            window[num] += 1
            summ += num
            if i+1 < k: continue

            if len(window) == k:
                res = max(res, summ)
            
            leftVal = nums[i-k+1]
            summ -= leftVal
            window[leftVal] -= 1
            if window[leftVal] == 0: del window[leftVal]
        
        return res
