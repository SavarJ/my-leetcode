class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        p = 0
        l = 0
        for r in range(n+1):
            if r == n or chars[r] != chars[l]:
                chars[p] = chars[l]
                p += 1
                if r-l > 1:
                    num = str(r-l)
                    for d in num:
                        chars[p] = d
                        p += 1
                
                l = r
        return p
