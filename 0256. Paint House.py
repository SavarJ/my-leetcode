class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp, curr = costs[-1], [0]*3
        for i in reversed(range(len(costs)-1)):
            for j in range(len(curr)):
                curr[j] = min(cost for k, cost in enumerate(dp) if k!=j) + costs[i][j]

            dp = curr.copy()

        return min(dp)

        # dp = [[0 for _ in range(3)] for row in range(len(costs))]
        # dp[-1] = costs[-1]
        
        # for i in reversed(range(len(costs)-1)):
        #     dp[i][0] = min(dp[i+1][1], dp[i+1][2]) + costs[i][0]
        #     dp[i][1] = min(dp[i+1][0], dp[i+1][2]) + costs[i][1]
        #     dp[i][2] = min(dp[i+1][0], dp[i+1][1]) + costs[i][2]

        # return min(dp[0])

        # @cache
        # def helper(i, prev):
        #     if i >= len(costs):
        #         return 0
            
        #     res = inf
        #     for j, cost in enumerate(costs[i]):
        #         if prev != j:
        #             res = min(res, cost+helper(i+1, j))
            
        #     return res
        
        # return helper(0, -1)
        
