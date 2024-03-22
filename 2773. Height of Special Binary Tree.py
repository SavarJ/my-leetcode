class Solution:
    def heightOfTree(self, root: Optional[TreeNode]) -> int:
        return 0 if not root or (root.left and root.left.right == root) else max(self.heightOfTree(root.left), self.heightOfTree(root.right))+1
