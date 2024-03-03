# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return 0 if not root else (root.left.val if root.left and not (root.left.left or root.left.right) else self.sumOfLeftLeaves(root.left)) + self.sumOfLeftLeaves(root.right)

        # if not root: return 0
        # if root.left and not (root.left.left or root.left.right): return root.left.val + self.sumOfLeftLeaves(root.right)
        # return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

        # def dfs(node, par):
        #     if not node: return 0
        #     if not (node.left or node.right) and par.left == node: return node.val
        #     return dfs(node.left, node) + dfs(node.right, node)
        
        # return dfs(root, root)
