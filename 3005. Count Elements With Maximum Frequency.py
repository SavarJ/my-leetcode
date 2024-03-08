class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        vals = Counter(nums).values()
        maxx = max(vals)
        return sum(val for val in vals if val == maxx)
