# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        res, stack = set(), [root]
        while stack:
            if node:= stack.pop():
                res.add(node.val)
                if len(res) > 1: return False
                stack.extend([node.left, node.right])
        return True
