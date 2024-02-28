# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        maxDepth, res = 0, root
        def dfs(node, d):
            nonlocal maxDepth, res
            if not node: return
            if d > maxDepth:
                res = node
                maxDepth = d
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        
        dfs(root, 0)
        return res.va
