class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        dp = [(0, -1), (0, -1)] # cost, index

        for i in reversed(range(n)):
            curr = [] # max heap
            smallest, smallestIdx = -dp[1][0], dp[1][1]
            secondSmallest, secondSmallestIdx = -dp[0][0], dp[0][1]
            for j in range(k):
                cost = costs[i][j]
                if j != smallestIdx:
                    heappush(curr, (-(cost+smallest), j) )
                else:
                    heappush(curr, (-(cost+secondSmallest), j) )
                
                if len(curr) > 2: heappop(curr) #limit it to smallest and second smallest

            dp = curr.copy()
        
        return -dp[1][0]
