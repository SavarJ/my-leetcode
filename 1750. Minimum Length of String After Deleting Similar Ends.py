class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s)-1
        while l < r and (char:=s[l]) == s[r]:
            while l < r and s[l] == char: 
                l+=1
            while l-1 < r and s[r] == char:
                r-=1
        
        return r-l+1
