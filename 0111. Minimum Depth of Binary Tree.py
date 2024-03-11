# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res, queue = 0, deque([root])
        while queue:
            res += 1
            for i in range(len(queue)):
                if node:=queue.popleft():
                    if not (node.left or node.right): return res
                    queue.extend([node.left, node.right])

        # def dfs(node):
        #     if not node: return inf
        #     if not (node.left or node.right): return 1
        #     return min(dfs(node.left), dfs(node.right))+1
        
        # return 0 if not root else dfs(root)
