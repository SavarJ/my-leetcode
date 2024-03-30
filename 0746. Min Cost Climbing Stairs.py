class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        curr = one = two = 0
        for i in reversed(range(len(cost))):
            curr = cost[i] + min(one, two)
            one, two = curr, one
        
        return min(one, two)

        # res = [0]*(len(cost)+2)
        # for i in reversed(range(len(cost))):
        #     res[i] = cost[i] + min(res[i+1], res[i+2])
        
        # return min(res[0], res[1])

        # @cache
        # def bt(i):
        #     if i >= len(cost): return 0
        #     return min(bt(i+1), bt(i+2))+ (cost[i] if i >= 0 else 0)
        
        # return bt(-1)
