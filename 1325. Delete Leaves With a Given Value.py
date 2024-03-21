class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root: return
        root.left, root.right = self.removeLeafNodes(root.left, target), self.removeLeafNodes(root.right, target)
        return None if not (root.left or root.right) and root.val == target else root
