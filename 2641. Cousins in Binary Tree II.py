class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(root, None)])
        while queue:
            parents_sum = Counter()
            level = []
            level_total = 0
            for i in range(len(queue)):
                node, par = queue.popleft()
                if node:
                    level_total += node.val
                    parents_sum[par] += node.val
    
                    queue.extend([(node.left, node), (node.right, node)])
                    level.append((node, par))
            
            for node, par in level:
                node.val = level_total - parents_sum[par]
        
        return root
