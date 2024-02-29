# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        level = 0
        while queue:
            prev = None
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    if level % 2 == 0:
                        if node.val % 2 == 0 or (prev and node.val <= prev): return False
                    else:
                        if node.val % 2 == 1 or (prev and node.val >= prev): return False
                    prev = node.val
                    queue.extend([node.left, node.right])
            level += 1

        return Tru
