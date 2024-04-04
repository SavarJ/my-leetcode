class Solution:
    def maxDepth(self, s: str) -> int:
        return max(accumulate({'(':1,')':-1}.get(c,0) for c in s))
