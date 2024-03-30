class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1, text2 = s, s[::-1]
        @cache
        def bt(i, j):
            if i >= len(text1) or j >= len(text2): return 0
            return 1 + bt(i+1, j+1) if text1[i] == text2[j] else max(bt(i+1, j), bt(i, j+1))

        return bt(0, 0)
