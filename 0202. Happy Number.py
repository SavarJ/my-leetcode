class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(num):
            res = 0
            while num:
                res += (num % 10)**2
                num //= 10
            return res
        
        slow, fast = n, helper(n)
        while slow != fast:
            slow, fast = helper(slow), helper(helper(fast))
        
        return slow == 1
