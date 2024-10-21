class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        res = 0
        def solve(i):
            nonlocal res
            if len(seen) + len(s)-i+1 <= res: return
            if res == len(s): return
            if i >= len(s): res = max(res, len(seen)) 

            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub in seen: continue
                seen.add(sub)
                solve(j+1)
                seen.remove(sub)
            
        solve(0)
        return res
