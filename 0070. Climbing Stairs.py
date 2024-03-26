class Solution:
    def climbStairs(self, n: int) -> int:
        curr = one = two = 1
        for i in range(1, n):
            curr = one + two
            one, two = curr, one
        
        return curr
