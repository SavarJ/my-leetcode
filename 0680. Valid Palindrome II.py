class Solution:
    def validPalindrome(self, s: str) -> bool:
        k = 1
        def solve(l, r):
            nonlocal k
            if l>=r: return True
            elif s[l] != s[r] and k:
                k -= 1
                return solve(l+1, r) or solve(l, r-1)
            elif s[l] == s[r]: return solve(l+1, r-1)
            else:
                return False

        return solve(0, len(s)-1)
