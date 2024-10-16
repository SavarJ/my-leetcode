class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        acc = 0
        def inorder(node):
            nonlocal acc
            if not node: return
            inorder(node.right)
            val = node.val
            node.val += acc
            acc += val
            inorder(node.left)
            return root
        
        return inorder(root)
