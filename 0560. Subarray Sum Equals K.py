class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, runningSum, pre = 0, 0, defaultdict(int, {0:1})
        for i in range(len(nums)):
            runningSum += nums[i]
            res += pre[runningSum-k]
            pre[runningSum] += 1
        return res
