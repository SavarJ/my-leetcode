class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1: return TreeNode(val, root)
        q = deque([root])
        for d in reversed(range(depth-1)):
            for i in range(len(q)):
                if node:= q.popleft():
                    if not d: node.left, node.right = TreeNode(val, left=node.left), TreeNode(val, right=node.right)
                    q.extend([node.left, node.right])
        return root
