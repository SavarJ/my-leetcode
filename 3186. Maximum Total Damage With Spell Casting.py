class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        keys = sorted(freq.keys())
        vals = [freq[key]*key for key in keys]
        k = 2

        n = len(keys)

        @cache
        def solve(i):
            if i >= n: return 0

            nextIdx = i+1
            for j in range(1, k+1):
                if i+j < n and keys[i+j] - keys[i] <= k:
                    nextIdx += 1
            
            take = vals[i] + solve(nextIdx)
            leave = solve(i+1)

            return max(take, leave)
        
        return solve(0)
