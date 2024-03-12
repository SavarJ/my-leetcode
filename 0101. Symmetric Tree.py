# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(a, b):
            if not a and not b: return True
            if not a or not b: return False
            return a.val == b.val and isMirror(a.left, b.right) and isMirror(a.right, b.left)
        
        return isMirror(root.left, root.right)

        # queue = deque([root])
        # while queue:
        #     level = []
        #     for i in range(len(queue)):
        #         if node := queue.popleft():
        #             queue.extend([node.left, node.right])
        #         level.append(node)
        #     for i in range(ceil(len(level)//2)):
        #         if getattr(level[i], 'val', None) != getattr(level[~i], 'val', None): return False

        # return True
