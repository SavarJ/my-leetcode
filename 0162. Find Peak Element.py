class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l<=r:
            m = (l+r)//2

            left, right = nums[m-1] if m>0 else -inf, nums[m+1] if m<n-1 else -inf
            curr = nums[m]

            if left < curr > right: return m
            elif left < curr < right:
                l = m+1
            else:
                r = m-1
