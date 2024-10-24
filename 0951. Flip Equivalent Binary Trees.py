class Solution:
    def flipEquiv(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a or not b: return a == b

        return a.val == b.val and \
                ((self.flipEquiv(a.left, b.left) and self.flipEquiv(a.right, b.right)) or \
                (self.flipEquiv(a.left, b.right) and self.flipEquiv(a.right, b.left)))
