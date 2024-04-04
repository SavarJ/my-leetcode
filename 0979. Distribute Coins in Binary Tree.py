class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0, 0
            leftBal, leftTotalMoves = dfs(node.left)
            rightBal, rightTotalMoves = dfs(node.right)
            return leftBal+rightBal+node.val-1, leftTotalMoves+rightTotalMoves+abs(leftBal)+abs(rightBal)
        
        return dfs(root)[1]
