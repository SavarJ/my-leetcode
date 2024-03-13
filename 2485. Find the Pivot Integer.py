class Solution:
    def pivotInteger(self, n: int) -> int:
        l, r = 1, n
        total = (n*(n+1))//2
        while l <= r:
            m = (l+r)//2
            x = (m*(m+1))//2
            if x == (total-x+m): return m
            if x < (total-x+m): l = m+1
            else: r = m-1
        return -1
