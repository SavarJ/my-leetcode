class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]+[inf]*(amount)
        for i in range(amount+1):
            for coin in coins:
                dp[i] = min(dp[i], inf if i-coin<0 else dp[i-coin]+1)
        return -1 if dp[-1] == inf else dp[-1]

        # cache = {0:0}
        # def bt(total):
        #     if total < 0: return inf
        #     if total in cache: return cache[total]
            
        #     cache[total] = min(bt(total-coin) for coin in coins) + 1
        #     return cache[total]

        # return -1 if (res:=bt(amount)) == inf else res
