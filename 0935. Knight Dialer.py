class Solution:
    def knightDialer(self, n: int) -> int:
        MOD, hops = 10**9+7, {1:[6, 8],2:[7,9],3:[8,4],4:[3,9,0],5:[],6:[1,7,0],7:[6,2],8:[1,3],9:[2,4],0:[4,6]}
        @cache
        def dfs(i, k): return 1 if k==0 else sum((dfs(hop, k-1)%MOD) for hop in hops[i])%MOD
        return sum((dfs(i, n-1)%MOD) for i in range(10))%MOD
