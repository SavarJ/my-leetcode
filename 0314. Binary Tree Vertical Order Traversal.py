class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = [[] for _ in range(201)]

        queue = deque([(root, 0)])
        while queue:
            for i in range(len(queue)):
                node, col = queue.popleft()
                if node:
                    cols[col+100].append(node.val)
                    queue.extend([(node.left, col-1), (node.right, col+1)])
        
        return [col for col in cols if col]
