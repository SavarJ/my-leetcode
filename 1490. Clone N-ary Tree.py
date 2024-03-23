class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root: return Node(root.val, [self.cloneTree(child) for child in root.children])
