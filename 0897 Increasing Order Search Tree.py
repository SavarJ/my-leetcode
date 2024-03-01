# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = res = TreeNode()
        def inorder(node):
            nonlocal res
            if not node: return
            inorder(node.left)
            res.right = node
            res = res.right
            node.left = None
            inorder(node.right)
        
        inorder(root)
        return ans.righ
