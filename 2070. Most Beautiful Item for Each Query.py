class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        Q = sorted([(q,i) for i,q in enumerate(queries)])
        res = [0] * len(Q)
        p = 0
        best = 0

        for q, i in Q:
            while p < len(items) and items[p][0] <= q:
                best = max(best, items[p][1])
                p += 1
            res[i] = best
        
        return res


        # items.sort()
        # maxx = [items[0][1]]
        # for i in range(1, len(items)):
        #     maxx.append(max(maxx[-1], items[i][1]))
        
        # @cache
        # def bs(target):
        #     l, r = 0, len(items)-1
        #     while l <= r:
        #         m = (l+r)//2
        #         if target >= items[m][0]:
        #             l = m+1
        #         else:
        #             r = m-1

        #     return 0 if r == -1 else maxx[r] # return the rightmost occ, or the next smallest

        # res = []
        # for price in queries:
        #     res.append(bs(price))
        # return res
