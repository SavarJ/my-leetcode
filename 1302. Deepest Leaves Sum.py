class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        while queue:
            total = 0
            for i in range(len(queue)):
                node = queue.popleft()
                total += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
        return total
