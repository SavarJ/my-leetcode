class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # max_or = reduce(or_, nums)
        # @cache
        # def solve(i, ans):
        #     if i >= len(nums): return ans == max_or
        #     return solve(i+1, ans) + solve(i+1, ans|nums[i])
        
        # return solve(0, 0)

        max_or = reduce(or_, nums)
        res = 0
        for subset in range(1, pow(2, len(nums))):
            ans = 0
            for i in range(len(nums)):
                if (1 << i) & subset:
                    ans |= nums[i]
            
            res += ans == max_or
        
        return res
