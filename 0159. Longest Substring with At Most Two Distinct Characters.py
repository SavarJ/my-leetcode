class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = l = 0
        window = {}
        for r in range(len(s)):
            window[s[r]] = r
            if len(window) > 2:
                minIdx = min(window.values())
                del window[s[minIdx]]
                l = minIdx+1
            res = max(res, r-l+1)
        return res

        # res = l = 0
        # window = Counter()
        # for r in range(len(s)):
        #     window[s[r]] += 1
        #     while len(window) > 2:
        #         window[s[l]]-=1
        #         if window[s[l]] == 0: del window[s[l]]
        #         l += 1
        #     res = max(res, r-l+1)
        # return res
