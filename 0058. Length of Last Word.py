class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = l = len(s)-1
        while r>=0 and s[r] == " ": r,l=r-1,l-1
        while l>=0 and s[l] != " ": l-=1
        return r-l
