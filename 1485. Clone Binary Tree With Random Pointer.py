class Solution:
    visit = {None:None}
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if root in self.visit: return self.visit[root]
        self.visit[root] = copy = NodeCopy(root.val)
        copy.left, copy.right, copy.random = self.copyRandomBinaryTree(root.left), self.copyRandomBinaryTree(root.right), self.copyRandomBinaryTree(root.random)
        return self.visit[root]
