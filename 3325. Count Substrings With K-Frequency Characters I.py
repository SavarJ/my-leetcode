class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        res = 0
        l = 0
        d = Counter()
        for r in range(len(s)):
            d[s[r]] += 1
            while d[s[r]] >= k:
                res += len(s)-r
                d[s[l]] -= 1
                l += 1
        return res
