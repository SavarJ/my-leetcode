class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def gpd(num):
            for i in range(2, ceil(sqrt(num))+1):
                if num % i == 0:
                    return num // i
                
            return -1

        res = 0
        for i in range(n - 2, -1, -1):
            while nums[i] > nums[i + 1]:
                g = gpd(nums[i])
                if g == -1: return -1
                nums[i] /= g
                res += 1

        return res
