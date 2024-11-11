class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = Counter()
        l = 0
        res = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res
