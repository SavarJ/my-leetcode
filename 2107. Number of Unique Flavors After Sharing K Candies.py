class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        '''
        find window of size k with the least unique elements?
        '''
        freq = Counter(candies)
        if k == 0: return len(freq)
        res = 0
        for r in range(len(candies)):
            freq[candies[r]] -= 1
            if freq[candies[r]] == 0: del freq[candies[r]]

            if r+1 < k: continue
            res = max(res, len(freq))

            freq[candies[r-k+1]] += 1

        return res
