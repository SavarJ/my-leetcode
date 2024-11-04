class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        '''
        x is always greater than y
        we can decrease all values by y k-times
        and also have additional k (x-y)s to decrease
        '''
        def solve(k):
            xOps = k
            for num in nums:
                diff = num - (k*y)
                if diff <= 0: continue
                opsNeeded = ceil(diff/(x-y))
                if opsNeeded > xOps: return False
                xOps -= opsNeeded
            
            return True

        l, r = 0, 10**9
        while l<=r:
            m = (l+r)//2
            if solve(m):
                r = m-1
            else:
                l = m+1
        
        return l
