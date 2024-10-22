class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pFound, qFound = False, False
        def helper(node):
            nonlocal pFound, qFound
            if not node: return
            if node == p: pFound = True
            elif node == q: qFound = True

            left, right = helper(node.left), helper(node.right)
            if node in [p, q]: return node
            return node if left and right else left or right
        
        res = helper(root)
        return res if pFound and qFound else None
