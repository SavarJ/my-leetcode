# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev, res = -inf, inf
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root.left: self.getMinimumDifference(root.left)
        self.res, self.prev = min(self.res, root.val-self.prev), root.val
        if root.right: self.getMinimumDifference(root.right)
        return self.res
