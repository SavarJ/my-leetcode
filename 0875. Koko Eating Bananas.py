class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # def solve(k):
        #     return sum(ceil(pile/k) for pile in piles) <= h 

        # l, r = 1, max(piles)
        # res = inf
        # while l<=r:
        #     m = (l+r)//2
        #     if solve(m):
        #         res = min(res, m)
        #         r = m-1
        #     else:
        #         l = m+1

        # return res

        return bisect_left(range(1, max(piles)+1), True, key=lambda k: sum(ceil(p/k) for p in piles) <= h) +1
