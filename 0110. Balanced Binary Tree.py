class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(node):
            nonlocal res

            if not node: return 0

            left, right = dfs(node.left), dfs(node.right)

            if abs(left-right) > 1:
                res = False
            
            return max(left, right)+1
        
        dfs(root)
        return res
