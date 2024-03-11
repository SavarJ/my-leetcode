# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            return p.val == q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right) if p and q else not (p or q)

        stack = [root]
        while stack:
            if node:= stack.pop():
                if node.val == subRoot.val and sameTree(node, subRoot): return True
                stack.extend([node.left, node.right])
        
        return False

        # def findPossibleRoots(a, b):
        #     if not a or not b: return []
        #     return ([a] if a.val == b.val else []) + findPossibleRoots(a.left, b) + findPossibleRoots(a.right, b)
        
        # def sameTree(p, q):
        #     return p.val == q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right) if p and q else not (p or q)
        
        # return any(sameTree(t, subRoot) for t in findPossibleRoots(root, subRoot))
