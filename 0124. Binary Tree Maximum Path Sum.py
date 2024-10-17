class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def solve(node):
            nonlocal res
            if not node: return -inf

            left = solve(node.left)
            right = solve(node.right)
            curr = node.val

            res = max(res, curr, left+curr, right+curr, left+right+curr)
            return max(left+curr, right+curr, curr)
        
        solve(root)
        return res
