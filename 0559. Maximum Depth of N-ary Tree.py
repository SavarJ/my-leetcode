class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return 0 if not root else max((self.maxDepth(child) for child in root.children), default=0) + 1
