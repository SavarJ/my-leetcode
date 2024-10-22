class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def depth(node): 
            if not node: return 0
            return 1 + depth(node.parent)
        
        pDepth, qDepth = depth(p), depth(q)
        
        while pDepth > qDepth:
            p = p.parent
            pDepth -= 1
        
        while qDepth > pDepth:
            q = q.parent
            qDepth -= 1

        while p != q:
            p, q = p.parent, q.parent
        
        return p

        # a, b = p, q
        # while a != b:
        #     a = a.parent if a else q
        #     b = b.parent if b else p
        # return a
