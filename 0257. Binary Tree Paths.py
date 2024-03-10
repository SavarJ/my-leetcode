# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node, path):
            if not node: return
            if node != root: path.append(f'->{node.val}')
            dfs(node.left, path), dfs(node.right, path)
            if not (node.left or node.right): res.append(''.join(path))
            path.pop()
        
        dfs(root, [str(root.val)])
        return res
