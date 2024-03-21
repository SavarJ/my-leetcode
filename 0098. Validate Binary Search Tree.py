class Solution:
    def isValidBST(self, root: Optional[TreeNode], minVal=-inf, maxVal=inf) -> bool:
        return True if not root else (minVal < root.val < maxVal) and self.isValidBST(root.left, minVal, root.val) and self.isValidBST(root.right, root.val, maxVal)
