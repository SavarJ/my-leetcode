class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res

            if not node: return 0

            left, right = dfs(node.left), dfs(node.right)

            res = max(res, left+right)
            return max(left, right)+1
        
        dfs(root)
        return res
