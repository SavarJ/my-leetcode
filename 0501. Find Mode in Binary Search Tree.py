# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res, prev = [], root.val
        curr = maxx = 0

        def dfs(node):
            nonlocal maxx, prev, curr, res
            if not node: return
            dfs(node.left)

            curr = curr+1 if prev == node.val else 1
            if curr > maxx:
                res, maxx = [node.val], curr
            elif curr == maxx:
                res.append(node.val)
            prev = node.val

            dfs(node.right)
        
        dfs(root)
        return res
