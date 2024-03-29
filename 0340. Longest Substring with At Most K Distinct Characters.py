class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_substr = 0
        window = Counter()
        for r in range(len(s)):
            window[s[r]]+=1
            if len(window) <= k:
                max_substr += 1
            else:
                window[s[r-max_substr]]-=1
                if window[s[r-max_substr]] == 0: del window[s[r-max_substr]] 
        return max_substr

        # if k == 0: return 0
        # if k >= len(s): return len(s)
        
        # def isValid(windowSize):
        #     window = Counter(s[:windowSize])
        #     if len(window) <= k:
        #         return True
        #     for i in range(windowSize, len(s)):
        #         window[s[i]]+=1
        #         window[s[i-windowSize]]-=1
        #         if window[s[i-windowSize]]==0: del window[s[i-windowSize]]
        #         if len(window) <= k:
        #             return True
            
        #     return False
        
        # ll, rr = k, len(s)
        # res = 0
        # while ll <= rr:
        #     windowSize = (ll+rr)//2
        #     if isValid(windowSize):
        #         ll = windowSize+1
        #         res = max(res, windowSize)
        #     else:
        #         rr = windowSize-1

        # return res
