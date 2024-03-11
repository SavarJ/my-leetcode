# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # seen, stack = set(), [root]
        # while stack:
        #     if node:=stack.pop():
        #         if k-node.val in seen: return True
        #         seen.add(node.val)
        #         stack.extend([node.left, node.right])
        # return False
        def inOrder(node):
            if node:
                yield from inOrder(node.left)
                yield node.val
                yield from inOrder(node.right)
        
        def inOrderRev(node):
            if node:
                yield from inOrderRev(node.right)
                yield node.val
                yield from inOrderRev(node.left)
        
        leftGen, rightGen = inOrder(root), inOrderRev(root)
        left, right = next(leftGen), next(rightGen)
        while left < right:
            if left + right == k: return True
            if left + right < k: left = next(leftGen)
            else: right = next(rightGen)
        
        return False
