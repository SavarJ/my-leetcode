# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not (root.left or root.right): return root.val
        left, right = self.evaluateTree(root.left), self.evaluateTree(root.right)
        return left or right if root.val == 2 else left and right
