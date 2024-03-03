# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        totals, count = defaultdict(int), defaultdict(int)
        def dfs(node, d):
            if not node: return
            totals[d], count[d] = totals[d]+node.val, count[d]+1
            dfs(node.left, d+1), dfs(node.right, d+1)

        dfs(root, 0)
        return [totals[i]/count[i] for i in range(len(totals))]
