class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        heap = []

        while queue:
            total = 0
            for i in range(len(queue)):
                node = queue.popleft()
                total += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            heappush(heap, total)
            if len(heap) > k:
                heappop(heap)
        
        return -1 if len(heap) != k else heappop(heap)
