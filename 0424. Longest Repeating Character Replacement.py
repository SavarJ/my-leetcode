class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        window = Counter()
        res = 0
        counts = Counter()
        maxx = 0

        for r in range(len(s)):
            if window[s[r]] != 0:
                counts[window[s[r]]] -= 1
            window[s[r]] += 1
            counts[window[s[r]]] += 1
            maxx = max(maxx, window[s[r]])

            while l<=r and r-l+1 - maxx > k:
                counts[window[s[l]]] -= 1
                window[s[l]] -= 1

                if window[s[l]] != 0:
                    counts[window[s[l]]] += 1
                if counts[maxx] == 0:
                    maxx -= 1

                if window[s[l]] == 0: del window[s[l]]
                l += 1
            
            res = max(res, r-l+1)
        
        return res
