class Solution:
    visit={None:None}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node in self.visit: return self.visit[node]
        self.visit[node] = copy = Node(node.val)
        copy.neighbors = list(map(self.cloneGraph, node.neighbors))
        return copy
