class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        return [vals:=list(Counter(nums).values()), maxx:=max(vals), vals.count(maxx)*maxx][2]
