class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res, path = [], []
        def dfs(node, k):
            if not node: return
            if not (node.left or node.right) and node.val == k: return res.append(path.copy()+[node.val])
            path.append(node.val)
            dfs(node.left, k-node.val), dfs(node.right, k-node.val)
            path.pop()
        dfs(root, targetSum)
        return res
