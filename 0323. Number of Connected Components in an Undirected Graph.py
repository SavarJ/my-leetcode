class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        ranks = [1]*n
        components = n

        def find(x):
            if parents[x] != x: parents[x] = find(parents[x])
            return parents[x]
        
        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1 == p2: return False
            
            if ranks[p1] >= ranks[p2]:
                parents[p2] = p1
                ranks[p1] += ranks[p2]
            else:
                parents[p1] = p2
                ranks[p2] += ranks[p1]
            return True

        for a,b in edges:
            if union(a,b):
                components -= 1
        
        return components
